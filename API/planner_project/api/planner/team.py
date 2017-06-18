#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.logic import  team_logic


#团队列表
@app.route("/team/team_list", methods=['POST'])
def team_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = team_logic.get_team_list(user["Id"],name,(page-1)*size,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#团队成员列表 还需要返回是否管理员
@app.route("/planner/team_member_list", methods=['POST'])
def team_member_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    temaId = request.form.get("temaId", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = team_logic.get_team_member_list(temaId,(page-1)*size,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

