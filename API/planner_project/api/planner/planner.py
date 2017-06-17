#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper
from planner_project.data_access import mysql
from planner_project.sql.planner import planner_sql


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
