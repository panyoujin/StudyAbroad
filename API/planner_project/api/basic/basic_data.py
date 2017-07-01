#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper
from planner_project.data_access import mysql
from planner_project.sql.service import service_sql

#服务区域列表
@app.route("/basic/arealist", methods=['POST'])
def area_list():
    ApiResponse = api_response.ApiResponse()
    data = mysql.get_list(service_sql.select_area_list,())
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#认证服务列表
@app.route("/basic/servicelist", methods=['POST'])
def service_list():
    ApiResponse = api_response.ApiResponse()
    data = mysql.get_list(service_sql.select_service_list,())
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)