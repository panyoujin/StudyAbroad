
from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import team_sql

#获取团队列表
def select_team_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(team_sql.select_team_list,(name,name,sear,sear,(page-1)*size,size))


#获取指定团队成员列表
def select_teamm_ember_list(teamid):
    if teamid == None or teamid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    return mysql.get_list(team_sql.select_teamm_ember_list,(teamid))



#删除用户
def delete_team(teamid,current_user_id):
    if teamid == None or teamid=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(team_sql.delete_team,(current_user_id,teamid,current_user_id,teamid,teamid))
    return data_register > 0



#删除用户
def delete_team_member(teamid,userid,current_user_id):
    if teamid == None or teamid=="" or userid == None or userid=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(team_sql.delete_team_member,(current_user_id,userid,teamid,teamid,teamid))
    return data_register > 0