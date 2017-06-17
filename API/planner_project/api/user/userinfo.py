#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response,custom_error,request_helper
from planner_project.data_access import mysql
from planner_project.sql.user import user_info_sql

#修改用户
@app.route("/userinfo/updateuserinfo", methods=['POST'])
def updateuserinfo():
    ApiResponse = api_response.ApiResponse()
    name= request.form.get("name", type=str, default=None)
    sex = request.form.get("sex", type=int, default=0)
    age = request.form.get("age", type=int, default=0)
    education = request.form.get("education", type=str, default=None)
    address = request.form.get("address", type=str, default=None)
    email = request.form.get("email", type=str, default=None)
    user = request_helper.current_user()
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
    user = request_helper.current_user()
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