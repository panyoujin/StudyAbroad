/*
SQLyog Ultimate v11.42 (64 bit)
MySQL - 5.7.18 : Database - StudyAbroad
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `Base_Contract` */

CREATE TABLE `Base_Contract` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `Content` varchar(500) DEFAULT NULL COMMENT '内容',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='标签';

/*Data for the table `Base_Contract` */

insert  into `Base_Contract`(`Id`,`Name`,`Content`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'第一份合同','第一份合同',0,0,'1','2017-06-08 18:34:02','1','2017-06-08 18:34:08','\0');

/*Table structure for table `Base_Cooperation` */

CREATE TABLE `Base_Cooperation` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CooperationName` varchar(50) DEFAULT NULL COMMENT '资源名称',
  `ImageUrl` varchar(256) DEFAULT NULL COMMENT '图片地址',
  `Description` varchar(500) DEFAULT NULL COMMENT '资源描述',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `ClickUrl` varchar(256) DEFAULT NULL COMMENT '点击跳转URL',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='合作资源';

/*Data for the table `Base_Cooperation` */

insert  into `Base_Cooperation`(`Id`,`CooperationName`,`ImageUrl`,`Description`,`IsTop`,`ClickUrl`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'中大',NULL,'中大',0,NULL,0,'1','2017-06-17 13:14:57','1','2017-06-17 13:15:00','\0');

/*Table structure for table `Base_HomePageCarouselImage` */

CREATE TABLE `Base_HomePageCarouselImage` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ImageName` varchar(50) DEFAULT NULL COMMENT '图片名称',
  `ImageUrl` varchar(256) DEFAULT NULL COMMENT '图片地址',
  `Description` varchar(500) DEFAULT NULL COMMENT '描述',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `ClickUrl` varchar(256) DEFAULT NULL COMMENT '点击跳转URL',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='首页轮播图';

/*Data for the table `Base_HomePageCarouselImage` */

/*Table structure for table `Base_Label` */

CREATE TABLE `Base_Label` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `Description` varchar(500) DEFAULT NULL COMMENT '描述',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='标签';

/*Data for the table `Base_Label` */

insert  into `Base_Label`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'帅','帅',0,0,'1','2017-06-08 18:33:32','1','2017-06-08 18:33:32','\0');
insert  into `Base_Label`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'美','0',1,0,'1','2017-06-08 18:33:32','1','2017-07-05 21:12:10','\0');
insert  into `Base_Label`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (3,'酷','酷',0,0,'1','2017-06-08 18:33:32','1','2017-06-08 18:33:32','\0');
insert  into `Base_Label`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'非常厉害','0',0,1,'1','2017-07-02 11:41:33','1','2017-07-02 11:41:33','\0');

/*Table structure for table `Base_PlatformInfo` */

CREATE TABLE `Base_PlatformInfo` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CustomerServiceTelephone` varchar(50) DEFAULT NULL COMMENT '客服电话',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='平台信息';

/*Data for the table `Base_PlatformInfo` */

insert  into `Base_PlatformInfo`(`Id`,`CustomerServiceTelephone`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'400-000-000-000','1','2017-06-08 18:29:29','1','2017-06-08 18:29:32','\0');

/*Table structure for table `Base_ServiceArea` */

CREATE TABLE `Base_ServiceArea` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `Description` varchar(500) DEFAULT NULL COMMENT '描述',
  `IsTop` int(11) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='服务区域';

/*Data for the table `Base_ServiceArea` */

insert  into `Base_ServiceArea`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'美国','美国',0,0,'1','2017-06-08 18:30:01','1','2017-06-08 18:30:03','\0');
insert  into `Base_ServiceArea`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'英国','0',1,0,'1','2017-06-08 18:30:13','1','2017-07-05 21:17:34','\0');
insert  into `Base_ServiceArea`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (3,'澳大利亚','0',0,12,'1','2017-07-02 00:00:56','1','2017-07-02 00:02:47','\0');
insert  into `Base_ServiceArea`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'2','0',1,2,'1','2017-07-02 00:09:24','1','2017-07-02 00:09:29','');

/*Table structure for table `Base_ServiceType` */

CREATE TABLE `Base_ServiceType` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `Description` varchar(500) DEFAULT NULL COMMENT '描述',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='服务类型';

/*Data for the table `Base_ServiceType` */

insert  into `Base_ServiceType`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'签证移民','0',1,12,'1','2017-06-08 18:31:06','1','2017-07-05 21:17:25','\0');
insert  into `Base_ServiceType`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'生活辅助','0',0,13,'1','2017-06-08 18:31:23','1','2017-07-02 00:06:03','\0');
insert  into `Base_ServiceType`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (3,'游学指引','游学指引',0,0,'1','2017-06-08 18:31:45','1','2017-06-08 18:31:48','\0');
insert  into `Base_ServiceType`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'其他','0',0,2,'1','2017-06-08 18:31:57','1','2017-07-01 23:50:50','\0');
insert  into `Base_ServiceType`(`Id`,`Name`,`Description`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (5,'1','0',1,1,'1','2017-07-02 00:07:31','1','2017-07-02 00:09:11','');

/*Table structure for table `Base_VerificationCode` */

CREATE TABLE `Base_VerificationCode` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Phone` varchar(20) DEFAULT NULL COMMENT '手机号码',
  `VCode` varchar(10) DEFAULT NULL COMMENT '验证码',
  `IsRead` int(2) DEFAULT '1' COMMENT '是否已读 1：未读，2：已读',
  `CodeType` int(2) DEFAULT NULL COMMENT '验证码类型 1：注册，2：忘记密码',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改用户',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 COMMENT='短信验证码表';

/*Data for the table `Base_VerificationCode` */

insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'1','1',1,1,NULL,'2017-07-01 15:41:16',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'13672760122','8583',1,1,NULL,'2017-07-01 17:17:50',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (3,'13672760122','0852',2,1,NULL,'2017-07-01 17:18:09',NULL,'2017-07-01 17:18:55','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'13111111111','9185',1,1,NULL,'2017-07-01 17:55:43',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (5,'13111111111','7608',1,1,NULL,'2017-07-01 17:55:54',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (6,'13111111111','0629',1,1,NULL,'2017-07-01 18:00:20',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (7,'13111111111','3217',1,1,NULL,'2017-07-01 18:00:25',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (8,'13111111111','2121',1,1,NULL,'2017-07-01 18:01:07',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (9,'13111111111','9904',1,1,NULL,'2017-07-01 18:02:33',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (10,'13111111111','8123',1,1,NULL,'2017-07-01 18:02:34',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (11,'13111111111','8369',1,1,NULL,'2017-07-01 18:02:40',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (12,'13111111111','7430',1,1,NULL,'2017-07-01 18:02:41',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (13,'13111111111','6375',1,1,NULL,'2017-07-01 18:03:01',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (14,'13345666666','5864',1,1,NULL,'2017-07-01 18:04:12',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (15,'13345666666','1053',1,1,NULL,'2017-07-01 18:05:24',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (16,'13345666666','0615',1,1,NULL,'2017-07-01 18:05:25',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (17,'13345666666','9285',1,1,NULL,'2017-07-01 18:05:25',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (18,'13111111111','5676',1,1,NULL,'2017-07-01 18:07:09',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (19,'13111111111','3080',1,1,NULL,'2017-07-01 18:07:23',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (20,'13111111111','5935',1,1,NULL,'2017-07-01 18:08:57',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (21,'13111111111','0703',1,1,NULL,'2017-07-01 19:49:12',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (22,'13111111111','3039',1,1,NULL,'2017-07-01 20:01:08',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (23,'13111111112','9469',2,1,NULL,'2017-07-01 20:08:10',NULL,'2017-07-01 20:08:40','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (24,'13672760122','5546',2,2,NULL,'2017-07-01 22:24:17',NULL,'2017-07-01 22:25:30','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (25,'13122222222','0053',2,2,NULL,'2017-07-01 22:55:14',NULL,'2017-07-01 22:56:55','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (26,'13111111112','1234',2,2,NULL,'2017-07-01 22:57:18',NULL,'2017-07-01 22:57:46','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (27,'13111111111','9101',1,1,NULL,'2017-07-01 22:58:21',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (28,'13111111111','5538',1,2,NULL,'2017-07-01 22:58:42',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (29,'13111111111','2673',2,2,NULL,'2017-07-01 22:59:44',NULL,'2017-07-01 23:00:35','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (30,'13672760130','3271',1,1,NULL,'2017-07-04 12:15:48',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (31,'13672760130','5630',1,1,NULL,'2017-07-06 12:29:55',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (32,'13672760130','1652',1,1,NULL,'2017-07-10 15:24:16',NULL,NULL,'\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (33,'13672760130','6739',2,1,NULL,'2017-07-10 15:36:13',NULL,'2017-07-10 15:36:30','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (34,'13672760130','1804',2,1,NULL,'2017-07-10 15:42:43',NULL,'2017-07-10 15:43:04','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (35,'13672760133','1245',2,1,NULL,'2017-07-10 16:08:02',NULL,'2017-07-10 16:08:30','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (36,'13672760130','0989',2,2,NULL,'2017-07-21 14:22:20',NULL,'2017-07-21 14:22:30','\0');
insert  into `Base_VerificationCode`(`Id`,`Phone`,`VCode`,`IsRead`,`CodeType`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (37,'13672760130','6121',1,1,NULL,'2017-07-25 22:10:05',NULL,NULL,'\0');

/*Table structure for table `DS_DemandService` */

CREATE TABLE `DS_DemandService` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) DEFAULT NULL COMMENT '用户',
  `Name` varchar(200) DEFAULT NULL COMMENT '名称',
  `Type` int(11) DEFAULT NULL COMMENT '类型 1需求 2服务',
  `ServiceAreaId` int(11) DEFAULT NULL COMMENT '区域',
  `ServiceTypeId` int(11) DEFAULT NULL COMMENT '服务',
  `PriceStart` decimal(10,0) DEFAULT NULL COMMENT '价格起',
  `PriceEnd` decimal(10,0) DEFAULT NULL COMMENT '价格止',
  `TimeStart` datetime DEFAULT NULL COMMENT '时间起',
  `TimeEnd` datetime DEFAULT NULL COMMENT '时间止',
  `Description` text COMMENT '描述',
  `IsUndertake` int(11) DEFAULT '0' COMMENT '是否已承接 2 已失效 1已承接 0未承接 承接后规划师不可再选择',
  `CollectionCount` int(11) DEFAULT '0' COMMENT '收藏数量',
  `Sort` int(11) DEFAULT '0' COMMENT '排序 越大越靠前',
  `IsTop` int(1) DEFAULT '0' COMMENT '是否置顶 0不置顶 1置顶',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='需求服务';

/*Data for the table `DS_DemandService` */

insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','需求1',1,1,1,'1','10','2017-06-15 15:31:31','2017-06-30 15:31:34',NULL,2,0,0,0,'8f82f44a-4e9a-11e7-9ee4-00163e04f047','2017-06-15 15:31:43','1','2017-07-08 12:21:44','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('2','1','服务1',2,1,1,'1','1','2017-06-15 15:32:21','2017-08-31 15:32:23',NULL,0,12,0,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-15 15:32:34','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-15 15:32:38','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('30352c3a-6549-11e7-b7bc-1c1b0d79990b','f5b759c2-6546-11e7-898d-1c1b0d79990b','只是需求而已',1,3,4,'5000','50000','2017-07-11 00:00:00','2017-07-20 00:00:00','我感觉我是超人',0,0,0,1,'f5b759c2-6546-11e7-898d-1c1b0d79990b','2017-07-10 16:24:27','1','2017-07-10 16:25:26','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3865b402-55d0-11e7-b4e8-20689dd1eb55','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','我有一个服务',2,2,1,'0','0','2017-08-12 00:00:00','2020-09-01 00:00:00','我有一个服务',0,0,0,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-20 15:50:48','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-20 15:50:48','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('4cb2d802-6642-11e7-8c59-20689dd1eb55','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','123',2,2,1,'12','23','2017-08-01 00:00:00','2017-09-01 00:00:00','1234',0,0,0,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-11 22:07:43','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-11 22:07:43','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('567e4266-55d0-11e7-b05f-20689dd1eb55','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','我有一个服务2',2,2,1,'100','10000','2017-08-12 00:00:00','2020-09-01 00:00:00','我有一个服务',0,0,0,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-20 15:51:38','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-20 15:51:38','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('60848ca4-64a1-11e7-aed3-00163e08b8b6','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','我是一个需求',2,3,1,'2','2200','2017-07-09 00:00:00','2017-07-09 23:59:59','我是一个需求',0,0,0,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-09 20:23:12','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-09 20:23:12','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('89c87f5c-6548-11e7-acc7-1c1b0d79990b','684f4a7a-6543-11e7-a863-1c1b0d79990b','一个需求',2,3,4,'5000','50000','2017-07-11 00:00:00','2017-07-20 00:00:00','我想成为一个很屌的人',0,0,0,0,'684f4a7a-6543-11e7-a863-1c1b0d79990b','2017-07-10 16:19:48','684f4a7a-6543-11e7-a863-1c1b0d79990b','2017-07-10 16:19:48','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('9741f0ca-6549-11e7-b2d4-1c1b0d79990b','f5b759c2-6546-11e7-898d-1c1b0d79990b','还是我的需求',1,3,4,'5000','50000','2017-07-11 00:00:00','2017-07-20 00:00:00','我感觉我是一个很屌的人',0,0,0,0,'f5b759c2-6546-11e7-898d-1c1b0d79990b','2017-07-10 16:27:20','f5b759c2-6546-11e7-898d-1c1b0d79990b','2017-07-10 16:27:20','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('ccba1138-55cf-11e7-9123-20689dd1eb55','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','我有一个需求',1,1,1,'0','10','2017-08-01 00:00:00','2017-10-01 00:00:00','这是一个需求',0,0,0,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-20 15:47:47','1','2017-07-08 12:21:55','\0');
insert  into `DS_DemandService`(`Id`,`UserId`,`Name`,`Type`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`Description`,`IsUndertake`,`CollectionCount`,`Sort`,`IsTop`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('d8d58cee-64a1-11e7-aed3-00163e08b8b6','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','需求我就是',2,3,3,'2','222110','2017-07-09 00:00:00','2017-07-12 23:59:59','需求我就是',0,0,0,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-09 20:26:34','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-09 20:26:34','\0');

/*Table structure for table `DS_DemandUndertake` */

CREATE TABLE `DS_DemandUndertake` (
  `Id` varchar(40) NOT NULL,
  `DemandId` varchar(40) DEFAULT NULL COMMENT '需求ID',
  `UserId` varchar(40) DEFAULT NULL COMMENT '规划师ID (IsUser=1 就是用户希望的规划师id；否则就是申请承接的规划师id)',
  `Status` varchar(200) DEFAULT '1' COMMENT '状态 1:申请中 2：申请通过 3：申请不通过；一个需求只能有一个申请通过，由后台控制 成功的同时把其他改为失败 并且创建订单',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  `IsUser` int(2) DEFAULT '0' COMMENT '是否用户发起  0:规划师发起承接 1:用户发布需求的时候发起',
  `ContractId` int(11) DEFAULT NULL COMMENT '合同id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='需求承接';

/*Data for the table `DS_DemandUndertake` */

insert  into `DS_DemandUndertake`(`Id`,`DemandId`,`UserId`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IsUser`,`ContractId`) values ('cb74b6f8-6549-11e7-b226-00163e08b8b6','30352c3a-6549-11e7-b7bc-1c1b0d79990b','684f4a7a-6543-11e7-a863-1c1b0d79990b','2','684f4a7a-6543-11e7-a863-1c1b0d79990b','2017-07-10 16:28:47','1','2017-07-12 16:22:12','\0',0,1);
insert  into `DS_DemandUndertake`(`Id`,`DemandId`,`UserId`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IsUser`,`ContractId`) values ('ce4728ce-57b7-11e7-a958-0242c0a80005','3865b402-55d0-11e7-b4e8-20689dd1eb55','03db356e-4e9a-11e7-899d-f0761c143ea4','1','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-06-23 02:01:00',NULL,NULL,'\0',0,1);

/*Table structure for table `DS_Order` */

CREATE TABLE `DS_Order` (
  `Id` varchar(36) NOT NULL,
  `PlannerUserId` varchar(40) NOT NULL COMMENT '规划师',
  `UserId` varchar(40) NOT NULL COMMENT '用户',
  `ContractId` int(11) NOT NULL COMMENT '合同ID',
  `Type` int(11) DEFAULT '1' COMMENT '类型 1需求 2服务',
  `DemandServiceId` varchar(40) NOT NULL COMMENT '服务/需求ID  如果是选择服务或需求就会有',
  `DemandServiceDescription` text NOT NULL COMMENT '服务/需求描述  如果是选择服务或需求就会有',
  `Description` text NOT NULL COMMENT '描述',
  `ServiceAreaId` int(11) DEFAULT NULL COMMENT '区域',
  `ServiceTypeId` int(11) DEFAULT NULL COMMENT '服务',
  `PriceStart` decimal(10,0) DEFAULT NULL COMMENT '价格起',
  `PriceEnd` decimal(10,0) DEFAULT NULL COMMENT '价格止',
  `TimeStart` datetime DEFAULT NULL COMMENT '时间起',
  `TimeEnd` datetime DEFAULT NULL COMMENT '时间止',
  `OrderStatus` int(11) DEFAULT '1' COMMENT '状态 1:通知后台 2:客服回访 3:拟定合同 4:线下签约 5:平台审查 6:付款确认 7:服务完成 ，其他待定',
  `TimeConsuming` int(11) DEFAULT NULL COMMENT '完成时间 单位 天 状态改为完成时计算',
  `Synthesis` int(11) DEFAULT '5' COMMENT '综合评分 评价时赋值',
  `Quality` int(11) DEFAULT '5' COMMENT '质量评分 评价时赋值',
  `Efficiency` int(11) DEFAULT '5' COMMENT '效率评分 评价时赋值',
  `Lable` varchar(500) DEFAULT NULL COMMENT '标签 评价时赋值',
  `EvaluateContent` varchar(500) DEFAULT NULL COMMENT '首评 评价时赋值',
  `Sort` int(11) DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表';

/*Data for the table `DS_Order` */

insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('08c1ffea-57fe-11e7-a958-0242c0a80005','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','FD1E3DDC-E93E-46E1-8D5C-4675492E3263',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',100,NULL,5,5,5,'帅','首评',0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:23:43',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('0b25b894-57fe-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:23:47',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('2906c6df-5801-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:46:06',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('34c6f07a-66db-11e7-952e-1c1b0d79990b','684f4a7a-6543-11e7-a863-1c1b0d79990b','f5b759c2-6546-11e7-898d-1c1b0d79990b',1,1,'30352c3a-6549-11e7-b7bc-1c1b0d79990b','我感觉我是超人','我感觉我是超人',3,4,'5000','50000','2017-07-11 00:00:00','2017-07-20 00:00:00',7,NULL,5,5,5,NULL,NULL,0,'1','2017-07-12 16:22:12','1','2017-07-15 18:13:13','\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3704020d-57fd-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:17:51',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('386fc5c5-57fd-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:17:54',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3c23cf4d-5801-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:46:38',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('42450a2e-57fd-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:18:10',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('56abfa50-57fe-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:25:54',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('5790dd5f-57fe-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:25:56',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('8055baa0-57fe-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:27:04',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('816f1f9d-57fe-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:27:06',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('9bb49b65-57ff-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:34:59',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('9c794ae8-57ff-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:35:01',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('9d340f05-57ff-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:35:02',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('c8fd1fe5-57fa-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:00:28',NULL,NULL,'\0');
insert  into `DS_Order`(`Id`,`PlannerUserId`,`UserId`,`ContractId`,`Type`,`DemandServiceId`,`DemandServiceDescription`,`Description`,`ServiceAreaId`,`ServiceTypeId`,`PriceStart`,`PriceEnd`,`TimeStart`,`TimeEnd`,`OrderStatus`,`TimeConsuming`,`Synthesis`,`Quality`,`Efficiency`,`Lable`,`EvaluateContent`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('cb0b8b40-57fa-11e7-a958-0242c0a80005','1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',1,1,'1','1','1',1,1,'1','1','2017-06-23 00:00:00','2017-06-30 00:00:00',1,NULL,5,5,5,NULL,NULL,0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-23 10:00:31',NULL,NULL,'\0');

/*Table structure for table `DS_OrderFlowingWater` */

CREATE TABLE `DS_OrderFlowingWater` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `OrderId` varchar(40) NOT NULL COMMENT 'DS_Order 表主键Id',
  `UserId` varchar(40) NOT NULL COMMENT '处理用户',
  `StartStatus` int(11) NOT NULL COMMENT '起状态',
  `EndStatus` int(11) NOT NULL COMMENT '止状态',
  `Remarks` varchar(500) NOT NULL COMMENT '备注',
  `ChangeTime` datetime DEFAULT NULL COMMENT '改变时间',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='订单流水表';

/*Data for the table `DS_OrderFlowingWater` */

insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'34c6f07a-66db-11e7-952e-1c1b0d79990b','f5b759c2-6546-11e7-898d-1c1b0d79990b',1,2,'','2017-07-12 16:22:12','1','2017-07-12 16:22:12',NULL,NULL,'\0');
insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (5,'34c6f07a-66db-11e7-952e-1c1b0d79990b','1',2,3,'','2017-07-15 18:11:52','1','2017-07-15 18:11:52',NULL,NULL,'\0');
insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (6,'34c6f07a-66db-11e7-952e-1c1b0d79990b','1',3,4,'','2017-07-15 18:13:01','1','2017-07-15 18:13:01',NULL,NULL,'\0');
insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (7,'34c6f07a-66db-11e7-952e-1c1b0d79990b','1',4,5,'','2017-07-15 18:13:06','1','2017-07-15 18:13:06',NULL,NULL,'\0');
insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (8,'34c6f07a-66db-11e7-952e-1c1b0d79990b','1',5,6,'','2017-07-15 18:13:09','1','2017-07-15 18:13:09',NULL,NULL,'\0');
insert  into `DS_OrderFlowingWater`(`Id`,`OrderId`,`UserId`,`StartStatus`,`EndStatus`,`Remarks`,`ChangeTime`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (9,'34c6f07a-66db-11e7-952e-1c1b0d79990b','1',6,7,'','2017-07-15 18:13:13','1','2017-07-15 18:13:13',NULL,NULL,'');

/*Table structure for table `MS_SystemNotice` */

CREATE TABLE `MS_SystemNotice` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) DEFAULT NULL COMMENT '用户id',
  `Content` varchar(200) DEFAULT NULL COMMENT '消息内容',
  `IsRead` int(2) DEFAULT '0' COMMENT '是否已读  0:未读 1:已读',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  `Type` int(2) DEFAULT '1' COMMENT '1:系统消息    后面待定',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `MS_SystemNotice` */

insert  into `MS_SystemNotice`(`Id`,`UserId`,`Content`,`IsRead`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`Type`) values ('34dda32c-66db-11e7-b226-00163e08b8b6','f5b759c2-6546-11e7-898d-1c1b0d79990b','您的需求已被承接.',0,'1','2017-07-12 16:22:12',NULL,NULL,'\0',1);
insert  into `MS_SystemNotice`(`Id`,`UserId`,`Content`,`IsRead`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`Type`) values ('34eb5855-66db-11e7-b226-00163e08b8b6','684f4a7a-6543-11e7-a863-1c1b0d79990b','您申请的承接需求通过.',0,'1','2017-07-12 16:22:12',NULL,NULL,'\0',1);

/*Table structure for table `Sys_P_Permission` */

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

/*Data for the table `Sys_P_Permission` */

insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10000,0,'System','系统管理','',0,'','系统管理','<i class=\"fa fa-cogs\"></i>');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10100,10000,'SystemUserIndex','用户管理','/System/UserIndex.html',0,'','用户管理','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10101,10100,'SystemUserList','查看用户列表','/System/UserList',0,'','查看用户列表','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10102,10100,'SystemUserDetail','查看用户信息','/System/UserDetail.html',0,'','查看用户信息','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10103,10100,'SystemUserAdd','增加用户','/System/UserAdd.html',0,'','增加用户','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10104,10100,'SystemUserEdit','修改用户信息','/System/UserEdit.html',0,'','修改用户信息','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10105,10100,'SystemUserUpdateStatus','变更用户状态','/System/UpdateUserStatus',0,'','变更用户状态','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10106,10100,'SystemUserRoleEdit','修改用户角色','/System/UserRoleEdit.html',0,'','修改用户角色','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10107,10100,'SystemUserDelete','删除用户','/System/UserDelete',0,'','删除用户','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10200,10000,'SystemRoleIndex','角色权限','/System/RoleIndex.html',0,'','角色权限','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10201,10200,'SystemRoleList','查看角色列表','/System/RoleList',0,'','角色列表','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10202,10200,'SystemRoleAdd','创建角色','/System/RoleAdd.html',0,'','创建角色','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10203,10200,'SystemRoleConfig','角色权限配置','/System/RoleConfig.html',0,'','角色权限配置','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (10204,10200,'SystemRoleDelete','角色删除','/System/RoleDelete',0,'','角色删除','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (20000,0,'Log','日志管理','',40,'','日志管理','<i class=\"fa fa-book\"></i>');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (20100,20000,'LogIndex','日志查询','/Log/LogIndex.html',0,'','日志查询','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (20101,20100,'LogList','查看日志信息','/Log/LogList',0,'','查看日志信息','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (20200,20000,'LogStatistics','日志统计','/Log/LogStatistics.html',0,'','日志查询','');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (20201,20200,'LogStatisticsData','日志统计信息','/Log/LogStatisticsData',0,'','日志统计信息',' ');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (30000,0,'Msg','消息管理','',20,'','消息管理','<i class=\"fa fa-envelope\"></i>');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (30100,30000,'MsgSmsIndex','短信查询','/Msg/MsgSmsIndex.html',0,'','短信查询',' ');
insert  into `Sys_P_Permission`(`PermissionId`,`ParentId`,`Name`,`MenuName`,`Url`,`Orderby`,`Visible`,`Remark`,`Icon`) values (30101,30100,'MsgSmsData','短信数据','/Msg/MsgSmsData',0,'','短信数据',' ');

/*Table structure for table `Sys_P_Role` */

CREATE TABLE `Sys_P_Role` (
  `RoleId` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `RoleName` varchar(30) NOT NULL COMMENT '角色名称',
  `Remark` varchar(150) DEFAULT NULL COMMENT '描述',
  `CreateDate` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`RoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `Sys_P_Role` */

insert  into `Sys_P_Role`(`RoleId`,`RoleName`,`Remark`,`CreateDate`) values (1,'平台管理员','拥有平台所有权限','2017-06-05 15:08:56');

/*Table structure for table `Sys_P_RolePermission` */

CREATE TABLE `Sys_P_RolePermission` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RoleId` int(11) NOT NULL COMMENT '角色Id',
  `PermissionId` int(11) NOT NULL COMMENT '权限Id',
  `Scope` int(11) NOT NULL DEFAULT '0' COMMENT '数据范围,0:个人,1:部门,2,全局',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8;

/*Data for the table `Sys_P_RolePermission` */

insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (120,1,10000,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (121,1,10100,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (122,1,10101,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (123,1,10102,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (124,1,10103,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (125,1,10104,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (126,1,10105,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (127,1,10106,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (128,1,10107,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (129,1,10200,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (130,1,10201,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (131,1,10202,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (132,1,10203,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (133,1,10204,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (134,1,20000,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (135,1,20100,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (136,1,20101,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (137,1,20200,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (138,1,20201,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (139,1,30000,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (140,1,30100,0);
insert  into `Sys_P_RolePermission`(`Id`,`RoleId`,`PermissionId`,`Scope`) values (141,1,30101,0);

/*Table structure for table `Sys_P_UserRole` */

CREATE TABLE `Sys_P_UserRole` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(40) NOT NULL COMMENT '用户id',
  `RoleId` int(11) NOT NULL COMMENT '角色id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `Sys_P_UserRole` */

insert  into `Sys_P_UserRole`(`Id`,`UserId`,`RoleId`) values (3,'1',1);

/*Table structure for table `Sys_User` */

CREATE TABLE `Sys_User` (
  `UserId` varchar(40) NOT NULL COMMENT '用户id',
  `UserName` varchar(36) NOT NULL COMMENT '登录名',
  `Password` varchar(150) NOT NULL COMMENT '密码',
  `NickName` varchar(20) NOT NULL COMMENT '用户名称',
  `Phone` varchar(15) DEFAULT '''' COMMENT '手机',
  `Email` varchar(36) DEFAULT '''' COMMENT '邮箱',
  `Descript` varchar(300) DEFAULT '''' COMMENT '描述',
  `CreateDate` datetime NOT NULL COMMENT '创建时间',
  `Status` int(11) NOT NULL DEFAULT '1' COMMENT '状态 1有效',
  `IsAdmin` int(1) NOT NULL DEFAULT '0' COMMENT '是否管理员',
  `LoginToken` varchar(50) DEFAULT NULL,
  `LoginIP` varchar(20) DEFAULT NULL,
  `LoginTime` datetime DEFAULT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `Sys_User` */

insert  into `Sys_User`(`UserId`,`UserName`,`Password`,`NickName`,`Phone`,`Email`,`Descript`,`CreateDate`,`Status`,`IsAdmin`,`LoginToken`,`LoginIP`,`LoginTime`) values ('1','admin','e10adc3949ba59abbe56e057f20f883e','平台管理员','13533324375','904709108@qq.com','平台管理员账号1','2017-06-05 15:08:22',1,1,'17d6eac6-7377-11e7-b342-00163e08b8b6','127.0.0.1','2017-07-28 17:28:19');

/*Table structure for table `T_Team` */

CREATE TABLE `T_Team` (
  `Id` varchar(40) NOT NULL COMMENT '主键Id',
  `AdminUserId` varchar(40) NOT NULL COMMENT 'U_User表主键Id',
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `ServiceAreaId` int(11) DEFAULT NULL COMMENT '服务区域',
  `ServiceDescription` varchar(50) DEFAULT NULL COMMENT '服务描述',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 1置顶 0 不置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='团队';

/*Data for the table `T_Team` */

insert  into `T_Team`(`Id`,`AdminUserId`,`Name`,`ServiceAreaId`,`ServiceDescription`,`IsTop`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','03db356e-4e9a-11e7-899d-f0761c143ea4','团队1',1,'团队1',0,0,'03db356e-4e9a-11e7-899d-f0761c143ea4','2017-06-18 12:37:51','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-06-18 12:37:55','\0');

/*Table structure for table `T_TeamMember` */

CREATE TABLE `T_TeamMember` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `TeamId` varchar(40) NOT NULL COMMENT 'T_Team 表主键Id',
  `UserId` varchar(40) NOT NULL COMMENT 'U_User 表主键Id',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='团队成员';

/*Data for the table `T_TeamMember` */

insert  into `T_TeamMember`(`Id`,`TeamId`,`UserId`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 12:40:53','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-06-18 12:40:58','\0');
insert  into `T_TeamMember`(`Id`,`TeamId`,`UserId`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (8,'1','FD1E3DDC-E93E-46E1-8D5C-4675492E3263',0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-03 11:52:32',NULL,NULL,'\0');

/*Table structure for table `T_TeamNotice` */

CREATE TABLE `T_TeamNotice` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) NOT NULL COMMENT '用户id',
  `TeamId` varchar(40) DEFAULT NULL COMMENT '团队id',
  `Message` varchar(100) DEFAULT NULL COMMENT '描述',
  `Status` int(2) DEFAULT NULL COMMENT '1:待审核,2：审核通过 3:审核拒绝',
  `IsAdmin` int(2) DEFAULT NULL COMMENT '是否团队管理员  1：是 2：否',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户id',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改用户',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  `UnionId` varchar(40) NOT NULL COMMENT '外键关联对应的团队消息id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='团队通知表';

/*Data for the table `T_TeamNotice` */

insert  into `T_TeamNotice`(`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`UnionId`) values ('04160bf8-5f3c-11e7-b226-00163e08b8b6','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','1','您正在申请加入 团队1 团队',2,2,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 23:35:02','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-03 11:52:32','\0','fffbd0c0-5f3b-11e7-9d9d-f0761c143ea4');
insert  into `T_TeamNotice`(`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`UnionId`) values ('0417ce38-5f3c-11e7-b226-00163e08b8b6','03db356e-4e9a-11e7-899d-f0761c143ea4','1','用户 jimmy.pan 正在申请加入团队',2,1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 23:35:02','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-03 11:52:32','\0','fffbd0c0-5f3b-11e7-9d9d-f0761c143ea4');
insert  into `T_TeamNotice`(`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`UnionId`) values ('858be43f-5fa6-11e7-b226-00163e08b8b6','4afcd9c2-5e3e-11e7-bd22-f0761c143ea4','1','您正在申请加入 团队1 团队',3,2,'4afcd9c2-5e3e-11e7-bd22-f0761c143ea4','2017-07-03 12:17:26','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-07-03 12:32:53','\0','85d73c62-5fa6-11e7-8d8c-f0761c143ea4');
insert  into `T_TeamNotice`(`Id`,`UserId`,`TeamId`,`Message`,`Status`,`IsAdmin`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`UnionId`) values ('858d5003-5fa6-11e7-b226-00163e08b8b6','03db356e-4e9a-11e7-899d-f0761c143ea4','1','用户 徐大师 正在申请加入团队',3,1,'4afcd9c2-5e3e-11e7-bd22-f0761c143ea4','2017-07-03 12:17:26','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-07-03 12:32:53','\0','85d73c62-5fa6-11e7-8d8c-f0761c143ea4');

/*Table structure for table `U_Album` */

CREATE TABLE `U_Album` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(40) NOT NULL COMMENT 'U_User 表主键Id',
  `PhotoName` varchar(40) DEFAULT NULL COMMENT '照片名称',
  `Url` varchar(256) NOT NULL DEFAULT '1' COMMENT '地址',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='用户相册';

/*Data for the table `U_Album` */

insert  into `U_Album`(`Id`,`UserId`,`PhotoName`,`Url`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (5,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2009-10-01','http://121.0.0.1:9000.jpg',0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:10:34','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:10:34','\0');
insert  into `U_Album`(`Id`,`UserId`,`PhotoName`,`Url`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (6,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2009-10-01','http://121.0.0.1:9000.jpg',0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 11:54:00','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 11:54:00','\0');
insert  into `U_Album`(`Id`,`UserId`,`PhotoName`,`Url`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (7,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','1498968508517_359195','files/2017-07-02/1c1cb1ec-5edc-11e7-8d3a-00163e08b8b6.jpg',1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 12:08:31','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-02 12:08:31','\0');

/*Table structure for table `U_BrowseRecord` */

CREATE TABLE `U_BrowseRecord` (
  `UserId` varchar(40) NOT NULL COMMENT '浏览人ID',
  `DemandServiceId` varchar(40) NOT NULL COMMENT '浏览的需求服务ID',
  `BrowseTime` datetime DEFAULT NULL COMMENT '浏览时间',
  PRIMARY KEY (`UserId`,`DemandServiceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='浏览记录';

/*Data for the table `U_BrowseRecord` */

insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','4cb2d802-6642-11e7-8c59-20689dd1eb55','2017-07-25 17:14:33');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','60848ca4-64a1-11e7-aed3-00163e08b8b6','2017-07-25 11:23:15');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','89c87f5c-6548-11e7-acc7-1c1b0d79990b','2017-07-25 11:23:11');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','9741f0ca-6549-11e7-b2d4-1c1b0d79990b','2017-07-25 11:49:52');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('f88b255e-55c3-11e7-a8f0-00163e04f047','4cb2d802-6642-11e7-8c59-20689dd1eb55','2017-07-30 16:27:06');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','1','2017-06-17 04:45:04');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2','2017-06-17 04:44:05');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','30352c3a-6549-11e7-b7bc-1c1b0d79990b','2017-07-16 19:20:12');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','4cb2d802-6642-11e7-8c59-20689dd1eb55','2017-07-24 22:52:44');
insert  into `U_BrowseRecord`(`UserId`,`DemandServiceId`,`BrowseTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','9741f0ca-6549-11e7-b2d4-1c1b0d79990b','2017-07-16 19:20:05');

/*Table structure for table `U_Collection` */

CREATE TABLE `U_Collection` (
  `UserId` varchar(40) NOT NULL COMMENT '收藏人ID',
  `DemandServiceId` varchar(40) NOT NULL COMMENT '被收藏的需求服务ID',
  `CollectionTime` datetime DEFAULT NULL COMMENT '收藏时间',
  PRIMARY KEY (`UserId`,`DemandServiceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='收藏表';

/*Data for the table `U_Collection` */

insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('1','1','2017-06-15 09:44:01');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('1','2','2017-06-15 07:44:59');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','1','2017-06-17 04:43:00');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2','2017-06-17 04:43:20');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','4cb2d802-6642-11e7-8c59-20689dd1eb55','2017-07-16 19:13:31');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','567e4266-55d0-11e7-b05f-20689dd1eb55','2017-07-09 17:26:44');
insert  into `U_Collection`(`UserId`,`DemandServiceId`,`CollectionTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','9741f0ca-6549-11e7-b2d4-1c1b0d79990b','2017-07-16 19:13:34');

/*Table structure for table `U_Education` */

CREATE TABLE `U_Education` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) DEFAULT NULL COMMENT '用户',
  `TimeStart` datetime DEFAULT NULL COMMENT '时间起',
  `TimeEnd` datetime DEFAULT NULL COMMENT '时间止',
  `University` varchar(200) DEFAULT NULL COMMENT '大学',
  `Degree` varchar(200) DEFAULT NULL COMMENT '学位',
  `Sort` int(11) DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='学历';

/*Data for the table `U_Education` */

insert  into `U_Education`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`University`,`Degree`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2009-10-13 13:21:20','2013-07-01 13:21:22','清华','本科',0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:23:10','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:23:12','\0');
insert  into `U_Education`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`University`,`Degree`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('23ad03ec-5754-11e7-a497-20689dd1eb55','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2009-10-01 00:00:00','2013-07-01 00:00:00','清华大学','学士',0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:37','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:37','\0');

/*Table structure for table `U_Evaluate` */

CREATE TABLE `U_Evaluate` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `OrderId` varchar(40) NOT NULL COMMENT 'DS_Order 表主键Id',
  `UserId` varchar(40) NOT NULL COMMENT '评价用户ID 填写评价的人',
  `Content` varchar(500) NOT NULL COMMENT '内容',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `IsFirst` int(11) DEFAULT '1' COMMENT '是否首评 显示在评论列表的，其他的显示在评论详情',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='评价表';

/*Data for the table `U_Evaluate` */

insert  into `U_Evaluate`(`Id`,`OrderId`,`UserId`,`Content`,`Sort`,`IsFirst`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (7,'08c1ffea-57fe-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','首评',0,1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-25 11:18:05','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-25 11:18:05','\0');
insert  into `U_Evaluate`(`Id`,`OrderId`,`UserId`,`Content`,`Sort`,`IsFirst`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (8,'08c1ffea-57fe-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','回复评论',0,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-25 11:18:45','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-25 11:18:45','\0');

/*Table structure for table `U_Follow` */

CREATE TABLE `U_Follow` (
  `UserId` varchar(40) NOT NULL COMMENT '关注人ID',
  `FollwUserId` varchar(40) NOT NULL COMMENT '被关注的用户ID',
  `FollwTime` datetime DEFAULT NULL COMMENT '关注时间',
  PRIMARY KEY (`UserId`,`FollwUserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `U_Follow` */

insert  into `U_Follow`(`UserId`,`FollwUserId`,`FollwTime`) values ('1','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-06-15 06:56:51');
insert  into `U_Follow`(`UserId`,`FollwUserId`,`FollwTime`) values ('1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-15 06:57:45');
insert  into `U_Follow`(`UserId`,`FollwUserId`,`FollwTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','03db356e-4e9a-11e7-899d-f0761c143ea4','2017-07-09 15:28:39');
insert  into `U_Follow`(`UserId`,`FollwUserId`,`FollwTime`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-07-08 15:03:24');

/*Table structure for table `U_PlannerStatistics` */

CREATE TABLE `U_PlannerStatistics` (
  `UserId` varchar(40) NOT NULL,
  `PraiseCount` int(11) NOT NULL DEFAULT '0' COMMENT '好评数量',
  `BadReviewCount` int(11) NOT NULL DEFAULT '0' COMMENT '差评数量',
  `CustomerCount` int(11) NOT NULL DEFAULT '0' COMMENT '客户数量',
  `OrderCount` int(11) NOT NULL DEFAULT '0' COMMENT '订单数量',
  `IsTop` int(1) NOT NULL DEFAULT '0' COMMENT '是否置顶 1置顶 0 不置顶',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `TeamId` varchar(40) DEFAULT NULL COMMENT '团队ID',
  `NewEvaluate` varchar(200) DEFAULT NULL COMMENT '最新评价',
  `Lables` varchar(200) DEFAULT NULL COMMENT '标签集合 定时任务',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) NOT NULL DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='规划师统计表';

/*Data for the table `U_PlannerStatistics` */

insert  into `U_PlannerStatistics`(`UserId`,`PraiseCount`,`BadReviewCount`,`CustomerCount`,`OrderCount`,`IsTop`,`Sort`,`TeamId`,`NewEvaluate`,`Lables`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('03db356e-4e9a-11e7-899d-f0761c143ea4',12,0,12,12,0,1,NULL,'很好人','帅,酷,漂亮','1','2017-06-18 12:40:16','1','2017-07-01 22:29:11','\0');
insert  into `U_PlannerStatistics`(`UserId`,`PraiseCount`,`BadReviewCount`,`CustomerCount`,`OrderCount`,`IsTop`,`Sort`,`TeamId`,`NewEvaluate`,`Lables`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3C3C46F6-9D2B-4918-92D4-6BC1B669C85F',104,0,100,100,0,20,'1','首评','帅,酷,漂亮','1','2017-06-08 18:36:19','1','2017-06-08 18:36:22','\0');

/*Table structure for table `U_Resour` */

CREATE TABLE `U_Resour` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) DEFAULT NULL COMMENT '用户',
  `TimeStart` datetime DEFAULT NULL COMMENT '时间起',
  `TimeEnd` datetime DEFAULT NULL COMMENT '时间止',
  `Description` varchar(200) DEFAULT NULL COMMENT '描述',
  `Sort` int(11) DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='资源背景';

/*Data for the table `U_Resour` */

insert  into `U_Resour`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','1990-09-27 13:23:24','2017-06-18 13:23:35','我有个很厉害的老爸',0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:23:51','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:23:54','\0');
insert  into `U_Resour`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('2bcb7eb4-5754-11e7-b06b-20689dd1eb55','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2009-10-01 00:00:00','2013-07-01 00:00:00','读书',1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:51','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:51','\0');

/*Table structure for table `U_Society` */

CREATE TABLE `U_Society` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) DEFAULT NULL COMMENT '用户',
  `TimeStart` datetime DEFAULT NULL COMMENT '时间起',
  `TimeEnd` datetime DEFAULT NULL COMMENT '时间止',
  `Description` varchar(200) DEFAULT NULL COMMENT '描述',
  `Sort` int(11) DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='社会背景';

/*Data for the table `U_Society` */

insert  into `U_Society`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2013-07-01 13:22:24','2017-06-18 13:22:43','清华大学教授',0,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:22:56','3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','2017-06-18 13:22:59','\0');
insert  into `U_Society`(`Id`,`UserId`,`TimeStart`,`TimeEnd`,`Description`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('2ec45d5a-5754-11e7-95dd-20689dd1eb55','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2009-10-01 00:00:00','2013-07-01 00:00:00','读书',1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:57','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-22 14:07:57','\0');

/*Table structure for table `U_UpgradeUserTemp` */

CREATE TABLE `U_UpgradeUserTemp` (
  `Id` varchar(40) NOT NULL,
  `UserId` varchar(40) NOT NULL COMMENT '用户id',
  `Sex` int(2) DEFAULT '0' COMMENT '性别 1:男 2:女 0:未知',
  `Name` varchar(50) DEFAULT NULL COMMENT '用户姓名',
  `Address` varchar(256) DEFAULT NULL COMMENT '所在地',
  `ServiceId` int(11) DEFAULT NULL COMMENT '服务id',
  `ServiceAreaId` int(11) DEFAULT NULL COMMENT '服务区域id',
  `Email` varchar(256) DEFAULT NULL COMMENT '邮箱',
  `Experience` varchar(500) DEFAULT NULL COMMENT '资历',
  `IDCard` varchar(20) DEFAULT NULL COMMENT '身份证',
  `IDCardPic` varchar(100) DEFAULT NULL COMMENT '身份证正面图片',
  `Status` int(2) DEFAULT '0' COMMENT '0：审核中 1：审核通过 2：审核不通过',
  `CreateUserID` varchar(40) DEFAULT NULL,
  `CreateTime` datetime DEFAULT NULL,
  `ModifUserID` varchar(40) DEFAULT NULL,
  `ModifTime` datetime DEFAULT NULL,
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  `IDCardBackPic` varchar(100) DEFAULT NULL COMMENT '身份证反面图片',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='注册规划师审核表';

/*Data for the table `U_UpgradeUserTemp` */

insert  into `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCard`,`IDCardPic`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IDCardBackPic`) values ('0f515730-55cb-11e7-a958-0242c0a80005','fbcb0ba6-55ca-11e7-a8f0-00163e04f047',1,'pyj3','茂名',1,1,'23@11','123',NULL,'files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',1,'fbcb0ba6-55ca-11e7-a8f0-00163e04f047','2017-06-20 15:13:48','1','2017-07-05 15:57:13','\0',NULL);
insert  into `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCard`,`IDCardPic`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IDCardBackPic`) values ('5816112e-6547-11e7-b226-00163e08b8b6','684f4a7a-6543-11e7-a863-1c1b0d79990b',1,'徐大师','中华人民共和国广东省',1,1,'12545@44','很吊的经历防守打法',NULL,'files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',1,'684f4a7a-6543-11e7-a863-1c1b0d79990b','2017-07-10 16:11:15','1','2017-07-10 16:11:38','\0',NULL);
insert  into `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCard`,`IDCardPic`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IDCardBackPic`) values ('bcffe289-55ca-11e7-a958-0242c0a80005','5ca8af60-55ca-11e7-a8f0-00163e04f047',1,'pyj2','茂名',4,1,'123@qq.com','叼的很',NULL,'files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',2,'5ca8af60-55ca-11e7-a8f0-00163e04f047','2017-06-20 15:11:30','1','2017-07-05 16:01:30','\0',NULL);
insert  into `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCard`,`IDCardPic`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IDCardBackPic`) values ('bebaef5d-55c8-11e7-a958-0242c0a80005','FD1E3DDC-E93E-46E1-8D5C-4675492E3263',2,'pyj1','茂名',4,1,'123@11','很吊的经历',NULL,'files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-20 14:57:13','1','2017-07-05 16:16:39','\0',NULL);
insert  into `U_UpgradeUserTemp`(`Id`,`UserId`,`Sex`,`Name`,`Address`,`ServiceId`,`ServiceAreaId`,`Email`,`Experience`,`IDCard`,`IDCardPic`,`Status`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`,`IDCardBackPic`) values ('ec5f13f3-55c9-11e7-a958-0242c0a80005','f88b255e-55c3-11e7-a8f0-00163e04f047',1,'pyj','茂名',4,1,'123@qq.com','叼的很',NULL,'files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',1,'f88b255e-55c3-11e7-a8f0-00163e04f047','2017-06-20 15:05:40','1','2017-07-05 16:08:25','\0',NULL);

/*Table structure for table `U_User` */

CREATE TABLE `U_User` (
  `Id` varchar(40) NOT NULL,
  `Account` varchar(50) DEFAULT NULL COMMENT '帐号',
  `Password` varchar(50) DEFAULT NULL COMMENT '密码',
  `Phone` varchar(20) DEFAULT NULL COMMENT '手机号码',
  `UserType` int(11) DEFAULT '1' COMMENT '用户类型 1普通用户 2菜鸟规划师 3规划师',
  `LoginTime` datetime DEFAULT NULL COMMENT '登录时间',
  `LoginToken` varchar(50) DEFAULT NULL COMMENT '登录Token',
  `LoginIP` varchar(50) DEFAULT NULL COMMENT '当前登录IP',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

/*Data for the table `U_User` */

insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('03db356e-4e9a-11e7-899d-f0761c143ea4','xujiang','123456','13533324375',2,'2017-07-03 12:32:27','9ec61e26-5fa8-11e7-8bc9-f0761c143ea4','127.0.0.1',NULL,'2017-06-11 11:35:15',NULL,NULL,'\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('051e54fe-5e56-11e7-aeaa-00163e08b8b6','13111111112','9a952cd91000872a8d7d1f5ee0c87317','13533324375',1,'2017-07-01 22:58:00','ad416e2a-5e6d-11e7-be9d-00163e08b8b6','127.0.0.1',NULL,'2017-07-01 20:08:40',NULL,NULL,'\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','admin','e10adc3949ba59abbe56e057f20f883e','13533324375',0,'2017-06-13 10:55:04','c158a4a2-5026-11e7-acc0-1c1b0d7ef3e7','127.0.0.1','1','2017-06-08 18:28:33','1','2017-07-25 19:48:37','\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','ghs','e10adc3949ba59abbe56e057f20f883e','13533324375',3,NULL,'a27815a6-530f-11e7-8b18-20689dd1eb56',NULL,'1','2017-06-08 18:34:57','1','2017-06-08 18:35:02','\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3d169c2a-5507-11e7-a8f0-00163e04f047','pyj1','e10adc3949ba59abbe56e057f20f883e','13533324375',1,NULL,NULL,NULL,NULL,'2017-06-19 15:52:03','1','2017-07-01 11:22:11','');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('4afcd9c2-5e3e-11e7-bd22-f0761c143ea4','13672760122','12563','13533324375',2,'2017-07-07 10:09:27','4e0afca8-62b9-11e7-8c8a-1c1b0d79990b','127.0.0.1',NULL,'2017-07-01 17:18:55',NULL,NULL,'\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('5ca8af60-55ca-11e7-a8f0-00163e04f047','pyj2','e10adc3949ba59abbe56e057f20f883e','13533324375',1,'2017-06-20 15:10:57','a9c41168-55ca-11e7-a8f0-00163e04f047','127.0.0.1',NULL,'2017-06-20 15:08:48','1','2017-07-01 11:21:56','');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','13672760130','e10adc3949ba59abbe56e057f20f883e','13672760130',2,'2017-07-25 22:13:57','7fb201de-7143-11e7-b342-00163e08b8b6','127.0.0.1',NULL,'2017-07-10 15:43:04','1','2017-07-10 16:11:38','\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('8f82f44a-4e9a-11e7-9ee4-00163e04f047','xujiang1','123456','13533324375',1,NULL,NULL,NULL,NULL,'2017-06-11 11:38:59',NULL,NULL,'\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('98c89b40-712f-11e7-b8c9-1c1b0d7ef3e7','admin2','e10adc3949ba59abbe56e057f20f883e','13413313355',0,NULL,NULL,NULL,'1','2017-07-25 19:51:29','1','2017-07-25 19:51:29','\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('f5b759c2-6546-11e7-898d-1c1b0d79990b','13672760133','123456','13672760133',1,'2017-07-10 16:23:10','02283b7a-6549-11e7-9685-1c1b0d79990b','127.0.0.1',NULL,'2017-07-10 16:08:30',NULL,NULL,'\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('f88b255e-55c3-11e7-a8f0-00163e04f047','lyc','e10adc3949ba59abbe56e057f20f883e','13533324375',2,'2017-07-16 23:00:56','922c33a6-6a37-11e7-921a-00163e08b8b6','127.0.0.1',NULL,'2017-06-20 14:23:03','1','2017-07-05 16:08:25','');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('fbcb0ba6-55ca-11e7-a8f0-00163e04f047','pyj3','202cb962ac59075b964b07152d234b70','13533324375',2,'2017-06-20 15:13:28','03b9ba1a-55cb-11e7-a8f0-00163e04f047','127.0.0.1',NULL,'2017-06-20 15:13:15','1','2017-07-05 15:59:58','\0');
insert  into `U_User`(`Id`,`Account`,`Password`,`Phone`,`UserType`,`LoginTime`,`LoginToken`,`LoginIP`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','pyj','e10adc3949ba59abbe56e057f20f883e','13533324375',2,'2017-07-30 09:38:20','c4baa916-74c7-11e7-b342-00163e08b8b6','127.0.0.1','1','2017-06-08 18:14:48','1','2017-07-05 16:16:39','\0');

/*Table structure for table `U_UserInfo` */

CREATE TABLE `U_UserInfo` (
  `UserId` varchar(40) NOT NULL COMMENT 'U_User主键Id',
  `Name` varchar(50) DEFAULT NULL COMMENT '名称',
  `Sex` int(11) DEFAULT '1' COMMENT '性别 1:男 2:女 0:未知',
  `Address` varchar(256) DEFAULT NULL COMMENT '地址',
  `Age` int(11) DEFAULT '0' COMMENT '年龄',
  `Education` varchar(256) DEFAULT NULL COMMENT '学历',
  `Email` varchar(256) DEFAULT NULL COMMENT '邮箱',
  `IDCard` varchar(20) DEFAULT NULL COMMENT '身份证',
  `IDCardJust` varchar(256) DEFAULT NULL COMMENT '身份证正面',
  `IDCardBack` varchar(256) DEFAULT NULL COMMENT '身份证反面',
  `HeadImage` varchar(256) DEFAULT NULL COMMENT '头像',
  `ServiceAreaId` int(11) DEFAULT NULL COMMENT '服务区域',
  `ServiceTypeId` int(11) DEFAULT NULL COMMENT '服务类型',
  `Autograph` varchar(200) DEFAULT NULL COMMENT '签名',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

/*Data for the table `U_UserInfo` */

insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('03db356e-4e9a-11e7-899d-f0761c143ea4','规划师2',1,NULL,0,NULL,NULL,NULL,NULL,NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',1,2,NULL,NULL,'2017-06-11 11:35:15',NULL,NULL,'\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('051e54fe-5e56-11e7-aeaa-00163e08b8b6',NULL,1,NULL,0,NULL,NULL,NULL,NULL,NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',NULL,NULL,NULL,NULL,'2017-07-01 20:08:40',NULL,NULL,'\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('1','系统管理员',1,'地球',0,NULL,NULL,NULL,NULL,NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',2,2,NULL,'1','2017-06-08 18:29:15','1','2017-06-08 18:29:19','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','规划师',1,'北京',30,'博士',NULL,NULL,NULL,NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',1,1,NULL,'1','2017-06-08 18:17:01','1','2017-06-08 18:17:01','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('3d169c2a-5507-11e7-a8f0-00163e04f047',NULL,1,NULL,0,NULL,NULL,NULL,NULL,NULL,'files/person.jpg',NULL,NULL,NULL,NULL,'2017-06-19 15:52:03','1','2017-07-01 11:22:11','');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('4afcd9c2-5e3e-11e7-bd22-f0761c143ea4','徐大师',1,NULL,0,NULL,NULL,NULL,NULL,NULL,'files/person.jpg',NULL,NULL,NULL,NULL,'2017-07-01 17:18:55',NULL,NULL,'\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('5ca8af60-55ca-11e7-a8f0-00163e04f047',NULL,1,NULL,0,NULL,NULL,NULL,NULL,NULL,'files/person.jpg',NULL,NULL,NULL,NULL,'2017-06-20 15:08:48','1','2017-07-01 11:21:56','');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('684f4a7a-6543-11e7-a863-1c1b0d79990b','徐大师',1,'中华人民共和国广东省',27,'很吊的经历防守打法','12545@44','None','files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',NULL,'files/person.jpg',1,1,NULL,NULL,'2017-07-10 15:43:04','1','2017-07-10 16:11:38','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('8f82f44a-4e9a-11e7-9ee4-00163e04f047','李四',2,'地址',30,'博士','123@123.com',NULL,NULL,NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',1,1,NULL,NULL,'2017-06-11 11:38:59','1','2017-07-02 11:56:19','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('f5b759c2-6546-11e7-898d-1c1b0d79990b','旭江的普通用户',1,'中华人民',11,'高中','456245@qq.com',NULL,NULL,NULL,'files/person.jpg',NULL,NULL,NULL,NULL,'2017-07-10 16:08:30','1','2017-07-10 16:12:52','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('f88b255e-55c3-11e7-a8f0-00163e04f047','pyj',1,'茂名',0,'叼的很','123@qq.com','None','files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',NULL,'files/person.jpg',1,4,NULL,NULL,'2017-06-20 14:23:03','1','2017-07-05 16:08:25','');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('fbcb0ba6-55ca-11e7-a8f0-00163e04f047','pyj3',1,'茂名',0,'123','23@11','None','files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',NULL,'files/person.jpg',1,1,NULL,NULL,'2017-06-20 15:13:15','1','2017-07-05 15:59:58','\0');
insert  into `U_UserInfo`(`UserId`,`Name`,`Sex`,`Address`,`Age`,`Education`,`Email`,`IDCard`,`IDCardJust`,`IDCardBack`,`HeadImage`,`ServiceAreaId`,`ServiceTypeId`,`Autograph`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values ('FD1E3DDC-E93E-46E1-8D5C-4675492E3263','潘总',1,'茂名',28,'很吊的经历，很叼','123123@qq.com','None','files/2017-06-29/fb856d12-5ce1-11e7-8d3a-00163e08b8b6.png',NULL,'files/2017-07-02/b8b47a76-5ee1-11e7-8d3a-00163e08b8b6.JPG',1,4,NULL,'1','2017-06-08 18:17:01','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-07-20 22:26:42','\0');

/*Table structure for table `U_UserLable` */

CREATE TABLE `U_UserLable` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(40) NOT NULL COMMENT 'U_User 表主键Id',
  `LableName` varchar(40) DEFAULT NULL COMMENT '标签',
  `Count` int(11) NOT NULL DEFAULT '1' COMMENT '数量',
  `Sort` int(11) NOT NULL DEFAULT '0' COMMENT '排序 越大越靠前',
  `CreateUserID` varchar(40) DEFAULT NULL COMMENT '创建用户',
  `CreateTime` datetime DEFAULT NULL COMMENT '创建时间',
  `ModifUserID` varchar(40) DEFAULT NULL COMMENT '修改人',
  `ModifTime` datetime DEFAULT NULL COMMENT '修改时间',
  `IsDelete` bit(1) DEFAULT b'0' COMMENT '是否删除',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='用户标签';

/*Data for the table `U_UserLable` */

insert  into `U_UserLable`(`Id`,`UserId`,`LableName`,`Count`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (1,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','帅',10000,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-08 18:19:23','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-08 18:19:26','\0');
insert  into `U_UserLable`(`Id`,`UserId`,`LableName`,`Count`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (2,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','酷',999,0,'FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-08 18:19:41','FD1E3DDC-E93E-46E1-8D5C-4675492E3263','2017-06-08 18:19:44','\0');
insert  into `U_UserLable`(`Id`,`UserId`,`LableName`,`Count`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (3,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','帅',1,0,'1','2017-06-14 18:37:56','1','2017-06-14 18:38:00','\0');
insert  into `U_UserLable`(`Id`,`UserId`,`LableName`,`Count`,`Sort`,`CreateUserID`,`CreateTime`,`ModifUserID`,`ModifTime`,`IsDelete`) values (4,'3C3C46F6-9D2B-4918-92D4-6BC1B669C85F','酷',2,1,'1','2017-06-14 18:38:15','1','2017-06-14 18:38:18','\0');

/* Procedure structure for procedure `pro_GetPermissions` */

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
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
