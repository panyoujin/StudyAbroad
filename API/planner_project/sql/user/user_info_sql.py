#修改用户信息
update_user_info="UPDATE `U_UserInfo` SET `Name` = '%s',`Sex` = '%s',`Age` = '%s',`Education` = '%s',`Address` = '%s'" \
                 ",`Email` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"
#修改用户信息
update_user_headimage="UPDATE `U_UserInfo` SET `HeadImage` = '%s',`ModifUserID` = '%s',`ModifTime` = NOW() " \
                 "WHERE `UserId` = '%s' ;"

select_userinfo_by_id="SELECT  `UserId`, `Name`, `Sex`, `Address`, `Age`, `Education`, `Email`, `IDCard`, `HeadImage`" \
                      ", `ServiceAreaId`, `ServiceTypeId` FROM `U_UserInfo`  " \
                      "WHERE `UserId`='%s' AND `IsDelete` = FALSE"