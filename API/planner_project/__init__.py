from flask import Flask, request
from planner_project.common import custom_error
from planner_project.common import api_response, request_helper

app = Flask(__name__)

app.secret_key = '123456'


@app.before_request
def before_request():
    # 如果请求不是从小程序过来，直接返回失败
    # if(request.user_agent!=""):
    #    raise custom_error.CustomFlaskErr(status_code=500, message="系统错误")
    # 获取url权限
    # 判断当前url是否需要登录
    # 判断当前url是否有权限
    # user = request_helper.current_user_mush_login()
    print("before_request:{0}{1}{2}{3}", request.remote_addr, request.url_rule, request.user_agent)


# @app.teardown_request
# def teardown_request(e):
#   #对数据进行压缩操作
#   print("teardown_request"+request.remote_addr+request.url_rule+request.user_agent)

@app.errorhandler(500)
def system_error(error):
    # 部署时需要去掉error.args[1]
    message = ""
    if len(error.args) > 1:
        message = error.args[1]
    else:
        message = error.args[0]
    ApiResponse = api_response.ApiResponse(message, 500, "系统错误")
    return api_response.response_return(ApiResponse)


@app.errorhandler(custom_error.CustomFlaskErr)
def handle_flask_error(error):
    ApiResponse = api_response.ApiResponse("", error.status_code, error.message)
    return api_response.response_return(ApiResponse)


import planner_project.api.user.register
import planner_project.api.user.login
import planner_project.api.home.index
import planner_project.api.planner.planner
import planner_project.api.demand_service.demand_service
import planner_project.api.platform.platform
import planner_project.api.user.userinfo
import planner_project.api.planner.team
import planner_project.api.user.upgrade_user
import planner_project.api.basic.basic_data
import planner_project.api.demand_service.order
import planner_project.api.demand_service.demand_undertake
import planner_project.api.order.order
import planner_project.api.basic.basic_verification_code
import planner_project.api.team.team_info
import planner_project.api.notice.system_notice

import planner_project.api.backweb.home
import planner_project.api.backweb.back_user
import planner_project.api.backweb.back_team
import planner_project.api.backweb.service_area
import planner_project.api.backweb.service_type
import planner_project.api.backweb.lable
import planner_project.api.backweb.back_planner
import planner_project.api.backweb.back_upgrade_user
import planner_project.api.backweb.back_demand_undertake
import planner_project.api.backweb.back_demand
import planner_project.api.backweb.back_order
import planner_project.api.backweb.back_sys_user
import planner_project.api.backweb.back_sys_role
import planner_project.api.dynamic.dynamic
