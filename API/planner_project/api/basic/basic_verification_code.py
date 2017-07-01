#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.basic import verification_code_sql
import  random

#服务区域列表
@app.route("/basic/get_vcode", methods=['POST'])
def get_vcode():
    Phone = request.form.get("Phone", type=str, default=None)
    if Phone == None or Phone=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="手机号码不能为空")

    CodeType = request.form.get("CodeType", type=int, default=None)
    if CodeType == None or CodeType=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="短信类型不能为空")

    vcode=str(random.randint(0, 9))
    vcode+=str(random.randint(0, 9))
    vcode+=str(random.randint(0, 9))
    vcode+=str(random.randint(0, 9))

    ApiResponse = api_response.ApiResponse()
    data = mysql.operate_object(verification_code_sql.insert_verification_codel,(Phone,vcode,CodeType))
    print(data)
    ApiResponse.message = "成功"
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)