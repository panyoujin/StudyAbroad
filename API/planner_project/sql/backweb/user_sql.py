#获取用户列表
select_user_list="SELECT u.`Id`,ui.`Name`,u.`Phone` ,sa.`Name` AS AreaName,st.`Name` TypeName,u.`CreateTime` "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE  u.`UserType`=1 AND u.`IsDelete`=FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR u.`Phone` LIKE '%s')  "\
                    "ORDER BY u.CreateTime DESC ,ui.`Name`  " \
                    "LIMIT %s , %s "
#获取用户列表数量
select_user_list_count="SELECT COUNT(0) AS listCount  "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE  u.`UserType`=1 AND u.`IsDelete`=FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR u.`Phone` LIKE '%s')  "

#获取用户详情
select_user_info="SELECT u.`Id`,ui.`Name`,u.`Phone`,ui.`Sex`,ui.`Age`,ui.`Email`,ui.`Education`,ui.`Address` "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE u.`UserType`=1 AND u.`Id`='%s'  "

#修改用户信息
update_user_info="UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"


#删除用户
delete_user="UPDATE `U_UserInfo` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;" \
                 "UPDATE `U_User` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `Id` = '%s' ;"