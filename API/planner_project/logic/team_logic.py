from planner_project.data_access import mysql
from planner_project.sql.team import team_sql

#获取指定用户所在的团队成员列表
def select_planner_team_member_list(userid,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(team_sql.select_planner_team_member_list,(userid,(page-1)*size,size))


#获取团队列表
def get_team_list(userid,name,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(team_sql.select_team_list,(userid,name,name,sear,(page-1)*size,size))


#获取团队成员列表
def get_team_member_list(teamId,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(team_sql.select_team_member_list,(teamId,(page-1)*size,size))
