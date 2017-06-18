from flask import Flask
from planner_project.common import custom_error
from planner_project.common import api_response

app = Flask(__name__)
@app.errorhandler(500)
def system_error(error):
    #部署时需要去掉error.args[1]
    message= ""
    if len(error.args)>1:
        message=error.args[1]
    else:
        message=error.args[0]
    ApiResponse = api_response.ApiResponse(message,500,"系统错误")
    return api_response.response_return(ApiResponse)

@app.errorhandler(custom_error.CustomFlaskErr)
def handle_flask_error(error):

    ApiResponse = api_response.ApiResponse("",error.status_code,error.message)
    return api_response.response_return(ApiResponse)

import  planner_project.api.user.register
import  planner_project.api.user.login
import  planner_project.api.home.index
import  planner_project.api.planner.planner
import  planner_project.api.demand_service.demand_service
import  planner_project.api.platform.platform
import  planner_project.api.user.userinfo
import  planner_project.api.planner.team