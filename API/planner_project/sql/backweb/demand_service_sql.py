# 获取需求承接表数据
select_demand_undertake_list = "SELECT du.`Id`,du.`DemandId`,du.`UserId`,du.`Status`,du.`CreateUserID`,du.`CreateTime`, " \
                               "if(du.IsUser=1,'是','否') IsUserStr,ds.PriceStart,ds.PriceEnd," \
                               "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName, " \
                               "ds.Description " \
                               "FROM `DS_DemandUndertake` du " \
                               "JOIN DS_DemandService ds on ds.Id=du.DemandId " \
                               "join Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                               "join Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                               "WHERE du.Status= 1" \
                               "ORDER BY du.CreateTime DESC " \
                               "LIMIT %s , %s"
# 获取需求承接表数据 总数
select_demand_undertake_count = "SELECT count(1) as count " \
                                "FROM `DS_DemandUndertake` du " \
                                "JOIN DS_DemandService ds on ds.Id=du.DemandId " \
                                "join Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                                "join Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                                "WHERE du.Status= 1" \
                                "ORDER BY du.CreateTime DESC "
