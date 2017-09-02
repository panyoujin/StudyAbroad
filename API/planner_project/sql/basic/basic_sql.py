
#基础信息
select_platforminfo="SELECT c.`Id`,c.`CustomerServiceTelephone`,c.`FlowImage`,c.`BigVImage` " \
                    "FROM `Base_PlatformInfo` c " \
                    "WHERE c.IsDelete=FALSE " \
                    "LIMIT 0, 1 "