#coding:utf-8
from flask import request,session
import uuid
import time
import json
from planner_project import app
from planner_project.common import api_response,request_helper
from planner_project.data_access import mysql
from planner_project.sql.user import user_sql

#登录
@app.route("/user/login", methods=['POST'])
def login():
    ApiResponse = api_response.ApiResponse
    Account = request.form.get("Account", type=str, default=None)
    Password = request.form.get("Password", type=str, default=None)
    if Account == None:
        ApiResponse.message = "账号不能为空"
        ApiResponse.status = 500
        return api_response.response_return(ApiResponse)
    if Password == None:
        ApiResponse.message = "密码不能为空"
        ApiResponse.status = 500
        return api_response.response_return(ApiResponse)
    guid = str(uuid.uuid1())
    ip = request.remote_addr
    count = mysql.operate_object(user_sql.update_user_token,(guid,ip,Account,Password))
    if count<=0 :
        ApiResponse.message = "账号或密码不正确"
        ApiResponse.status = 500
        return api_response.response_return(ApiResponse)
    #写token
    # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = mysql.get_list(user_sql.select_user_info,(Account))
    #session[guid]=json.dumps(user)
    data = {"token":guid,"datetime":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
    ApiResponse.message = "登录成功"
    ApiResponse.status = 200
    ApiResponse.data=json.dumps(data)
    return api_response.response_return(ApiResponse)


#登录
@app.route("/user/get_login_user", methods=['POST'])
def get_login_user():
    ApiResponse = api_response.ApiResponse
    user = request_helper.current_user()
    if any(user):
        ApiResponse.message = "成功"
        ApiResponse.status = 200
        ApiResponse.data = user
        return api_response.response_return(ApiResponse)
    ApiResponse.message = "请先登录"
    ApiResponse.status = 600
    return api_response.response_return(ApiResponse)

