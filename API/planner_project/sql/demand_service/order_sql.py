# 查询指定规划师完成的订单列表
select_planner_complete_order_list = "SELECT du.`Id`,du.`DemandServiceId`,du.`UserId`,du.`OrderStatus`,du.`CreateUserID`,du.`CreateTime`,  " \
                                     "ds.PriceStart,ds.PriceEnd, " \
                                     "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName,  " \
                                     "ds.Description,ui.Name,u.Phone,plannerU.Name AS PlannerName,plannerUser.Phone AS plannerPhone , " \
                                     "du.`OrderStatus`,ui.`HeadImage`, du.EvaluateContent , " \
                                     "CASE du.`OrderStatus` " \
                                     "   WHEN 2 THEN '客服回访' " \
                                     "  WHEN 3 THEN '拟定合同' " \
                                     "  WHEN 4 THEN '线下签约' " \
                                     "  WHEN 5 THEN '平台审查' " \
                                     " WHEN 6 THEN '付款确认' " \
                                     " WHEN 7 THEN '服务完成' " \
                                     " ELSE '订单有误' " \
                                     "END AS OrderStatusStr " \
                                     "FROM `DS_Order` du  " \
                                     "JOIN DS_DemandService ds ON ds.Id=du.DemandServiceId  " \
                                     "JOIN Base_ServiceArea sa ON sa.Id=ds.ServiceAreaId  " \
                                     "JOIN Base_ServiceType st ON st.Id=ds.ServiceTypeId  " \
                                     "JOIN U_UserInfo plannerU ON du.`PlannerUserId`=plannerU.UserId " \
                                     "JOIN U_UserInfo ui ON ui.UserId=du.`UserId`   " \
                                     "JOIN U_User u ON u.Id=du.`UserId`   " \
                                     "JOIN U_User plannerUser ON plannerUser.Id=du.`PlannerUserId`   " \
                                     "WHERE du.IsDelete= FALSE " \
                                     "AND plannerU.`UserId`='%s' " \
                                     "AND du.`OrderStatus`=7 " \
                                     "ORDER BY du.CreateTime DESC " \
                                     "LIMIT %s , %s"
# 查询指定规划师的订单列表
select_planner_order_list = "SELECT du.`Id`,du.`DemandServiceId`,du.`UserId`,du.`OrderStatus`,du.`CreateUserID`,du.`CreateTime`,  " \
                            "ds.PriceStart,ds.PriceEnd, " \
                            "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName,  " \
                            "ds.Description,ui.Name,u.Phone,plannerU.Name AS PlannerName,plannerUser.Phone AS plannerPhone , " \
                            "du.`OrderStatus`,ui.`HeadImage`, " \
                            "CASE du.`OrderStatus` " \
                            "   WHEN 2 THEN '客服回访' " \
                            "  WHEN 3 THEN '拟定合同' " \
                            "  WHEN 4 THEN '线下签约' " \
                            "  WHEN 5 THEN '平台审查' " \
                            " WHEN 6 THEN '付款确认' " \
                            " WHEN 7 THEN '服务完成' " \
                            " ELSE '订单有误' " \
                            "END AS OrderStatusStr ,IF(ee.Id IS NULL,0,1) AS isEvaluate,IF(du.OrderStatus=7,1,0) AS isFished " \
                            "FROM `DS_Order` du  " \
                            "JOIN DS_DemandService ds ON ds.Id=du.DemandServiceId  " \
                            "JOIN Base_ServiceArea sa ON sa.Id=ds.ServiceAreaId  " \
                            "JOIN Base_ServiceType st ON st.Id=ds.ServiceTypeId  " \
                            "JOIN U_UserInfo plannerU ON du.`PlannerUserId`=plannerU.UserId " \
                            "JOIN U_UserInfo ui ON ui.UserId=du.`UserId`   " \
                            "JOIN U_User u ON u.Id=du.`UserId`   " \
                            "JOIN U_User plannerUser ON plannerUser.Id=du.`PlannerUserId`   " \
                            "LEFT JOIN `U_Evaluate` ee ON ee.`OrderId`=du.`Id` AND ee.IsFirst=1 " \
                            "WHERE du.IsDelete= FALSE " \
                            "AND plannerU.`UserId`='%s' " \
                            "ORDER BY du.CreateTime DESC " \
                            "LIMIT %s , %s"

# 查询指定规划师的订单详情
select_planner_order_detail = "SELECT du.`Id`,du.`DemandServiceId`,du.`UserId`,du.`OrderStatus`,du.`CreateUserID`,du.`CreateTime`,du.`ModifTime`,  " \
                              "ds.PriceStart,ds.PriceEnd, " \
                              "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName,  " \
                              "ds.Description,ui.Name,u.Phone,plannerU.Name AS PlannerName,plannerUser.Phone AS plannerPhone , " \
                              "du.`OrderStatus`,ui.`HeadImage`,'' as OrderFlowing, " \
                              "CASE du.`OrderStatus` " \
                              "   WHEN 2 THEN '客服回访' " \
                              "  WHEN 3 THEN '拟定合同' " \
                              "  WHEN 4 THEN '线下签约' " \
                              "  WHEN 5 THEN '平台审查' " \
                              " WHEN 6 THEN '付款确认' " \
                              " WHEN 7 THEN '服务完成' " \
                              " ELSE '订单有误' " \
                              "END AS OrderStatusStr " \
                              "FROM `DS_Order` du  " \
                              "JOIN DS_DemandService ds ON ds.Id=du.DemandServiceId  " \
                              "JOIN Base_ServiceArea sa ON sa.Id=ds.ServiceAreaId  " \
                              "JOIN Base_ServiceType st ON st.Id=ds.ServiceTypeId  " \
                              "JOIN U_UserInfo plannerU ON du.`PlannerUserId`=plannerU.UserId " \
                              "JOIN U_UserInfo ui ON ui.UserId=du.`UserId`   " \
                              "JOIN U_User u ON u.Id=du.`UserId`   " \
                              "JOIN U_User plannerUser ON plannerUser.Id=du.`PlannerUserId`   " \
                              "WHERE du.IsDelete= FALSE " \
                              "AND du.`Id`='%s' "
# 获取订单的状态 以及时间
get_order_status = "SELECT `Id`,`OrderId`,`StartStatus`,`EndStatus`,`ChangeTime` FROM `DS_OrderFlowingWater` " \
                   "WHERE `OrderId`='%s' AND `IsDelete`=FALSE " \
                   "ORDER BY `CreateTime` DESC"
# 获取指定订单的评论
select_order_evaluate = "SELECT e.`OrderId`,e.`Content`,e.`CreateTime` ,ui.`Name` " \
                        "FROM `U_Evaluate` e " \
                        "LEFT JOIN `U_UserInfo` ui ON e.`UserId` = ui.`UserId` " \
                        "WHERE e.`OrderId`='%s' AND e.`IsFirst`=1 " \
                        "ORDER BY e.`CreateTime` " \
                        "LIMIT %s , %s"

insert_order = "INSERT INTO `StudyAbroad`.`DS_Order` (`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`," \
               "`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`," \
               "`CreateUserID`,`CreateTime`) " \
               "VALUES (UUID(),'%s','%s',%s,%s,'%s','%s','%s',%s,%s,%s,%s,'%s','%s','%s',NOW())"

select_order_createtime = "SELECT IF(DATE_ADD(`CreateTime`,INTERVAL 30 SECOND) >= NOW(),0,1) AS isCanInsert FROM `DS_Order` WHERE `CreateUserID`='%s' ORDER BY `CreateTime` DESC LIMIT 1"

select_order_is_evaluate="SELECT count(0) as total FROM U_Evaluate WHERE OrderId='%s';"
# 新增评论
insert_evaluate = "UPDATE `DS_Order` SET `EvaluateContent`='%s',`Synthesis`='%s',`Quality`='%s',`Efficiency`='%s',`Lable`='%s' " \
                  "WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=7 " \
                  "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s');" \
                  "UPDATE `U_PlannerStatistics` ps,`DS_Order` o  SET ps.`NewEvaluate` = o.`EvaluateContent`" \
                  ",ps.`PraiseCount`=`PraiseCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 1 ELSE 0 END)" \
                  ",`BadReviewCount`=`BadReviewCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 0 ELSE 1 END) " \
                  "WHERE ps.`UserId`=o.`PlannerUserId` AND o.`Id`='%s' AND o.`UserId`='%s' AND o.`OrderStatus`=7 " \
                  "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s');" \
                  "INSERT INTO `U_Evaluate` ( `OrderId`, `UserId`, `Content`, `Sort`, `IsFirst`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                  "SELECT  '%s', '%s', '%s', '%s',1, '%s', NOW(), '%s', NOW(), FALSE " \
                  "FROM DS_Order WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=7 " \
                  "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s') LIMIT 0,1;" \
                  "UPDATE `U_UserLable` ul,`DS_Order` o  SET ul.`Count`=ul.`Count`+1,ul.`ModifUserID`='%s',ul.`ModifTime`=NOW() " \
                  "WHERE  o.`Id`='%s' AND o.`UserId`='%s' AND o.`OrderStatus`=7 AND ul.`UserId`=o.`PlannerUserId` AND ul.`LableName`='%s' ; " \
                  "INSERT INTO `U_UserLable` (`UserId`,`LableName`,`Count`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID` ,`ModifTime`,`IsDelete`) " \
                  "SELECT o.`PlannerUserId`,'%s',1,0,'%s',NOW(),'%s',NOW(),FALSE FROM `DS_Order` o " \
                  "WHERE  o.`Id`='%s' AND o.`UserId`='%s' AND o.`OrderStatus`=7  " \
                  "AND NOT EXISTS (SELECT Id FROM U_UserLable WHERE UserId=o.PlannerUserId AND LableName='%s') LIMIT 0,1;"
# 回复评论
replay_evaluate = "INSERT INTO `U_Evaluate` ( `OrderId`, `UserId`, `Content`, `Sort`, `IsFirst`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                  "SELECT  '%s', '%s', '%s', '%s',0, '%s', NOW(), '%s', NOW(), FALSE " \
                  "FROM DS_Order WHERE `Id`='%s' AND (`UserId`='%s' OR PlannerUserId='%s') AND `OrderStatus`=7 " \
                  "AND EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s') LIMIT 0,1;"

# 查询指定订单的评论详情
select_evaluate_info = "SELECT e.`OrderId`,e.`Content`,e.`CreateTime` ,ui.`Name`, ui.`HeadImage` " \
                       "FROM `U_Evaluate` e " \
                       "LEFT JOIN `U_UserInfo` ui ON e.`UserId` = ui.`UserId` " \
                       "WHERE e.`OrderId`='%s' " \
                       "ORDER BY e.`IsFirst` DESC,e.`Sort` DESC,e.`CreateTime` DESC " \
                       "LIMIT %s , %s"
# 新增订单流水表数据
insert_order_flowing = "insert into `DS_OrderFlowingWater` (`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`) " \
                       "values('%s','%s',%s,%s,'',now(),'%s',now())"
#更新订单状态
update_order_status = "UPDATE `DS_Order` SET OrderStatus=%s,ModifUserID='%s',ModifTime=NOW() WHERE Id='%s' AND OrderStatus=%s"

#订单完成的时候修改规划师统计的订单数量和客户数量
update_planner_statistics = "UPDATE `U_PlannerStatistics` ps JOIN `DS_Order` o SET  ps.CustomerCount=ps.CustomerCount+1,ps.OrderCount=ps.OrderCount+1,ps.ModifUserID='%s',ps.ModifTime=NOW() WHERE  o.Id='%s' AND ps.UserId=o.`PlannerUserId` AND o.OrderStatus= %s AND %s=7"

