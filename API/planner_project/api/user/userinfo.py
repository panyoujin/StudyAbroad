#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response,custom_error,request_helper
from planner_project.data_access import mysql
from planner_project.sql.user import user_info_sql,user_sql
from planner_project.sql.basic import  verification_code_sql

#修改用户
@app.route("/userinfo/updateuserinfo", methods=['POST'])
def updateuserinfo():
    print("updateuserinfo")
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("name", type=str, default=None)
    sex = request.form.get("sex", type=int, default=0)
    age = request.form.get("age", type=int, default=0)
    education = request.form.get("education", type=str, default=None)
    address = request.form.get("address", type=str, default=None)
    email = request.form.get("email", type=str, default=None)
    user = request_helper.current_user_mush_login()
    data_register = mysql.operate_object(user_info_sql.update_user_info,(name,sex,age,education,address,email,user["Id"],user["Id"]))
    if data_register > 0:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#修改用户头像
@app.route("/userinfo/updateheadimage", methods=['POST'])
def updateheadimage():
    ApiResponse = api_response.ApiResponse()
    headimage= request.form.get("headimage", type=str, default=None)
    user = request_helper.current_user_mush_login()
    data_register = mysql.operate_object(user_info_sql.update_user_headimage,(headimage,user["Id"],user["Id"]))
    if data_register > 0:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#获取用户信息
@app.route("/userinfo/get_user_info", methods=['POST'])
def get_user_info():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        userid = request_helper.current_user_mush_login()["Id"]

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    userinfo = mysql.get_object(user_info_sql.select_userinfo_by_id,(userid))
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")

#忘记密码功能  修改用户密码
@app.route("/userinfo/update_user_password", methods=['POST'])
def update_user_password():
    ApiResponse = api_response.ApiResponse()
    Phone= request.form.get("Phone", type=str, default=None)
    NewPassword = request.form.get("NewPassword", type=str, default=None)
    VCode = request.form.get("VCode", type=str, default=None)
    if Phone == None or Phone=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="手机号码不能为空")
    if NewPassword == None or NewPassword=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="新密码不能为空")
    if VCode == None or VCode=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码不能为空")

    vocde_exists = mysql.get_object(verification_code_sql.select_verification_lastcode, (Phone,2))
    if vocde_exists== None :
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码已失效")
    if vocde_exists["VCode"]!=VCode:
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码不正确")
    #设置验证码已读
    mysql.operate_object(verification_code_sql.update_verificatioin_vcode,(vocde_exists["Id"]))

    data_exce = mysql.operate_object(user_sql.update_user_password,(NewPassword,Phone))

    if data_exce > 0:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#用户相册列表
@app.route("/userinfo/user_album", methods=['POST'])
def user_album():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user_mush_login()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(user_info_sql.select_user_album,(user["Id"],(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#获取最新合同
@app.route("/userinfo/new_contract", methods=['POST'])
def new_contract():
    ApiResponse = api_response.ApiResponse()
    data = mysql.get_object(user_info_sql.select_new_contract,())
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)