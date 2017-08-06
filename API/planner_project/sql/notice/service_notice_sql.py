# 根据规划师id获取团队消息
select_service_notice_list1 = "SELECT o.`Id`,o.`PlannerUserId`,o.`UserId`,o.`DemandServiceId`,o.`DemandServiceDescription`,o.`Description`, " \
                              "ds.`Name` AS serviceName,ds.`Description`,o.OrderStatus,'' AS OrderStatusStr " \
                              "FROM `DS_Order` o " \
                              "JOIN `DS_DemandService` ds ON o.`DemandServiceId` = ds.`Id` " \
                              "WHERE o.PlannerUserId='%s'  ORDER BY IFNULL(o.ModifTime,o.CreateTime) DESC " \
                              "LIMIT %s,%s"

# 根据用户id获取团队消息
select_service_notice_list2 = "SELECT o.`Id`,o.`PlannerUserId`,o.`UserId`,o.`DemandServiceId`,o.`DemandServiceDescription`,o.`Description`, " \
                              "ds.`Name` AS serviceName,ds.`Description`,o.OrderStatus,'' AS OrderStatusStr " \
                              "FROM `DS_Order` o " \
                              "JOIN `DS_DemandService` ds ON o.`DemandServiceId` = ds.`Id` " \
                              "WHERE o.UserId='%s'  ORDER BY IFNULL(o.ModifTime,o.CreateTime) DESC " \
                              "LIMIT %s,%s"
