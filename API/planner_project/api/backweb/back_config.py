from planner_project import app
from flask import request
from planner_project.data_access import mysql
from planner_project.common import api_response, request_back_helper, custom_error
from planner_project.sql.backweb import config_sql


# 获取基础配置列表
@app.route("/backweb/config/select_base_config_list", methods=['POST'])
def select_base_config_list():
    ApiResponse = api_response.ApiResponse()
    ApiResponse.data = mysql.get_list(config_sql.select_config_list, ())
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 新增基础配置
@app.route("/backweb/config/insert_base_config", methods=['POST'])
def insert_base_config():
    ApiResponse = api_response.ApiResponse()
    Key = request.form.get("Key", type=str, default=None)
    if Key is None or Key == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="key不能为空")
    Value = request.form.get("Value", type=str, default=None)
    Remark = request.form.get("Remark", type=str, default=None)
    imageUrl = request.form.get("imageUrl", type=str, default=None)

    if mysql.operate_object(config_sql.insert_config, (Key, Value, Remark, imageUrl)) <= 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 删除基础配置
@app.route("/backweb/config/delete_base_config", methods=['POST'])
def delete_base_config():
    ApiResponse = api_response.ApiResponse()
    Key = request.form.get("Key", type=str, default=None)
    if Key is None or Key == "":
        raise custom_error.CustomFlaskErr(status_code=500, message="key不能为空")
    if mysql.operate_object(config_sql.delete_config, (Key)) <= 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)


# 获取单个基础配置
@app.route("/backweb/config/get_base_config_by_id", methods=['POST'])
def get_base_config_by_id():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=int, default=0)
    if Id <= 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="Id不能为空")

    ApiResponse.data = mysql.get_list(config_sql.get_base_config_by_id, (Id))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)

# 获取单个基础配置
@app.route("/backweb/config/update_base_config_by_id", methods=['POST'])
def update_base_config_by_id():
    ApiResponse = api_response.ApiResponse()
    Id = request.form.get("Id", type=int, default=0)
    if Id <= 0:
        raise custom_error.CustomFlaskErr(status_code=500, message="Id不能为空")
    Value = request.form.get("Value", type=str, default=None)
    Remark = request.form.get("Remark", type=str, default=None)
    imageUrl = request.form.get("imageUrl", type=str, default=None)

    ApiResponse.data = mysql.get_list(config_sql.update_config, (Value,Remark,imageUrl,Id))
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    return api_response.response_return(ApiResponse)