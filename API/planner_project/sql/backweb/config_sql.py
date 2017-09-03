#查询基础配置列表
select_config_list="SELECT `Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE ORDER BY `CreateTime` DESC "
#新增基础配置
insert_config="INSERT INTO `Base_Congif`(`Key`,`Value`,`Remark`,`CreateTime`,`Img`) VALUES('%s','%s','%s',NOW(),'%s') "
#删除基础配置
delete_config="UPDATE  `Base_Congif` SET `IsDelete`=TRUE WHERE `Key`='%s'"