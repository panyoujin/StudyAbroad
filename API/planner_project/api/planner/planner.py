#coding:utf-8
import uuid
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.planner import planner_sql
from planner_project.logic import  team_logic,order_logic,planner_logic
from planner_project.logic.order_logic import  order_sql


#规划师搜索
@app.route("/planner/search", methods=['POST'])
def search():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    data = mysql.get_list(planner_sql.select_search_planner,(name,name,sear,sear,sear,sear,(page-1)*size,size))
    if data and len(data):
        for i in range(len(data)):
            if data[i]!=None and data[i]["Lables"]!=None and len(data[i]["Lables"]):
                lablesArray=data[i]["Lables"].split(",")
                data[i]["Lables"]=lablesArray
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#关注
@app.route("/planner/follow", methods=['POST'])
def follow():
    ApiResponse = api_response.ApiResponse()
    user = request_helper.current_user()
    plannerId = request.form.get("plannerId", type=str, default=None)
    if any(user) and plannerId !=None:
        count = mysql.operate_object(planner_sql.planner_follw, (user["Id"],plannerId))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#取消关注
@app.route("/planner/unfollow", methods=['POST'])
def unfollow():
    ApiResponse = api_response.ApiResponse()
    user = request_helper.current_user()
    plannerId = request.form.get("plannerId", type=str, default=None)
    if any(user) and plannerId !=None:
        count = mysql.operate_object(planner_sql.planner_unfollw, (user["Id"],plannerId))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#我的关注列表
@app.route("/planner/follow_list", methods=['POST'])
def follow_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user_mush_login()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(planner_sql.select_follw_planner,(user["Id"],(page-1)*size,size))
    if data and len(data):
        for i in range(len(data)):
            lablesArray=data[i]["Lables"].split(",")
            data[i]["Lables"]=lablesArray
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#规划师详情
@app.route("/planner/plannerinfo", methods=['POST'])
def plannerinfo():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    planner= planner_logic.select_planner_info(plannerId)
    teamlist = team_logic.select_planner_team_member_list(plannerId,page,size)
    qualifications=planner_logic.select_planner_qualifications(plannerId,0,2)
    complete_order_list=order_logic.select_planner_complete_order_list(plannerId,0,1)
    lables=planner_logic.select_planner_lables(plannerId,0,4)
    evaluate=planner_logic.select_planner_evaluate(plannerId,0,1)
    data = { 'planner':planner,"teamlist": teamlist,"qualifications":qualifications,"order":complete_order_list,"lables":lables,"evaluate":evaluate}
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#规划师资历
@app.route("/planner/qualifications", methods=['POST'])
def qualifications():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    education=planner_logic.select_planner_education(plannerId,page,size)
    society=planner_logic.select_planner_society(plannerId,page,size)
    resour=planner_logic.select_planner_resour(plannerId,page,size)
    data={"education":education,"society":society,"resour":resour}
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#规划师评价列表
@app.route("/planner/planner_evaluate", methods=['POST'])
def planner_evaluate():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    evaluate = planner_logic.select_planner_evaluate(plannerId,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = evaluate
    return api_response.response_return(ApiResponse)


#规划师案例列表
@app.route("/planner/complete_order_list", methods=['POST'])
def complete_order_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    complete_order_list = order_logic.select_planner_complete_order_list(request_helper.current_user_mush_login()["Id"],page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = complete_order_list
    return api_response.response_return(ApiResponse)



#我的客户
@app.route("/planner/order_list", methods=['POST'])
def order_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)

    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    complete_order_list = order_logic.select_planner_order_list(request_helper.current_user_mush_login()["Id"],page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = complete_order_list
    return api_response.response_return(ApiResponse)

#我的订单详细
@app.route("/planner/get_order_detail", methods=['POST'])
def get_order_detail():
    ApiResponse = api_response.ApiResponse()
    OrderId = request.form.get("OrderId", type=str, default=None)
    if OrderId == None or OrderId == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="订单id不能为空")

    ApiResponse.data = mysql.get_object(order_sql.select_planner_order_detail,(OrderId))

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


#新增学历
@app.route("/planner/insert_education", methods=['POST'])
def insert_education():
    ApiResponse = api_response.ApiResponse()
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
    user= request_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = mysql.operate_object(planner_sql.insert_education,(guid,user["Id"],TimeStart,TimeEnd,University,Degree,Sort,user["Id"],user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改学历
@app.route("/planner/update_education", methods=['POST'])
def update_education():
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
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.update_education,(TimeStart,TimeEnd,University,Degree,Sort,user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除学历
@app.route("/demand_service/delete_education", methods=['POST'])
def delete_education():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的学历")
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.delete_education,(user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#新增资源背景
@app.route("/planner/insert_resour", methods=['POST'])
def insert_resour():
    ApiResponse = api_response.ApiResponse()
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user= request_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = mysql.operate_object(planner_sql.insert_resour,(guid,user["Id"],TimeStart,TimeEnd,Description,Sort,user["Id"],user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改资源背景
@app.route("/planner/update_resour", methods=['POST'])
def update_resour():
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
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.update_resour,(TimeStart,TimeEnd,Description,Sort,user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除资源背景
@app.route("/planner/delete_resour", methods=['POST'])
def delete_resour():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的资源背景")
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.delete_society,(user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#新增社会背景
@app.route("/planner/insert_society", methods=['POST'])
def insert_society():
    ApiResponse = api_response.ApiResponse()
    TimeStart = request.form.get("TimeStart", type=str, default=None)
    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeStart == None or TimeStart=="" or TimeEnd==None or TimeEnd=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="起止时间不能为空")
    Description = request.form.get("Description", type=str, default=None)
    if Description == None or Description=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="社会背景不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user= request_helper.current_user_mush_login()
    guid = str(uuid.uuid1())
    data = mysql.operate_object(planner_sql.insert_society,(guid,user["Id"],TimeStart,TimeEnd,Description,Sort,user["Id"],user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改社会背景
@app.route("/planner/update_society", methods=['POST'])
def update_society():
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
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.update_education,(TimeStart,TimeEnd,Description,Sort,user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除社会背景
@app.route("/planner/delete_society", methods=['POST'])
def delete_society():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id == None or Id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的社会背景")
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.delete_society,(user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#新增相片
@app.route("/planner/insert_album", methods=['POST'])
def insert_album():
    ApiResponse = api_response.ApiResponse()
    PhotoName = request.form.get("PhotoName", type=str, default=None)
    if PhotoName == None or PhotoName=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="照片名称不能为空")
    Url = request.form.get("Url", type=str, default=None)
    if Url == None or Url=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="照片地址不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.insert_album,(user["Id"],PhotoName,Url,Sort,user["Id"],user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#修改相片
@app.route("/planner/update_album", methods=['POST'])
def update_album():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=int, default=0)
    if Id <=0:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要修改的照片")
    PhotoName = request.form.get("PhotoName", type=str, default=None)
    if PhotoName == None or PhotoName=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="照片名称不能为空")
    Url = request.form.get("Url", type=str, default=None)
    if Url == None or Url=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="照片地址不能为空")
    Sort = request.form.get("Sort", type=int, default=0)
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.update_album,(PhotoName,Url,Sort,user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#删除相片
@app.route("/planner/delete_album", methods=['POST'])
def delete_album():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=int, default=0)
    if Id <=0:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要删除的照片")
    user= request_helper.current_user_mush_login()
    data = mysql.operate_object(planner_sql.delete_society,(user["Id"],Id,user["Id"]))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取规划师标签列表
@app.route("/planner/get_planner_lables", methods=['POST'])
def get_planner_lables():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    lables=planner_logic.select_planner_lables(plannerId,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = lables
    return api_response.response_return(ApiResponse)
