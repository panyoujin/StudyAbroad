#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.service import service_sql
from planner_project.sql.basic import basic_sql

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



#获取基础信息
@app.route("/basic/platforminfo", methods=['POST'])
def platforminfo():
    ApiResponse = api_response.ApiResponse()
    data= mysql.get_object(basic_sql.select_platforminfo, ())
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#获取基础配置
@app.route("/basic/get_config", methods=['POST'])
def get_config():
    ApiResponse = api_response.ApiResponse()
    Key = request.form.get("Key", type=str, default=None)
    if Key is None or Key == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="key不能为空")
    data= mysql.get_object(basic_sql.get_config, (Key))
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#获取基础配置列表
@app.route("/basic/get_config_list", methods=['POST'])
def get_config_list():
    ApiResponse = api_response.ApiResponse()
    Key = request.form.get("Key", type=str, default=None)
    if Key is None or Key == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="key不能为空")
    data= mysql.get_object(basic_sql.get_config_list, (Key))
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
#获取基础配置列表
@app.route("/basic/get_config_all", methods=['POST'])
def get_config_all():
    ApiResponse = api_response.ApiResponse()
    data= mysql.get_list(basic_sql.get_config_all, ())
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
