#获取用户列表
select_planner_list="SELECT u.`Id`,ui.`Name`,ui.`HeadImage`,u.`Phone`,ps.`NewEvaluate`,ps.`CustomerCount`  ,ps.`PraiseCount`" \
                    ",ps.`BadReviewCount`,t.`Name` AS TeamName,Lables,ps.Sort ,ps.`IsTop`,sa.`Name` AS AreaName,st.`Name` TypeName  " \
                    "FROM `U_User` u   " \
                    "JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id`   " \
                    "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id`   " \
                    "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id`   " \
                    "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ui.`ServiceAreaId`   " \
                    "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ui.`ServiceTypeId` " \
                    "WHERE u.`UserType` IN (2,3) AND u.`IsDelete` = FALSE    " \
                     "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR sa.`Name` LIKE '%s' OR st.`Name` LIKE '%s') " \
                     "ORDER BY ps.`IsTop` DESC,ps.Sort DESC ,u.`Id` " \
                    "LIMIT %s , %s "

#获取用户详情
select_planner_info="SELECT u.`Id`,ui.`Name`,u.`Phone`,ui.`Sex`,ui.`Age`,ui.`Email`,ui.`Education`,ui.`Address` "\
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE u.`UserType` in (2,3) AND u.`Id`='%s'  "


#学历背景
select_planner_education = "SELECT e.`Id`,e.`TimeStart`'e.`TimeEnd`,e.`Degree`e.`University`,e.`Sort`,e.`CreateTime`  " \
                                "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "


#社会背景
select_planner_society = "SELECT s.`Id`,s.`TimeStart`,s.`TimeEnd`,s.`Description`,s.`Sort`,s.`CreateTime`  " \
                                "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "


#资源背景
select_planner_resour = "SELECT r.`Id`,r.`TimeStart`,r.`TimeEnd`,r.`Description`,r.`Sort`,r.`CreateTime`  " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "
