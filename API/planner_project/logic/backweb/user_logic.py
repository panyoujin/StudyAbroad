
from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import user_sql

#获取用户列表
def select_user_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(user_sql.select_user_list,(name,name,sear,sear,(page-1)*size,size))

#获取用户详情
def select_user_info(userId):
    return mysql.get_object(user_sql.select_user_info, (userId))

#修改用户信息
def update_userinfo(name,sex,age,education,address,email,userId,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    if name == None or name=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="姓名不能为空")
    data_register = mysql.operate_object(user_sql.update_user_info,(name,sex,age,education,address,email,current_user_id,userId))
    return data_register > 0


#删除用户
def delete_user(userId,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(user_sql.delete_user,(current_user_id,userId,current_user_id,userId))
    return data_register > 0