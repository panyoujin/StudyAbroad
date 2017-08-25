#coding:utf-8
from flask import request

from planner_project import app
from planner_project.common import api_response, custom_error, request_back_helper
from planner_project.logic.backweb import baseinfo_logic


#获取轮询信息
@app.route("/backweb/base/select_platforminfo", methods=['POST'])
def select_platforminfo():
    ApiResponse = api_response.ApiResponse()

    platforminfo = baseinfo_logic.select_customer_telephone()
    Contract = baseinfo_logic.select_contract()
    ApiResponse.data={"platforminfo":platforminfo,"Contract":Contract}
    return api_response.response_return(ApiResponse)


#修改客服电话信息
@app.route("/backweb/base/update_platforminfo", methods=['POST'])
def update_platforminfo():
    ApiResponse = api_response.ApiResponse()
    CustomerServiceTelephone= request.form.get("CustomerServiceTelephone", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  baseinfo_logic.update_customer_telephone(CustomerServiceTelephone,user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#修改合同
@app.route("/backweb/base/update_Contract", methods=['POST'])
def update_Contract():
    ApiResponse = api_response.ApiResponse()
    ContractContent= request.form.get("ContractContent", type=str, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  baseinfo_logic.update_contract(ContractContent,user["UserId"])
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")


#获取轮询列表
@app.route("/backweb/base/select_carouselimage_list", methods=['POST'])
def select_carouselimage_list():
    ApiResponse = api_response.ApiResponse()
    size = request.form.get("size", type=int, default=10)
    page = request.form.get("page", type=int, default=1)
    data = baseinfo_logic.select_carouselimage_list(page, size)
    ApiResponse.message = "成功"
    ApiResponse.status = 200
    ApiResponse.data = data
    return api_response.response_return(ApiResponse)



#获取轮询信息
@app.route("/backweb/base/select_carouselimage_info", methods=['POST'])
def select_carouselimage_info():
    ApiResponse = api_response.ApiResponse()
    imageId= request.form.get("imageId", type=int, default=None)

    if imageId == None or imageId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数imageId不能为空")
    imageInfo = baseinfo_logic.select_carouselimage_info(imageId)
    if imageInfo !=None and any(imageInfo):
        ApiResponse.data=imageInfo
        return api_response.response_return(ApiResponse)
    raise custom_error.CustomFlaskErr(status_code=500, message="轮询不存在")


#修改轮询信息
@app.route("/backweb/base/update_carouselimage_info", methods=['POST'])
def update_carouselimage_info():
    ApiResponse = api_response.ApiResponse()
    imageId= request.form.get("imageId", type=int, default=None)
    description= request.form.get("Description", type=str, default=None)
    imageUrl = request.form.get("ImageUrl", type=str, default=None)
    clickUrl = request.form.get("ClickUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  baseinfo_logic.update_carouselimage_info(description,imageUrl,clickUrl,isTop,sort,user["UserId"],imageId)
    if data_register:
        ApiResponse.message = "修改成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="修改失败")



#删除轮询信息
@app.route("/backweb/base/delete_carouselimage", methods=['POST'])
def delete_carouselimage():
    ApiResponse = api_response.ApiResponse()
    imageId= request.form.get("imageId", type=int, default=None)
    user = request_back_helper.current_user_mush_login()
    data_register =  baseinfo_logic.delete_carouselimage(imageId, user["UserId"])
    if data_register:
        ApiResponse.message = "删除成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="删除失败")



#新增轮询信息
@app.route("/backweb/base/insert_carouselimage", methods=['POST'])
def insert_carouselimage():
    ApiResponse = api_response.ApiResponse()
    description= request.form.get("Description", type=str, default=None)
    imageUrl = request.form.get("ImageUrl", type=str, default=None)
    clickUrl = request.form.get("ClickUrl", type=str, default=None)
    isTop = request.form.get("IsTop", type=int, default=0)
    sort = request.form.get("Sort", type=int, default=0)
    user = request_back_helper.current_user_mush_login()
    data_register =  baseinfo_logic.insert_carouselimage(description,imageUrl,clickUrl,isTop,sort,user["UserId"])
    if data_register:
        ApiResponse.message = "新增成功"
        ApiResponse.status = 200
        return api_response.response_return(ApiResponse)

    raise custom_error.CustomFlaskErr(status_code=500, message="新增失败")

