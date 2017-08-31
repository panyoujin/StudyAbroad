#获取用户列表
select_user_list="SELECT u.`Id`,u.`Account`,u.`Phone`,u.`Password`,u.`UserType`,ui.`Name`,u.`Phone` ,u.`CreateTime` "\
                      ",(SELECT GROUP_CONCAT(sa.`Name`) FROM `Base_ServiceArea` sa WHERE FIND_IN_SET(sa.`Id`,ui.`ServiceAreaId`)>0) AS AreaName" \
                      ",(SELECT GROUP_CONCAT(st.`Name`) FROM `Base_ServiceType` st WHERE FIND_IN_SET(st.`Id`,ui.`ServiceTypeId`)>0) AS TypeName " \
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE  u.`UserType`=1 AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR u.`Phone` LIKE '%s')  "\
                    "ORDER BY u.CreateTime DESC ,ui.`Name`  " \
                    "LIMIT %s , %s "
#获取用户列表数量
select_user_list_count="SELECT COUNT(0) AS listCount  "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE   u.`UserType`=1 AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR u.`Phone` LIKE '%s')  "

#获取用户详情
select_user_info="SELECT u.`Id`,u.`Account`,u.`Phone`,u.`Password`,u.`UserType`,ui.`Name`,u.`Phone`,ui.`Sex`,ui.`Age`,ui.`Email`,ui.`Education`,ui.`Address`,ui.`HeadImage`,ui.`IDCard`,ui.`IDCardJust`,ui.`IDCardBack` "\
                      ",(SELECT GROUP_CONCAT(sa.`Name`) FROM `Base_ServiceArea` sa WHERE FIND_IN_SET(sa.`Id`,ui.`ServiceAreaId`)>0) AS AreaName" \
                      ",(SELECT GROUP_CONCAT(st.`Name`) FROM `Base_ServiceType` st WHERE FIND_IN_SET(st.`Id`,ui.`ServiceTypeId`)>0) AS TypeName " \
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE u.`Id`='%s'  AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE "

#修改用户信息
update_user_info="UPDATE `U_User` SET `Account`='%s',`Phone`='%s',`Password`='%s',`UserType`='%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `Id` = '%s' ;" \
                 "UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`HeadImage` = '%s',`IDCard` = '%s',`IDCardJust` = '%s',`IDCardBack` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"


#删除用户
delete_user="UPDATE `U_UserInfo` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;" \
                 "UPDATE `U_User` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `Id` = '%s' ;"

#插入用户
insert_user="INSERT INTO `U_User` (`Id`,`Account`,`Phone`,`Password`,`UserType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)  " \
                "VALUES('%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE) ; " \
            "INSERT INTO `U_UserInfo` (`UserId`,`Name`,`Sex`,`Age`,`Education`,`Address`,`Email`,`HeadImage`,IDCard,IDCardJust,IDCardBack,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)  " \
                "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE) ;"

#查询用户是否存在
select_userid_by_account = "SELECT `Id` FROM `U_User` WHERE Account ='%s' and `IsDelete`= FALSE"
