#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,custom_error,request_helper
from planner_project.logic import  user_logic


#用户列表
@app.route("/back_web/user/select_user_list", methods=['POST'])
def select_user_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data =user_logic.select_user_list(name,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改用户信息
@app.route("/back_web/user/back_updateuserinfo", methods=['POST'])
def back_updateuserinfo():
    print("updateuserinfo")
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    name= request.form.get("name", type=str, default=None)
    sex = request.form.get("sex", type=int, default=0)
    age = request.form.get("age", type=int, default=0)
    education = request.form.get("education", type=str, default=None)
    address = request.form.get("address", type=str, default=None)
    email = request.form.get("email", type=str, default=None)
    user = request_helper.current_user()
    data_register =  user_logic.update_userinfo(name,sex,age,education,address,email,userid,user["Id"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#获取用户信息
@app.route("/back_web/user/select_user_info", methods=['POST'])
def select_user_info():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    userinfo = user_logic.select_user_info(userid)
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")