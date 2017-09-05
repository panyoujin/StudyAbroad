# 查询基础配置列表
select_config_list = "SELECT `Id`,`Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE ORDER BY `CreateTime` DESC "
# 查询单个基础配置根据id
get_base_config_by_id = "SELECT `Id`,`Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE AND `Id`=%s ORDER BY `CreateTime` DESC "
# 新增基础配置
insert_config = "INSERT INTO `Base_Congif`(`Key`,`Value`,`Remark`,`CreateTime`,`Img`) VALUES('%s','%s','%s',NOW(),'%s') "
# 删除基础配置
delete_config = "UPDATE  `Base_Congif` SET `IsDelete`=TRUE WHERE `Key`='%s'"
# 更新基础配置
update_config = "UPDATE `Base_Congif` SET `Value`='%s',`Remark`='%s',`Img`='%s' WHERE Id=%s "
