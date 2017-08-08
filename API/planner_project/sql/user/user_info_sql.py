#修改用户信息
update_user_info="UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"
#修改用户信息
update_user_headimage="UPDATE `U_UserInfo` SET `HeadImage` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"

select_userinfo_by_id="SELECT  ui.`UserId`, ui.`Name`, ui.`Sex`, ui.`Address`, ui.`Age`, ui.`Education`, ui.`Email`, ui.`IDCard`,ui.`Autograph` " \
                      ", ui.`IDCardJust`, ui.`IDCardBack`, ui.`HeadImage` , ui.`ServiceAreaId`,ui.`ServiceTypeId`,u.`Phone`,u.`UserType`  " \
                      "FROM `U_User` u   " \
                      "LEFT JOIN `U_UserInfo` ui ON ui.`UserId`=u.`Id`  " \
                      "WHERE u.`Id`='%s' AND u.`IsDelete` = FALSE"

#查询相册
select_user_album = "SELECT ua.`Id`,ua.`UserId`,ua.`PhotoName`,ua.`Url`,ua.`Sort` " \
                      "FROM `U_Album` ua " \
                       "WHERE ua.`UserId`='%s' AND ua.IsDelete=FALSE " \
                       "ORDER BY ua.Sort DESC,`Id` DESC " \
                       "LIMIT %s, %s "

#获取最新合同
select_new_contract="SELECT bc.`Id`,bc.`Name`,bc.`Content` " \
         "FROM `Base_Contract` bc " \
         "WHERE bc.`IsDelete` = FALSE " \
         "ORDER BY bc.`IsTop` DESC,bc.`Sort` DESC,bc.`CreateTime` DESC LIMIT 0,1"

#查询资料列表
select_user_file = "SELECT f.`Id`,f.`UserId`,f.`FileName`,f.`Url`,f.`Sort` " \
                      "FROM `U_File` f " \
                       "WHERE f.IsDelete=FALSE " \
                       "ORDER BY f.IsTop DESC,f.Sort DESC,`Id` DESC " \
                       "LIMIT %s, %s "