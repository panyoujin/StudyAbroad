#coding:utf-8
from flask import request
from planner_project import app
from planner_project.common import api_response,request_helper,custom_error
from planner_project.data_access import mysql
from planner_project.logic import  team_logic
import  uuid


#团队列表
@app.route("/team/team_list", methods=['POST'])
def team_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    name = request.form.get("name", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    userId=""
    user = request_helper.current_user()
    if user != None and any(user):
        userId=user["Id"]
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = team_logic.get_team_list(userId,name,page,size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#团队成员列表 还需要返回是否管理员
@app.route("/planner/team_member_list", methods=['POST'])
def team_member_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    temaId = request.form.get("temaId", type=str, default="")
    page = request.form.get("page", type=int, default=1)
    if page<=0:
        page=1
    if size<=0:
        size=10
    data = team_logic.get_team_member_list(temaId,(page-1)*size,size)
    if data and len(data):
        for i in range(len(data)):
            if data[i]!=None and data[i]["Lables"]!=None and len(data[i]["Lables"]):
                lablesArray=data[i]["Lables"].split(",")
                data[i]["Lables"]=lablesArray
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)


#新增团队
@app.route("/planner/insert_team", methods=['POST'])
def insert_team():
    ApiResponse = api_response.ApiResponse()
    name = request.form.get("name", type=str, default=None)
    serviceAreaId = request.form.get("serviceAreaId", type=int, default=0)
    serviceDescription = request.form.get("serviceDescription", type=str, default=None)
    user = request_helper.current_user_mush_login()
    if user["UserType"] < 2:
        raise custom_error.CustomFlaskErr(status_code=500, message="请先申请成为规划师再注册团队！")
    guid = str(uuid.uuid1())
    teamId= team_logic.select_user_teamid(user["Id"])
    if teamId != None:
        raise custom_error.CustomFlaskErr(status_code=500, message="你已经是其他团队的成员，如需注册团队请先退出其他团队！")
    data=team_logic.insert_team(guid,user["Id"],name,serviceAreaId,serviceDescription)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)



#获取用户的团队
@app.route("/planner/select_user_team", methods=['POST'])
def select_user_team():
    ApiResponse = api_response.ApiResponse()
    userid= request.form.get("userid", type=str, default=None)
    if userid == None or userid=="":
        userid = request_helper.current_user_mush_login()["Id"]
    teamId= team_logic.select_user_team(userid)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data=teamId
    return api_response.response_return(ApiResponse)

