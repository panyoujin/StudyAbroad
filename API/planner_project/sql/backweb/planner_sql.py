#获取用户列表
select_planner_list="SELECT u.`Id`,ui.`Name`,ui.`HeadImage`,u.`Phone`,ps.`NewEvaluate`,ps.`CustomerCount`  ,ps.`PraiseCount`" \
                    ",ps.`BadReviewCount`,t.`Name` AS TeamName,Lables,ps.Sort ,ps.`IsTop`,ps.`BigV`,u.CreateTime  " \
                      ",(SELECT GROUP_CONCAT(sa.`Name`) FROM `Base_ServiceArea` sa WHERE FIND_IN_SET(sa.`Id`,ui.`ServiceAreaId`)>0 AND sa.`IsDelete` = FALSE) AS AreaName" \
                      ",(SELECT GROUP_CONCAT(st.`Name`) FROM `Base_ServiceType` st WHERE FIND_IN_SET(st.`Id`,ui.`ServiceTypeId`)>0 AND st.`IsDelete` = FALSE) AS TypeName " \
                    "FROM `U_User` u   " \
                    "JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id`   " \
                    "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id`   " \
                    "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id`   " \
                    "WHERE u.`UserType` IN (2,3) AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE AND ps.`IsDelete` = FALSE    " \
                     "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s') " \
                     "ORDER BY ps.`IsTop` DESC,ps.Sort DESC ,u.`Id` " \
                    "LIMIT %s , %s "
#获取用户列表
select_planner_list_count="SELECT  COUNT(0) AS listCount FROM `U_User` u   " \
                    "JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id`   " \
                    "JOIN `U_PlannerStatistics` ps ON ps.`UserId`=u.`Id`   " \
                    "LEFT JOIN `T_Team` t ON ps.`TeamId`=t.`Id`   " \
                    "WHERE u.`UserType` IN (2,3) AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE AND ps.`IsDelete` = FALSE    " \
                     "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s') "


#获取用户详情
select_planner_info="SELECT u.`Id`,u.`Account`,ui.`Name`,u.`Phone`,ui.`Sex`,ui.`Age`,ui.`Email`,ui.`Education`,ui.`Address`,ui.`HeadImage`,ui.`IDCard`,ui.`IDCardJust`,ui.`IDCardBack`,ui.`ServiceAreaId`,ui.`ServiceTypeId` "\
                      ",(SELECT GROUP_CONCAT(sa.`Name`) FROM `Base_ServiceArea` sa WHERE FIND_IN_SET(sa.`Id`,ui.`ServiceAreaId`)>0 AND sa.`IsDelete` = FALSE) AS AreaName" \
                      ",(SELECT GROUP_CONCAT(st.`Name`) FROM `Base_ServiceType` st WHERE FIND_IN_SET(st.`Id`,ui.`ServiceTypeId`)>0 AND st.`IsDelete` = FALSE) AS TypeName " \
                    "FROM `U_User` u "\
                    "LEFT JOIN `U_UserInfo` ui ON u.`Id`=ui.`UserId` "\
                    "WHERE u.`UserType` in (2,3) AND u.`Id`='%s'  AND u.`IsDelete` = FALSE AND ui.`IsDelete` = FALSE "


#学历背景
select_planner_education = "SELECT e.`Id`,e.`TimeStart`,e.`TimeEnd`,e.`Degree`,e.`University`,e.`Sort`,e.`CreateTime`  " \
                                "FROM `U_Education` e " \
                                "WHERE e.`UserId`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#学历背景详情
select_education_info = "SELECT e.`Id`,e.`TimeStart`,e.`TimeEnd`,e.`Degree`,e.`University`,e.`Sort`,e.`CreateTime`  " \
                                "FROM `U_Education` e " \
                                "WHERE e.`Id`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#社会背景
select_planner_society = "SELECT s.`Id`,s.`TimeStart`,s.`TimeEnd`,s.`Description`,s.`Sort`,s.`CreateTime`  " \
                                "FROM `U_Society` s " \
                                "WHERE s.`UserId`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#社会背景
select_society_info = "SELECT s.`Id`,s.`TimeStart`,s.`TimeEnd`,s.`Description`,s.`Sort`,s.`CreateTime`  " \
                                "FROM `U_Society` s " \
                                "WHERE s.`Id`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#资源背景
select_planner_resour = "SELECT r.`Id`,r.`TimeStart`,r.`TimeEnd`,r.`Description`,r.`Sort`,r.`CreateTime`  " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`UserId`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#资源背景
select_resour_info = "SELECT r.`Id`,r.`TimeStart`,r.`TimeEnd`,r.`Description`,r.`Sort`,r.`CreateTime`  " \
                                "FROM `U_Resour` r " \
                                "WHERE r.`Id`='%s' AND `IsDelete` = FALSE " \
                                "ORDER BY `Sort` DESC,`CreateTime` DESC "

#新增学历
insert_education ="INSERT INTO `U_Education` ( `Id`, `UserId`, `TimeStart`, `TimeEnd`, `University`, `Degree`, `Sort`, `CreateUserID`, `CreateTime`, `ModifUserID`, `ModifTime`, `IsDelete`) " \
                  "VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NOW(), '%s', NOW(), FALSE ) ;"
#修改学历
update_education ="UPDATE `U_Education` SET`TimeStart` = '%s',`TimeEnd` = '%s',`University` = '%s',`Degree` = '%s',`Sort` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW()" \
                  " WHERE `Id` = '%s';"
#删除学历
delete_education ="UPDATE `U_Education` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
                  "WHERE `Id` = '%s'"

#新增资源背景
insert_resour ="INSERT INTO `U_Resour` (`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
               "VALUES('%s','%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE) "
#修改资源背景
update_resour ="UPDATE `U_Resour` SET `TimeStart` = '%s',`TimeEnd` = '%s',`Description` = '%s',`Sort` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
               "WHERE `Id` = '%s'"
#删除资源背景
delete_resour ="UPDATE `U_Resour` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
               "WHERE `Id` = '%s'"


#新增社会背景
insert_society ="INSERT INTO `U_Society` (`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
                "VALUES('%s','%s','%s','%s','%s','%s','%s',NOW(),'%s',NOW(),FALSE)"
#修改社会背景
update_society ="UPDATE `U_Society`  SET `TimeStart` = '%s',`TimeEnd` = '%s',`Description` = '%s',`Sort` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                "WHERE `Id` = '%s'"
#删除社会背景
delete_society ="UPDATE `U_Society` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW() " \
                "WHERE `Id` = '%s'"

#修改大v
update_BigV ="UPDATE `U_PlannerStatistics` SET `BigV`=%s, `ModifUserID`='%s', `ModifTime`=NOW() " \
                "WHERE `UserId` = '%s'"


#修改用户信息
update_planner="UPDATE `U_User` SET `Account`='%s',`Phone`='%s',`Password`='%s',`UserType`='%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `Id` = '%s' ;" \
                 "UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`HeadImage` = '%s',`IDCard` = '%s',`IDCardJust` = '%s',`IDCardBack` = '%s',ServiceAreaId = '%s',ServiceTypeId = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"