#coding:utf-8
from flask import request
import uuid

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import sys_role_logic


#获取角色列表
@app.route("/backweb/system/select_sys_role_list", methods=['POST'])
def select_sys_role_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    user = request_back_helper.current_user_mush_login()
    data = sys_role_logic.select_sys_role_list(name)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取角色信息
@app.route("/backweb/system/select_sys_role_info", methods=['POST'])
def select_sys_role_info():
    ApiResponse = api_response.ApiResponse()
    role_id = request.form.get("role_id", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    roleinfo = sys_role_logic.select_sys_role_info(role_id)
    if roleinfo !=None and any(roleinfo):
        ApiResponse.data=roleinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="角色不存在")


#修改角色信息
@app.route("/backweb/system/update_sys_role", methods=['POST'])
def update_sys_role():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("name", type=str, default=None)
    remark = request.form.get("remark", type=str, default=None)
    role_id= request.form.get("role_id", type=int, default=None)
    permissionids = request.form.get("permissionids", type=str, default="")
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_role_logic.update_sys_role(name,remark,role_id,user["UserId"])
    data_register= sys_role_logic.insert_role_permission(role_id,permissionids,user["UserId"])
    ApiResponse.message = "修改成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#删除角色信息
@app.route("/backweb/system/delete_sys_role", methods=['POST'])
def delete_sys_role():
    ApiResponse = api_response.ApiResponse()
    role_id= request.form.get("role_id", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_role_logic.delete_sys_role(role_id, user["UserId"])
    ApiResponse.message = "删除成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


#新增角色信息
@app.route("/backweb/system/insert_sys_role", methods=['POST'])
def insert_sys_role():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("name", type=str, default=None)
    remark = request.form.get("remark", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  sys_role_logic.insert_sys_role(name,remark,user["UserId"])
    ApiResponse.message = "新增成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


#角色菜单受权信息
@app.route("/backweb/system/insert_role_permission", methods=['POST'])
def insert_role_permission():
    ApiResponse = api_response.ApiResponse()
    role_id= request.form.get("role_id", type=int, default=None)
    permissionId = request.form.get("permissionId", type=str, default="")
    user = request_back_helper.current_user_mush_login()
    data_register= sys_role_logic.insert_role_permission(role_id,permissionId,user["UserId"])
    ApiResponse.message = "受权成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#获取菜单列表
@app.route("/backweb/system/select_permission_list", methods=['POST'])
def select_permission_list():
    ApiResponse = api_response.ApiResponse()
    user = request_back_helper.current_user_mush_login()
    data = sys_role_logic.select_permission_list(user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取角色菜单ID列表
@app.route("/backweb/system/select_role_permission_list", methods=['POST'])
def select_role_permission_list():
    ApiResponse = api_response.ApiResponse()
    role_id = request.form.get("role_id", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data = sys_role_logic.select_role_permission_list(role_id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取角色列表
@app.route("/backweb/system/select_user_role_list", methods=['POST'])
def select_user_role_list():
    ApiResponse = api_response.ApiResponse()
    user_id = request.form.get("user_id", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data = sys_role_logic.select_user_role_list(user_id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)