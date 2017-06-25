from planner_project.data_access import mysql
from planner_project.sql.demand_service import order_sql

#查询指定规划师完成的订单列表
def select_planner_complete_order_list(userid,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(order_sql.select_planner_complete_order_list,(userid,(page-1)*size,size))


#查询指定规划师的订单列表
def select_planner_order_list(userid,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(order_sql.select_planner_order_list,(userid,(page-1)*size,size))



#获取指定订单的评论
def select_order_evaluate(orderId,page,size):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(order_sql.select_order_evaluate,(orderId,(page-1)*size,size))


#新增评论
def insert_evaluate(orderId,userId,content,sort,synthesis,quality,efficiency,lable):
    if synthesis<=0 or synthesis>5:
        synthesis=5
    if quality<=0 or quality>5:
        quality=5
    if efficiency<=0 or efficiency>5:
        efficiency=5
    return mysql.operate_object(order_sql.insert_evaluate,(content,synthesis,quality,efficiency,lable,orderId,userId,orderId
                                                           ,orderId,userId,orderId
                                                           ,orderId,userId,content,sort,userId,userId,orderId,userId,orderId))


#回复评论
def replay_evaluate(orderId,userId,content,sort):
    return mysql.operate_object(order_sql.replay_evaluate,(orderId,userId,content,sort,userId,userId,orderId,userId,userId,orderId))


#查询指定订单的评论详情
def select_evaluate_info(orderId,page=1,size=10):
    if page<=0:
        page=1
    if size<=0:
        size=10
    return mysql.get_list(order_sql.select_evaluate_info,(orderId,(page-1)*size,size))
