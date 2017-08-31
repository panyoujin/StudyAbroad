# 获取指定用户所在的团队成员列表
select_planner_team_member_list = "SELECT tm.UserId,ui.`Name`,ui.`HeadImage`,tm.`Sort` " \
                                  "FROM `U_PlannerStatistics` ps " \
                                  "JOIN `T_TeamMember` tm ON ps.`TeamId` = tm.`TeamId` " \
                                  "JOIN `U_UserInfo` ui ON ui.`UserId`=tm.`UserId` " \
                                  "WHERE ps.`UserId`='%s' AND tm.`IsDelete`= FALSE " \
                                  "ORDER BY tm.`Sort` DESC,tm.`CreateTime` DESC " \
                                  "LIMIT %s, %s "

# 新增团队
insert_team = "INSERT INTO `T_Team` (`Id`,`AdminUserId`,`Name`,`ServiceAreaId`,`ServiceDescription`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`) " \
              "VALUES( '%s', '%s', '%s', %s, '%s', '%s', NOW(), '%s', NOW()) ;" \
              "INSERT INTO `T_TeamMember` (`TeamId`,`UserId`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`) " \
              "VALUES( '%s', '%s', 999, '%s', NOW(), '%s', NOW()) ;" \
              "UPDATE `U_PlannerStatistics` SET `TeamId`='%s',`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `UserId` = '%s' ;"

# 获取团队列表
select_team_list = " SELECT t.`Id`,t.`Name` TeamName,ui.`Name` UserName,ui.`HeadImage`,t.`CreateTime` " \
                   "FROM `T_Team` t " \
                   "LEFT JOIN `U_PlannerStatistics` ps ON t.`AdminUserId`=ps.`UserId` " \
                   "JOIN `U_UserInfo` ui ON ui.`UserId`=t.`AdminUserId`  " \
                   "WHERE t.`IsDelete`=FALSE AND (ps.`UserId` IS NULL OR ps.`UserId` != '%s' ) " \
                   "AND ('%s'  IS NULL OR '%s'='' OR t.`Name` LIKE '%s') " \
                   "ORDER BY t.`IsTop` DESC,t.`Sort` DESC,t.`CreateTime` DESC " \
                   "LIMIT %s, %s "

# 获取用户所在团队信息
select_user_team = " SELECT t.`Id`,t.`Name` TeamName,ui.`Name` UserName,ui.`HeadImage`,t.`CreateTime` " \
                   "FROM `U_PlannerStatistics` ps " \
                   "JOIN `T_Team` t ON ps.`TeamId`=t.`Id`  " \
                   "JOIN `U_UserInfo` ui ON ui.`UserId`=t.`AdminUserId`  " \
                   "WHERE t.`IsDelete`=FALSE AND ps.`UserId`='%s'" \
                   "LIMIT 0, 1 "

# 获取指定用户所在的团队成员列表
select_team_member_list = "SELECT tm.UserId,ui.`Name`,ui.`HeadImage`,ps.`NewEvaluate`,ps.`CustomerCount`,ps.`PraiseCount`,ps.`BadReviewCount`,ps.Lables,ps.Sort " \
                          "FROM `T_TeamMember` tm " \
                          "JOIN `U_PlannerStatistics` ps ON ps.`UserId` = tm.`UserId`  " \
                          "JOIN `U_UserInfo` ui ON ui.`UserId`=tm.`UserId` " \
                          "WHERE tm.`TeamId`='%s' AND tm.`IsDelete`= FALSE " \
                          "ORDER BY tm.`Sort` DESC,tm.`CreateTime` DESC " \
                          "LIMIT %s, %s "

# 查询是否已经是团队成员
exists_team_peoper = "SELECT tt.`Id`,tt.`UserId`,tt.`TeamId`,tt.`Message`,tt.`Status`,tt.`IsAdmin`,tt.UnionId " \
                     "FROM `T_TeamNotice` tt " \
                     "JOIN `T_TeamMember` tm ON tt.TeamId=tm.TeamId AND tt.UserId=tm.UserId" \
                     "WHERE tt.`UserId`='%s' AND tt.`TeamId`='%s' AND tt.`IsDelete`=FALSE AND tm.`IsDelete`=FALSE "

# 查询是否已经是团队成员根据noticeid
exists_team_peoper_bynoticeid = "SELECT t1.`Id`,t1.`UserId`,t1.`TeamId`,t1.`Message`,t1.`Status`,t1.`IsAdmin`,t1.UnionId,t2.`UserId` AS duUserId " \
                                "FROM `T_TeamNotice` t1  " \
                                "JOIN `T_TeamNotice` t2 ON t1.`UnionId`=t2.`UnionId`  " \
                                "WHERE  t1.`IsAdmin`=1 AND t2.`IsAdmin`=2 AND t1.`Id`='%s'"

# 获取团队信息
select_team_adminid = "SELECT `Id`,`AdminUserId`,`Name` FROM `T_Team` WHERE `Id`='%s'"

# 获取用户的团队通知列表
select_team_notice_list = "SELECT tn.`Id`,tn.`UserId`,tn.`TeamId`,tn.`Message`,tn.`Status`,tn.`IsAdmin`,tn.`CreateTime`,t.`Name`,tn.`UnionId`  FROM T_TeamNotice tn JOIN `T_Team` t ON tn.`TeamId`=t.`Id`  WHERE UserId='%s'  ORDER BY IFNULL(tn.`ModifTime`,tn.`CreateTime`)  DESC LIMIT %s , %s "

# 新增团队通知
insert_team_notice = "INSERT INTO `StudyAbroad`.`T_TeamNotice` (`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`UnionId` ) VALUES(UUID(),'%s','%s','%s',%s,%s,'%s',NOW(),'%s')"
# 新增团队成员
insert_team_member = "INSERT INTO `T_TeamMember` (`TeamId`,`UserId`,`CreateUserID`,`CreateTime`) VALUES ('%s','%s','%s',NOW())"
# 修改管理员的团队通知
update_team_admin_notice = "UPDATE T_TeamNotice SET `Status`=2,`ModifTime`=NOW(),`ModifUserID`='%s' WHERE `Id`='%s' AND `Status`=1"
# 修改出管理员外的团队通知
update_team_notice = "UPDATE `T_TeamNotice` SET `Status`=2,`ModifTime`=NOW(),`ModifUserID`='%s' WHERE `UnionId`='%s' AND `IsAdmin`=2"
# 修改用户信息的团队id
update_planner_statistics = " UPDATE U_PlannerStatistics SET `TeamId`='%s',`ModifTime`=NOW(),`ModifUserID`='%s' WHERE `UserId`='%s' "

# 管理员不同意的团队通知
disagree_team_admin_notice = "UPDATE T_TeamNotice SET `Status`=3,`ModifTime`=NOW(),`ModifUserID`='%s' WHERE `Id`='%s' AND `Status`=1"

# 修改出管理员外不同意的团队通知
disagree_team_notice = "UPDATE `T_TeamNotice` SET `Status`=3,`ModifTime`=NOW(),`ModifUserID`='%s' WHERE `UnionId`='%s' AND `IsAdmin`=2"
# 判断是否团队管理员
is_team_admin = "SELECT COUNT(1) as total FROM `T_Team` WHERE `Id`='%s' AND `AdminUserId`='%s'"
# 退出团队
quit_team = "UPDATE `T_TeamMember` SET `ModifUserID`='%s',`ModifTime`=NOW(),`IsDelete`=TRUE WHERE `TeamId`='%s' AND `UserId`='%s'"
# 解散团队1
disband_team1 = "UPDATE `T_Team` SET `ModifUserID`='%s',`ModifTime`=NOW(),`IsDelete`=TRUE WHERE `Id`='%s' AND `AdminUserId`='%s'"
# 解散团队2
disband_team2 = "UPDATE  `T_TeamMember` SET `ModifUserID`='%s',`ModifTime`=NOW(),`IsDelete`=TRUE WHERE `TeamId`='%s'"
# 用改规划师资料表的团队id为空
update_planner_statistics_null = "UPDATE U_PlannerStatistics SET TeamId=NULL,`ModifTime`=NOW() WHERE UserId='%s'"
