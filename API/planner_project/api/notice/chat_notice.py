# coding:utf-8
import uuid
from flask import request
from planner_project import app
from planner_project.common import api_response, request_helper, custom_error
from planner_project.data_access import mysql
from planner_project.sql.notice import chat_notice_sql

# 新增聊天信息
@app.route("/notice/insert_chat", methods=['POST'])
def insert_chat():
    SendUserId = request_helper.current_user_mush_login()["Id"]
    ApiResponse = api_response.ApiResponse()
    ReceiveUserId = request.form.get("ReceiveUserId", type=str, default=None)
    Content = request.form.get("Content", type=str, default=None)
    if ReceiveUserId is None or ReceiveUserId == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="接收者id不能为空")
    if Content is None or Content == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="消息内容不能为空")

    user_info = mysql.get_object(chat_notice_sql.select_user_info, (SendUserId))
    if user_info is None:
        raise custom_error.CustomFlaskErr(status_code=500, message="该用户不存在")
    chat_main = mysql.get_object(chat_notice_sql.select_chat_main, (SendUserId,ReceiveUserId,ReceiveUserId,SendUserId))
    guid = str(uuid.uuid1())
    print(chat_main)
    if chat_main == None :
        mysql.operate_object(chat_notice_sql.insert_chat_main,(guid,SendUserId,ReceiveUserId,Content,SendUserId))
    else:
        guid=chat_main["Id"]
        mysql.operate_object(chat_notice_sql.update_chat_main,(Content,SendUserId,guid))

    system_content=user_info["Name"]+" 发来一条消息";
    mysql.operate_object(chat_notice_sql.insert_chat_content,(guid,SendUserId,Content,SendUserId))
    existx_chat=mysql.get_object(chat_notice_sql.existx_chat_notice,(guid,ReceiveUserId))

    if existx_chat["total"]==0:
        mysql.operate_object(chat_notice_sql.insert_chat_notice, (ReceiveUserId, system_content, SendUserId,guid,SendUserId))
    else:
        mysql.operate_object(chat_notice_sql.update_chat_notice,(system_content,SendUserId,guid,ReceiveUserId))

    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 获取聊天信息
@app.route("/notice/get_chat_list", methods=['POST'])
def get_chat_list():
    SendUserId = request_helper.current_user_mush_login()["Id"]
    ReceiveUserId = request.form.get("ReceiveUserId", type=str, default=None)
    if ReceiveUserId is None or ReceiveUserId == '':
        raise custom_error.CustomFlaskErr(status_code=500, message="接收者id不能为空")

    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    if page <= 0:
        page = 1
    if size <= 0:
        size = 10
    data = mysql.get_list(chat_notice_sql.select_chat_list, (SendUserId,ReceiveUserId,ReceiveUserId,SendUserId, (page - 1) * size, size))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)