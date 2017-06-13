#查询前几个 轮询图片
select_top_carousel = "SELECT `Id`,`ImageName`,`ImageUrl`,`Description`,`IsTop`,`ClickUrl`,`Sort` " \
                       "FROM `Base_HomePageCarouselImage` " \
                       "WHERE IsDelete=FALSE " \
                       "ORDER BY IsTop DESC ,Sort DESC,`Id` " \
                       "LIMIT 0, %s "