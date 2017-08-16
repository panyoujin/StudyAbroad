
#查询动态列表
select_dynamic_list ="SELECT d.`Id`,d.`UserId`,d.`Content`,d.`ImageUrl`,d.`DynamicType`,d.`ReadCount`,d.`CreateUserID`,d.`CreateTime`,ui.`Name` AS UserName,ui.`HeadImage`,d.`IsTop` " \
                        "FROM `MS_Dynamic` d " \
                        "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=d.`UserId` " \
                        "WHERE d.`IsDelete` =FALSE " \
                        "AND ('%s' IS NULL OR '%s'='' OR d.`Content` LIKE '%s' OR ui.`Name` LIKE '%s')  "\
                        "ORDER BY d.`IsTop` DESC,d.`Sort` DESC,d.`CreateTime` DESC " \
                        "LIMIT %s, %s "

#动态信息
select_dynamic_info="SELECT d.`Id`,d.`UserId`,d.`Content`,d.`ImageUrl`,d.`DynamicType`,d.`ReadCount`,d.`CreateUserID`,d.`CreateTime`,ui.`Name` AS UserName,ui.`HeadImage` " \
                    "FROM `MS_Dynamic` d " \
                    "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=d.`UserId` " \
                    "WHERE d.`IsDelete` =FALSE AND d.`Id` = %s ;"

#修改信息
update_dynamic_info="UPDATE `MS_Dynamic` SET `Content`='%s',`ImageUrl`='%s',`IsTop`='%s',`Sort`='%s',ReadCount='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_dynamic="UPDATE `MS_Dynamic` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';"

#新增系统公告
insert_dynamic="INSERT INTO `MS_Dynamic` (`UserId`,`DynamicType`,`Content`,`ImageUrl`,`IsTop`,`Sort`,ReadCount,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`)  " \
               "VALUES('%s',2,'%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW()) ;"