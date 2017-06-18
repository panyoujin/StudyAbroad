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