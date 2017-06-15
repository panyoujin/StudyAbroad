from flask import request,session,abort
from planner_project.common import api_response
from planner_project.data_access import mysql
from planner_project.sql.user import user_sql

def current_user():
    ApiResponse = api_response.ApiResponse
    token = request.cookies["token"]
    if token != None:
        # if session[token] != None:
        #     ApiResponse.message = "成功"
        #     ApiResponse.status = 200
        #     ApiResponse.data = json.dumps(session[token])
        #     return api_response.response_return(ApiResponse)
        #本地缓存中不存在去数据库拿
        user = mysql.get_object(user_sql.select_user_login_info,(token))
        #user = mysql.get_list(user_sql.select_user_login_info,(token))
        if user!=None and any(user):
            return  user
    ApiResponse.message = "请先登录"
    ApiResponse.status = 600
    abort(api_response.response_return(ApiResponse))