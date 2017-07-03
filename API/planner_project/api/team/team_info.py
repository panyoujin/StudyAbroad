#coding:utf-8
import json,uuid

from flask import request
from planner_project.common import api_response,request_helper,custom_error
from planner_project import app
from planner_project.data_access import mysql
from planner_project.sql.team import team_sql
from planner_project.sql.user import user_sql

#申请加入团队
@app.route("/team/join_team", methods=['POST'])
def join_team():
    ApiResponse = api_response.ApiResponse()
    userId = request_helper.current_user_mush_login()["Id"]
    user_info = mysql.get_object(user_sql.select_user_by_id, (userId))
    if user_info is None or user_info["UserType"]==1:
        raise custom_error.CustomFlaskErr(status_code=500, message="你还不是规划师")

    TeamId = request.form.get("TeamId", type=str, default=None)
    if TeamId is None or TeamId=='':
        raise custom_error.CustomFlaskErr(status_code=500, message="团队id不能为空")

    exists_team=mysql.get_object(team_sql.exists_team_peoper,(userId,TeamId))

    if exists_team is not None and exists_team["Status"]==1 :
        raise custom_error.CustomFlaskErr(status_code=500, message="您已经申请过加入该团队，请耐心等待审核")
    if exists_team is not None and exists_team["Status"]==2 :
        raise custom_error.CustomFlaskErr(status_code=500, message="您已经是该团队成员")

    team_detail = mysql.get_object(team_sql.select_team_adminid, (TeamId))

    if team_detail is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="您所申请的团队不存在")

    guid = str(uuid.uuid1())
    sql_list = [team_sql.insert_team_notice,team_sql.insert_team_notice]
    args_list = [(userId,TeamId,"您正在申请加入 "+team_detail["Name"]+" 团队",1,2,userId,guid),
                 (team_detail["AdminUserId"],TeamId,"用户 "+request_helper.current_user_mush_login()["Name"]+" 正在申请加入团队",1,1,userId,guid)]

    data_register = mysql.operate__many(sql_list,args_list)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#获取团队消息
@app.route("/team/get_team_notice", methods=['POST'])
def get_team_notice():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    if page<=0:
        page=1
    if size<=0:
        size=10
    userId = request_helper.current_user_mush_login()["Id"]

    data = mysql.get_list(team_sql.select_team_notice_list,(userId,(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#同意加入团队
@app.route("/team/agree_join_team", methods=['POST'])
def agree_join_team():
    ApiResponse = api_response.ApiResponse()
    userId = request_helper.current_user_mush_login()["Id"]

    NoticeId = request.form.get("NoticeId", type=str, default=None)
    if NoticeId is None or NoticeId == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="团队通知id不能为空")

    exists_team = mysql.get_object(team_sql.exists_team_peoper_bynoticeid, (NoticeId))

    if exists_team is not None and exists_team["IsAdmin"] != 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="您不是团队管理员")
    if exists_team is  None or exists_team["Status"] != 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="您没有需要审核的团队消息")

    sql_list = [team_sql.insert_team_member,team_sql.update_team_admin_notice,team_sql.update_team_notice]
    args_list = [(exists_team["TeamId"],userId,userId),(userId,NoticeId),(userId, exists_team["UnionId"])]
    resultInt = mysql.operate__many(sql_list,args_list)
    if resultInt <=0:
        raise custom_error.CustomFlaskErr(status_code=500, message="审批失败")
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#不同意加入团队
@app.route("/team/disagree_join_team", methods=['POST'])
def disagree_join_team():
    ApiResponse = api_response.ApiResponse()
    userId = request_helper.current_user_mush_login()["Id"]

    NoticeId = request.form.get("NoticeId", type=str, default=None)
    if NoticeId is None or NoticeId == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="团队通知id不能为空")
    exists_team = mysql.get_object(team_sql.exists_team_peoper_bynoticeid, (NoticeId))
    if exists_team is not None and exists_team["IsAdmin"] != 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="您不是团队管理员")
    if exists_team is  None or exists_team["Status"] != 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="您没有需要审核的团队消息")

    sql_list = [team_sql.disagree_team_admin_notice,team_sql.disagree_team_notice]
    args_list = [(userId,NoticeId),(userId, exists_team["UnionId"])]
    resultInt = mysql.operate__many(sql_list,args_list)
    if resultInt <=0:
        raise custom_error.CustomFlaskErr(status_code=500, message="审批失败")
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)