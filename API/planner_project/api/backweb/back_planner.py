#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import back_planner_logic


#用户列表
@app.route("/backweb/planner/select_planner_list", methods=['POST'])
def select_planner_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    data = back_planner_logic.select_planner_list(name, page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
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

#获取资源背景
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


#获取资源背景详情
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

#获取社会背景
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

#获取社会背景详情
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
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
@app.route("/backweb/demand_service/back_delete_education", methods=['POST'])
def back_delete_education():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
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
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的资源背景")
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.delete_society,(Id,user["UserId"])
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = back_planner_logic.insert_society,(guid,userid,TimeStart,TimeEnd,Description,Sort,user["UserId"])
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
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
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
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的社会背景")
    user = request_back_helper.current_user_mush_login()
    data = back_planner_logic.delete_society,(Id,user["UserId"])
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
