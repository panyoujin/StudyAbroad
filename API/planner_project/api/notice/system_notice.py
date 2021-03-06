# coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response, request_helper, custom_error
from planner_project.data_access import mysql
from planner_project.sql.notice import system_notice_sql
from planner_project.sql.notice import service_notice_sql


# 获取系统消息列表
@app.route("/notice/get_system_notice_list", methods=['POST'])
def get_system_notice_list():
    userId = request_helper.current_user_mush_login()["Id"]
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(system_notice_sql.select_system_notice_list, (userId, (page - 1) * size, size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


# 修改系统消息已读状态
@app.route("/notice/update_system_notice_status", methods=['POST'])
def update_system_notice_status():
    userId = request_helper.current_user_mush_login()["Id"]
    ApiResponse = api_response.ApiResponse()
    noticeId = request.form.get("Id", type=str, default=None)
    if noticeId is None or noticeId == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="消息id不能为空")
    mysql.operate_object(system_notice_sql.update_system_notice_status, (userId, noticeId))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 获取服务消息
@app.route("/notice/get_service_notice_list", methods=['POST'])
def get_service_notice_list():
    userId = request_helper.current_user_mush_login()["Id"]
    UserType = request_helper.current_user_mush_login()["UserType"]

    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    if UserType == 1:
        data = mysql.get_list(service_notice_sql.select_service_notice_list2, (userId, (page - 1) * size, size))
    else:
        data = mysql.get_list(service_notice_sql.select_service_notice_list1, (userId, (page - 1) * size, size))
    if len(data) > 0:
        for item in data:
            if item["OrderStatus"] == 1:
                item["OrderStatusStr"] = "通知后台"
                continue
            if item["OrderStatus"] == 2:
                item["OrderStatusStr"] = "客服回访"
                continue
            if item["OrderStatus"] == 3:
                item["OrderStatusStr"] = "拟定合同"
                continue
            if item["OrderStatus"] == 4:
                item["OrderStatusStr"] = "线下签约"
                continue
            if item["OrderStatus"] == 5:
                item["OrderStatusStr"] = "平台审查"
                continue
            if item["OrderStatus"] == 6:
                item["OrderStatusStr"] = "付款确认"
                continue
            if item["OrderStatus"] == 7:
                item["OrderStatusStr"] = "服务完成"
                continue

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)
