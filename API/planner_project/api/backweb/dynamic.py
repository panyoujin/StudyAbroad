#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import dynamic_logic


#获取资料列表
@app.route("/backweb/system/select_ms_dynamic_list", methods=['POST'])
def select_ms_dynamic_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    content = request.form.get("content", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = dynamic_logic.select_dynamic_list(content, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取资料信息
@app.route("/backweb/system/select_ms_dynamic_info", methods=['POST'])
def select_ms_dynamic_info():
    ApiResponse = api_response.ApiResponse()
    dynamicId= request.form.get("dynamicId", type=int, default=None)

    if dynamicId == None or dynamicId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数dynamicId不能为空")
    fileInfo = dynamic_logic.select_dynamic_info(dynamicId)
    if fileInfo !=None and any(fileInfo):
        ApiResponse.data=fileInfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="资料不存在")


#修改资料信息
@app.route("/backweb/system/update_ms_dynamic_info", methods=['POST'])
def update_ms_dynamic_info():
    ApiResponse = api_response.ApiResponse()
    dynamicId= request.form.get("dynamicId", type=int, default=None)
    content= request.form.get("content", type=str, default=None)
    imageUrl = request.form.get("imageUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    readCount = request.form.get("readCount", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  dynamic_logic.update_dynamic_info(content,imageUrl,isTop,sort,readCount,user["UserId"],dynamicId)
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#删除资料信息
@app.route("/backweb/system/delete_ms_dynamic", methods=['POST'])
def delete_ms_dynamic():
    ApiResponse = api_response.ApiResponse()
    dynamicId= request.form.get("dynamicId", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  dynamic_logic.delete_dynamic(dynamicId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")



#新增资料信息
@app.route("/backweb/system/insert_ms_dynamic", methods=['POST'])
def insert_ms_dynamic():
    ApiResponse = api_response.ApiResponse()
    content= request.form.get("content", type=str, default=None)
    imageUrl = request.form.get("imageUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    readCount = request.form.get("readCount", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  dynamic_logic.insert_dynamic(content,imageUrl,isTop,sort,readCount,user["UserId"])
    if data_register:
        ApiResponse.message = "新增成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")

