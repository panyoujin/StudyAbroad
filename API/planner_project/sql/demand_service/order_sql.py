#查询指定规划师完成的订单列表
select_planner_complete_order_list="SELECT o.`Id`,o.`Description` ,o.`TimeConsuming`,o.`EvaluateContent`,ui.`Name` " \
                                   "FROM `DS_Order` o " \
                                   "LEFT JOIN `U_UserInfo` ui ON o.`UserId`=ui.`UserId` " \
                                   "WHERE o.`PlannerUserId`='%s' AND o.`OrderStatus`=100 " \
                                   "ORDER BY o.`Sort` DESC,o.`ModifTime` DESC "\
                                    "LIMIT %s , %s "
#查询指定规划师的订单列表
select_planner_order_list="SELECT o.`Id`,o.`Description` ,o.`TimeConsuming`,o.`EvaluateContent`,ui.`Name` " \
                                   "FROM `DS_Order` o " \
                                   "LEFT JOIN `U_UserInfo` ui ON o.`UserId`=ui.`UserId` " \
                                   "WHERE o.`PlannerUserId`='%s' " \
                                   "ORDER BY o.`Sort` DESC,o.`ModifTime` DESC "\
                                    "LIMIT %s , %s "


#获取指定订单的评论
select_order_evaluate="SELECT e.`OrderId`,e.`Content`,e.`CreateTime` ,ui.`Name` " \
                      "FROM `U_Evaluate` e " \
                      "LEFT JOIN `U_UserInfo` ui ON e.`UserId` = ui.`UserId` " \
                      "WHERE e.`OrderId`='%s' AND e.`IsFirst`=1 " \
                      "ORDER BY e.`CreateTime` " \
                      "LIMIT %s , %s"

insert_order="INSERT INTO `StudyAbroad`.`DS_Order` (`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`," \
              "`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`," \
              "`CreateUserID`,`CreateTime`) " \
              "VALUES (UUID(),'%s','%s',%s,%s,'%s','%s','%s',%s,%s,%s,%s,'%s','%s','%s',NOW())"

select_order_createtime = "SELECT IF(DATE_ADD(`CreateTime`,INTERVAL 30 SECOND) >= NOW(),0,1) AS isCanInsert FROM `DS_Order` WHERE `CreateUserID`='%s' ORDER BY `CreateTime` DESC LIMIT 1"