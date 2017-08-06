from planner_project.data_access import mysql
from planner_project.sql.team import team_sql
from planner_project.common import  custom_error

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



#新增团队
def insert_team(teamId,userid,name,serviceAreaId,serviceDescription):
    if teamId == None or teamId=="" or userid == None or userid==""or name == None or name=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="输入不正确，请刷新后重试")
    return mysql.operate_object(team_sql.insert_team,(teamId,userid,name,serviceAreaId,serviceDescription,userid,userid,
                                                teamId, userid,userid,userid,
                                                teamId, userid, userid))
#获取用户的团队
def select_user_team(userid):
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="输入不正确，请刷新后重试")
    return mysql.get_object(team_sql.select_user_team,(userid))