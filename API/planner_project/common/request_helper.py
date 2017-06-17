from flask import request,session,abort
from planner_project.common import api_response,custom_error
from planner_project.data_access import mysql
from planner_project.sql.user import user_sql


def get_token():
    token = request.cookies["token"]
    if token != None:
        return token
    raise custom_error.CustomFlaskErr(status_code=600,message="请先登录")
#获取当前登录用户 未登录返回None
def current_user():
    ApiResponse = api_response.ApiResponse
    token = request.cookies["token"]
    if token == None:
        return None
        # if session[token] != None:
        #     ApiResponse.message = "成功"
        #     ApiResponse.status = 200
        #     ApiResponse.data = json.dumps(session[token])
        #     return api_response.response_return(ApiResponse)
        #本地缓存中不存在去数据库拿
    user = mysql.get_object(user_sql.select_user_login_info,(token))
    return user

#获取当前登录用户 如果未登录将终止请求并返回 600
def current_user_mush_login():
    ApiResponse = api_response.ApiResponse
    user = current_user()
    if user!=None and any(user):
        return  user
    #调用统一异常处理
    raise custom_error.CustomFlaskErr(status_code=600,message="请先登录")