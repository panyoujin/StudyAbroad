from flask import request,session,abort
from planner_project.common import api_response,custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import user_sql,home_sql


def get_token():
    token = request.cookies.get("token")
    if token != None:
        return token
    raise custom_error.CustomFlaskErr(status_code=600,message="请先登录")
#获取当前登录用户 未登录返回None
def current_user():
    user = session.get("user", None)
    return user

#获取当前登录用户 如果未登录将终止请求并返回 600
def current_user_mush_login():
    user = current_user()
    if user!=None and any(user):
        return  user
    #调用统一异常处理
    raise custom_error.CustomFlaskErr(status_code=600,message="请先登录")

#更新当前用户缓存
def set_session_login():
    token= get_token()
    session["user"] = mysql.get_object(home_sql.select_sysuser_login_info, (token))