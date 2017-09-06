# coding:utf-8
from flask import request
import uuid
import hashlib
from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import user_logic, team_logic


# 用户列表
@app.route("/backweb/user/select_user_list", methods=['POST'])
def select_user_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data, listCount = user_logic.select_user_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    if listCount is not None:
        ApiResponse.listCount = listCount["listCount"]
    return api_response.response_return(ApiResponse)


# 获取用户信息
@app.route("/backweb/user/select_user_info", methods=['POST'])
def select_user_info():
    ApiResponse = api_response.ApiResponse()
    userid = request.form.get("userid", type=str, default=None)

    if userid == None or userid == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    userinfo = user_logic.select_user_info(userid)
    if userinfo != None and any(userinfo):
        ApiResponse.data = userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")


# 修改用户信息
@app.route("/backweb/user/back_updateuserinfo", methods=['POST'])
def back_updateuserinfo():
    ApiResponse = api_response.ApiResponse()
    userid = request.form.get("UserId", type=str, default=None)
    account = request.form.get("Account", type=str, default=None)
    phone = request.form.get("Phone", type=str, default=None)
    password = request.form.get("Password", type=str, default=None)
    userType = request.form.get("UserType", type=int, default=0)
    name = request.form.get("Name", type=str, default=None)
    sex = request.form.get("Sex", type=int, default=0)
    age = request.form.get("Age", type=int, default=0)
    education = request.form.get("Education", type=str, default=None)
    address = request.form.get("Address", type=str, default=None)
    email = request.form.get("Email", type=str, default=None)
    headImage = request.form.get("HeadImage", type=str, default=None)
    IDCard = request.form.get("IDCard", type=str, default=None)
    IDCardJust = request.form.get("IDCardJust", type=str, default=None)
    IDCardBack = request.form.get("IDCardBack", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register = user_logic.update_userinfo(account, phone, password, userType, name, sex, age, education, address,
                                               email, headImage, IDCard, IDCardJust, IDCardBack, userid, user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


# 删除用户信息
@app.route("/backweb/user/delete_user", methods=['POST'])
def delete_user():
    ApiResponse = api_response.ApiResponse()
    userid = request.form.get("UserId", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register = user_logic.delete_user(userid, user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


# 修改用户信息
@app.route("/backweb/user/back_insert_userinfo", methods=['POST'])
def back_insert_userinfo():
    ApiResponse = api_response.ApiResponse()
    account = request.form.get("Account", type=str, default=None)
    phone = request.form.get("Phone", type=str, default=None)
    password = request.form.get("Password", type=str, default=None)
    userType = request.form.get("UserType", type=int, default=0)
    name = request.form.get("Name", type=str, default=None)
    sex = request.form.get("Sex", type=int, default=0)
    age = request.form.get("Age", type=int, default=0)
    education = request.form.get("Education", type=str, default=None)
    address = request.form.get("Address", type=str, default=None)
    email = request.form.get("Email", type=str, default=None)
    headImage = request.form.get("HeadImage", type=str, default=None)
    if headImage is None or headImage == '':
        headImage = "files/person.jpg"
    IDCard = request.form.get("IDCard", type=str, default=None)
    IDCardJust = request.form.get("IDCardJust", type=str, default=None)
    IDCardBack = request.form.get("IDCardBack", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    password = hashlib.md5(password.encode(encoding='gb2312')).hexdigest()

    data_register = user_logic.insert_userinfo(guid, account, phone, password, userType, name, sex, age, education,
                                               address, email, headImage, IDCard, IDCardJust, IDCardBack,
                                               user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")
