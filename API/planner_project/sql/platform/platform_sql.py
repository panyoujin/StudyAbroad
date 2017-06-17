#查询前几个 轮询图片
select_platform_cooperation = "SELECT `Id`,`CooperationName`,`ImageUrl`,`Description`,`ClickUrl`,`Sort` " \
                       "FROM `Base_Cooperation` " \
                       "WHERE IsDelete=FALSE " \
                       "ORDER BY IsTop DESC ,Sort DESC,`Id` " \
                       "LIMIT %s, %s "