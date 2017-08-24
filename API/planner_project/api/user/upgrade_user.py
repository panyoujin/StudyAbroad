#coding:utf-8
from flask import request
import uuid
from planner_project import app
from planner_project.common import api_response,custom_error,request_helper
from planner_project.data_access import mysql
from planner_project.sql.user import user_upgrade
#申请规划师
@app.route("/userinfo/upgrade_user", methods=['POST'])
def upgrade_user():
    ApiResponse = api_response.ApiResponse()
    Sex = request.form.get("Sex", type=int, default=0)
    if Sex == 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="性别不能为空")
    Name = request.form.get("Name", type=str, default=None)
    if Name == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="姓名不能为空")
    Address = request.form.get("Address", type=str, default=None)
    if Address == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="地址不能为空")
    ServiceId = request.form.get("ServiceId", type=int, default=0)
    if ServiceId == 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="服务不能为空")
    ServiceAreaId = request.form.get("ServiceAreaId", type=int, default=0)
    if ServiceAreaId == 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="服务区域不能为空")
    Email = request.form.get("Email", type=str, default=None)
    if Email == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="邮箱不能为空")
    Experience = request.form.get("Experience", type=str, default=None)
    if Experience == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="资历不能为空")
    IDCard = request.form.get("IDCard", type=str, default=None)
    if IDCard == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="身份证不能为空")
    IDCardPic = request.form.get("IDCardPic", type=str, default=None)
    if IDCardPic == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="身份证正面不能为空")
    IDCardBackPic = request.form.get("IDCardBackPic", type=str, default=None)
    if IDCardBackPic == None:
        raise custom_error.CustomFlaskErr(status_code=500, message="身份证反面不能为空")

    userId = request_helper.current_user_mush_login()["Id"]

    data_exists = mysql.get_list(user_upgrade.select_exists_upgrade,(userId))

    if len(data_exists):
        raise custom_error.CustomFlaskErr(status_code=500, message="你已经存在申请过注册规划师")

    requestData = (userId,Sex,Name,Address,ServiceId,ServiceAreaId,Email,Experience,IDCardPic,userId,IDCardBackPic,IDCard)
    data_register = mysql.operate_object(user_upgrade.insert_upgrade_user, requestData)

    if data_register > 0:
        ApiResponse.message = "申请成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="申请失败")