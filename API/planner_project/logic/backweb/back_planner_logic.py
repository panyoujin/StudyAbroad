
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
