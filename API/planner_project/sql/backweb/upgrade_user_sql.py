# 获取规划师升级列表
get_upgrade_apply_list = "SELECT ut.`Id`,ut.`UserId`,IF(ut.`Sex`=1,'男','女') AS Sex,ut.`Name`,ut.`Address`,st.`Name` AS ServiceTypeName,sa.`Name` AS ServiceAreaName,ut.`Email`," \
                         "ut.`Experience`,ut.`IDCard`,ut.`IDCardPic`,ut.`Status`,IF(ut.`Status`=0,'审核中',IF(ut.`Status`=1,'审核通过','审核不通过')) AS StatusStr ,ut.`CreateTime` " \
                         "FROM `U_UpgradeUserTemp` ut " \
                         "JOIN `Base_ServiceType` st ON ut.`ServiceId`=st.`Id` " \
                         "JOIN `Base_ServiceArea` sa ON ut.`ServiceAreaId`=sa.`Id` " \
                         "WHERE ut.`IsDelete`=FALSE  " \
                         "AND ('%s' IS NULL OR '%s'='' OR ut.`Name` LIKE '%s') " \
                         "ORDER BY ut.`Status` ASC,ut.`CreateTime` DESC " \
                         "LIMIT %s , %s "
# 获取规划师升级列表 总数
get_upgrade_apply_count = "SELECT count(1) as count " \
                          "FROM `U_UpgradeUserTemp` ut " \
                          "JOIN `Base_ServiceType` st ON ut.`ServiceId`=st.`Id` " \
                          "JOIN `Base_ServiceArea` sa ON ut.`ServiceAreaId`=sa.`Id` " \
                          "WHERE ut.`IsDelete`=FALSE  " \
                          "AND ('%s' IS NULL OR '%s'='' OR ut.`Name` LIKE '%s') "
# 获取规划师升级数据详情
get_upgrade_apply_detail = "SELECT ut.`Id`,ut.`UserId`,IF(ut.`Sex`=1,'男','女') AS Sex,ut.`Name`,ut.`Address`,st.`Name` AS ServiceTypeName, " \
                           "sa.`Name` AS ServiceAreaName,ut.`Email`, " \
                           "ut.`Experience`,ut.`IDCard`,ut.`IDCardPic`,ut.`IDCardBackPic`,ut.`Status`, " \
                           "IF(ut.`Status`=0,'审核中',IF(ut.`Status`=1,'审核通过','审核不通过')) AS StatusStr ,ut.`CreateTime`, " \
                           "uu.Phone " \
                           "FROM `U_UpgradeUserTemp` ut " \
                           "JOIN `Base_ServiceType` st ON ut.`ServiceId`=st.`Id` " \
                           "JOIN `Base_ServiceArea` sa ON ut.`ServiceAreaId`=sa.`Id` " \
                           "JOIN U_User uu on ut.UserId=uu.Id " \
                           "WHERE ut.`IsDelete`=FALSE and ut.Id='%s'"
# 更新规划师升级的申请状态
update_upgrade_status = "UPDATE U_UpgradeUserTemp SET Status=%s,ModifTime=now(),ModifUserID='%s' WHERE Id='%s' AND Status=0"

# 查询规划师升级数据
get_upgrade_info_by_id = "SELECT `Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`, IDCard, `IDCardPic`,`Status`, `IDCardBackPic` FROM `U_UpgradeUserTemp`" \
                         " where Id='%s'"

# 根据用户id 修改用户账号类型
update_user_type = "UPDATE U_User SET UserType=2,ModifUserID='%s',ModifTime=now() WHERE Id='%s'"

# 修改用户信息表数据
update_user_info = "UPDATE U_UserInfo SET Name='%s',Sex=%s,Address='%s',Education='%s',Email='%s',IDCard='%s',IDCardJust='%s',ServiceAreaId=%s,ServiceTypeId=%s,ModifUserID='%s',ModifTime=Now(),IDCardBack='%s' " \
                   "where UserId='%s'"
# 规划师统计表
insert_planner_statistics="INSERT INTO `U_PlannerStatistics`(`UserId`,`CreateTime`) VALUES('%s',NOW())"