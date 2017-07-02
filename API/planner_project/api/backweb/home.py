#coding:utf-8
from flask import request,session,make_response
import uuid
import time
import json
from planner_project import app
from planner_project.common import api_response,custom_error,request_back_helper
from planner_project.data_access import mysql
from planner_project.sql.backweb import home_sql

#登录
@app.route("/backweb/home/login", methods=['POST'])
def home_login():
    print("home_login")
    ApiResponse = api_response.ApiResponse()
    UserName = request.form.get("UserName", type=str, default=None)
    Password = request.form.get("Password", type=str, default=None)
    if UserName == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="账号不能为空")
    if Password == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="密码不能为空")
    guid = str(uuid.uuid1())
    ip = request.remote_addr
    count = mysql.operate_object(home_sql.update_sysuser_token,(guid,ip,UserName,Password))
    if count<=0 :
        raise custom_error.CustomFlaskErr(status_code=500, message="账号或密码不正确")
    #写token
    # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = mysql.get_object(home_sql.select_sysuser_login_info, (guid))
    session["user"]=user
    data = {"token":guid,"datetime":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"user":user}
    ApiResponse.message = "登录成功"
    ApiResponse.status = 200
    ApiResponse.data=data
    return api_response.response_return(ApiResponse)



#登录
@app.route("/backweb/home/get_current_login_user", methods=['POST'])
def get_current_login_user():
    ApiResponse = api_response.ApiResponse()
    user = request_back_helper.current_user_mush_login()
    ApiResponse.message = "获取成功"
    ApiResponse.status = 200
    ApiResponse.data=user
    return api_response.response_return(ApiResponse)
