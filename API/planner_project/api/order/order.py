#coding:utf-8

import datetime
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.sql.demand_service import order_sql


#承接需求
@app.route("/order/insert_order", methods=['POST'])
def insert_order():
    ApiResponse = api_response.ApiResponse()
    userId = request_helper.current_user_mush_login()["Id"]

    order_createtime = mysql.get_object(order_sql.select_order_createtime, (userId))

    if order_createtime is not None:
        if order_createtime["isCanInsert"] == 0:
            raise custom_error.CustomFlaskErr(status_code=500, message="30秒内不能多次提交订单")

    PlannerUserId = request.form.get("PlannerUserId", type=str, default=None)
    if PlannerUserId == None or PlannerUserId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="规划师id不能为空")

        # raise custom_error.CustomFlaskErr(status_code=500, message="用户id不能为空")

    ContractId = request.form.get("ContractId", type=str, default=None)
    if ContractId == None or ContractId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="合同id不能为空")

    Type = request.form.get("Type", type=str, default=None)
    if Type == None or Type=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="类型不能为空")

    DemandServiceId = request.form.get("DemandServiceId", type=str, default=None)
    if DemandServiceId == None or DemandServiceId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="需求或者服务id不能为空")

    DemandServiceDescription = request.form.get("DemandServiceDescription", type=str, default=None)
    if DemandServiceDescription == None or DemandServiceDescription=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="需求或者服务描述不能为空")

    Description = request.form.get("Description", type=str, default='')

    ServiceAreaId = request.form.get("ServiceAreaId", type=str, default=None)
    if ServiceAreaId == None or ServiceAreaId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="区域id不能为空")

    ServiceTypeId = request.form.get("ServiceTypeId", type=str, default=None)
    if ServiceTypeId == None or ServiceTypeId=="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="服务id不能为空")

    PriceStart = request.form.get("PriceStart", type=float, default=0)

    PriceEnd = request.form.get("PriceEnd", type=float, default=0)

    TimeStart = request.form.get("TimeStart", type=str, default=None)
    if TimeStart == '' or TimeStart == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="开始时间不能为空")

    TimeEnd = request.form.get("TimeEnd", type=str, default=None)
    if TimeEnd == '' or TimeEnd == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="结束时间不能为空")

    insertResult = mysql.operate_object(order_sql.insert_order, (PlannerUserId,userId,ContractId,Type,DemandServiceId,
                                                                 DemandServiceDescription,Description,ServiceAreaId,ServiceTypeId,
                                                                 PriceStart,PriceEnd,TimeStart,TimeEnd,userId))
    if insertResult > 0:
        ApiResponse.message = "申请成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="申请失败")