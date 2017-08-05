from planner_project.data_access import mysql
from planner_project.sql.demand_service import demand_service_sql


#是否已收藏
def get_whether_collection(userid,demandServiceId):
    return mysql.get_object(demand_service_sql.get_whether_collection,(demandServiceId,userid))