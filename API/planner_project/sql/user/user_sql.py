#查询用户是否存在
select_exists_user = "SELECT 1 FROM `U_User` WHERE Account ='%s'"
#新增用户表
insert_user = "INSERT INTO `U_User` (`Id`,`Account`,`Password`,`CreateTime`) VALUES('%s','%s','%s',NOW())"
#新增用户信息表
insert_userinfo = "INSERT INTO `U_UserInfo`(`UserId`,`CreateTime`)  VALUES('%s',NOW())"
