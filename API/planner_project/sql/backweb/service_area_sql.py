#区域列表
select_service_area_list="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_ServiceArea` " \
                         "WHERE `IsDelete`=FALSE " \
                         "AND ('%s' IS NULL OR '%s'='' OR `Name` LIKE '%s')  "\
                         "ORDER BY `IsTop` DESC ,`Sort` DESC,`CreateTime` DESC "\
                         "LIMIT %s , %s "

#区域信息
select_service_area_info="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_ServiceArea` " \
                         "WHERE `Id`='%s' AND `IsDelete`=FALSE "

#修改信息
update_service_area_info="UPDATE `Base_ServiceArea` SET `Name`='%s',`Description`='%s',`IsTop`='%s',`Sort`='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_service_area="UPDATE `Base_ServiceArea` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';" \
                    "UPDATE `U_UserInfo` SET `ServiceAreaId`=NULL,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `ServiceAreaId` = '%s';"

#新增区域
insert_service_area="INSERT INTO `Base_ServiceArea` (`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`" \
                    ",`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)"\
                    "VALUES( '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"