#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.planner import planner_sql
from planner_project.logic import  team_logic,order_logic,planner_logic


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
    user = request_helper.current_user()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(planner_sql.select_follw_planner,(user["Id"],(page-1)*size,size))
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
    complete_order_list = order_logic.select_planner_complete_order_list(plannerId,page,size)
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
    plannerId = request.form.get("plannerId", type=str, default=None)
    if plannerId == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择规划师")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    complete_order_list = order_logic.select_planner_order_list(plannerId,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = complete_order_list
    return api_response.response_return(ApiResponse)