from planner_project.data_access import mysql
from planner_project.sql.notice import system_notice_sql

#新增系统消息
def insert_system_notice(userId,content,createUserId):
    mysql.operate_object(system_notice_sql.insert_system_notice, (userId, content,createUserId))