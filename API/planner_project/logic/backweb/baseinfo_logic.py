from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import baseinfo_sql


#获取基础信息
def select_platforminfo():
    return mysql.get_object(baseinfo_sql.select_platforminfo, ())

#修改基础信息
def update_platforminfo(CustomerServiceTelephone,FlowImage,BigVImage,current_user_id):
    if CustomerServiceTelephone == None or CustomerServiceTelephone=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(baseinfo_sql.update_platforminfo,(CustomerServiceTelephone,FlowImage,BigVImage,current_user_id))
    return data_register > 0

#获取合同
def select_contract():
    return mysql.get_object(baseinfo_sql.select_contract, ())

#修改合同
def update_contract(content,current_user_id):
    if content == None or content=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(baseinfo_sql.update_contract,(current_user_id,content,current_user_id,current_user_id))
    return data_register > 0

#获取轮询列表
def select_carouselimage_list(page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(baseinfo_sql.select_carouselimage_list,((page-1)*size,size))

#获取轮询详情
def select_carouselimage_info(imageId):
    return mysql.get_object(baseinfo_sql.select_carouselimage_info, (imageId))

#修改轮询信息
def update_carouselimage_info(description,imageUrl,clickUrl,isTop,sort,current_user_id,imageId):
    if imageUrl == None or imageUrl=="" or imageId == None or imageId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(baseinfo_sql.update_carouselimage_info,(description,imageUrl,clickUrl,isTop,sort,current_user_id,imageId))
    return data_register > 0


#删除轮询
def delete_carouselimage(imageId,current_user_id):
    if imageId == None or imageId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(baseinfo_sql.delete_carouselimage,(current_user_id,imageId))
    return data_register > 0



#新增轮询信息
def insert_carouselimage(description,imageUrl,clickUrl,isTop,sort,current_user_id):
    if imageUrl == None or imageUrl=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(baseinfo_sql.insert_carouselimage,(description,imageUrl,clickUrl,isTop,sort,current_user_id,current_user_id))
    return data_register > 0

