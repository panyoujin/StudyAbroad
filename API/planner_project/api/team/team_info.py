#coding:utf-8
import json,uuid

from flask import request
from planner_project.common import api_response,request_helper,custom_error
from planner_project import app
from planner_project.data_access import mysql
from planner_project.sql.team import team_sql

#申请加入团队
@app.route("/team/join_team", methods=['POST'])
def join_team():
    ApiResponse = api_response.ApiResponse()

    userId = request_helper.current_user_mush_login()["Id"]

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
    args_list = [(userId,TeamId,"您正在申请加入 "+team_detail["Name"]+" 团队",1,2,userId,guid),(team_detail["AdminUserId"],TeamId,"用户 "+request_helper.current_user_mush_login()["Name"]+" 正在申请加入团队",1,1,userId,guid)]

    data_register = mysql.operate__many(sql_list,args_list)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#申请加入团队
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
    print(userId)
    data = mysql.get_list(team_sql.select_team_notice_list,(userId,(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
