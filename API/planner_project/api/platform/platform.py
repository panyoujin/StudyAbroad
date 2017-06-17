#coding:utf-8
import json

from flask import request

from planner_project import app
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.platform import platform_sql


#平台合作资源
@app.route("/platform/cooperation", methods=['POST'])
def cooperation():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    data = mysql.get_list(platform_sql.select_platform_cooperation, ((page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)