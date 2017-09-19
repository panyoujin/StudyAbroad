
from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import user_sql,upgrade_user_sql

#获取用户列表
def select_user_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"

    listCount = mysql.get_object(user_sql.select_user_list_count,(name,name,sear,sear))
    data= mysql.get_list(user_sql.select_user_list,(name,name,sear,sear,(page-1)*size,size))
    return data,listCount

#获取用户详情
def select_user_info(userId):
    return mysql.get_object(user_sql.select_user_info, (userId))

#修改用户信息
def update_userinfo(account,phone,password,userType,name,realName,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,userId,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    if account == None or account=="" or name == None or name==""or realName == None or realName=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="帐号姓名昵称不能为空")
    a_userid = mysql.get_object(user_sql.select_userid_by_account, (account))
    if a_userid!=None and a_userid!="" and a_userid["Id"]!=userId:
        raise custom_error.CustomFlaskErr(status_code=500, message="账号已经存在")
    data_register = mysql.operate_object(user_sql.update_user_info,(account,phone,password,userType,current_user_id,userId
                                                                    ,name,realName,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,current_user_id,userId))
    if userType==2 or userType ==3:
        mysql.operate_object(upgrade_user_sql.insert_planner_statistics,(userId,current_user_id,current_user_id,userId,userId))
    return data_register > 0


#删除用户
def delete_user(userId,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    data_register = mysql.operate_object(user_sql.delete_user,(current_user_id,userId,current_user_id,userId))
    return data_register > 0

#新增用户信息
def insert_userinfo(userId,account,phone,password,userType,name,realName,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    if account == None or account=="" or name == None or name==""or realName == None or realName=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="帐号姓名不能为空")
    a_userid = mysql.get_object(user_sql.select_userid_by_account, (account))
    if a_userid!=None and a_userid!="" :
        raise custom_error.CustomFlaskErr(status_code=500, message="账号已经存在")
    data_register = mysql.operate_object(user_sql.insert_user,(userId,account,phone,password,userType,current_user_id,current_user_id
                                                               ,userId,name,realName,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,current_user_id,current_user_id))
    if userType==2 or userType ==3:
        mysql.operate_object(upgrade_user_sql.insert_planner_statistics,(userId,current_user_id,current_user_id,userId,userId))
    return data_register > 0