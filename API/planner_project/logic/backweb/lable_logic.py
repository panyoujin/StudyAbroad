from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import lable_sql

#获取标签列表
def select_lable_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(lable_sql.select_lable_list,(name,name,sear,(page-1)*size,size))

#获取标签详情
def select_lable_info(lableId):
    return mysql.get_object(lable_sql.select_lable_info, (lableId))

#修改标签信息
def update_lable_info(name,description,isTop,sort,current_user_id,lableId):
    if name == None or name=="" or lableId == None or lableId==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(lable_sql.update_lable_info,(name,description,isTop,sort,current_user_id,lableId))
    return data_register > 0


#删除标签
def delete_lable(lableId,current_user_id):
    if lableId == None or lableId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(lable_sql.delete_lable,(current_user_id,lableId,current_user_id,lableId))
    return data_register > 0



#新增标签信息
def insert_lable(name,description,isTop,sort,current_user_id):
    if name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(lable_sql.insert_lable,(name,description,isTop,sort,current_user_id,current_user_id))
    return data_register > 0

