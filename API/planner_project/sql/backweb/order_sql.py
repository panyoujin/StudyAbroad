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
