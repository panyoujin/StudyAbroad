/*
SQLyog Ultimate v11.42 (64 bit)
MySQL - 5.7.18 : Database - StudyAbroad
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`StudyAbroad` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `StudyAbroad`;

/*Table structure for table `Sys_P_Permission` */

DROP TABLE IF EXISTS `Sys_P_Permission`;

CREATE TABLE `Sys_P_Permission` (
  `PermissionId` int(11) NOT NULL COMMENT '权限ID',
  `ParentId` int(11) NOT NULL DEFAULT '0' COMMENT '父权限Id',
  `Name` varchar(30) NOT NULL COMMENT '权限名称',
  `MenuName` varchar(30) NOT NULL COMMENT '菜单名称',
  `Url` varchar(150) NOT NULL COMMENT '权限相对url地址',
  `Orderby` int(11) NOT NULL DEFAULT '0' COMMENT '菜单排序，数据越大越靠前',
  `Visible` bit(1) NOT NULL DEFAULT b'1' COMMENT '是否显示菜单',
  `Remark` varchar(50) DEFAULT NULL COMMENT '描述',
  `Icon` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`PermissionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_P_Role` */

DROP TABLE IF EXISTS `Sys_P_Role`;

CREATE TABLE `Sys_P_Role` (
  `RoleId` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `RoleName` varchar(30) NOT NULL COMMENT '角色名称',
  `Remark` varchar(150) DEFAULT NULL COMMENT '描述',
  `CreateDate` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`RoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_P_RolePermission` */

DROP TABLE IF EXISTS `Sys_P_RolePermission`;

CREATE TABLE `Sys_P_RolePermission` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RoleId` int(11) NOT NULL COMMENT '角色Id',
  `PermissionId` int(11) NOT NULL COMMENT '权限Id',
  `Scope` int(11) NOT NULL DEFAULT '0' COMMENT '数据范围,0:个人,1:部门,2,全局',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_P_UserRole` */

DROP TABLE IF EXISTS `Sys_P_UserRole`;

CREATE TABLE `Sys_P_UserRole` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL COMMENT '用户id',
  `RoleId` int(11) NOT NULL COMMENT '角色id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_User` */

DROP TABLE IF EXISTS `Sys_User`;

CREATE TABLE `Sys_User` (
  `UserId` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `UserName` varchar(36) NOT NULL COMMENT '登录名',
  `Password` varchar(150) NOT NULL COMMENT '密码',
  `NickName` varchar(20) NOT NULL COMMENT '用户名称',
  `Phone` varchar(15) DEFAULT '''' COMMENT '手机',
  `Email` varchar(36) DEFAULT '''' COMMENT '邮箱',
  `Descript` varchar(300) DEFAULT '''' COMMENT '描述',
  `CreateDate` datetime NOT NULL COMMENT '创建时间',
  `Status` int(11) NOT NULL DEFAULT '1' COMMENT '状态',
  `IsAdmin` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/* Procedure structure for procedure `pro_GetPermissions` */

/*!50003 DROP PROCEDURE IF EXISTS  `pro_GetPermissions` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `pro_GetPermissions`()
BEGIN
	/*获取所有的权限*/
	SELECT DISTINCT p.* 
	FROM Sys_P_Permission p
	ORDER BY p.Orderby DESC;
    END */$$
DELIMITER ;

/* Procedure structure for procedure `pro_GetRolePermissions` */

/*!50003 DROP PROCEDURE IF EXISTS  `pro_GetRolePermissions` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `pro_GetRolePermissions`(in RoleId INT)
BEGIN
	/*获取指定角色拥有的权限*/
	SELECT DISTINCT p.* 
	FROM Sys_P_RolePermission rp
	JOIN Sys_P_Permission p ON p.`PermissionId`=rp.`PermissionId`
	WHERE rp.`RoleId`=RoleId
	ORDER BY p.Orderby DESC;
    END */$$
DELIMITER ;

/* Procedure structure for procedure `pro_GetUserPermissions` */

/*!50003 DROP PROCEDURE IF EXISTS  `pro_GetUserPermissions` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `pro_GetUserPermissions`(in UserId INT)
BEGIN
	/*获取用户拥有的权限*/
	SELECT distinct p.* FROM Sys_P_UserRole ur
	JOIN Sys_P_RolePermission rp ON rp.`RoleId`=ur.`RoleId`
	JOIN Sys_P_Permission p ON p.`PermissionId`=rp.`PermissionId`
	WHERE ur.`UserId`=UserId;
    END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
