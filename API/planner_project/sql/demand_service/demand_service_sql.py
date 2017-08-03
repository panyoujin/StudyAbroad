#需求服务列表
select_search_demand_service = "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name` AS UserName,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName "\
                       "FROM `DS_DemandService` ds " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`IsDelete` = FALSE " \
                       "ORDER BY ds.`Sort` DESC ,ds.`CreateTime` DESC " \
                       "LIMIT %s , %s "
#需求服务详情
select_demand_service_info = "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name` AS UserName,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName "\
                       "FROM `DS_DemandService` ds " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`Id`='%s' AND ds.`IsDelete` = FALSE " \
                       "ORDER BY ds.`Sort` DESC ,ds.`CreateTime` DESC " \
                       "LIMIT 0 , 1 "

#收藏
demand_service_collection="INSERT INTO `U_Collection` (`UserId`,`DemandServiceId`,`CollectionTime`) VALUES('%s','%s',NOW())" \
                          " ON DUPLICATE KEY UPDATE CollectionTime=NOW() "
#是否已收藏
get_whether_collection="SELECT COUNT(0) as collection_count FROM U_Collection WHERE DemandServiceId='%s' AND UserId='%s';"

#查询收藏列表
select_collection_demand_service =  "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name` AS UserName,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName,c.CollectionTime "\
                       "FROM `U_Collection` c " \
                       "JOIN `DS_DemandService` ds ON c.DemandServiceId = ds.Id " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`IsDelete` = FALSE  AND c.UserId='%s' " \
                       "ORDER BY c.CollectionTime DESC " \
                       "LIMIT %s , %s "

#我的发布记录
select_my_demand_service = "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name` AS UserName,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName "\
                       "FROM `DS_DemandService` ds " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`UserId`='%s' AND ds.`IsDelete` = FALSE " \
                       "ORDER BY ds.`Sort` DESC ,ds.`CreateTime` DESC " \
                       "LIMIT %s , %s "

#浏览
demand_service_browse="INSERT INTO `U_BrowseRecord` (`UserId`,`DemandServiceId`,`BrowseTime`) VALUES('%s','%s',NOW()) " \
                          " ON DUPLICATE KEY UPDATE BrowseTime=NOW() "

#查询浏览列表
select_browse_demand_service =  "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name` AS UserName,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName,br.BrowseTime "\
                       "FROM `U_BrowseRecord` br " \
                       "JOIN `DS_DemandService` ds ON br.DemandServiceId = ds.Id " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`IsDelete` = FALSE  AND br.UserId='%s' " \
                       "ORDER BY br.BrowseTime DESC " \
                       "LIMIT %s , %s "

#新增需求
insert_demand_service="INSERT INTO `DS_DemandService` (`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) " \
                      "VALUES(  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),FALSE) ";

#修改需求
update_browse_service="UPDATE `DS_DemandService` SET `Name` = '%s', `ServiceAreaId` = '%s', `ServiceTypeId` = '%s'" \
                      ", `PriceStart` = '%s', `PriceEnd` = '%s', `TimeStart` = '%s', `TimeEnd` = '%s', `Description` = '%s'" \
                      ", `ModifUserID`='%s', `ModifTime`=NOW() " \
                      "WHERE `Id` = '%s' AND `UserId` = '%s'";


#删除需求
delete_browse_service ="UPDATE `DS_DemandService` SET `IsDelete`=TRUE, `ModifUserID`='%s', `ModifTime`=NOW()  " \
                       "WHERE `Id` = '%s' AND `UserId` = '%s'"
