#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.logic import  dynamic_logic
import  uuid


#获取动态列表
@app.route("/dynamic/select_dynamic_list", methods=['POST'])
def select_dynamic_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    data = dynamic_logic.select_dynamic_list(page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#获取指定的用户动摇列表
@app.route("/dynamic/select_user_dynamic_list", methods=['POST'])
def select_user_dynamic_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    userid= request.form.get("userid", type=str, default=None)
    data = dynamic_logic.select_user_dynamic_list(userid,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#新增动态
@app.route("/dynamic/insert_dynanic", methods=['POST'])
def insert_dynanic():
    ApiResponse = api_response.ApiResponse()
    content = request.form.get("content", type=str, default=None)
    imageUrl = request.form.get("imageUrl", type=str, default=None)
    user = request_helper.current_user_mush_login()
    data=dynamic_logic.insert_dynanic(user["Id"],content,imageUrl)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#获取指定的动态
@app.route("/dynamic/select_dynamic_info", methods=['POST'])
def select_dynamic_info():
    ApiResponse = api_response.ApiResponse()
    dynamicId = request.form.get("dynamicId", type=int, default=None)
    dynamic= dynamic_logic.select_dynamic_info(dynamicId)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data=dynamic
    return api_response.response_return(ApiResponse)

