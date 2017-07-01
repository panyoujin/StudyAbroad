#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import user_logic,team_logic

#团队列表
@app.route("/backweb/team/select_team_list", methods=['POST'])
def select_team_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = team_logic.select_team_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取指定团队成员列表
@app.route("/backweb/team/select_teamm_ember_list", methods=['POST'])
def select_teamm_ember_list():
    ApiResponse = api_response.ApiResponse()
    teamid= request.form.get("teamId", type=str, default=None)

    if teamid == None or teamid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数teamId不能为空")
    data = team_logic.select_teamm_ember_list(teamid)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#删除团队
@app.route("/backweb/team/delete_team", methods=['POST'])
def delete_team():
    ApiResponse = api_response.ApiResponse()
    teamId= request.form.get("teamId", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  team_logic.delete_team(teamId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")

#删除团队成员
@app.route("/backweb/team/delete_team_member", methods=['POST'])
def delete_team_member():
    ApiResponse = api_response.ApiResponse()
    teamId= request.form.get("teamId", type=str, default=None)
    userid= request.form.get("UserId", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  team_logic.delete_team_member(teamId,userid, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")
