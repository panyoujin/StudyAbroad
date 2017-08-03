#查询是否申请过承接需求
select_exists_demand_service="SELECT COUNT(1) as total FROM `DS_DemandUndertake` " \
                             "WHERE `DemandId`='%s' AND `UserId`='%s' AND `Status` IN (1,2) AND `IsDelete`=FALSE"
#查询需求是否存在
select_exists_demand="SELECT `Id`,`IsUndertake` FROM `DS_DemandService` WHERE `Id`='%s' AND `IsDelete`=FALSE"

#新增申请承接
insert_demand_undertake="INSERT INTO `StudyAbroad`.`DS_DemandUndertake` (`Id`,`DemandId`,`UserId`,`CreateUserID`,`CreateTime`" \
                        ",IsUser,ContractId) VALUES (UUID(),'%s','%s','%s',NOW(),%s,%s) "


