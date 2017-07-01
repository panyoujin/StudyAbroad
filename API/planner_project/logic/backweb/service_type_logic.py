from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import service_type_sql

#获取服务列表
def select_service_type_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(service_type_sql.select_service_type_list,(name,name,sear,(page-1)*size,size))

#获取服务详情
def select_service_type_info(typeId):
    return mysql.get_object(service_type_sql.select_service_type_info, (typeId))

#修改服务信息
def update_service_type_info(name,description,isTop,sort,current_user_id,typeId):
    if name == None or name=="" or typeId == None or typeId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_type_sql.update_service_type_info,(name,description,isTop,sort,current_user_id,typeId))
    return data_register > 0


#删除服务
def delete_service_type(typeId,current_user_id):
    if typeId == None or typeId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_type_sql.delete_service_type,(current_user_id,typeId,current_user_id,typeId))
    return data_register > 0



#新增服务信息
def insert_service_type(name,description,isTop,sort,current_user_id):
    if name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_type_sql.insert_service_type,(name,description,isTop,sort,current_user_id,current_user_id))
    return data_register > 0

