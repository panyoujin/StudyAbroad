#coding:utf-8
import uuid
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.logic import order_logic


#新增评论
@app.route("/order/insert_evaluate", methods=['POST'])
def insert_evaluate():
    ApiResponse = api_response.ApiResponse()

    orderId = request.form.get("orderId", type=str, default=None)
    if orderId == None or orderId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要评论的订单")
    content = request.form.get("content", type=str, default=None)
    if content == None or content=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请输入评价内容")

    lable = request.form.get("lable", type=str, default=None)
    sort = request.form.get("sort", type=int, default=0)
    synthesis = request.form.get("synthesis", type=int, default=5)
    quality = request.form.get("quality", type=int, default=5)
    efficiency = request.form.get("efficiency", type=int, default=5)
    user= request_helper.current_user_mush_login()
    data = order_logic.insert_evaluate(orderId, user["Id"], content, sort, synthesis, quality, efficiency, lable)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)

#回复评论
@app.route("/order/replay_evaluate", methods=['POST'])
def replay_evaluate():
    ApiResponse = api_response.ApiResponse()

    orderId = request.form.get("orderId", type=str, default=None)
    if orderId == None or orderId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请选择需要评论的订单")
    content = request.form.get("content", type=str, default=None)
    if content == None or content=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="请输入评价内容")

    sort = request.form.get("sort", type=int, default=0)
    user= request_helper.current_user_mush_login()
    data = order_logic.replay_evaluate(orderId, user["Id"], content, sort)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#查询指定订单的评论详情
@app.route("/order/select_evaluate_info", methods=['POST'])
def select_evaluate_info():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    orderId = request.form.get("orderId", type=str, default=None)
    if orderId == None or orderId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="订单号不能为空")
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    evaluate = order_logic.select_evaluate_info(orderId,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = evaluate
    return api_response.response_return(ApiResponse)