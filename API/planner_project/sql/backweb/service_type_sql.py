#区域列表
select_service_type_list="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_ServiceType` " \
                         "WHERE `IsDelete`=FALSE " \
                         "AND ('%s' IS NULL OR '%s'='' OR `Name` LIKE '%s')  "\
                         "ORDER BY `IsTop` DESC ,`Sort` DESC,`CreateTime` DESC "\
                         "LIMIT %s , %s "

#区域信息
select_service_type_info="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_ServiceType` " \
                         "WHERE `Id`='%s' AND `IsDelete`=FALSE "

#修改信息
update_service_type_info="UPDATE `Base_ServiceType` SET `Name`='%s',`Description`='%s',`IsTop`='%s',`Sort`='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_service_type="UPDATE `Base_ServiceType` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';" \
                    "UPDATE `U_UserInfo` SET `ServiceTypeId`=NULL,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `ServiceTypeId` = '%s';"

insert_service_type="INSERT INTO `Base_ServiceType` (`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`" \
                    ",`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)"\
                    "VALUES( '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"