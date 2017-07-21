-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: rmt
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add menu',7,'add_menu'),(20,'Can change menu',7,'change_menu'),(21,'Can delete menu',7,'delete_menu'),(22,'Can add role',8,'add_role'),(23,'Can change role',8,'change_role'),(24,'Can delete role',8,'delete_role'),(25,'Can add role config',9,'add_roleconfig'),(26,'Can change role config',9,'change_roleconfig'),(27,'Can delete role config',9,'delete_roleconfig'),(28,'Can add role menu',10,'add_rolemenu'),(29,'Can change role menu',10,'change_rolemenu'),(30,'Can delete role menu',10,'delete_rolemenu'),(31,'Can add client',11,'add_client'),(32,'Can change client',11,'change_client'),(33,'Can delete client',11,'delete_client'),(34,'Can add requirement',12,'add_requirement'),(35,'Can change requirement',12,'change_requirement'),(36,'Can delete requirement',12,'delete_requirement'),(37,'Can add resume management',13,'add_resumemanagement'),(38,'Can change resume management',13,'change_resumemanagement'),(39,'Can delete resume management',13,'delete_resumemanagement'),(40,'Can add hr management',14,'add_hrmanagement'),(41,'Can change hr management',14,'change_hrmanagement'),(42,'Can delete hr management',14,'delete_hrmanagement'),(43,'Can add user profile',15,'add_userprofile'),(44,'Can change user profile',15,'change_userprofile'),(45,'Can delete user profile',15,'delete_userprofile'),(46,'Can add interview schedule',16,'add_interviewschedule'),(47,'Can change interview schedule',16,'change_interviewschedule'),(48,'Can delete interview schedule',16,'delete_interviewschedule');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Ru3hWkr0uhs1$QdIKtpi61e4vd7ZcNrQoBMk9LUuFOxXCIzyFkNoeSys=','2017-07-20 07:01:29',1,'rmt@brisatech.com','Subodh','Kar','rmt@brisatech.com',1,1,'2017-07-06 09:32:44'),(2,'pbkdf2_sha256$12000$C34BRepckUdS$GYkQL8HtBg3izNSybhelsCsDK4O1ETtEMNIGuhHxiRU=','2017-07-18 11:20:29',0,'ta@brisatech.com','Talent','Acquisition','ta@brisatech.com',1,1,'2017-07-11 12:22:35'),(3,'pbkdf2_sha256$12000$HCRH1UIsG8oX$1pevk4ITDlGyFpF3kU0ZCvF1CE/JXO7JSWS4q2KhuT4=','2017-07-20 07:01:16',0,'hr@brisatech.com','HR','Brisa Tech','hr@brisatech.com',1,1,'2017-07-12 04:36:26'),(4,'pbkdf2_sha256$12000$KRLhmnLsMhzF$BfSvwmaAd9FMxrk6zNY8AALtXA7zW66R+0lIqLMgaT0=','2017-07-12 11:11:27',0,'felix.stephen@brisatech.com','Felix','Stephen','felix.stephen@brisatech.com',0,1,'2017-07-12 11:11:27'),(7,'pbkdf2_sha256$12000$iUc4eSSjRZzZ$hL6K2y0BNUiRaJGJb/FLQVQPKanyPPqPzkf7aRLSXCg=','2017-07-13 09:26:01',0,'test@test.com','test','test','test@test.com',1,1,'2017-07-12 12:10:52');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-07-06 09:40:35',1,7,'1',' - ',1,''),(2,'2017-07-06 09:40:42',1,7,'1',' - ',3,''),(3,'2017-07-06 10:05:42',1,4,'1','rmt@brisatech.com',2,'Changed first_name and last_name.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'menu','rolemgmt','menu'),(8,'role','rolemgmt','role'),(9,'role config','rolemgmt','roleconfig'),(10,'role menu','rolemgmt','rolemenu'),(11,'client','rmtmgmt','client'),(12,'requirement','rmtmgmt','requirement'),(13,'resume management','rmtmgmt','resumemanagement'),(14,'hr management','rmtmgmt','hrmanagement'),(15,'user profile','rmtmgmt','userprofile'),(16,'interview schedule','rmtmgmt','interviewschedule');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4sl549k154luqfjh4zm5qghki8eerc52','MTgxNmU3NWQ3NWFmZDQwYmY0Nzc5MmZlYmRhZTkyZTBjZDhkMzMxZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2017-07-24 11:27:01'),('c1gtthvi39tlnh0xltiefrum917qbxha','MTgxNmU3NWQ3NWFmZDQwYmY0Nzc5MmZlYmRhZTkyZTBjZDhkMzMxZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2017-08-03 07:01:29'),('izjsvndohe7qwg5zlhv6xbkea060r62l','YTBiMmUyOTYyMmZmZTFhYWZiNDk3NzQxY2IzYTM1ZWJiZTUwMDI4Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2017-08-01 11:20:29');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_client`
--

DROP TABLE IF EXISTS `rmtmgmt_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` longtext,
  `location` varchar(100) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `rmtmgmt_client_0c98d849` (`created_by_id`),
  CONSTRAINT `created_by_id_refs_id_a819727c` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_client`
--

LOCK TABLES `rmtmgmt_client` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_client` DISABLE KEYS */;
INSERT INTO `rmtmgmt_client` VALUES (1,'2017-07-20 12:04:00','2017-07-20 12:04:00','DELL','DELL - Bangalore','Bangalore',1,1),(2,'2017-07-20 12:04:22','2017-07-20 12:04:22','San Disk','San Disk - Bangalore','Bangalore',1,1);
/*!40000 ALTER TABLE `rmtmgmt_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_hrmanagement`
--

DROP TABLE IF EXISTS `rmtmgmt_hrmanagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_hrmanagement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `resume_id` int(11) DEFAULT NULL,
  `offered_ctc` varchar(50) DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  `remarks` longtext,
  `approval_status` int(11) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `approved_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rmtmgmt_hrmanagement_dd710737` (`resume_id`),
  KEY `rmtmgmt_hrmanagement_0c98d849` (`created_by_id`),
  KEY `rmtmgmt_hrmanagement_64fcc5c2` (`approved_by_id`),
  CONSTRAINT `approved_by_id_refs_id_7261e006` FOREIGN KEY (`approved_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `created_by_id_refs_id_7261e006` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `resume_id_refs_id_7aaddd7b` FOREIGN KEY (`resume_id`) REFERENCES `rmtmgmt_resumemanagement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_hrmanagement`
--

LOCK TABLES `rmtmgmt_hrmanagement` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_hrmanagement` DISABLE KEYS */;
INSERT INTO `rmtmgmt_hrmanagement` VALUES (1,'2017-07-21 08:47:15','2017-07-21 08:49:45',1,'200000','2017-07-23','Approved by Subodh',2,1,1),(2,'2017-07-21 09:03:22','2017-07-21 09:04:16',3,'5000000','2017-07-23','I am approving',2,1,1),(3,'2017-07-21 09:14:42','2017-07-21 09:14:52',2,NULL,NULL,'done',2,1,1),(4,'2017-07-21 09:55:38','2017-07-21 10:36:31',4,NULL,NULL,'sgfd',2,1,1),(5,'2017-07-21 10:44:59','2017-07-21 11:13:34',5,'100000','2017-07-31',NULL,1,1,NULL);
/*!40000 ALTER TABLE `rmtmgmt_hrmanagement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_interviewschedule`
--

DROP TABLE IF EXISTS `rmtmgmt_interviewschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_interviewschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `requirement_id` int(11) DEFAULT NULL,
  `scheduled_by_id` int(11) DEFAULT NULL,
  `approved_by_id` int(11) DEFAULT NULL,
  `scheduled_date` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `resume_status` int(11) DEFAULT NULL,
  `remarks1` longtext,
  `remarks2` longtext,
  PRIMARY KEY (`id`),
  KEY `rmtmgmt_interviewschedule_4ff051c7` (`candidate_id`),
  KEY `rmtmgmt_interviewschedule_19c1813d` (`requirement_id`),
  KEY `rmtmgmt_interviewschedule_f7fb45fd` (`scheduled_by_id`),
  KEY `rmtmgmt_interviewschedule_64fcc5c2` (`approved_by_id`),
  CONSTRAINT `approved_by_id_refs_id_607607e8` FOREIGN KEY (`approved_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `candidate_id_refs_id_15338d4c` FOREIGN KEY (`candidate_id`) REFERENCES `rmtmgmt_resumemanagement` (`id`),
  CONSTRAINT `requirement_id_refs_id_10976d9d` FOREIGN KEY (`requirement_id`) REFERENCES `rmtmgmt_requirement` (`id`),
  CONSTRAINT `scheduled_by_id_refs_id_607607e8` FOREIGN KEY (`scheduled_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_interviewschedule`
--

LOCK TABLES `rmtmgmt_interviewschedule` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_interviewschedule` DISABLE KEYS */;
INSERT INTO `rmtmgmt_interviewschedule` VALUES (7,'2017-07-21 08:44:42','2017-07-21 08:44:42',1,1,1,1,NULL,2,2,'got selected by felix',NULL),(8,'2017-07-21 08:45:49','2017-07-21 08:45:49',1,1,1,1,NULL,2,3,'got selected by neha',NULL),(9,'2017-07-21 08:47:15','2017-07-21 08:47:15',1,1,1,1,NULL,2,4,'COL is needs to be approved',NULL),(10,'2017-07-21 09:02:56','2017-07-21 09:02:56',3,1,1,1,NULL,2,2,'Got Selected by ashock',NULL),(11,'2017-07-21 09:03:11','2017-07-21 09:03:11',3,1,1,1,NULL,2,3,'Got selected by felix',NULL),(12,'2017-07-21 09:03:21','2017-07-21 09:03:21',3,1,1,1,NULL,2,4,'Waiting for Approval',NULL),(13,'2017-07-21 09:05:02','2017-07-21 09:05:02',3,1,1,1,NULL,2,5,'Got selected in client short listing',NULL),(14,'2017-07-21 09:14:01','2017-07-21 09:14:01',2,1,1,1,NULL,2,2,'T-con',NULL),(15,'2017-07-21 09:14:18','2017-07-21 09:14:18',2,1,1,1,NULL,2,3,'ghdvhjvdf',NULL),(16,'2017-07-21 09:14:42','2017-07-21 09:14:42',2,1,1,1,NULL,2,4,'accepted',NULL),(17,'2017-07-21 09:44:27','2017-07-21 09:44:27',4,1,1,1,NULL,2,2,'Got selected',NULL),(18,'2017-07-21 09:44:42','2017-07-21 09:44:42',4,1,1,1,NULL,2,3,'Got Selected by Ashock',NULL),(19,'2017-07-21 09:55:38','2017-07-21 09:55:38',4,1,1,1,NULL,2,4,'Yes got approved',NULL),(20,'2017-07-21 10:44:33','2017-07-21 10:44:34',5,2,1,1,NULL,2,2,'Good',NULL),(21,'2017-07-21 10:44:48','2017-07-21 10:44:48',5,2,1,1,NULL,2,3,'Take up for next level',NULL),(22,'2017-07-21 10:44:59','2017-07-21 10:44:59',5,2,1,1,NULL,2,4,'Got Approved',NULL),(23,'2017-07-21 11:19:05','2017-07-21 11:19:05',5,2,1,1,NULL,2,5,'got',NULL),(24,'2017-07-21 11:23:41','2017-07-21 11:23:41',5,2,1,1,NULL,2,6,'jhgvujf',NULL),(25,'2017-07-21 11:23:50','2017-07-21 11:23:50',5,2,1,1,NULL,2,7,'hfdf',NULL),(26,'2017-07-21 11:24:21','2017-07-21 11:24:21',5,2,1,1,NULL,2,8,'hfthyfef',NULL);
/*!40000 ALTER TABLE `rmtmgmt_interviewschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_requirement`
--

DROP TABLE IF EXISTS `rmtmgmt_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_requirement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `client_id` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `position_name` varchar(100) NOT NULL,
  `desc` longtext,
  `skills` varchar(200) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `no_of_position` int(10) unsigned DEFAULT NULL,
  `open_position` int(10) unsigned DEFAULT NULL,
  `location` varchar(200) NOT NULL,
  `position_status` int(11) NOT NULL,
  `min_exp` varchar(50) NOT NULL,
  `annual_billing` varchar(100) NOT NULL,
  `remarks` longtext,
  `created_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rmtmgmt_requirement_4fea5d6a` (`client_id`),
  KEY `rmtmgmt_requirement_0c98d849` (`created_by_id`),
  CONSTRAINT `client_id_refs_id_08388b46` FOREIGN KEY (`client_id`) REFERENCES `rmtmgmt_client` (`id`),
  CONSTRAINT `created_by_id_refs_id_28066e9a` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_requirement`
--

LOCK TABLES `rmtmgmt_requirement` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_requirement` DISABLE KEYS */;
INSERT INTO `rmtmgmt_requirement` VALUES (1,'2017-07-20 12:07:14','2017-07-21 10:27:16',1,'DELL-Bangalore','Automation Engineer','We required people who know very well in Perl','Python, SAS, Selenium','3 Y',10,5,'Bangalore',1,'2 Y','20 L','Bring peoples from BangPyer\'s',NULL),(2,'2017-07-21 10:42:59','2017-07-21 10:42:59',2,'SD-New Generation','Automation Test Engineer','Python Automation - Selenium ','SAS / Python / Django / Perl','4 Y',20,10,'Bangalore',1,'2 Y','50 L','Good candidates are required',NULL);
/*!40000 ALTER TABLE `rmtmgmt_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_resumemanagement`
--

DROP TABLE IF EXISTS `rmtmgmt_resumemanagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_resumemanagement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `requirement_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(75) DEFAULT NULL,
  `mobile` varchar(50) DEFAULT NULL,
  `skills` varchar(200) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `ctc` varchar(20) NOT NULL,
  `ectc` varchar(20) NOT NULL,
  `notice_period` varchar(20) DEFAULT NULL,
  `current_location` varchar(100) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `remarks` longtext,
  `resume` varchar(100) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rmtmgmt_resumemanagement_19c1813d` (`requirement_id`),
  KEY `rmtmgmt_resumemanagement_0c98d849` (`created_by_id`),
  CONSTRAINT `created_by_id_refs_id_d00da3d2` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `requirement_id_refs_id_7c4ad77b` FOREIGN KEY (`requirement_id`) REFERENCES `rmtmgmt_requirement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_resumemanagement`
--

LOCK TABLES `rmtmgmt_resumemanagement` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_resumemanagement` DISABLE KEYS */;
INSERT INTO `rmtmgmt_resumemanagement` VALUES (1,'2017-07-20 12:10:26','2017-07-21 08:47:15',1,'Felix','Stephen','felix.stephen@brisatech.com','9590314151','Python / Django / HTML','2 Y','2018-08-21','4L','7L','2D','Bangalore',4,'He is good at in Python','static/uploads/Python_Debugger_Cheatsheet.pdf',NULL),(2,'2017-07-21 08:54:43','2017-07-21 09:14:42',1,'Ashock','Kumar','ashock.kumar@brisatech.com','1234567890','Python / Django / Selenium','4 Y','2017-06-01','6L','15L','2 M','Bangalore',4,'','static/uploads/Felix_Stephen_offer_4',NULL),(3,'2017-07-21 09:02:40','2017-07-21 09:05:02',1,'Stephen','Felix','stephen.felix@gmail.com','0987654321','python / django','4Y','2017-08-31','7L','10L','2 M','Bangalore',5,'','static/uploads/Revanth_offer_1.pdf',NULL),(4,'2017-07-21 09:44:16','2017-07-21 09:55:38',1,'Ramesh','BG','ramesh@brisatech.com','1234567890','Python / Django','3 Y','1980-08-02','4 L','15 L','2 Month','Bangalore',4,'','static/uploads/Felix_Stephen_offer_4_1',NULL),(5,'2017-07-21 10:44:23','2017-07-21 11:24:21',2,'Test Sandisk','Sandisk','snadisk@test.com','1234567890','Python / Django / Shell Scripting','2 Y','2000-08-08','4 L','10 L','1 M','Bangalore',8,'','static/uploads/Felix_Stephen_offer_4_2',NULL);
/*!40000 ALTER TABLE `rmtmgmt_resumemanagement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmtmgmt_userprofile`
--

DROP TABLE IF EXISTS `rmtmgmt_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmtmgmt_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `approved_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rmtmgmt_userprofile_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_793dc52e` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmtmgmt_userprofile`
--

LOCK TABLES `rmtmgmt_userprofile` WRITE;
/*!40000 ALTER TABLE `rmtmgmt_userprofile` DISABLE KEYS */;
INSERT INTO `rmtmgmt_userprofile` VALUES (1,'2017-07-12 12:10:53','2017-07-12 12:10:53',7,'9590315151',NULL);
/*!40000 ALTER TABLE `rmtmgmt_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolemgmt_menu`
--

DROP TABLE IF EXISTS `rolemgmt_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolemgmt_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `active` int(11) NOT NULL,
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rolemgmt_menu_f52cfca0` (`slug`),
  KEY `rolemgmt_menu_410d0aac` (`parent_id`),
  CONSTRAINT `parent_id_refs_id_6fecd953` FOREIGN KEY (`parent_id`) REFERENCES `rolemgmt_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolemgmt_menu`
--

LOCK TABLES `rolemgmt_menu` WRITE;
/*!40000 ALTER TABLE `rolemgmt_menu` DISABLE KEYS */;
INSERT INTO `rolemgmt_menu` VALUES (1,'2017-07-07 09:06:30','2017-07-07 09:06:30','Resume Management','resume-management',NULL,'resume-management',2,0),(2,'2017-07-07 09:06:39','2017-07-07 09:06:39','Requirement Management','requirement-management',NULL,'requirement-management',2,1),(3,'2017-07-07 09:06:47','2017-07-07 09:06:47','HR Management','hr-management',NULL,'hr-management',2,2),(4,'2017-07-07 09:06:54','2017-07-07 09:06:54','Role Management','role-management',NULL,'role-management',2,3),(5,'2017-07-07 09:07:08','2017-07-07 09:07:08','Reports','reports',NULL,'reports',2,6),(6,'2017-07-12 05:29:15','2017-07-12 05:29:15','Approvals','approvals',NULL,'approvals',2,4),(7,'2017-07-12 06:16:37','2017-07-12 06:16:37','Interview Schedule','interview-schedule',NULL,'interview-schedule',2,5);
/*!40000 ALTER TABLE `rolemgmt_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolemgmt_role`
--

DROP TABLE IF EXISTS `rolemgmt_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolemgmt_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `active` int(11) NOT NULL,
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rolemgmt_role_f52cfca0` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolemgmt_role`
--

LOCK TABLES `rolemgmt_role` WRITE;
/*!40000 ALTER TABLE `rolemgmt_role` DISABLE KEYS */;
INSERT INTO `rolemgmt_role` VALUES (1,'2017-07-07 09:29:36','2017-07-07 09:29:36','RMT Admin','rmt-admin','rmt-admin',2,0),(2,'2017-07-07 09:30:04','2017-07-07 09:30:04','Human Resource Manager','human-resource-manager','human-resource-manager',2,1),(3,'2017-07-07 09:30:43','2017-07-07 09:30:43','Business Analysist','business-analysist','business-analysist',2,2),(4,'2017-07-07 09:31:11','2017-07-07 09:31:11','Talent Acquisition','talent-acquisition','talent-acquisition',2,3);
/*!40000 ALTER TABLE `rolemgmt_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolemgmt_roleconfig`
--

DROP TABLE IF EXISTS `rolemgmt_roleconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolemgmt_roleconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `active` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rolemgmt_roleconfig_6340c63c` (`user_id`),
  KEY `rolemgmt_roleconfig_278213e1` (`role_id`),
  CONSTRAINT `role_id_refs_id_fe8ecb9a` FOREIGN KEY (`role_id`) REFERENCES `rolemgmt_role` (`id`),
  CONSTRAINT `user_id_refs_id_bcf6b9ee` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolemgmt_roleconfig`
--

LOCK TABLES `rolemgmt_roleconfig` WRITE;
/*!40000 ALTER TABLE `rolemgmt_roleconfig` DISABLE KEYS */;
INSERT INTO `rolemgmt_roleconfig` VALUES (1,'2017-07-07 09:37:12','2017-07-07 09:37:12',1,1,2),(2,'2017-07-11 12:25:17','2017-07-11 12:25:17',2,4,2),(3,'2017-07-12 04:42:31','2017-07-12 04:42:31',3,2,2),(4,'2017-07-13 11:00:24','2017-07-18 11:07:14',7,3,2);
/*!40000 ALTER TABLE `rolemgmt_roleconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolemgmt_rolemenu`
--

DROP TABLE IF EXISTS `rolemgmt_rolemenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolemgmt_rolemenu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_on` datetime NOT NULL,
  `modified_on` datetime NOT NULL,
  `role_id` int(11) NOT NULL,
  `active` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rolemgmt_rolemenu_278213e1` (`role_id`),
  CONSTRAINT `role_id_refs_id_5557612a` FOREIGN KEY (`role_id`) REFERENCES `rolemgmt_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolemgmt_rolemenu`
--

LOCK TABLES `rolemgmt_rolemenu` WRITE;
/*!40000 ALTER TABLE `rolemgmt_rolemenu` DISABLE KEYS */;
INSERT INTO `rolemgmt_rolemenu` VALUES (1,'2017-07-07 09:34:41','2017-07-07 09:34:41',1,2),(2,'2017-07-11 12:34:51','2017-07-11 12:35:46',4,2),(3,'2017-07-12 04:41:35','2017-07-12 04:41:35',2,2);
/*!40000 ALTER TABLE `rolemgmt_rolemenu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolemgmt_rolemenu_menu`
--

DROP TABLE IF EXISTS `rolemgmt_rolemenu_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolemgmt_rolemenu_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rolemenu_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rolemenu_id` (`rolemenu_id`,`menu_id`),
  KEY `rolemgmt_rolemenu_menu_418d072b` (`rolemenu_id`),
  KEY `rolemgmt_rolemenu_menu_08fd5523` (`menu_id`),
  CONSTRAINT `menu_id_refs_id_fc8c6ac0` FOREIGN KEY (`menu_id`) REFERENCES `rolemgmt_menu` (`id`),
  CONSTRAINT `rolemenu_id_refs_id_8f030d44` FOREIGN KEY (`rolemenu_id`) REFERENCES `rolemgmt_rolemenu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolemgmt_rolemenu_menu`
--

LOCK TABLES `rolemgmt_rolemenu_menu` WRITE;
/*!40000 ALTER TABLE `rolemgmt_rolemenu_menu` DISABLE KEYS */;
INSERT INTO `rolemgmt_rolemenu_menu` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(10,1,6),(11,1,7),(6,2,1),(7,3,1),(8,3,2),(9,3,3);
/*!40000 ALTER TABLE `rolemgmt_rolemenu_menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-21 16:58:25
