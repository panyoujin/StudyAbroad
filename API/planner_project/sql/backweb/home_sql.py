
#修改Token
update_sysuser_token = "UPDATE `Sys_User` SET `LoginTime` = NOW(), `LoginToken` = '%s', `LoginIP` = '%s' " \
                    "WHERE `UserName` = '%s' AND `Password`='%s' AND `Status`=1 "

#通过token查询用户信息
select_sysuser_login_info = "SELECT u.`UserId`,u.`UserName`,u.`NickName`,u.`Phone`,u.`Email`,u.`Descript`,u.`CreateDate`,u.`IsAdmin`,ur.`RoleId` " \
                         "FROM `Sys_User` u " \
                         "LEFT JOIN `Sys_P_UserRole` ur ON u.`UserId`=ur.`UserId` " \
                         "WHERE LoginToken ='%s'"