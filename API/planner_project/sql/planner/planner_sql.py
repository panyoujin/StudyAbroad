#查询前几个 规划师
select_top_planner = "SELECT ui.`UserId`,ui.`Name`,ui.`HeadImage`,ps.`Sort` " \
                       "FROM `U_User` u " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "WHERE u.`IsDelete`=FALSE AND u.`UserType` IN (2,3) " \
                       "ORDER BY ps.Sort DESC ,u.`Id` " \
                       "LIMIT 0, %s "

#查询前几个 规划师
select_search_planner = "SELECT * FROM ( SELECT u.`Id`,ui.`Name`,ui.`HeadImage`,ps.`NewEvaluate`,ps.`CustomerCount`" \
                     ",ps.`PraiseCount`,ps.`BadReviewCount`,t.`Name` AS TeamName,Lables,ps.Sort " \
                       "FROM `U_User` u " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "LEFT JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ui.`ServiceAreaId` " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ui.`ServiceTypeId` " \
                       "LEFT JOIN `U_UserLable` ul ON ul.`UserId`=u.`Id` " \
                       "WHERE u.`UserType` IN (2,3) AND u.`IsDelete` = FALSE " \
                       "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR sa.`Name` LIKE '%s' OR st.`Name` LIKE '%s' OR ul.`LableName` LIKE '%s') " \
                        "GROUP BY u.`Id`) AS t "\
                       "ORDER BY Sort DESC ,`Id` " \
                       "LIMIT %s , %s "
#关注
planner_follw="INSERT INTO `U_Follow` (`UserId`,`FollwUserId`,`FollwTime`) VALUES('%s','%s',NOW()) "

#查询关注的 规划师
select_follw_planner = "SELECT u.`Id`,ui.`Name`,ui.`HeadImage`,ps.`NewEvaluate`,ps.`CustomerCount`" \
                     ",ps.`PraiseCount`,ps.`BadReviewCount`,t.`Name` AS TeamName,Lables,ps.Sort " \
                       "FROM `U_Follow` f " \
                       "JOIN `U_User` u ON f.`FollwUserId`=u.`Id` " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id` " \
                       "WHERE f.UserId='%s' AND u.`IsDelete`=FALSE AND u.`UserType` IN (2,3) " \
                       "ORDER BY ps.Sort DESC ,u.`Id` " \
                       "LIMIT %s , %s "
