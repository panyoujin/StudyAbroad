#需求服务列表
select_search_demand_service = "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name`,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName "\
                       "FROM `DS_DemandService` ds " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`IsDelete` = FALSE " \
                       "ORDER BY ds.`Sort` DESC ,ds.`CreateTime` DESC " \
                       "LIMIT %s , %s "

#收藏
demand_service_collection="INSERT INTO `U_Collection` (`UserId`,`DemandServiceId`,`CollectionTime`) VALUES('%s','%s',NOW()) "

#查询收藏列表
select_collection_demand_service =  "SELECT ds.`Id`,ds.UserId,ds.`Name`,ds.`Type`,ds.`ServiceAreaId`,ds.`ServiceTypeId` " \
                        ",ds.`PriceStart`,ds.`PriceEnd`,ds.`TimeStart`,ds.`TimeEnd`,ds.`CreateTime`,ds.`CollectionCount` " \
                        ",ds.`Sort`,ds.`IsTop`,ui.`Name`,ui.`HeadImage`,sa.`Name` AS AreaName,st.`Name` AS TypeName "\
                       "FROM `U_Collection` c " \
                       "JOIN `DS_DemandService` ds ON c.DemandServiceId = ds.Id " \
                       "JOIN `U_UserInfo` AS ui ON ds.`UserId`=ui.`UserId` " \
                       "LEFT JOIN `Base_ServiceArea` sa ON sa.`Id`=ds.`ServiceAreaId`  " \
                       "LEFT JOIN `Base_ServiceType` st ON st.`Id`=ds.`ServiceTypeId` " \
                       "WHERE ds.`IsDelete` = FALSE  AND c.UserId='%s' " \
                       "ORDER BY ds.`Sort` DESC ,ds.`CreateTime` DESC " \
                       "LIMIT %s , %s "