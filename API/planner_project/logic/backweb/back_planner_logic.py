
from planner_project.common import custom_error
from planner_project.data_access import mysql
from planner_project.sql.backweb import planner_sql

#获取规划师列表
def select_planner_list(name,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    sear="%"+ name +"%"
    return mysql.get_list(planner_sql.select_planner_list,(name,name,sear,sear,sear,(page-1)*size,size))

#获取规划师详情
def select_planner_info(userId):
    return mysql.get_object(planner_sql.select_planner_info, (userId))

#学历背景
def select_planner_education(userid):
    return mysql.get_list(planner_sql.select_planner_education,(userid))


#社会背景
def select_planner_society(userid):
    return mysql.get_list(planner_sql.select_planner_society,(userid))


#资源背景
def select_planner_resour(userid):
    return mysql.get_list(planner_sql.select_planner_resour,(userid))

#新增学历背景
def insert_education(id,userid,TimeStart,TimeEnd,University,Degree,Sort,insertuserid):
    return mysql.get_list(planner_sql.insert_education,(id,userid,TimeStart,TimeEnd,University,Degree,Sort,insertuserid,insertuserid))


#修改学历背景
def update_education(TimeStart,TimeEnd,University,Degree,Sort,Id,updateuserid):
    return mysql.get_list(planner_sql.update_education,(TimeStart,TimeEnd,University,Degree,Sort,updateuserid,Id))


#删除学历背景
def delete_education(id,updateuserid):
    return mysql.get_list(planner_sql.delete_education,(updateuserid,id))


#新增资源背景
def insert_resour(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid):
    return mysql.get_list(planner_sql.insert_resour,(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid,insertuserid))


#修改资源背景
def update_resour(TimeStart,TimeEnd,Description,Sort,Id,updateuserid):
    return mysql.get_list(planner_sql.update_resour,(TimeStart,TimeEnd,Description,Sort,updateuserid,Id))


#删除资源背景
def delete_resour(id,updateuserid):
    return mysql.get_list(planner_sql.delete_resour,(updateuserid,id))


#新增社会背景
def insert_society(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid):
    return mysql.get_list(planner_sql.insert_society,(id,userid,TimeStart,TimeEnd,Description,Sort,insertuserid,insertuserid))


#修改社会背景
def update_society(TimeStart,TimeEnd,Description,Sort,Id,updateuserid):
    return mysql.get_list(planner_sql.update_society,(TimeStart,TimeEnd,Description,Sort,updateuserid,Id))


#删除社会背景
def delete_society(id,updateuserid):
    return mysql.get_list(planner_sql.delete_society,(updateuserid,id))
