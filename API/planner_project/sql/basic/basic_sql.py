
#基础信息
select_platforminfo="SELECT c.`Id`,c.`CustomerServiceTelephone`,c.`FlowImage`,c.`BigVImage` " \
                    "FROM `Base_PlatformInfo` c " \
                    "WHERE c.IsDelete=FALSE " \
                    "LIMIT 0, 1 "
#根据key获取基础配置
get_config="SELECT `Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE AND `Key`='%s' ORDER BY `CreateTime` DESC  LIMIT 1"
#根据key获取基础配置列表
get_config_list="SELECT `Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE AND `Key`='%s' ORDER BY `CreateTime` DESC"
#获取全部配置
get_config_all="SELECT `Key`,`Value`,`Remark`,`Img` FROM `Base_Congif` WHERE `IsDelete`=FALSE  ORDER BY `CreateTime` DESC"

