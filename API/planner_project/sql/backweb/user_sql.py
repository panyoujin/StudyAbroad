#获取用户列表
select_user_list="SELECT u.`Id`,ui.`Name`,u.`Phone` ,sa.`Name` AS AreaName,st.`Name` TypeName,u.`CreateTime` "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE u.`UserType`=1 AND u.`IsDelete`=FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR u.`Phone` LIKE '%s')  "\
                    "ORDER BY u.CreateTime DESC ,ui.`Name`  " \
                    "LIMIT %s , %s "

#获取用户详情
select_user_info="SELECT u.`Id`,ui.`Name`,u.`Phone` ,sa.`Name` AS AreaName,st.`Name` TypeName,u.`CreateTime` "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE u.`UserType`=1 AND u.`Id`='%s'  "

#修改用户信息
update_user_info="UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"