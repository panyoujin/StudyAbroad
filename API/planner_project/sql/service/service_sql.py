#查询前几个 服务
select_top_service = "SELECT s.`Id`,s.`Name`,s.`Sort` " \
                       "FROM `Base_ServiceType` s " \
                       "WHERE s.`IsDelete` =FALSE " \
                       "ORDER BY s.`Sort` DESC,s.`Id` " \
                       "LIMIT 0, %s "