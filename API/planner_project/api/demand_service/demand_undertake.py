#coding:utf-8
import uuid
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error,enum
from planner_project.data_access import mysql
from planner_project.sql.demand_service import demand_undertake
from planner_project.sql.user import user_info_sql

#承接需求
@app.route("/demand_undertake/insert_undertake", methods=['POST'])
def insert_undertake():
    ApiResponse = api_response.ApiResponse()

    DemandId = request.form.get("DemandId", type=str, default=None)
    if DemandId == None or DemandId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="需求id不能为空")
    ContractId = request.form.get("ContractId", type=int, default=0)
    if ContractId == None or ContractId == 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="合同id不能为空")

    userId = request_helper.current_user_mush_login()["Id"]

    userInfo = mysql.get_object(user_info_sql.select_userinfo_by_id, (userId))
    if userInfo == None or userInfo["UserType"]== 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="你还不是规划师")

    service_exists = mysql.get_object(demand_undertake.select_exists_demand, (DemandId))
    if service_exists == None or service_exists["IsUndertake"] == 1:
        raise custom_error.CustomFlaskErr(status_code=500, message="该需求不存在或者已被承接")

    data_exists = mysql.get_object(demand_undertake.select_exists_demand_service, (DemandId,userId))

    if data_exists["total"] > 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="你已经存在承接该需求的记录")

    insertResult = mysql.operate_object(demand_undertake.insert_demand_undertake, (DemandId, userId,userId,enum.IsUser.no,ContractId))
    if insertResult > 0:
        ApiResponse.message = "申请成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="申请失败")