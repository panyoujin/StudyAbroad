#首页查询前几个 规划师
select_top_planner = "SELECT ui.`UserId`,ui.`Name`,ui.`HeadImage`,ps.`Sort` " \
                       "FROM `U_User` u " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "WHERE u.`IsDelete`=FALSE AND u.`UserType` IN (2,3) " \
                       "ORDER BY ps.Sort DESC ,u.`Id` " \
                       "LIMIT 0, %s "

#查询规划师
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
planner_follw="INSERT INTO `U_Follow` (`UserId`,`FollwUserId`,`FollwTime`) VALUES('%s','%s',NOW()) " \
                          " ON DUPLICATE KEY UPDATE FollwTime=NOW() "
#取消关注
planner_unfollw="DELETE  FROM `StudyAbroad`.`U_Follow`  WHERE `UserId`='%s' AND `FollwUserId` = '%s' "

#查询关注的 规划师
select_follw_planner = "SELECT u.`Id`,ui.`Name`,ui.`HeadImage`,ps.`NewEvaluate`,ps.`CustomerCount`" \
                     ",ps.`PraiseCount`,ps.`BadReviewCount`,t.`Name` AS TeamName,Lables,ps.Sort,f.FollwTime " \
                       "FROM `U_Follow` f " \
                       "JOIN `U_User` u ON f.`FollwUserId`=u.`Id` " \
                       "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id` " \
                       "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id` " \
                       "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id` " \
                       "WHERE f.UserId='%s' AND u.`IsDelete`=FALSE AND u.`UserType` IN (2,3) " \
                       "ORDER BY f.FollwTime DESC " \
                       "LIMIT %s , %s "


#查询规划师详情
select_planner_info = "SELECT ui.`UserId`,ui.`Name`,ui.`HeadImage`,ui.`Autograph`,ps.`NewEvaluate`,ps.`CustomerCount` " \
                      ",ps.`PraiseCount`,ps.`BadReviewCount`,sa.`Name`,st.`Name` " \
                      "FROM `U_PlannerStatistics` ps " \
                      "JOIN `U_UserInfo` ui ON ui.`UserId`=ps.`UserId` " \
                      "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ui.`ServiceAreaId`  " \
                      "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ui.`ServiceTypeId`  " \
                      "WHERE ps.`UserId`='%s'"


#查询规划师资历
select_planner_qualifications = "SELECT 30 `Type`,CONCAT('学位：',e.`Degree`,' 毕业大学：',YEAR(e.`TimeStart`),'-',YEAR(e.`TimeEnd`),' ',e.`University`) AS Content,e.`Sort`,e.`CreateTime`  " \
                                "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' " \
                                "UNION ALL  " \
                                "SELECT 20 `Type`,CONCAT(YEAR(s.`TimeStart`),'-',YEAR(s.`TimeEnd`),' ',s.`Description`) AS Content,s.`Sort`,s.`CreateTime`  " \
                                "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' " \
                                "UNION ALL  " \
                                "SELECT 10 `Type`,CONCAT(YEAR(r.`TimeStart`),'-',YEAR(r.`TimeEnd`),' ',r.`Description`) AS Content,r.`Sort`,r.`CreateTime`  " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' " \
                                "ORDER BY `Type` DESC,`Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#学历背景
select_planner_education = "SELECT e.`Id`,CONCAT('学位：',e.`Degree`,' 毕业大学：',YEAR(e.`TimeStart`),'-',YEAR(e.`TimeEnd`),' ',e.`University`) AS Content,e.`Sort`,e.`CreateTime`  " \
                                "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#社会背景
select_planner_society = "SELECT s.`Id`,CONCAT(YEAR(s.`TimeStart`),'-',YEAR(s.`TimeEnd`),' ',s.`Description`) AS Content,s.`Sort`,s.`CreateTime`  " \
                                "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#资源背景
select_planner_resour = "SELECT r.`Id`,CONCAT(YEAR(r.`TimeStart`),'-',YEAR(r.`TimeEnd`),' ',r.`Description`) AS Content,r.`Sort`,r.`CreateTime`  " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#获取指定规划师评论列表
select_planner_evaluate="SELECT e.`OrderId`,e.`Content`,e.`CreateTime` ,ui.`Name` " \
                      "FROM `U_Evaluate` e " \
                      "LEFT JOIN `U_UserInfo` ui ON e.`UserId` = ui.`UserId` " \
                      "LEFT JOIN `DS_Order` o ON o.`Id`=e.`OrderId` " \
                      "WHERE o.`PlannerUserId`='%s' AND e.`IsFirst`=1 " \
                      "ORDER BY e.`Sort` DESC,e.`CreateTime` DESC " \
                      "LIMIT %s , %s"


#获取指定规划师标签列表
select_planner_lables="SELECT ul.`LableName` FROM `U_UserLable` ul " \
                      "WHERE ul.`UserId`='%s' "\
                      "LIMIT %s , %s"
