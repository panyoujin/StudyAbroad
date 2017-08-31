# 所有动态列表
select_dynamic_list="SELECT d.`Id`,d.`UserId`,d.`Content`,d.`ImageUrl`,d.`DynamicType`,d.`ReadCount`,d.`CreateUserID`,d.`CreateTime`,ui.`Name` AS UserName,ui.`HeadImage` " \
                        "FROM `MS_Dynamic` d " \
                        "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=d.`UserId` " \
                        "WHERE d.`IsDelete` =FALSE " \
                        "ORDER BY d.`IsTop` DESC,d.`Sort` DESC,d.`CreateTime` DESC " \
                        "LIMIT %s, %s "

#指定用户的动态列表
select_user_dynamic_list="SELECT d.`Id`,d.`UserId`,d.`Content`,d.`ImageUrl`,d.`DynamicType`,d.`ReadCount`,d.`CreateUserID`,d.`CreateTime`,ui.`Name` AS UserName,ui.`HeadImage` " \
                        "FROM `MS_Dynamic` d " \
                        "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=d.`UserId` " \
                        "WHERE d.`IsDelete` =FALSE AND ui.`IsDelete` =FALSE AND d.`UserId` = '%s' " \
                        "ORDER BY d.`IsTop` DESC,d.`Sort` DESC,d.`CreateTime` DESC " \
                        "LIMIT %s, %s "
#新增动态
insert_dynanic="INSERT INTO `MS_Dynamic` (`UserId`,`DynamicType`,`Content`,`ImageUrl`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`)  " \
               "VALUES('%s',1,'%s','%s','%s',NOW(),'%s',NOW()) ;"

#指定动态详情
select_dynamic_info="SELECT d.`Id`,d.`UserId`,d.`Content`,d.`ImageUrl`,d.`DynamicType`,d.`ReadCount`,d.`CreateUserID`,d.`CreateTime`,ui.`Name` AS UserName,ui.`HeadImage` " \
                    "FROM `MS_Dynamic` d " \
                    "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=d.`UserId` " \
                    "WHERE d.`IsDelete` =FALSE AND ui.`IsDelete` =FALSE AND d.`Id` = %s ;"

#修改阅读数
update_dynamic_readcount="UPDATE MS_Dynamic SET ReadCount=ReadCount+1 WHERE Id = %s;"