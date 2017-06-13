#coding:utf-8
from flask import request,session
import uuid
import time
import json
from planner_project import app
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.carousel import carousel_sql
from planner_project.sql.planner import planner_sql
from planner_project.sql.service import service_sql

#首页轮询图
@app.route("/home/carousel", methods=['POST'])
def carousel():
    ApiResponse = api_response.ApiResponse
    count = request.form.get("count", type=int, default=5)
    data = mysql.get_list(carousel_sql.select_top_carousel,(count))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = json.dumps(data)
    return api_response.response_return(ApiResponse)


#首页规划师
@app.route("/home/planner", methods=['POST'])
def planner():
    ApiResponse = api_response.ApiResponse
    count = request.form.get("count", type=int, default=5)
    data = mysql.get_list(planner_sql.select_top_planner,(count))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#首页服务
@app.route("/home/service", methods=['POST'])
def service():
    ApiResponse = api_response.ApiResponse
    count = request.form.get("count", type=int, default=5)
    data = mysql.get_list(service_sql.select_top_service,(count))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
