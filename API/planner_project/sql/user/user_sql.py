#查询用户是否存在
select_exists_user = "SELECT 1 FROM `U_User` WHERE Account ='%s'"
#新增用户表
insert_user = "INSERT INTO `U_User` (`Id`,`Account`,`Password`,`CreateTime`) VALUES('%s','%s','%s',NOW())"
#新增用户信息表
insert_userinfo = "INSERT INTO `U_UserInfo`(`UserId`,`CreateTime`)  VALUES('%s',NOW())"
#通过帐号查询用户信息
select_user_info = "SELECT u.`Id`,u.`Account`,u.`Phone`,u.`UserType`,ui.`Name`, ui.`HeadImage` " \
                         "FROM `U_User` u " \
                   "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                         "WHERE Account ='%s'"
#根据用户id查询用户是否
select_user_by_id="SELECT `Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken` FROM `U_User` WHERE Id='%s' AND `IsDelete`=FALSE"

#通过token查询用户信息
select_user_login_info = "SELECT u.`Id`,u.`Account`,u.`Phone`,u.`UserType`,ui.`Name`, ui.`HeadImage` " \
                         "FROM `U_User` u " \
                         "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                         "WHERE LoginToken ='%s'"
#修改Token
update_user_token = "UPDATE `U_User` SET `LoginTime` = NOW(), `LoginToken` = '%s', `LoginIP` = '%s' WHERE `Account` = '%s' AND `Password`='%s'"

#修改用户密码
update_user_password="UPDATE `U_User` SET `Password`='%s' WHERE Account='%s'"