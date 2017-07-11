#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response,custom_error
from planner_project.data_access import mysql
from planner_project.sql.user import user_sql
from planner_project.sql.basic import verification_code_sql

@app.route("/helloworld", methods=['GET'])
def helloworld():
    return "旭江超帅"

#注册用户
@app.route("/user/register", methods=['POST'])
def register():
    ApiResponse = api_response.ApiResponse()
    Account = request.form.get("Account", type=str, default=None)
    Password = request.form.get("Password", type=str, default=None)
    VCode = request.form.get("VCode", type=str, default=None)
    if Account == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="账号不能为空")
    if Password == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="密码不能为空")
    if VCode == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码不能为空")

    data_exists = mysql.get_list(user_sql.select_exists_user,(Account))
    if len(data_exists):
        raise custom_error.CustomFlaskErr(status_code=500, message="账号已经存在")

    vocde_exists = mysql.get_object(verification_code_sql.select_verification_lastcode, (Account,1))
    if vocde_exists== None :
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码已失效")
    if vocde_exists["VCode"]!=VCode:
        raise custom_error.CustomFlaskErr(status_code=500, message="验证码不正确")
    #设置验证码已读
    mysql.operate_object(verification_code_sql.update_verificatioin_vcode,(vocde_exists["Id"]))

    guid = str(uuid.uuid1())
    sql_list = [user_sql.insert_user,user_sql.insert_userinfo]
    args_list = [(guid,Account,Password,Account),(guid)]

    data_register = mysql.operate__many(sql_list,args_list)
    if data_register > 0:
        ApiResponse.message = "注册成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    raise custom_error.CustomFlaskErr(status_code=500, message="注册失败")



