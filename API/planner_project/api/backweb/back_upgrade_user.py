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


# 获取规划师升级数据详情
@app.route("/backweb/user/get_upgrade_apply_detail", methods=['POST'])
def get_upgrade_apply_detail():
    request_back_helper.current_user_mush_login()
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=str, default=None)
    if Id is None or Id == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数id不能为空")
    ApiResponse.data = mysql.get_object(upgrade_user_sql.get_upgrade_apply_detail, (Id))

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 获取规划师升级数据详情
@app.route("/backweb/user/update_upgrade_user", methods=['POST'])
def update_upgrade_user():
    UserId = request_back_helper.current_user_mush_login()["UserId"]
    Id = request.form.get("Id", type=str, default=None)
    Status = request.form.get("Status", type=int, default=-1)

    if Id is None or Id == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数id不能为空")
    if Status == -1:
        raise custom_error.CustomFlaskErr(status_code=500, message="参数状态不能为空")
    #查询规划师升级数据
    upgradeInfo = mysql.get_object(upgrade_user_sql.get_upgrade_info_by_id, (Id))

    if upgradeInfo is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="该审核数据不存在")
    if upgradeInfo["Status"] != 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="该审核数据已处理，请勿重复操作")
    # 审核不通过
    if Status == 2:
        success = mysql.operate_object(upgrade_user_sql.update_upgrade_status, (Status, UserId, Id))
        if success <= 0:
            raise custom_error.CustomFlaskErr(status_code=500, message="审核失败")
    # 审核通过
    if Status == 1:
        idCard=" "#判断IDCard是否不存在
        if 'IDCard' in upgradeInfo and upgradeInfo["IDCard"] is not None:
            idCard = upgradeInfo["IDCard"]
        sql_list = [upgrade_user_sql.update_upgrade_status,
                    upgrade_user_sql.update_user_type,
                    upgrade_user_sql.update_user_info,
                    upgrade_user_sql.insert_planner_statistics]
        args_list = [(Status, UserId, Id),
                     (UserId,upgradeInfo["UserId"]),
                     (upgradeInfo["Name"],upgradeInfo["Sex"],upgradeInfo["Address"],upgradeInfo["Experience"],
                      upgradeInfo["Email"],idCard,upgradeInfo["IDCardPic"],upgradeInfo["IDCardBackPic"],upgradeInfo["ServiceAreaId"],
                      upgradeInfo["ServiceId"],UserId,upgradeInfo["UserId"]),
                     (upgradeInfo["UserId"],UserId,UserId,upgradeInfo["UserId"],upgradeInfo["UserId"])]
        success = mysql.operate__many(sql_list, args_list)
        if success <= 0:
            raise custom_error.CustomFlaskErr(status_code=500, message="审核失败")

    ApiResponse = api_response.ApiResponse()
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)
