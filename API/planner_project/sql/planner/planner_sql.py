#查询前几个 规划师
select_top_planner = "SELECT ui.`UserId`,ui.`Name`,ui.`HeadImage`,ps.`Sort` " \
                       "FROM `U_User` u " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "WHERE u.`IsDelete`=FALSE AND u.`UserType` IN (2,3) " \
                       "ORDER BY ps.Sort DESC ,u.`Id` " \
                       "LIMIT 0, %s "