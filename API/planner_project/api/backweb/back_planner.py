#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import back_planner_logic


#用户列表
@app.route("/backweb/planner/select_planner_list", methods=['POST'])
def select_planner_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = back_planner_logic.select_planner_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取用户信息
@app.route("/backweb/planner/select_planner_info", methods=['POST'])
def select_planner_info():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    userinfo = back_planner_logic.select_planner_info(userid)
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")

