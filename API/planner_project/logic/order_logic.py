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

