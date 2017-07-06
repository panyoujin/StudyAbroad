#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.backweb import demand_service_sql

#用户列表
@app.route("/backweb/demand/select_demand_undertake_list", methods=['POST'])
def select_demand_undertake_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(demand_service_sql.select_demand_undertake_list, ((page - 1) * size, size))
    listCount = mysql.get_object(demand_service_sql.select_demand_undertake_count, ())

    if listCount is not None:
        ApiResponse.data = data
        ApiResponse.listCount = listCount["count"]

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)
