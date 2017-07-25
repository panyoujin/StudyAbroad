from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import sys_role_sql

#获取角色列表
def select_sys_role_list(name):
    return mysql.get_list(sys_role_sql.select_sys_role_list,(name,name,"%"+ name +"%"))

#获取角色详情
def select_sys_role_info(role_id):
    if role_id == None or role_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数role_id不能为空")
    return mysql.get_object(sys_role_sql.select_sys_role_info, (role_id))

#修改角色信息
def update_sys_role(name,remark,role_id,current_user_id):
    if role_id == None or role_id=="" or name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_role_sql.update_sys_role,(name,remark,role_id))
    return data_register > 0


#删除角色
def delete_sys_role(role_id,current_user_id):
    if role_id == None or role_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_role_sql.delete_sys_role,(role_id,role_id))
    return data_register > 0

#新增角色信息
def insert_sys_role(name,remark,current_user_id):
    if name == None or name=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(sys_role_sql.insert_sys_role,(name,remark))
    return data_register > 0



#获取菜单列表
def select_permission_list(current_user_id):
    if  current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    return mysql.get_list(sys_role_sql.select_permission_list,())


#获取角色菜单ID列表
def select_role_permission_list(role_id,current_user_id):
    if role_id == None or role_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    return mysql.get_list(sys_role_sql.select_role_permission_list,(role_id))


#获取角色菜单受权
def insert_role_permission(role_id,permissionids,current_user_id):
    if role_id == None or role_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    return mysql.get_list(sys_role_sql.insert_role_permission,(role_id,role_id,permissionids))


#获取用户角色ID
def select_user_role_list(user_id,current_user_id):
    if user_id == None or user_id=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    return mysql.get_object(sys_role_sql.select_user_role_list,(user_id))