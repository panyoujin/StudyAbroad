#获取团队列表
select_team_list="SELECT t.`Id`,ui.`RealName`,t.`Name` AS TeamName,u.`Phone` ,sa.`Name` AS AreaName,st.`Name` AS TypeName,t.`CreateTime` ,t.`IsTop` "\
                    "FROM `T_Team` t  "\
                    "LEFT JOIN `U_UserInfo` ui ON t.`AdminUserId`=ui.`UserId` "\
                    "LEFT JOIN `U_User` u ON u.`Id`=ui.`UserId`  "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE t.`IsDelete`=FALSE "\
                    "AND ('%s' IS NULL OR '%s'='' OR ui.`Name` LIKE '%s' OR t.`Name` LIKE '%s')  "\
                    "ORDER BY t.`IsTop` DESC ,t.`Sort` DESC ,t.`CreateTime` DESC   " \
                    "LIMIT %s , %s "

#获取指定团队成员列表
select_teamm_ember_list="SELECT tm.`Id`,tm.`TeamId`,tm.`UserId`,ui.`RealName`,u.`Phone` ,sa.`Name` AS AreaName,st.`Name` AS TypeName,tm.`CreateTime` "\
                    "FROM `T_TeamMember` tm   "\
                    "JOIN `U_UserInfo` ui ON tm.`UserId`=ui.`UserId`  "\
                    "JOIN `U_User` u ON u.`Id`=ui.`UserId`  "\
                    "LEFT JOIN `Base_ServiceArea` sa ON ui.`ServiceAreaId`=sa.`Id` "\
                    "LEFT JOIN `Base_ServiceType` st ON ui.`ServiceTypeId`=st.`Id` "\
                    "WHERE  tm.`TeamId`='%s' AND u.`IsDelete`=FALSE "\
                    "ORDER BY tm.`Sort` DESC ,tm.`CreateTime` DESC   "


#删除团队
delete_team="UPDATE `T_Team` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id` = '%s' ;" \
            "UPDATE `U_PlannerStatistics` SET `TeamId`=NULL,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `TeamId` = '%s' ;" \
            "DELETE FROM `T_TeamMember` WHERE TeamId= '%s' ;"


#删除团队成员
delete_team_member="UPDATE `U_PlannerStatistics` SET `TeamId`=NULL,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `UserId` = '%s' ;" \
                    "DELETE FROM `T_TeamMember` WHERE TeamId= '%s' AND `UserId`='%s' ;"