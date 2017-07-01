#新增验证码
insert_verification_codel = "INSERT INTO Base_VerificationCode (`Phone`,`VCode`,`CodeType`,`CreateTime`) values ('%s','%s',%s,now())"

#根据该手机 对应类型的最后一条短信验证码
select_verification_lastcode="select Id,`VCode` from `Base_VerificationCode` where `Phone`='%s' and `IsRead`=1 and `IsDelete`=false and `CodeType`=%s and ADDDATE(CreateTime,INTERVAL 5 MINUTE) >= NOW() order by `CreateTime` desc limit 1"

#修改验证码已读
update_verificatioin_vcode="UPDATE `Base_VerificationCode` SET IsRead=2,`ModifTime`=NOW() WHERE `Id`=%s"