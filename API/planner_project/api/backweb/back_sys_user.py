#coding:utf-8
from flask import request
import uuid

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import sys_user_logic


#获取用户列表
@app.route("/backweb/system/select_sys_user_list", methods=['POST'])
def select_sys_user_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    uname = request.form.get("uname", type=str, default="")
    nname = request.form.get("nname", type=str, default="")
    phone = request.form.get("phone", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    user = request_back_helper.current_user_mush_login()
    data = sys_user_logic.select_sys_user_list(uname,nname,phone, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取用户信息
@app.route("/backweb/system/select_sys_user_info", methods=['POST'])
def select_sys_user_info():
    ApiResponse = api_response.ApiResponse()
    user_id = request.form.get("user_id", type=str, default="")
    user = request_back_helper.current_user_mush_login()
    userinfo = sys_user_logic.select_sys_user_info(user_id)
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")


#修改用户信息
@app.route("/backweb/system/update_sys_user", methods=['POST'])
def update_sys_user():
    ApiResponse = api_response.ApiResponse()
    user_id= request.form.get("user_id", type=str, default=None)
    uname= request.form.get("uname", type=str, default=None)
    nname = request.form.get("nname", type=str, default=None)
    phone = request.form.get("phone", type=str, default=None)
    email = request.form.get("email", type=str, default=None)
    role_id= request.form.get("role_id", type=int, default=None)
    descript = request.form.get("descript", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_user_logic.update_sys_user(uname,nname,phone,email,descript,user_id,user["UserId"])
    sys_user_logic.update_sys_userrole(user_id,role_id,user["UserId"])
    ApiResponse.message = "修改成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#删除用户信息
@app.route("/backweb/system/delete_sys_user", methods=['POST'])
def delete_sys_user():
    ApiResponse = api_response.ApiResponse()
    user_id= request.form.get("user_id", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_user_logic.delete_sys_user(user_id, user["UserId"])
    ApiResponse.message = "删除成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)




#新增用户信息
@app.route("/backweb/system/insert_sys_user", methods=['POST'])
def insert_sys_user():
    ApiResponse = api_response.ApiResponse()
    uname= request.form.get("uname", type=str, default=None)
    user = sys_user_logic.select_sys_user_info_by_username(uname)
    if user!=None and any(user):
        raise custom_error.CustomFlaskErr(status_code=500, message="用户已存在")
    nname = request.form.get("nname", type=str, default=None)
    phone = request.form.get("phone", type=str, default=None)
    email = request.form.get("email", type=str, default=None)
    descript = request.form.get("descript", type=str, default=None)
    guid = str(uuid.uuid1())
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_user_logic.insert_sys_user(guid,uname,nname,phone,email,descript,user["UserId"])
    ApiResponse.message = "新增成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#角色菜单受权信息
@app.route("/backweb/system/update_sys_userrole", methods=['POST'])
def update_sys_userrole():
    ApiResponse = api_response.ApiResponse()
    user_id= request.form.get("user_id", type=str, default=None)
    role_id = request.form.get("role_id", type=str, default="")
    user = request_back_helper.current_user_mush_login()
    data_register= sys_user_logic.update_sys_userrole(user_id,role_id,user["UserId"])
    ApiResponse.message = "受权成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)