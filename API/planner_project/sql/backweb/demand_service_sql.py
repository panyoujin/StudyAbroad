# 获取需求承接表数据
select_demand_undertake_list = "SELECT du.`Id`,du.`DemandId`,du.`UserId`,du.`Status`,du.`CreateUserID`,du.`CreateTime`, " \
                               "if(du.IsUser=1,'是','否') IsUserStr,ds.PriceStart,ds.PriceEnd," \
                               "ds.TimeStart,ds.TimeEnd,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName, " \
                               "ds.Description,ui.Name,u.Phone,plannerU.Name AS PlannerName,plannerUser.Phone as plannerPhone " \
                               "FROM `DS_DemandUndertake` du " \
                               "JOIN DS_DemandService ds on ds.Id=du.DemandId " \
                               "join Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                               "join Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                               "JOIN U_UserInfo plannerU on du.UserId=plannerU.UserId " \
                               "JOIN U_UserInfo ui on ui.UserId=ds.UserId " \
                               "JOIN U_User u on u.Id=ds.UserId " \
                               "JOIN U_User plannerUser on plannerUser.Id=du.UserId " \
                               "WHERE du.Status= 1 " \
                               "ORDER BY du.CreateTime DESC " \
                               "LIMIT %s , %s"
# 获取需求承接表数据 总数
select_demand_undertake_count = "SELECT count(1) as count " \
                                "FROM `DS_DemandUndertake` du " \
                                "JOIN DS_DemandService ds on ds.Id=du.DemandId " \
                                "join Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                                "join Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                                "JOIN U_UserInfo plannerU on du.UserId=plannerU.UserId " \
                                "JOIN U_UserInfo ui on ui.UserId=ds.UserId " \
                                "JOIN U_User u on u.Id=ds.UserId " \
                                "JOIN U_User plannerUser on plannerUser.Id=du.UserId " \
                                "WHERE du.Status= 1"

# ==============需求管理
# 后台获取需求列表
select_demand_list = "SELECT ds.Description ,sa.Name AS ServiceAreaName,st.Name AS ServiceTypeName, " \
                     "u.Phone,ds.CreateTime,ui.Name,format(ds.PriceStart,2) PriceStart," \
                     "format(ds.PriceEnd,2) AS PriceEnd,TimeStart,TimeEnd, " \
                     "if(ds.IsTop=0,'否','是') AS TopStr,if(ui.Sex=1,'男','女') AS Sex,ui.Age,ui.Address, " \
                     "if(ds.IsUndertake=0,'未承接',if(ds.IsUndertake=1,'已承接','已失效')) UndertakeStr," \
                     " ds.IsUndertake ,ds.Id,ds.IsTop " \
                     "from DS_DemandService ds " \
                     "JOIN U_User u on ds.UserId=u.Id " \
                     "JOIN Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                     "JOIN Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                     "JOIN U_UserInfo ui on ds.UserId=ui.UserId " \
                     " where ds.Type=1 " \
                     "ORDER BY ds.IsUndertake ASC ,ds.CreateTime DESC " \
                     "LIMIT %s,%s"
# 后台获取需求列表 数量
select_demand_count = "SELECT count(1) AS count " \
                      "from DS_DemandService ds " \
                      "JOIN U_User u on ds.UserId=u.Id " \
                      "JOIN Base_ServiceArea sa on sa.Id=ds.ServiceAreaId " \
                      "JOIN Base_ServiceType st on st.Id=ds.ServiceTypeId " \
                      "JOIN U_UserInfo ui on ds.UserId=ui.UserId where ds.Type=1"

#修改需求的置顶状态或者失效状态
update_demand_status="UPDATE DS_DemandService SET IsTop=%s,IsUndertake=%s,ModifUserID='%s',ModifTime=now() WHERE Id='%s' "
#如果设置需求失效，把对应的承接需求也设置拒绝
update_demand_undertake_status="UPDATE DS_DemandUndertake SET Status=3 ,ModifUserID='%s',ModifTime=now() WHERE DemandId='%s'"