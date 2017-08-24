#客服电话
select_customer_telephone="SELECT c.`Id`,c.`CustomerServiceTelephone` " \
                    "FROM `Base_PlatformInfo` c " \
                    "WHERE c.IsDelete=FALSE " \
                    "LIMIT 0, 1 "

#修改客服电话
update_customer_telephone="UPDATE `Base_PlatformInfo` SET `CustomerServiceTelephone`='%s',`ModifUserID` = '%s',`ModifTime` = NOW();"

#合同信息
select_contract="SELECT c.`Id`,c.`Content` " \
                    "FROM `Base_Contract` c " \
                    "WHERE c.IsDelete=FALSE " \
                    "ORDER BY c.IsTop DESC,c.Sort DESC,`Id` DESC " \
                    "LIMIT 0, 1 "

#修改合同信息
update_contract="UPDATE `Base_Contract` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW();" \
                "INSERT INTO `Base_Contract`(`Name`,`Content`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)" \
                "VALUES( '最新合同',  '%s',  1,  0,  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"


#查询轮播列表
select_carouselimage_list = "SELECT c.`Id`,c.`Description`,c.`ImageUrl`,c.`ClickUrl`,`IsTop`,c.`Sort`,`CreateTime` " \
                    "FROM `Base_HomePageCarouselImage` c " \
                    "WHERE c.IsDelete=FALSE " \
                    "ORDER BY c.IsTop DESC,c.Sort DESC,`Id` DESC " \
                    "LIMIT %s, %s "

#轮播信息
select_carouselimage_info="SELECT c.`Id`,c.`Description`,c.`ImageUrl`,c.`ClickUrl`,`IsTop`,c.`Sort`,`CreateTime` " \
                    "FROM `Base_HomePageCarouselImage` c " \
                    "WHERE c.`Id`='%s' AND c.`IsDelete`=FALSE "

#修改信息
update_carouselimage_info="UPDATE `Base_HomePageCarouselImage` SET `Description`='%s',`ImageUrl`='%s',`ClickUrl`='%s',`IsTop`='%s',`Sort`='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_carouselimage="UPDATE `Base_HomePageCarouselImage` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';"

#新增轮播
insert_carouselimage="INSERT INTO `Base_HomePageCarouselImage` (`Description`,`ImageUrl`,`ClickUrl`,`IsTop`,`Sort`,`CreateUserID`" \
                    ",`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)"\
                    "VALUES( '%s',  '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"