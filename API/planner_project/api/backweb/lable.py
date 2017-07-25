#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import lable_logic


#获取标签列表
@app.route("/backweb/system/select_lable_list", methods=['POST'])
def select_lable_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = lable_logic.select_lable_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取标签信息
@app.route("/backweb/system/select_lable_info", methods=['POST'])
def select_lable_info():
    ApiResponse = api_response.ApiResponse()
    lableId= request.form.get("lableId", type=int, default=None)

    if lableId == None or lableId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数lableId不能为空")
    lableinfo = lable_logic.select_lable_info(lableId)
    if lableinfo !=None and any(lableinfo):
        ApiResponse.data=lableinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="标签不存在")


#修改标签信息
@app.route("/backweb/system/update_lable_info", methods=['POST'])
def update_lable_info():
    ApiResponse = api_response.ApiResponse()
    lableId= request.form.get("lableId", type=int, default=None)
    name= request.form.get("Name", type=str, default=None)
    description = request.form.get("Description", type=str, default=0)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  lable_logic.update_lable_info(name,description,isTop,sort,user["UserId"],lableId)
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#删除标签信息
@app.route("/backweb/system/delete_lable", methods=['POST'])
def delete_lable():
    ApiResponse = api_response.ApiResponse()
    lableId= request.form.get("lableId", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  lable_logic.delete_lable(lableId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")



#新增标签信息
@app.route("/backweb/system/insert_lable", methods=['POST'])
def insert_lable():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("Name", type=str, default=None)
    description = request.form.get("Description", type=str, default=0)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  lable_logic.insert_lable(name,description,isTop,sort,user["UserId"])
    if data_register:
        ApiResponse.message = "新增成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")

