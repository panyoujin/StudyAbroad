#查询前几个 服务
select_top_service = "SELECT s.`Id`,s.`Name`,s.`Sort` " \
                       "FROM `Base_ServiceType` s " \
                       "WHERE s.`IsDelete` =FALSE " \
                       "ORDER BY s.`Sort` DESC,s.`Id` " \
                       "LIMIT 0, %s "
#查询服务列表
select_service_list="SELECT `Id`,`Name` FROM `Base_ServiceType` " \
                    "WHERE `IsDelete`=FALSE ORDER BY `IsTop` DESC,`Sort` DESC,`CreateTime` DESC"

#查询服务区域列表
select_area_list="SELECT `Id`,`Name` FROM `Base_ServiceArea` " \
                 "WHERE `IsDelete`=FALSE ORDER BY `Sort` DESC,`CreateTime` DESC"