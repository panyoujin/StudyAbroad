# 获取规划师升级列表
get_upgrade_apply_list = "SELECT ut.`Id`,ut.`UserId`,IF(ut.`Sex`=1,'男','女') AS Sex,ut.`Name`,ut.`Address`,st.`Name` AS ServiceTypeName,sa.`Name` AS ServiceAreaName,ut.`Email`,"\
                         "ut.`Experience`,ut.`IDCard`,ut.`IDCardPic`,ut.`Status`,IF(ut.`Status`=0,'审核中',IF(ut.`Status`=1,'审核通过','审核不通过')) AS StatusStr ,ut.`CreateTime` "\
                         "FROM `U_UpgradeUserTemp` ut "\
                         "JOIN `Base_ServiceType` st ON ut.`ServiceId`=st.`Id` "\
                         "JOIN `Base_ServiceArea` sa ON ut.`ServiceAreaId`=sa.`Id` "\
                         "WHERE ut.`IsDelete`=FALSE  "\
                         "AND ('%s' IS NULL OR '%s'='' OR ut.`Name` LIKE '%s') "\
                         "ORDER BY ut.`Status` ASC,ut.`CreateTime` DESC "\
                         "LIMIT %s , %s "

get_upgrade_apply_count="SELECT count(1) as count " \
                         "FROM `U_UpgradeUserTemp` ut "\
                         "JOIN `Base_ServiceType` st ON ut.`ServiceId`=st.`Id` "\
                         "JOIN `Base_ServiceArea` sa ON ut.`ServiceAreaId`=sa.`Id` "\
                         "WHERE ut.`IsDelete`=FALSE  "\
                         "AND ('%s' IS NULL OR '%s'='' OR ut.`Name` LIKE '%s') "\

