#角色列表
select_sys_role_list="SELECT r.`RoleId`,r.`RoleName`,r.`Remark`,r.`CreateDate` FROM `Sys_P_Role` r "\
                     "WHERE ('%s' IS NULL OR '%s'='' OR r.`RoleName` LIKE '%s') "


#角色信息
select_sys_role_info="SELECT r.`RoleId`,r.`RoleName`,r.`Remark`,r.`CreateDate` FROM `Sys_P_Role` r " \
                     "WHERE r.`RoleId`=%s "

#插入角色
insert_sys_role="INSERT INTO `Sys_P_Role` (`RoleName`,`Remark`,`CreateDate`) " \
                "VALUES( '%s',  '%s', NOW()) ;"

#修改角色
update_sys_role="UPDATE `Sys_P_Role` SET `RoleName` = '%s',`Remark` = '%s' WHERE `RoleId` = '%s' ; "


#删除角色
delete_sys_role="DELETE FROM `Sys_P_UserRole`  WHERE `RoleId`='%s';" \
                 "DELETE FROM `Sys_P_Role` WHERE `RoleId` = '%s' ; "

#菜单列表
select_permission_list="SELECT `PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon` "\
                        "FROM`StudyAbroad`.`Sys_P_Permission` ORDER BY Orderby DESC"


#角色菜单ID列表
select_role_permission_list="SELECT rp.`PermissionId`  FROM `Sys_P_RolePermission` rp WHERE rp.`RoleId` = '%s'"


#赋权限
insert_role_permission="DELETE FROM `Sys_P_RolePermission` WHERE `RoleId`='%s'; " \
                        "INSERT INTO `Sys_P_RolePermission`(`RoleId`,`PermissionId`) " \
                       "SELECT '%s',`PermissionId` FROM `Sys_P_Permission` WHERE `PermissionId` IN ('%s');"