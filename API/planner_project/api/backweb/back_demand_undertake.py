# coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response, request_back_helper, custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import demand_service_sql
from planner_project.sql.notice import system_notice_sql


# 查询承接服务列表
@app.route("/backweb/demand/select_demand_undertake_list", methods=['POST'])
def select_demand_undertake_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(demand_service_sql.select_demand_undertake_list, ((page - 1) * size, size))
    listCount = mysql.get_object(demand_service_sql.select_demand_undertake_count, ())

    if listCount is not None:
        ApiResponse.data = data
        ApiResponse.listCount = listCount["count"]

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 生成订单
@app.route("/backweb/demand/generate_order", methods=['POST'])
def generate_order():
    userId = request_back_helper.current_user_mush_login()["UserId"]
    Id = request.form.get("Id", type=str, default=None)
    if Id is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确")
    myundertake = mysql.get_object(demand_service_sql.select_my_demand_undertake, (Id))
    if myundertake is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="没有找到该承接的需求")
    guid = str(uuid.uuid1())#生成订单id
    sql_list = [demand_service_sql.insert_order,
                demand_service_sql.insert_order_flowing,
                demand_service_sql.update_demand_undertake_success,
                demand_service_sql.update_demand_undertake_fail,
                demand_service_sql.update_demand_service_success]
    args_list = [(guid, myundertake["PlannerUserId"], myundertake["UserId"], myundertake["ContractId"],
                  myundertake["DemandId"], myundertake["Description"], myundertake["Description"],
                  myundertake["ServiceAreaId"], myundertake["ServiceTypeId"], myundertake["PriceStart"],
                  myundertake["PriceEnd"], myundertake["TimeStart"], myundertake["TimeEnd"], userId),
                 (guid, myundertake["UserId"], userId),
                 (userId, Id),
                 (userId, myundertake["DemandId"], Id),
                 (myundertake["DemandId"])]
    resultInt = mysql.operate__many(sql_list, args_list)
    print(resultInt)
    if resultInt > 0:
        #给发送需求的用户 发出通知
        mysql.operate_object(system_notice_sql.insert_system_notice,(myundertake["UserId"], "您的需求已被承接.", userId))
        #给承接用户需求的 规划师发出通知
        notice_list = mysql.get_list(demand_service_sql.select_demand_undertake_notice_list, (myundertake["DemandId"]))
        for item in notice_list:
            if item["Id"] == Id:
                mysql.operate_object(system_notice_sql.insert_system_notice,
                                     (item["UserId"], "您申请的承接 "+myundertake["Name"]+" 的需求通过.", userId))
            else:
                mysql.operate_object(system_notice_sql.insert_system_notice,
                                     (item["UserId"], "您申请的承接 "+myundertake["Name"]+" 的需求不通过.", userId))
    ApiResponse = api_response.ApiResponse()
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)
