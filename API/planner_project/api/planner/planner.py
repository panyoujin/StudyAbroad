#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.planner import planner_sql


#规划师搜索
@app.route("/planner/search", methods=['POST'])
def search():
    ApiResponse = api_response.ApiResponse
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=str, default=1)
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

