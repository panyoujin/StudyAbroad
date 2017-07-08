#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response,request_back_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import demand_service_sql

#获取需求列表
@app.route("/backweb/demand/select_demand_list", methods=['POST'])
def select_demand_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(demand_service_sql.select_demand_list, ((page - 1) * size, size))
    listCount = mysql.get_object(demand_service_sql.select_demand_count, ())

    if listCount is not None:
        ApiResponse.data = data
        ApiResponse.listCount = listCount["count"]
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#修改需求状态
@app.route("/backweb/demand/update_demand_status", methods=['POST'])
def update_demand_status():
    userId = request_back_helper.current_user_mush_login()["UserId"]

    ApiResponse = api_response.ApiResponse()
    id = request.form.get("id", type=str, default=None)
    IsUndertake = request.form.get("IsUndertake", type=int, default=-1)
    IsTop = request.form.get("IsTop", type=int, default=-1)

    if id is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确")
    if IsUndertake == -1:
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确")
    if IsTop==-1 :
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确")


    if IsUndertake==2:
        sql_list = [demand_service_sql.update_demand_status,
                    demand_service_sql.update_demand_undertake_status]
        args_list = [(IsTop, IsUndertake, userId,id),
                     ( userId,id),]
        mysql.operate__many(sql_list,args_list)
    else :
        mysql.operate_object(demand_service_sql.update_demand_status,(IsTop, IsUndertake, userId,id))

    ApiResponse = api_response.ApiResponse()
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)
