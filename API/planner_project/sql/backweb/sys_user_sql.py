#用户列表
select_sys_user_list="SELECT  u.`UserId`,u.`UserName`,u.`NickName`,u.`Phone`,u.`Email`,u.`Descript`,u.`Status` " \
                     "FROM `Sys_User` u " \
                     "WHERE ('%s' IS NULL OR '%s'='' OR u.`UserName` LIKE '%s') " \
                     "AND ('%s' IS NULL OR '%s'='' OR u.`NickName` LIKE '%s') " \
                     "AND ('%s' IS NULL OR '%s'='' OR u.`Phone` LIKE '%s') "\
                    "LIMIT %s , %s "


#用户列表
select_sys_user_info="SELECT  u.`UserId`,u.`UserName`,u.`NickName`,u.`Phone`,u.`Email`,u.`Descript`,u.`Status` " \
                     "FROM `Sys_User` u " \
                     "WHERE u.`UserId`='%s' "

#插入用户
insert_sys_user="INSERT INTO `Sys_User` (`UserId`,`UserName`,`Password`,`NickName`,`Phone`,`Email`,`Descript`,`CreateDate`,`Status`,`IsAdmin`) " \
                "VALUES(  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  1,  0) ;" \
                "INSERT INTO `U_User` (`Id`,`Account`,`Password`,`Phone`,`UserType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)  " \
                "VALUES('%s','%s','%s','%s',0,'%s',NOW(),'%s',NOW(),FALSE) ;"

#修改用户
update_sys_user="UPDATE `Sys_User` SET `UserName` = '%s',`NickName` = '%s',`Phone` = '%s',`Email` = '%s',`Descript` = '%s'" \
                ",`Status` = %s,`IsAdmin` = %s WHERE `UserId` = '%s' ; " \
                "UPDATE `U_User` SET`Account` = '%s',`Phone` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id` = '%s' ;"
#赋权限
insert_user_role="DELETE FROM `Sys_P_UserRole` ur WHERE ur.`UserId`='%s'; " \
                 "INSERT INTO `Sys_P_UserRole`(`UserId`,`RoleId`) SELECT '%s',`RoleId` FROM `Sys_P_Role` WHERE `RoleId` IN ('%s');"