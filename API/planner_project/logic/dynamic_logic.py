from planner_project.data_access import mysql
from planner_project.sql.dynamic import dynamic_sql
from planner_project.common import  custom_error

#获取动态列表
def select_dynamic_list(page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(dynamic_sql.select_dynamic_list,((page-1)*size,size))


#获取指定的用户动摇列表
def select_user_dynamic_list(userid,page,size):
    if userid == None or userid=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="输入不正确，请刷新后重试")
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(dynamic_sql.select_user_dynamic_list,(userid,(page-1)*size,size))

#新增动态
def insert_dynanic(userid,content,imageUrl):
    if userid == None or userid=="" or content == None or content=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="输入不正确，请刷新后重试")
    return mysql.operate_object(dynamic_sql.insert_dynanic,(userid,content,imageUrl,userid,userid))

#获取指定的动态
def select_dynamic_info(dynamicId):
    if dynamicId == None or dynamicId=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="输入不正确，请刷新后重试")
    mysql.operate_object(dynamic_sql.update_dynamic_readcount, (dynamicId))
    return mysql.get_object(dynamic_sql.select_dynamic_info,(dynamicId))