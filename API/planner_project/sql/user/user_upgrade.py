#判断是否申请过注册规划师
select_exists_upgrade = "SELECT 1 FROM `U_UpgradeUserTemp` WHERE `UserId`='%s' AND `Status` IN (0,1)"
#申请注册规划师
insert_upgrade_user="INSERT INTO `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCardPic`,`CreateUserID`,`CreateTime`,IDCardBackPic) " \
                    "VALUES(UUID(),'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',NOW(),'%s')"
