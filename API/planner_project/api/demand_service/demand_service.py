#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper
from planner_project.data_access import mysql
from planner_project.sql.demand_service import demand_service_sql


#需求服务搜索
@app.route("/demand_service/searchds", methods=['POST'])
def searchds():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(demand_service_sql.select_search_demand_service,((page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#收藏
@app.route("/demand_service/collection", methods=['POST'])
def collection():
    ApiResponse = api_response.ApiResponse()
    user = request_helper.current_user_mush_login()
    demandServiceId = request.form.get("demandServiceId", type=str, default=None)
    if any(user) and demandServiceId !=None and demandServiceId !="":
        count = mysql.operate_object(demand_service_sql.demand_service_collection, (user["Id"],demandServiceId))
    ApiResponse.message = "收藏成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#我的收藏列表
@app.route("/demand_service/collection_list", methods=['POST'])
def collection_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user_mush_login()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(demand_service_sql.select_collection_demand_service,(user["Id"],(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#我发布的需求服务
@app.route("/demand_service/mydemand", methods=['POST'])
def mydemand():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user_mush_login()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(demand_service_sql.select_my_demand_service,(user["Id"],(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#浏览 后期可能放在读取详情里面，如果读取详情客户端自己解决，那么就要保留这个接口
@app.route("/demand_service/browse", methods=['POST'])
def browse():
    ApiResponse = api_response.ApiResponse()
    user = request_helper.current_user_mush_login()
    demandServiceId = request.form.get("demandServiceId", type=str, default=None)
    if any(user) and demandServiceId !=None:
        count = mysql.operate_object(demand_service_sql.demand_service_browse, (user["Id"],demandServiceId))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

#我的浏览列表
@app.route("/demand_service/browse_list", methods=['POST'])
def browse_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    user = request_helper.current_user_mush_login()
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = mysql.get_list(demand_service_sql.select_browse_demand_service,(user["Id"],(page-1)*size,size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

