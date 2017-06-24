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
#新增评论
insert_evaluate="UPDATE `DS_Order` SET `EvaluateContent`='%s',`Synthesis`='%s',`Quality`='%s',`Efficiency`='%s',`Lable`='%s' " \
                "WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=100;" \
                "UPDATE `U_PlannerStatistics` ps,`DS_Order` o  SET ps.`NewEvaluate` = o.`EvaluateContent`" \
                ",ps.`PraiseCount`=`PraiseCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 1 ELSE 0 END)" \
                ",`BadReviewCount`=`BadReviewCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 0 ELSE 1 END) " \
                "WHERE ps.`UserId`=o.`PlannerUserId` AND o.`Id`='%s' AND o.`UserId`='%s' AND o.`OrderStatus`=100 " \
                "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s');"\
                 "INSERT INTO `U_Evaluate` ( `OrderId`, `UserId`, `Content`, `Sort`, `IsFirst`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                 "SELECT  '%s', '%s', '%s', '%s',TRUE, '%s', NOW(), '%s', NOW(), FALSE " \
                "FROM DS_Order WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=100 " \
                "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s') LIMIT 0,1;"
#新增评论
insert_evaluate="UPDATE `DS_Order` SET `EvaluateContent`='%s',`Synthesis`='%s',`Quality`='%s',`Efficiency`='%s',`Lable`='%s' " \
                "WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=100" \
                "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s');"\
                "UPDATE `U_PlannerStatistics` ps,`DS_Order` o  SET ps.`NewEvaluate` = o.`EvaluateContent`" \
                ",ps.`PraiseCount`=`PraiseCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 1 ELSE 0 END)" \
                ",`BadReviewCount`=`BadReviewCount`+(CASE o.`Synthesis`>=3 WHEN TRUE THEN 0 ELSE 1 END) " \
                "WHERE ps.`UserId`=o.`PlannerUserId` AND o.`Id`='%s' AND o.`UserId`='%s' AND o.`OrderStatus`=100 " \
                "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s');"\
                 "INSERT INTO `U_Evaluate` ( `OrderId`, `UserId`, `Content`, `Sort`, `IsFirst`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                 "SELECT  '%s', '%s', '%s', '%s',1, '%s', NOW(), '%s', NOW(), FALSE " \
                "FROM DS_Order WHERE `Id`='%s' AND `UserId`='%s' AND `OrderStatus`=100 " \
                "AND NOT EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s') LIMIT 0,1;"
#回复评论
replay_evaluate="INSERT INTO `U_Evaluate` ( `OrderId`, `UserId`, `Content`, `Sort`, `IsFirst`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                 "SELECT  '%s', '%s', '%s', '%s',0, '%s', NOW(), '%s', NOW(), FALSE " \
                "FROM DS_Order WHERE `Id`='%s' AND (`UserId`='%s' OR PlannerUserId='%s') AND `OrderStatus`=100 " \
                "AND EXISTS (SELECT Id FROM U_Evaluate WHERE OrderId='%s') LIMIT 0,1;"