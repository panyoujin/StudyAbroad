from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import service_area_sql

#获取区域列表
def select_service_area_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(service_area_sql.select_service_area_list,(name,name,sear,(page-1)*size,size))

#获取区域详情
def select_service_area_info(areaId):
    return mysql.get_object(service_area_sql.select_service_area_info, (areaId))

#修改区域信息
def update_service_area_info(name,description,isTop,sort,current_user_id,areaId):
    if name == None or name=="" or areaId == None or areaId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_area_sql.update_service_area_info,(name,description,isTop,sort,current_user_id,areaId))
    return data_register > 0


#删除区域
def delete_service_area(areaId,current_user_id):
    if areaId == None or areaId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_area_sql.delete_service_area,(current_user_id,areaId,current_user_id,areaId))
    return data_register > 0


#新增区域信息
def insert_service_area(name,description,isTop,sort,current_user_id):
    if name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(service_area_sql.insert_service_area,(name,description,isTop,sort,current_user_id,current_user_id))
    return data_register > 0

