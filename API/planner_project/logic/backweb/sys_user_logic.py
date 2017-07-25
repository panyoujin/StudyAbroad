from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import sys_user_sql

#获取用户列表
def select_sys_user_list(uname,nname,phone,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(sys_user_sql.select_sys_user_list,(uname,uname,"%"+ uname +"%",nname,nname,"%"+ nname +"%",phone,phone,"%"+ phone +"%",(page-1)*size,size))

#获取用户详情
def select_sys_user_info(user_id):
    if user_id == None or user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数user_id不能为空")
    return mysql.get_object(sys_user_sql.select_sys_user_info, (user_id))

#获取用户详情
def select_sys_user_info_by_username(username):
    if username == None or username=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数user_id不能为空")
    return mysql.get_object(sys_user_sql.select_sys_user_info_by_username, (username))

#修改用户信息
def update_sys_user(uname,nname,phone,email,descript,user_id,current_user_id):
    if uname == None or uname=="" or user_id == None or user_id==""or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_user_sql.update_sys_user,(uname,nname,phone,email,descript,user_id
                                                                       ,uname,phone,current_user_id,user_id))
    return data_register > 0


#删除用户
def delete_sys_user(user_id,current_user_id):
    if user_id == None or user_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_user_sql.delete_sys_user,(user_id,user_id))
    return data_register > 0

#新增用户信息
def insert_sys_user(user_id,uname,nname,phone,email,descript,current_user_id):
    if user_id == None or user_id=="" or uname == None or uname==""  or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_user_sql.insert_sys_user,(user_id,uname,nname,phone,email,descript
                                                                       ,user_id,uname,current_user_id,current_user_id))
    return data_register > 0


#修改用户角色
def update_sys_userrole(user_id,role_id,current_user_id):
    if user_id == None or user_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_user_sql.insert_user_role,(user_id,user_id,role_id))
    return data_register > 0

