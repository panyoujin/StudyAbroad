#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.user import user_sql


#注册用户
@app.route("/user/register", methods=['POST'])
def register():
    ApiResponse = api_response.ApiResponse
    Account = request.form.get("Account", type=str, default=None)
    Password = request.form.get("Password", type=str, default=None)
    if Account == None:
        ApiResponse.message = "账号不能为空"
        ApiResponse.status = 0
        return api_response.response_return(ApiResponse)
    if Password == None:
        ApiResponse.message = "密码不能为空"
        ApiResponse.status = 0
        return api_response.response_return(ApiResponse)
    data_exists = mysql.get_list(user_sql.select_exists_user,(Account))
    if len(data_exists):
        ApiResponse.message = "账号已经存在"
        ApiResponse.status = 0
        return api_response.response_return(ApiResponse)

    sql_list = [user_sql.insert_user,user_sql.insert_userinfo]
    args_list = [(str(uuid.uuid1()),Account,Password),(Account)]

    data_register = mysql.operate__many(sql_list,args_list)
    if data_register > 0:
        ApiResponse.message = "注册成功"
        ApiResponse.status = 1
        return api_response.response_return(ApiResponse)

    # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ApiResponse.message = "注册失败"
    ApiResponse.status = 1
    return api_response.response_return(ApiResponse)




