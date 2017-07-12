# coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response, request_back_helper, custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import order_sql

# 订单列表
@app.route("/backweb/order/select_order_list", methods=['POST'])
def select_order_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    # name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(order_sql.select_order_list, ((page - 1) * size, size))
    listCount = mysql.get_object(order_sql.select_order_count, ())

    if listCount is not None:
        ApiResponse.data = data
        ApiResponse.listCount = listCount["count"]

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)