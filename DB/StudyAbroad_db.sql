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

/*Table structure for table `Sys_P_Role` */

CREATE TABLE `Sys_P_Role` (
  `RoleId` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `RoleName` varchar(30) NOT NULL COMMENT '角色名称',
  `Remark` varchar(150) DEFAULT NULL COMMENT '描述',
  `CreateDate` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`RoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_P_RolePermission` */

CREATE TABLE `Sys_P_RolePermission` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RoleId` int(11) NOT NULL COMMENT '角色Id',
  `PermissionId` int(11) NOT NULL COMMENT '权限Id',
  `Scope` int(11) NOT NULL DEFAULT '0' COMMENT '数据范围,0:个人,1:部门,2,全局',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8;

/*Table structure for table `Sys_P_UserRole` */

CREATE TABLE `Sys_P_UserRole` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(40) NOT NULL COMMENT '用户id',
  `RoleId` int(11) NOT NULL COMMENT '角色id',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

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

/*Table structure for table `U_BrowseRecord` */

CREATE TABLE `U_BrowseRecord` (
  `UserId` varchar(40) NOT NULL COMMENT '浏览人ID',
  `DemandServiceId` varchar(40) NOT NULL COMMENT '浏览的需求服务ID',
  `BrowseTime` datetime DEFAULT NULL COMMENT '浏览时间',
  PRIMARY KEY (`UserId`,`DemandServiceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='浏览记录';

/*Table structure for table `U_Collection` */

CREATE TABLE `U_Collection` (
  `UserId` varchar(40) NOT NULL COMMENT '收藏人ID',
  `DemandServiceId` varchar(40) NOT NULL COMMENT '被收藏的需求服务ID',
  `CollectionTime` datetime DEFAULT NULL COMMENT '收藏时间',
  PRIMARY KEY (`UserId`,`DemandServiceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='收藏表';

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

/*Table structure for table `U_Follow` */

CREATE TABLE `U_Follow` (
  `UserId` varchar(40) NOT NULL COMMENT '关注人ID',
  `FollwUserId` varchar(40) NOT NULL COMMENT '被关注的用户ID',
  `FollwTime` datetime DEFAULT NULL COMMENT '关注时间',
  PRIMARY KEY (`UserId`,`FollwUserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
