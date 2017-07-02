#获取指定用户所在的团队成员列表
select_planner_team_member_list="SELECT ui.`Name`,ui.`HeadImage`,tm.`Sort` " \
                                "FROM `U_PlannerStatistics` ps " \
                                "JOIN `T_TeamMember` tm ON ps.`TeamId` = tm.`TeamId` AND tm.`UserId` != ps.`UserId` " \
                                "JOIN `U_UserInfo` ui ON ui.`UserId`=tm.`UserId` " \
                                "WHERE ps.`UserId`='%s' AND tm.`IsDelete`= FALSE " \
                                "ORDER BY tm.`Sort` DESC,tm.`CreateTime` DESC " \
                                "LIMIT %s, %s "

#获取团队列表
select_team_list=" SELECT t.`Id`,t.`Name` TeamName,ui.`Name` UserName,ui.`HeadImage`,IF(ps.`UserId` IS NULL,0,1) AS Isjoin,t.`CreateTime` " \
                 "FROM `T_Team` t " \
                 "LEFT JOIN `U_PlannerStatistics` ps ON ps.`TeamId`=t.`Id` AND ps.`UserId`='%s'  " \
                 "JOIN `U_UserInfo` ui ON ui.`UserId`=t.`AdminUserId`  "\
                 "WHERE t.`IsDelete`=FALSE AND ('%s'  IS NULL OR '%s'='' OR t.`Name` LIKE '%s')" \
                 "ORDER BY Isjoin DESC,t.`IsTop` DESC,t.`Sort` DESC,t.`CreateTime` DESC " \
                 "LIMIT %s, %s "

#获取指定用户所在的团队成员列表
select_team_member_list="SELECT ui.`Name`,ui.`HeadImage`,ps.`NewEvaluate`,ps.`CustomerCount`,ps.`PraiseCount`,ps.`BadReviewCount`,ps.Lables,ps.Sort " \
                        "FROM `T_TeamMember` tm " \
                        "JOIN `U_PlannerStatistics` ps ON ps.`TeamId` = tm.`TeamId` AND tm.`UserId` != ps.`UserId` " \
                        "JOIN `U_UserInfo` ui ON ui.`UserId`=tm.`UserId` " \
                        "WHERE tm.`TeamId`='%s' AND tm.`IsDelete`= FALSE " \
                        "ORDER BY tm.`Sort` DESC,tm.`CreateTime` DESC " \
                        "LIMIT %s, %s "
#查询是否已经是团队成员
exists_team_peoper="SELECT `Id`,`UserId`,`TeamId`,`Message`,`Status` FROM `T_TeamNotice` WHERE `UserId`='%s' AND `TeamId`='%s' AND `IsDelete`=FALSE"

#获取团队信息
select_team_adminid="SELECT `Id`,`AdminUserId`,`Name` FROM `T_Team` WHERE `Id`='%s'"
#获取用户的团队通知列表
select_team_notice_list="SELECT tn.`Id`,tn.`UserId`,tn.`TeamId`,tn.`Message`,tn.`Status`,tn.`IsAdmin`,tn.`CreateTime`,t.`Name`,tn.`UnionId`  FROM T_TeamNotice tn JOIN `T_Team` t ON tn.`TeamId`=t.`Id`  WHERE UserId='%s' ORDER BY tn.`CreateTime` DESC"

#新增团队通知
insert_team_notice="INSERT INTO `StudyAbroad`.`T_TeamNotice` (`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`UnionId` ) VALUES(UUID(),'%s','%s','%s',%s,%s,'%s',NOW(),'%s')"