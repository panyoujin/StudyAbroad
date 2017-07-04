# coding:utf-8
from flask import request, json

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.data_access import mysql
from planner_project.sql.backweb import upgrade_user_sql


# 获取规划师升级审核列表
@app.route("/backweb/user/get_upgrade_apply_list", methods=['POST'])
def get_upgrade_apply_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    sear = "%" + name + "%"
    data = mysql.get_list(upgrade_user_sql.get_upgrade_apply_list, (sear, sear, sear, (page - 1) * size, size))
    listCount = mysql.get_object(upgrade_user_sql.get_upgrade_apply_count, (sear, sear, sear))

    ApiResponse.message = "成功"
    ApiResponse.status = 200

    if listCount is not None:
        ApiResponse.data = data
        ApiResponse.listCount = listCount["count"]
    return api_response.response_return(ApiResponse)
