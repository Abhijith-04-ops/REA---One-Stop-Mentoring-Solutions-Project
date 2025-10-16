/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - rea
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`rea` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `rea`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add app_review',7,'add_app_review'),(20,'Can change app_review',7,'change_app_review'),(21,'Can delete app_review',7,'delete_app_review'),(22,'Can add chat',8,'add_chat'),(23,'Can change chat',8,'change_chat'),(24,'Can delete chat',8,'delete_chat'),(25,'Can add complaint',9,'add_complaint'),(26,'Can change complaint',9,'change_complaint'),(27,'Can delete complaint',9,'delete_complaint'),(28,'Can add diary',10,'add_diary'),(29,'Can change diary',10,'change_diary'),(30,'Can delete diary',10,'delete_diary'),(31,'Can add emotions',11,'add_emotions'),(32,'Can change emotions',11,'change_emotions'),(33,'Can delete emotions',11,'delete_emotions'),(34,'Can add login',12,'add_login'),(35,'Can change login',12,'change_login'),(36,'Can delete login',12,'delete_login'),(37,'Can add mentor',13,'add_mentor'),(38,'Can change mentor',13,'change_mentor'),(39,'Can delete mentor',13,'delete_mentor'),(40,'Can add mentor_review',14,'add_mentor_review'),(41,'Can change mentor_review',14,'change_mentor_review'),(42,'Can delete mentor_review',14,'delete_mentor_review'),(43,'Can add motivation',15,'add_motivation'),(44,'Can change motivation',15,'change_motivation'),(45,'Can delete motivation',15,'delete_motivation'),(46,'Can add request',16,'add_request'),(47,'Can change request',16,'change_request'),(48,'Can delete request',16,'delete_request'),(49,'Can add tips',17,'add_tips'),(50,'Can change tips',17,'change_tips'),(51,'Can delete tips',17,'delete_tips'),(52,'Can add user',18,'add_user'),(53,'Can change user',18,'change_user'),(54,'Can delete user',18,'delete_user'),(55,'Can add requests',16,'add_requests'),(56,'Can change requests',16,'change_requests'),(57,'Can delete requests',16,'delete_requests');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'REA_app','app_review'),(8,'REA_app','chat'),(9,'REA_app','complaint'),(10,'REA_app','diary'),(11,'REA_app','emotions'),(12,'REA_app','login'),(13,'REA_app','mentor'),(14,'REA_app','mentor_review'),(15,'REA_app','motivation'),(16,'REA_app','requests'),(17,'REA_app','tips'),(18,'REA_app','user'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'REA_app','0001_initial','2023-11-30 05:39:37'),(2,'contenttypes','0001_initial','2023-11-30 05:39:37'),(3,'auth','0001_initial','2023-11-30 05:39:37'),(4,'admin','0001_initial','2023-11-30 05:39:37'),(5,'admin','0002_logentry_remove_auto_add','2023-11-30 05:39:37'),(6,'contenttypes','0002_remove_content_type_name','2023-11-30 05:39:37'),(7,'auth','0002_alter_permission_name_max_length','2023-11-30 05:39:37'),(8,'auth','0003_alter_user_email_max_length','2023-11-30 05:39:37'),(9,'auth','0004_alter_user_username_opts','2023-11-30 05:39:37'),(10,'auth','0005_alter_user_last_login_null','2023-11-30 05:39:37'),(11,'auth','0006_require_contenttypes_0002','2023-11-30 05:39:37'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-30 05:39:37'),(13,'auth','0008_alter_user_username_max_length','2023-11-30 05:39:37'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-30 05:39:37'),(15,'sessions','0001_initial','2023-11-30 05:39:37'),(16,'REA_app','0002_app_review_rating','2023-11-30 07:18:17'),(17,'REA_app','0003_auto_20231209_1047','2023-12-09 05:17:20'),(18,'REA_app','0004_chat_type','2023-12-10 04:40:00'),(19,'REA_app','0005_auto_20240111_1411','2024-01-11 08:41:24'),(20,'REA_app','0006_auto_20240131_1117','2024-01-31 05:47:20'),(21,'REA_app','0007_auto_20240131_1119','2024-01-31 05:49:13');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('89tbhrreb5nqv6tmd4px1nn04tesmfes','NGViNDc2YjFmMGZlNzgwOTZlZjFmZDFlMzU1ZDY4NGU2MzY1OGJjMDp7ImxvZ2luaWQiOjQsImxpZCI6IiIsInVpZCI6IjEifQ==','2024-01-03 05:57:30'),('bd6pytyv8dixjrtdnjiyb9pu6zvnf3n8','YTAzNmMwNTc4NzczMmRiNTE1YWExMjk2Nzk4MWRlZjY5ODgyYTViNzp7ImxpZCI6Mn0=','2024-01-24 13:54:08'),('d06ntjl3qadg5ib09wflcwggaol81g0o','MThmYTc5MjkyYWUwYzgwNTZlZDY5NGJlN2JmYTAyMjI3MTlkZjBjMjp7ImxpZCI6MX0=','2024-01-09 11:47:30'),('fvo0rddgfyfpm8lkksdcqzu7yl4dwqgg','MThmYTc5MjkyYWUwYzgwNTZlZDY5NGJlN2JmYTAyMjI3MTlkZjBjMjp7ImxpZCI6MX0=','2024-01-09 06:19:15'),('na1hipfma0hadark24t3nbuudptj5ry9','YTNhNmZhNGU2OWQ4MTA1OTQ0ZWZmMGY3YzYyN2NhODA0MmJiYjc1Njp7ImxpZCI6IiIsInVpZCI6IjEifQ==','2024-02-22 08:43:38'),('te4oo1wma4o452xztu121lm4uxn7v8o0','YTAzNmMwNTc4NzczMmRiNTE1YWExMjk2Nzk4MWRlZjY5ODgyYTViNzp7ImxpZCI6Mn0=','2024-01-25 10:13:49');

/*Table structure for table `rea_app_app_review` */

DROP TABLE IF EXISTS `rea_app_app_review`;

CREATE TABLE `rea_app_app_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `rating` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_app_review_USER_id_d7fca349_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_app_review_USER_id_d7fca349_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_app_review` */

insert  into `rea_app_app_review`(`id`,`review`,`date`,`USER_id`,`rating`) values (1,'good','23',1,'5'),(2,'abcd','21/01/2024',1,'5.0'),(3,'as','21/01/2024',1,'5.0'),(4,'good','28/01/2024',1,'4.5'),(5,'gg','28/01/2024',1,'5.0');

/*Table structure for table `rea_app_chat` */

DROP TABLE IF EXISTS `rea_app_chat`;

CREATE TABLE `rea_app_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `MENTOR_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `type` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_chat_MENTOR_id_31f779aa_fk_REA_app_mentor_id` (`MENTOR_id`),
  KEY `REA_app_chat_USER_id_d323a4c1_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_chat_MENTOR_id_31f779aa_fk_REA_app_mentor_id` FOREIGN KEY (`MENTOR_id`) REFERENCES `rea_app_mentor` (`id`),
  CONSTRAINT `REA_app_chat_USER_id_d323a4c1_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_chat` */

insert  into `rea_app_chat`(`id`,`message`,`date`,`MENTOR_id`,`USER_id`,`type`) values (1,'hi','2024-01-28',3,1,'user'),(2,'wht','2024-01-28',1,1,'user'),(3,'hlo','2024-01-28',3,1,'mentor'),(4,'ss','2024-01-28',3,1,'user'),(5,'yess','2024-01-28',1,1,'mentor'),(6,'hlo','2024-01-28',1,1,'mentor'),(7,'','2024-01-30',1,1,'mentor'),(8,'','2024-01-30',1,1,'mentor'),(9,'','2024-01-30',1,1,'mentor'),(10,'','2024-01-31',1,1,'mentor'),(11,'h','2024-01-31',1,1,'mentor'),(12,'j','2024-01-31',1,1,'mentor');

/*Table structure for table `rea_app_complaint` */

DROP TABLE IF EXISTS `rea_app_complaint`;

CREATE TABLE `rea_app_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(200) NOT NULL,
  `Cdate` varchar(200) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `Rdate` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_complaint_USER_id_5bf7106e_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_complaint_USER_id_5bf7106e_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_complaint` */

insert  into `rea_app_complaint`(`id`,`complaint`,`Cdate`,`reply`,`Rdate`,`USER_id`) values (1,'dee','22','ok daa','2024-01-23',1),(2,'nice','23/01/2024-15/08/17','','',1),(3,'abc','23/01/2024-15/10/30','ok ok','2024-02-08',1),(4,'hi','23/01/2024-15/16/36','pending','',1);

/*Table structure for table `rea_app_diary` */

DROP TABLE IF EXISTS `rea_app_diary`;

CREATE TABLE `rea_app_diary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(2000) NOT NULL,
  `emotion` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `date` varchar(200) NOT NULL,
  `time` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_diary_USER_id_ad69b4ed_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_diary_USER_id_ad69b4ed_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_diary` */

insert  into `rea_app_diary`(`id`,`content`,`emotion`,`USER_id`,`date`,`time`) values (27,'Today was a beautiful day filled with joy and happiness. I woke up feeling refreshed and ready to take on the day. The sun was shining, the birds were chirping, and everything just felt right.\n\nI had ','joy',1,'31-01-2024','11:09:44'),(28,'Today has been an emotional roller coaster, and I find myself overwhelmed by the intensity of my feelings. It’s as if my heart has become a raging storm, with emotions swirling and crashing against th','anticipation',1,'31-01-2024','11:10:49'),(29,'Today was a really tough day. I woke up feeling a deep sadness that seemed to grip me from the inside out. Everything felt heavy and overwhelming, and I didn’t have the energy or motivation to do much','sadness',1,'31-01-2024','11:12:23'),(30,'Today is Valentine’s Day, and I feel so grateful to have such an amazing partner in my life. We started the day with breakfast in bed, and my partner surprised me with a beautiful bouquet of roses and','joy',1,'31-01-2024','11:12:44'),(32,'Today is Halloween, and I’m feeling really anxious about going out tonight. I love dressing up and going to parties, but this year feels different. With all the recent reports of violence and crime in','fear',1,'31-01-2024','11:13:48'),(33,'Today is Halloween, and I’m feeling really anxious about going out tonight. I love dressing up and going to parties, but this year feels different. With all the recent reports of violence and crime in the area, I’m scared for my safety.\n\nI keep replaying worst-case scenarios in my head, imagining all the ways things could go wrong. What if I get mugged? What if someone attacks me? What if there’s a shooting? The fear is overwhelming, and I don’t know how to shake it.\n\nI’ve tried talking to frien','fear',1,'31-01-2024','11:17:35');

/*Table structure for table `rea_app_emotions` */

DROP TABLE IF EXISTS `rea_app_emotions`;

CREATE TABLE `rea_app_emotions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `emotion` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_emotions_USER_id_89876fa6_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_emotions_USER_id_89876fa6_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_emotions` */

/*Table structure for table `rea_app_login` */

DROP TABLE IF EXISTS `rea_app_login`;

CREATE TABLE `rea_app_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_login` */

insert  into `rea_app_login`(`id`,`username`,`usertype`,`password`) values (1,'admin','admin','12345'),(2,'mentor','mentor','12345'),(3,'user','user','12345678'),(4,'ment','pending','12345'),(5,'anf@124','mentor','12345'),(11,'edwin ','user','12e45678'),(17,'ajsj123@gmail.com','user','12345678');

/*Table structure for table `rea_app_mentor` */

DROP TABLE IF EXISTS `rea_app_mentor`;

CREATE TABLE `rea_app_mentor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_mentor_LOGIN_id_f9dcaba7_fk_REA_app_login_id` (`LOGIN_id`),
  CONSTRAINT `REA_app_mentor_LOGIN_id_f9dcaba7_fk_REA_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `rea_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_mentor` */

insert  into `rea_app_mentor`(`id`,`photo`,`name`,`email`,`phone`,`gender`,`LOGIN_id`) values (1,'','Abhijith','s',1234567891,'Male',2),(2,'/static/mentor_photo/20231209-095436.jpg','mentor1','ment',123456777,'Male',4),(3,'/static/mentor_photo/20231226-171707.jpg','abc','anf@124',123,'Male',5);

/*Table structure for table `rea_app_mentor_review` */

DROP TABLE IF EXISTS `rea_app_mentor_review`;

CREATE TABLE `rea_app_mentor_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(300) NOT NULL,
  `date` varchar(200) NOT NULL,
  `MENTOR_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_mentor_review_MENTOR_id_1d022ad9_fk_REA_app_mentor_id` (`MENTOR_id`),
  KEY `REA_app_mentor_review_USER_id_da83a2d5_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_mentor_review_MENTOR_id_1d022ad9_fk_REA_app_mentor_id` FOREIGN KEY (`MENTOR_id`) REFERENCES `rea_app_mentor` (`id`),
  CONSTRAINT `REA_app_mentor_review_USER_id_da83a2d5_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_mentor_review` */

insert  into `rea_app_mentor_review`(`id`,`review`,`date`,`MENTOR_id`,`USER_id`) values (1,'good','21',3,1),(2,'great','21/01/2024',3,1);

/*Table structure for table `rea_app_motivation` */

DROP TABLE IF EXISTS `rea_app_motivation`;

CREATE TABLE `rea_app_motivation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `MENTOR_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_motivation_MENTOR_id_6d806e95_fk_REA_app_mentor_id` (`MENTOR_id`),
  CONSTRAINT `REA_app_motivation_MENTOR_id_6d806e95_fk_REA_app_mentor_id` FOREIGN KEY (`MENTOR_id`) REFERENCES `rea_app_mentor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_motivation` */

insert  into `rea_app_motivation`(`id`,`content`,`title`,`date`,`MENTOR_id`) values (2,'abcddd','a','20231209-103639',2),(4,'abc','a','20231226-153240',1),(5,'','a','20231226-153321',2),(6,'','b','20231226-153339',1),(7,'sd','abc','20231226-153606',1),(8,'','','20231226-153801',1),(10,'abcde','abc','20240121-112734',3);

/*Table structure for table `rea_app_requests` */

DROP TABLE IF EXISTS `rea_app_requests`;

CREATE TABLE `rea_app_requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `MENTOR_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_request_MENTOR_id_ec57ea40_fk_REA_app_mentor_id` (`MENTOR_id`),
  KEY `REA_app_request_USER_id_651309ea_fk_REA_app_user_id` (`USER_id`),
  CONSTRAINT `REA_app_request_MENTOR_id_ec57ea40_fk_REA_app_mentor_id` FOREIGN KEY (`MENTOR_id`) REFERENCES `rea_app_mentor` (`id`),
  CONSTRAINT `REA_app_request_USER_id_651309ea_fk_REA_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `rea_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_requests` */

insert  into `rea_app_requests`(`id`,`status`,`date`,`MENTOR_id`,`USER_id`) values (5,'approve','21/01/2024-11:20:13',3,1),(6,'approve','27/01/2024-13:38:09',1,1);

/*Table structure for table `rea_app_tips` */

DROP TABLE IF EXISTS `rea_app_tips`;

CREATE TABLE `rea_app_tips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tip` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `MENTOR_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_tips_MENTOR_id_4bb812be_fk_REA_app_mentor_id` (`MENTOR_id`),
  CONSTRAINT `REA_app_tips_MENTOR_id_4bb812be_fk_REA_app_mentor_id` FOREIGN KEY (`MENTOR_id`) REFERENCES `rea_app_mentor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_tips` */

insert  into `rea_app_tips`(`id`,`tip`,`date`,`MENTOR_id`) values (3,'abc','20231209-102751',2),(4,'abc','20231226-153259',1),(5,'av','20231226-153351',1),(6,'abc','20240121-112109',3);

/*Table structure for table `rea_app_user` */

DROP TABLE IF EXISTS `rea_app_user`;

CREATE TABLE `rea_app_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `REA_app_user_LOGIN_id_5ef513f6_fk_REA_app_login_id` (`LOGIN_id`),
  CONSTRAINT `REA_app_user_LOGIN_id_5ef513f6_fk_REA_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `rea_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `rea_app_user` */

insert  into `rea_app_user`(`id`,`photo`,`name`,`email`,`phone`,`gender`,`LOGIN_id`) values (1,'/static/user/20240123-141134.jpg','pappan','ahsbs@gmail.com',1234567891,'Female',3),(7,'/static/mentor_photo/20231226-171707.jpg','abc','abc@gmail.com',123456789,'Male',1),(13,'1706443142900.png','edwin','edwin ',1234567891,'Male',1),(14,'1707368478751.png','pinky','pinky123gmail.com',1234567891,'Male',1),(15,'1707368697607.png','abhijith','abhijith123@gmail.com',1234567890,'Male',1),(16,'1707369477106.png','abc','abc123gmail.com',1234567891,'Male',1),(17,'1707370071537.png','abdndnd','abc1',1234567891,'Male',1),(18,'1707370116534.png','abdhddh','abc1',1234567891,'Male',1),(19,'1707370734868.png','ahsnsnx','ajsj123@gmail.com',1234567891,'Male',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
