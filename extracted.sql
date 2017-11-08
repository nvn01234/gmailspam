/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : gmail

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-11-09 01:01:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for extracted
-- ----------------------------
DROP TABLE IF EXISTS `extracted`;
CREATE TABLE `extracted` (
  `data_set` varchar(255) DEFAULT NULL,
  `raw` longtext,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tokenize` longtext,
  `lang` varchar(255) DEFAULT NULL,
  `normalized` longtext,
  `label` varchar(255) DEFAULT NULL,
  `numOfLink` int(11) DEFAULT NULL,
  `numOfImage` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6296 DEFAULT CHARSET=utf8;
