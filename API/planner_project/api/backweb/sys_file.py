#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import sys_file_logic


#获取资料列表
@app.route("/backweb/system/select_sys_file_list", methods=['POST'])
def select_sys_file_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = sys_file_logic.select_sys_file_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取资料信息
@app.route("/backweb/system/select_sys_file_info", methods=['POST'])
def select_sys_file_info():
    ApiResponse = api_response.ApiResponse()
    fileId= request.form.get("fileId", type=int, default=None)

    if fileId == None or fileId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数fileId不能为空")
    fileInfo = sys_file_logic.select_sys_file_info(fileId)
    if fileInfo !=None and any(fileInfo):
        ApiResponse.data=fileInfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="资料不存在")


#修改资料信息
@app.route("/backweb/system/update_sys_file_info", methods=['POST'])
def update_sys_file_info():
    ApiResponse = api_response.ApiResponse()
    fileId= request.form.get("fileId", type=int, default=None)
    name= request.form.get("Name", type=str, default=None)
    fileUrl = request.form.get("fileUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_file_logic.update_sys_file_info(name,fileUrl,isTop,sort,user["UserId"],fileId)
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#删除资料信息
@app.route("/backweb/system/delete_sys_file", methods=['POST'])
def delete_sys_file():
    ApiResponse = api_response.ApiResponse()
    fileId= request.form.get("fileId", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_file_logic.delete_sys_file(fileId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")



#新增资料信息
@app.route("/backweb/system/insert_sys_file", methods=['POST'])
def insert_sys_file():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("Name", type=str, default=None)
    fileUrl = request.form.get("fileUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_file_logic.insert_sys_file(name,fileUrl,isTop,sort,user["UserId"])
    if data_register:
        ApiResponse.message = "新增成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")

