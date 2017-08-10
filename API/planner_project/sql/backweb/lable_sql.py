#标签列表
select_lable_list="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_Label` " \
                         "WHERE `IsDelete`=FALSE " \
                         "AND ('%s' IS NULL OR '%s'='' OR `Name` LIKE '%s')  "\
                         "ORDER BY `IsTop` DESC ,`Sort` DESC,`CreateTime` DESC "\
                         "LIMIT %s , %s "

#标签信息
select_lable_info="SELECT `Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateTime` " \
                         "FROM `Base_Label` " \
                         "WHERE `Id`='%s' AND `IsDelete`=FALSE "

#修改信息
update_lable_info="UPDATE `Base_Label` SET `Name`='%s',`Description`='%s',`IsTop`='%s',`Sort`='%s',`ModifUserID`='%s',`ModifTime`=NOW()"\
                         "WHERE `Id`='%s' "


#删除信息
delete_lable="UPDATE `Base_Label` SET `IsDelete`=TRUE,`ModifUserID` = '%s',`ModifTime` = NOW() WHERE `Id`= '%s';"

#新增标签
insert_lable="INSERT INTO `Base_Label` (`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`" \
                    ",`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`)"\
                    "VALUES( '%s',  '%s',  '%s',  '%s',  '%s',  NOW(),  '%s',  NOW(),  FALSE) ;"