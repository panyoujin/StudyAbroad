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

#是否已关注
get_whether_follw="SELECT COUNT(0) as fllow_count FROM U_Follow WHERE FollwUserId='%s' AND UserId='%s';"

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
                      ",ps.`PraiseCount`,ps.`BadReviewCount`,sa.`Name` AreaName,st.`Name` TypeName " \
                      "FROM `U_PlannerStatistics` ps " \
                      "JOIN `U_UserInfo` ui ON ui.`UserId`=ps.`UserId` " \
                      "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ui.`ServiceAreaId`  " \
                      "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ui.`ServiceTypeId`  " \
                      "WHERE ps.`UserId`='%s'"


#查询规划师资历
select_planner_qualifications = "SELECT 30 `Type`,CONCAT('学位：',e.`Degree`,' 毕业大学：',YEAR(e.`TimeStart`),'-'" \
                                ",YEAR(e.`TimeEnd`),' ',e.`University`) AS Content,e.`Sort`,e.`CreateTime`  " \
                                ",e.`Id`,e.`TimeStart`,e.`TimeEnd`,e.`University`,e.`Degree`,'' AS Description " \
                                "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' " \
                                "UNION ALL  " \
                                "SELECT 20 `Type`,CONCAT(YEAR(s.`TimeStart`),'-',YEAR(s.`TimeEnd`),' ',s.`Description`) " \
                                "AS Content,s.`Sort`,s.`CreateTime`  " \
                                ",s.`Id`,s.`TimeStart`,s.`TimeEnd`,'','',s.`Description` " \
                                "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' " \
                                "UNION ALL  " \
                                "SELECT 10 `Type`,CONCAT(YEAR(r.`TimeStart`),'-',YEAR(r.`TimeEnd`),' ',r.`Description`) " \
                                    "AS Content,r.`Sort`,r.`CreateTime`  " \
                                ",r.`Id`,r.`TimeStart`,r.`TimeEnd`,'','',r.`Description` " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' " \
                                "ORDER BY `Type` DESC,`Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#学历背景
select_planner_education = "SELECT e.`Id`,CONCAT('学位：',e.`Degree`,' 毕业大学：',YEAR(e.`TimeStart`),'-',YEAR(e.`TimeEnd`),' ',e.`University`) AS Content,e.`Sort`,e.`CreateTime`  " \
                                ",e.`TimeStart`,e.`TimeEnd`,e.`University`,e.`Degree`,'' AS Description " \
                           "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#社会背景
select_planner_society = "SELECT s.`Id`,CONCAT(YEAR(s.`TimeStart`),'-',YEAR(s.`TimeEnd`),' ',s.`Description`) AS Content,s.`Sort`,s.`CreateTime`  " \
                                ",s.`TimeStart`,s.`TimeEnd`,'','',s.`Description " \
                         "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#资源背景
select_planner_resour = "SELECT r.`Id`,CONCAT(YEAR(r.`TimeStart`),'-',YEAR(r.`TimeEnd`),' ',r.`Description`) AS Content,r.`Sort`,r.`CreateTime`  " \
                                ",r.`TimeStart`,r.`TimeEnd`,'','',r.`Description` " \
                        "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC " \
                                "LIMIT %s , %s "


#获取指定规划师评论列表
select_planner_evaluate="SELECT e.`OrderId`,e.`Content`,e.`CreateTime` ,ui.`Name`, ui.`HeadImage` " \
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

#新增学历
insert_education ="INSERT INTO `U_Education` ( `Id`, `UserId`, `TimeStart`, `TimeEnd`, `University`, `Degree`, `Sort`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                  "VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NOW(), '%s', NOW(), FALSE ) ;"
#修改学历
update_education ="UPDATE `U_Education` SET `TimeStart` = '%s',`TimeEnd` = '%s',`University` = '%s',`Degree` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                  " WHERE `Id` = '%s'  AND `UserId` = '%s';"
#删除学历
delete_education ="UPDATE `U_Education` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
                  "WHERE `Id` = '%s' AND `UserId` = '%s'"

#新增资源背景
insert_resour ="INSERT INTO `U_Resour` (`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
               "VALUES('%s','%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE) "
#修改资源背景
update_resour ="UPDATE `U_Resour` SET `TimeStart` = '%s',`TimeEnd` = '%s',`Description` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
               "WHERE `Id` = 'Id' AND `UserId` = 'UserId'"
#删除资源背景
delete_resour ="UPDATE `U_Resour` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
               "WHERE `Id` = '%s' AND `UserId` = '%s'"


#新增社会背景
insert_society ="INSERT INTO `U_Society` (`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
                "VALUES('%s','%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE)"
#修改社会背景
update_society ="UPDATE `U_Society`  SET `TimeStart` = '%s',`TimeEnd` = '%s',`Description` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                "WHERE `Id` = 'Id' AND `UserId` = '%s'"
#删除社会背景
delete_society ="UPDATE `U_Society` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
                "WHERE `Id` = '%s' AND `UserId` = '%s'"



#新增相片
insert_album ="INSERT INTO `U_Album` (`UserId`,`PhotoName`,`Url`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
                "VALUES('%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE)"
#修改相片
update_album ="UPDATE `U_Album`  SET `PhotoName` = '%s',`Url` = '%s',`Sort` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                "WHERE `Id` = 'Id' AND `UserId` = '%s'"
#删除相片
delete_album ="UPDATE `U_Album` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
                "WHERE `Id` = '%s' AND `UserId` = '%s'"
#系统标签列表
select_lable_list="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_Label` " \
                         "WHERE `IsDelete`=FALSE " \
                         "ORDER BY `IsTop` DESC ,`Sort` DESC,`CreateTime` DESC "\
                         "LIMIT %s , %s "