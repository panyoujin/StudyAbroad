select_order_list = "SELECT du.`Id`,du.`DemandServiceId`,du.`UserId`,du.`OrderStatus`,du.`CreateUserID`,du.`CreateTime`, " \
                    "ds.PriceStart,ds.PriceEnd, " \
                    "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName, " \
                    "ds.Description,ui.Name,u.Phone,plannerU.Name AS PlannerName,plannerUser.Phone AS plannerPhone " \
                    "FROM `DS_Order` du " \
                    "JOIN DS_DemandService ds ON ds.Id=du.DemandServiceId " \
                    "JOIN Base_ServiceArea sa ON sa.Id=ds.ServiceAreaId  " \
                    "JOIN Base_ServiceType st ON st.Id=ds.ServiceTypeId  " \
                    "JOIN U_UserInfo plannerU ON du.UserId=plannerU.UserId  " \
                    "JOIN U_UserInfo ui ON ui.UserId=ds.UserId  " \
                    "JOIN U_User u ON u.Id=ds.UserId  " \
                    "JOIN U_User plannerUser ON plannerUser.Id=du.UserId " \
                    "WHERE du.IsDelete= FALSE " \
                    "ORDER BY du.CreateTime DESC " \
                    "LIMIT %s , %s"

select_order_count = "SELECT COUNT(1) AS count " \
                     "FROM `DS_Order` du " \
                     "JOIN DS_DemandService ds ON ds.Id=du.DemandServiceId " \
                     "JOIN Base_ServiceArea sa ON sa.Id=ds.ServiceAreaId  " \
                     "JOIN Base_ServiceType st ON st.Id=ds.ServiceTypeId  " \
                     "JOIN U_UserInfo plannerU ON du.UserId=plannerU.UserId  " \
                     "JOIN U_UserInfo ui ON ui.UserId=ds.UserId  " \
                     "JOIN U_User u ON u.Id=ds.UserId  " \
                     "JOIN U_User plannerUser ON plannerUser.Id=du.UserId " \
                     "WHERE du.IsDelete= FALSE "

# 新增订单流水表数据
insert_order_flowing = "insert into `DS_OrderFlowingWater` (`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`) " \
                       "values('%s','%s',%s,%s,'',now(),'%s',now())"
#更新订单状态
update_order_status="UPDATE `DS_Order` SET OrderStatus=%s,ModifUserID='%s',ModifTime=NOW() WHERE Id='%s' AND OrderStatus=%s"