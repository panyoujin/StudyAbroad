
from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import planner_sql,user_sql,upgrade_user_sql

#获取规划师列表
def select_planner_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    listCount = mysql.get_object(planner_sql.select_planner_list_count,(name,name,sear))
    data = mysql.get_list(planner_sql.select_planner_list,(name,name,sear,(page-1)*size,size))
    return  data,listCount

#获取规划师详情
def select_planner_info(userId):
    return mysql.get_object(planner_sql.select_planner_info, (userId))


#修改用户信息
def update_planner(account,phone,userType,name,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,ServiceAreaId,ServiceTypeId,userId,current_user_id):
    if userId == None or userId=="" or current_user_id == None or current_user_id=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="参数不正确，请刷新后重试")
    if account == None or account=="" or name == None or name=="":
        raise custom_error.CustomFlaskErr(status_code=500, message="帐号姓名不能为空")
    a_userid = mysql.get_object(user_sql.select_userid_by_account, (account))
    if a_userid!=None and a_userid!="" and a_userid["Id"]!=userId:
        raise custom_error.CustomFlaskErr(status_code=500, message="账号已经存在")
    data_register = mysql.operate_object(planner_sql.update_planner,(account,phone,userType,current_user_id,userId
                                                                    ,name,sex,age,education,address,email,headImage,IDCard,IDCardJust,IDCardBack,ServiceAreaId,ServiceTypeId,current_user_id,userId))
    #if userType==2 or userType ==3:
    #    mysql.operate_object(upgrade_user_sql.insert_planner_statistics,(userId,current_user_id,current_user_id,userId,userId))
    return data_register > 0

#学历背景
def select_planner_education(userid):
    return mysql.get_list(planner_sql.select_planner_education,(userid))

#学历背景详情
def select_education_info(id):
    return mysql.get_object(planner_sql.select_education_info,(id))

#社会背景
def select_planner_society(userid):
    return mysql.get_list(planner_sql.select_planner_society,(userid))

#社会背景详情
def select_society_info(id):
    return mysql.get_object(planner_sql.select_society_info,(id))

#资源背景
def select_planner_resour(userid):
    return mysql.get_list(planner_sql.select_planner_resour,(userid))


#资源背景详情
def select_resour_info(id):
    return mysql.get_object(planner_sql.select_resour_info,(id))

#新增学历背景
def insert_education(id,userid,TimeStart,TimeEnd,University,Degree,Sort,insertuserid):
    return mysql.operate_object(planner_sql.insert_education,(id,userid,TimeStart,TimeEnd,University,Degree,Sort
                                                              ,insertuserid,insertuserid))


#修改学历背景
def update_education(TimeStart,TimeEnd,University,Degree,Sort,Id,updateuserid):
    return mysql.operate_object(planner_sql.update_education,(TimeStart,TimeEnd,University,Degree,Sort,updateuserid,Id))


#删除学历背景
def delete_education(id,updateuserid):
    return mysql.operate_object(planner_sql.delete_education,(updateuserid,id))


#新增资源背景
def insert_resour(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid):
    return mysql.operate_object(planner_sql.insert_resour,(id,userid,TimeStart,TimeEnd,Description,Sort
                                                           ,insertuserid,insertuserid))


#修改资源背景
def update_resour(TimeStart,TimeEnd,Description,Sort,Id,updateuserid):
    return mysql.operate_object(planner_sql.update_resour,(TimeStart,TimeEnd,Description,Sort,updateuserid,Id))


#删除资源背景
def delete_resour(id,updateuserid):
    return mysql.operate_object(planner_sql.delete_resour,(updateuserid,id))


#新增社会背景
def insert_society(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid):
    return mysql.operate_object(planner_sql.insert_society,(id,userid,TimeStart,TimeEnd,Description,Sort
                                                           ,insertuserid,insertuserid))


#修改社会背景
def update_society(TimeStart,TimeEnd,Description,Sort,Id,updateuserid):
    return mysql.operate_object(planner_sql.update_society,(TimeStart,TimeEnd,Description,Sort,updateuserid,Id))


#删除社会背景
def delete_society(id,updateuserid):
    return mysql.operate_object(planner_sql.delete_society,(updateuserid,id))

#修改大v
def update_BigV(isv,id,updateuserid):
    return mysql.operate_object(planner_sql.update_BigV, (isv,updateuserid,id))
    #return mysql.operate_object(planner_sql.update_BigV,(isv,updateuserid,id))
