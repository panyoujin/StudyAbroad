from planner_project.data_access import mysql
from planner_project.sql.planner import planner_sql

#规划师详情
def select_planner_info(userid):

    return mysql.get_object(planner_sql.select_planner_info,(userid))
#资历
def select_planner_qualifications(userid,page=1,size=2):
    if page<=0:
        page=1
    if size<=0:
        size=2
    return mysql.get_list(planner_sql.select_planner_qualifications,(userid,userid,userid,(page-1)*size,size))
#学历背景
def select_planner_education(userid,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_planner_education,(userid,(page-1)*size,size))


#社会背景
def select_planner_society(userid,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_planner_society,(userid,(page-1)*size,size))


#资源背景
def select_planner_resour(userid,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_planner_resour,(userid,(page-1)*size,size))


#获取指定规划师评论列表
def select_planner_evaluate(userid,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_planner_evaluate,(userid,(page-1)*size,size))


#获取指定规划师标签列表
def select_planner_lables(userid,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_planner_lables,(userid,(page-1)*size,size))


#是否已关注
def get_whether_follw(userid,plannerId):
    return mysql.get_object(planner_sql.get_whether_follw,(plannerId,userid))


#获取标签列表
def select_lable_list(page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(planner_sql.select_lable_list,((page-1)*size,size))