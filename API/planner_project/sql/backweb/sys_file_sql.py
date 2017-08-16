
#查询资料列表
select_sys_file_list = "SELECT f.`Id`,f.`FileName`,f.`Url`,`IsTop`,f.`Sort`,`CreateTime` " \
                    "FROM `Sys_File` f " \
                    "WHERE f.IsDelete=FALSE " \
                    "AND ('%s' IS NULL OR '%s'='' OR f.`FileName` LIKE '%s')  "\
                    "ORDER BY f.IsTop DESC,f.Sort DESC,`Id` DESC " \
                    "LIMIT %s, %s "

#资料信息
select_sys_file_info="SELECT f.`Id`,f.`FileName`,f.`Url`,`IsTop`,f.`Sort`,`CreateTime` " \
                    "FROM `Sys_File` f " \
                    "WHERE f.`Id`='%s' AND f.`IsDelete`=FALSE "

#修改信息
update_sys_file_info="UPDATE `Sys_File` SET `FileName`='%s',`Url`='%s',`IsTop`='%s',`Sort`='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_sys_file="UPDATE `Sys_File` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';"

#新增资料
insert_sys_file="INSERT INTO `Sys_File` (`FileName`,`Url`,`IsTop`,`Sort`,`CreateUserID`" \
                    ",`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)"\
                    "VALUES( '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"