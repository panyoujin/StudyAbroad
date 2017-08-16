from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import dynamic_sql

#获取动态列表
def select_dynamic_list(content,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ content +"%"
    return mysql.get_list(dynamic_sql.select_dynamic_list,(content,content,sear,sear,(page-1)*size,size))

#获取动态详情
def select_dynamic_info(dynamicId):
    return mysql.get_object(dynamic_sql.select_dynamic_info, (dynamicId))

#修改动态信息
def update_dynamic_info(content,imageUrl,isTop,sort,readCount,current_user_id,dynamicId):
    if content == None or content=="" or dynamicId == None or dynamicId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(dynamic_sql.update_dynamic_info,(content,imageUrl,isTop,sort,readCount,current_user_id,dynamicId))
    return data_register > 0


#删除动态
def delete_dynamic(dynamicId,current_user_id):
    if dynamicId == None or dynamicId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(dynamic_sql.delete_dynamic,(current_user_id,dynamicId))
    return data_register > 0



#新增动态信息
def insert_dynamic(content,imageUrl,isTop,sort,readCount,current_user_id):
    if content == None or content=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(dynamic_sql.insert_dynamic,(current_user_id,content,imageUrl,isTop,sort,readCount,current_user_id,current_user_id))
    return data_register > 0

