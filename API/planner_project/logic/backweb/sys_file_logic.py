from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import sys_file_sql

#获取资料列表
def select_sys_file_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(sys_file_sql.select_sys_file_list,(name,name,sear,(page-1)*size,size))

#获取资料详情
def select_sys_file_info(fileId):
    return mysql.get_object(sys_file_sql.select_sys_file_info, (fileId))

#修改资料信息
def update_sys_file_info(name,fileUrl,isTop,sort,current_user_id,fileId):
    if name == None or name=="" or fileId == None or fileId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_file_sql.update_sys_file_info,(name,fileUrl,isTop,sort,current_user_id,fileId))
    return data_register > 0


#删除资料
def delete_sys_file(fileId,current_user_id):
    if fileId == None or fileId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_file_sql.delete_sys_file,(current_user_id,fileId))
    return data_register > 0



#新增资料信息
def insert_sys_file(name,fileUrl,isTop,sort,current_user_id):
    if name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_file_sql.insert_sys_file,(name,fileUrl,isTop,sort,current_user_id,current_user_id))
    return data_register > 0

