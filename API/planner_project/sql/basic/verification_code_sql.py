#新增验证码
insert_verification_codel = "INSERT INTO Base_VerificationCode (`Phone`,`VCode`,`CodeType`,`CreateTime`) values ('%s','%s',%s,now())"

#根据该手机 对应类型的最后一条短信验证码
select_verification_lastcode="select Id,`VCode` from `Base_VerificationCode` where `Phone`='%s' and `IsRead`=1 and `IsDelete`=false and `CodeType`=%s order by `CreateTime` desc limit 1"