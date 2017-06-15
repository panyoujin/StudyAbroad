from flask import Flask
from planner_project.common import custom_error
from planner_project.common import api_response

app = Flask(__name__)
@app.errorhandler(custom_error.CustomFlaskErr)
def handle_flask_error(error):

    ApiResponse = api_response.ApiResponse
    ApiResponse.message = error.message
    ApiResponse.status = error.status_code
    return api_response.response_return(ApiResponse)

import  planner_project.api.user.register
import  planner_project.api.user.login
import  planner_project.api.home.index
import  planner_project.api.planner.planner
import  planner_project.api.demand_service.demand_service