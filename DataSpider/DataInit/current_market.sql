/*
Navicat MySQL Data Transfer

Source Server         : STOCK
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : stock_1.0

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-05-15 09:53:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for current_market
-- ----------------------------
DROP TABLE IF EXISTS `current_market`;
CREATE TABLE `current_market` (
  `index` bigint(20) DEFAULT NULL,
  `code` text,
  `name` text,
  `changepercent` double DEFAULT NULL,
  `trade` double DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `settlement` double DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL,
  `turnoverratio` double DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `per` double DEFAULT NULL,
  `pb` double DEFAULT NULL,
  `mktcap` double DEFAULT NULL,
  `nmc` double DEFAULT NULL,
  KEY `ix_current_market_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
