# 获取系统消息
select_system_notice_list = "SELECT Id,UserId,Content,IsRead,CreateTime FROM MS_SystemNotice " \
                            "WHERE IsDelete=FALSE AND UserId='%s' " \
                            "ORDER BY IsRead ASC ,CreateTime DESC " \
                            "LIMIT %s,%s"
#新增系统消息
insert_system_notice="INSERT INTO MS_SystemNotice(Id,UserId,Content,CreateUserID,CreateTime) VALUES (uuid(),'%s','%s','%s',now());"

#修改系统消息的已读状态
update_system_notice_status="UPDATE MS_SystemNotice SET IsRead=1,ModifTime=now(),ModifUserID='%s' WHERE Id='%s';"