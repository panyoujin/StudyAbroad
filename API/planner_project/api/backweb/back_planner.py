#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import back_planner_logic
from planner_project.data_access import mysql
from planner_project.sql.backweb import planner_sql


#用户列表
@app.route("/backweb/planner/select_planner_list", methods=['POST'])
def select_planner_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data, listCount = back_planner_logic.select_planner_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    if listCount is not None:
        ApiResponse.listCount = listCount["listCount"]
    return api_response.response_return(ApiResponse)



#获取用户信息
@app.route("/backweb/planner/select_planner_info", methods=['POST'])
def select_planner_info():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    userinfo = back_planner_logic.select_planner_info(userid)
    if userinfo !=None and any(userinfo):
        ApiResponse.data=userinfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="用户不存在")

# 修改用户信息
@app.route("/backweb/user/back_updateplanner", methods=['POST'])
def back_updateplanner():
    ApiResponse = api_response.ApiResponse()
    userid = request.form.get("UserId", type=str, default=None)
    account = request.form.get("Account", type=str, default=None)
    phone = request.form.get("Phone", type=str, default=None)
    userType = request.form.get("UserType", type=int, default=0)
    name = request.form.get("Name", type=str, default=None)
    realName = request.form.get("RealName", type=str, default=None)
    sex = request.form.get("Sex", type=int, default=0)
    age = request.form.get("Age", type=int, default=0)
    education = request.form.get("Education", type=str, default=None)
    address = request.form.get("Address", type=str, default=None)
    email = request.form.get("Email", type=str, default=None)
    headImage = request.form.get("HeadImage", type=str, default=None)
    IDCard = request.form.get("IDCard", type=str, default=None)
    IDCardJust = request.form.get("IDCardJust", type=str, default=None)
    IDCardBack = request.form.get("IDCardBack", type=str, default=None)
    ServiceAreaId = request.form.get("ServiceAreaId", type=str, default=None)
    ServiceTypeId = request.form.get("ServiceTypeId", type=str, default=None)
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register = back_planner_logic.update_planner(account, phone, userType, name,realName, sex, age, education, address,
                                               email, headImage, IDCard, IDCardJust, IDCardBack,ServiceAreaId,ServiceTypeId, userid,Sort, user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#获取学历背景
@app.route("/backweb/planner/select_education_list", methods=['POST'])
def select_education_list():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    education = back_planner_logic.select_planner_education(userid)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = education
    return api_response.response_return(ApiResponse)

#获取学历背景详情
@app.route("/backweb/planner/select_education_info", methods=['POST'])
def select_education_info():
    ApiResponse = api_response.ApiResponse()
    id= request.form.get("id", type=str, default=None)

    if id == None or id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数id不能为空")
    education = back_planner_logic.select_education_info(id)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = education
    return api_response.response_return(ApiResponse)

#获取社会背景
@app.route("/backweb/planner/select_society_list", methods=['POST'])
def select_society_list():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    society = back_planner_logic.select_planner_society(userid)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = society
    return api_response.response_return(ApiResponse)


#获取社会背景详情
@app.route("/backweb/planner/select_society_info", methods=['POST'])
def select_society_info():
    ApiResponse = api_response.ApiResponse()
    id= request.form.get("id", type=str, default=None)

    if id == None or id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数id不能为空")
    education = back_planner_logic.select_society_info(id)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = education
    return api_response.response_return(ApiResponse)

#获取资源背景
@app.route("/backweb/planner/select_resour_list", methods=['POST'])
def select_resour_list():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)

    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    resour = back_planner_logic.select_planner_resour(userid)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = resour
    return api_response.response_return(ApiResponse)

#获取资源背景详情
@app.route("/backweb/planner/select_resour_info", methods=['POST'])
def select_resour_info():
    ApiResponse = api_response.ApiResponse()
    id= request.form.get("id", type=str, default=None)

    if id == None or id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数id不能为空")
    education = back_planner_logic.select_resour_info(id)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = education
    return api_response.response_return(ApiResponse)

#新增学历
@app.route("/backweb/planner/back_add_education", methods=['POST'])
def back_add_education():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    University = request.form.get("University", type=str, default=None)
    if University == None or University=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="毕业学校不能为空")
    Degree = request.form.get("Degree", type=str, default=None)
    if Degree == None or Degree=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="学位不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = back_planner_logic.insert_education(guid,userid,TimeStart,TimeEnd,University,Degree,Sort,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改学历
@app.route("/backweb/planner/back_update_education", methods=['POST'])
def back_update_education():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的学历")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    University = request.form.get("University", type=str, default=None)
    if University == None or University=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="毕业学校不能为空")
    Degree = request.form.get("Degree", type=str, default=None)
    if Degree == None or Degree=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="学位不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.update_education(TimeStart,TimeEnd,University,Degree,Sort,Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除学历
@app.route("/backweb/planner/back_delete_education", methods=['POST'])
def back_delete_education():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的学历")
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.delete_education(Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#新增资源背景
@app.route("/backweb/planner/back_add_resour", methods=['POST'])
def back_add_resour():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = back_planner_logic.insert_resour(guid,userid,TimeStart,TimeEnd,Description,Sort,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改资源背景
@app.route("/backweb/planner/back_update_resour", methods=['POST'])
def back_update_resour():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的资源背景")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="资源背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.update_resour(TimeStart,TimeEnd,Description,Sort,Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除资源背景
@app.route("/backweb/planner/back_delete_resour", methods=['POST'])
def back_delete_resour():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的资源背景")
    user = request_back_helper.current_user_mush_login()
    data=mysql.operate_object(planner_sql.delete_resour,(user["UserId"],Id))
    #data = back_planner_logic.delete_society,(Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#新增社会背景
@app.route("/backweb/planner/back_add_society", methods=['POST'])
def back_add_society():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数userid不能为空")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = mysql.operate_object(planner_sql.insert_society,(id,userid,TimeStart,TimeEnd,Description,Sort
                                                           ,user["UserId"],user["UserId"]))
    #data = back_planner_logic.insert_society,(guid,userid,TimeStart,TimeEnd,Description,Sort,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改社会背景
@app.route("/backweb/planner/back_update_society", methods=['POST'])
def back_update_society():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的社会背景")
    TimeStart = request.form.get("TimeStart", type=str, default="")
    TimeEnd = request.form.get("TimeEnd", type=str, default="")
    #if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
     #   raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.update_education,(TimeStart,TimeEnd,Description,Sort,Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除社会背景
@app.route("/backweb/planner/back_delete_society", methods=['POST'])
def back_delete_society():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的社会背景")
    user = request_back_helper.current_user_mush_login()
    data=mysql.operate_object(planner_sql.delete_society,(user["UserId"],Id))
    #data = back_planner_logic.delete_society,(Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#修改大v
@app.route("/backweb/planner/update_BigV", methods=['POST'])
def update_BigV():
    ApiResponse = api_response.ApiResponse()
    UserId = request.form.get("UserId", type=str, default=None)
    BigV = request.form.get("BigV", type=int, default=0)
    if UserId == None or UserId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的规划师")
    user = request_back_helper.current_user_mush_login()
    data=mysql.operate_object(planner_sql.update_BigV,(BigV,user["UserId"],UserId))
    #data = back_planner_logic.update_BigV,(BigV,UserId,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)