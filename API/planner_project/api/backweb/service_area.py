#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import service_area_logic


#获取区域列表
@app.route("/backweb/system/select_service_area_list", methods=['POST'])
def select_service_area_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = service_area_logic.select_service_area_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取区域信息
@app.route("/backweb/system/select_service_area_info", methods=['POST'])
def select_service_area_info():
    ApiResponse = api_response.ApiResponse()
    areaId= request.form.get("areaId", type=int, default=None)

    if areaId == None or areaId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数areaId不能为空")
    userinfo = service_area_logic.select_service_area_info(areaId)
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="区域不存在")


#修改区域信息
@app.route("/backweb/system/update_service_area_info", methods=['POST'])
def update_service_area_info():
    ApiResponse = api_response.ApiResponse()
    areaId= request.form.get("AreaId", type=int, default=None)
    name= request.form.get("Name", type=str, default=None)
    description = request.form.get("Description", type=str, default=0)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  service_area_logic.update_service_area_info(name,description,isTop,sort,user["UserId"],areaId)
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#删除区域信息
@app.route("/backweb/system/delete_service_area", methods=['POST'])
def delete_service_area():
    ApiResponse = api_response.ApiResponse()
    areaId= request.form.get("areaId", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  service_area_logic.delete_service_area(areaId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")


#修改服务信息
@app.route("/backweb/system/insert_service_area", methods=['POST'])
def insert_service_area():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("Name", type=str, default=None)
    description = request.form.get("Description", type=str, default=0)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  service_area_logic.insert_service_area(name,description,isTop,sort,user["UserId"])
    if data_register:
        ApiResponse.message = "新增成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")

