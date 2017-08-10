# 查询用户信息
select_user_info = "SELECT `UserId`,`Name` FROM `U_UserInfo` WHERE UserId='%s'"

# 查询聊天主表信息
select_chat_main = "SELECT `Id`,`SendUserId`,`ReceiveUserId`,`Content` FROM `N_ChatMain` WHERE (`SendUserId`='%s' AND ReceiveUserId='%s')OR(`SendUserId`='%s' AND ReceiveUserId='%s') "

# 新增聊天主表信息
insert_chat_main = "INSERT INTO `N_ChatMain` (`Id`,`SendUserId`,`ReceiveUserId`,`Content`,`CreateUserID`,`CreateTime`)  VALUES('%s','%s','%s','%s','%s',NOW())"

# 修改聊天主表信息
update_chat_main = "UPDATE N_ChatMain SET Content='%s',`ModifUserID`='%s',`ModifTime`=NOW() WHERE `Id`='%s'"
# 新增聊天内容表
insert_chat_content = "INSERT INTO `N_ChatContent` (`Id`,`ChatId`,`UserId`,`Content`,`CreateUserID`,`CreateTime`) VALUES(UUID(),'%s','%s','%s','%s',NOW()) "
# 新增系统消息
insert_chat_notice = "INSERT INTO MS_SystemNotice(Id,UserId,Content,CreateUserID,CreateTime,`Type`,`ChatId`,`ReceiveUserId`) VALUES (UUID(),'%s','%s','%s',NOW(),2,'%s','%s');"

# 获取聊天内容
select_chat_list = "SELECT cm.`UserId`,cm.`Content`,cm.`Type`,cm.`CreateTime`,sendUser.`Name` FROM N_ChatMain cc " \
                   "JOIN `N_ChatContent` cm ON cc.Id=cm.ChatId " \
                   "JOIN `U_UserInfo` sendUser ON cm.`UserId`=sendUser.UserId " \
                   " WHERE (cc.`SendUserId`='%s' AND cc.ReceiveUserId='%s')OR(cc.`SendUserId`='%s' AND cc.ReceiveUserId='%s') " \
                   "ORDER BY  cm.CreateTime DESC " \
                   "LIMIT %s,%s"

existx_chat_notice="SELECT COUNT(1) as total FROM  `MS_SystemNotice` WHERE `ChatId`='%s' AND `UserId`='%s'"

update_chat_notice="UPDATE MS_SystemNotice SET `Content`='%s',`CreateUserID`='%s',`CreateTime`=NOW(),`IsRead`=0 WHERE `ChatId`='%s' AND `UserId`='%s'"