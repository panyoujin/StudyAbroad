#coding:utf-8
from flask import request,session
import uuid
import time
import json
from planner_project import app
from planner_project.common import api_response
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
    count = mysql.operate_object(user_sql.update_user_token,(guid,"172.17.16.191",Account,Password))
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
    token = request.form.get("token", type=str, default=None)
    if token == None:
        ApiResponse.message = "请先登录"
        ApiResponse.status = 600
        return api_response.response_return(ApiResponse)
    # if session[token] != None:
    #     ApiResponse.message = "成功"
    #     ApiResponse.status = 200
    #     ApiResponse.data = json.dumps(session[token])
    #     return api_response.response_return(ApiResponse)
    #本地缓存中不存在去数据库拿
    user = mysql.get_list(user_sql.select_user_login_info,(token))
    print(user)
    if any(user):
        ApiResponse.message = "成功"
        ApiResponse.status = 200
        ApiResponse.data = json.dumps(user, cls=api_response.ComplexEncoder)
        return api_response.response_return(ApiResponse)
    ApiResponse.message = "请先登录"
    ApiResponse.status = 600
    return api_response.response_return(ApiResponse)

