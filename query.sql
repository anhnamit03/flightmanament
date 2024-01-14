CREATE DATABASE  IF NOT EXISTS `flightmanament` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flightmanament`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: flightmanament
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `sign` varchar(5) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `longitude` float DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES ('HAN','Nội Bài','Phú Minh, Sóc Sơn, Hà Nội',10.8163,106.664,1),('SGN','Tân Sơn Nhất','Trường Sơn, Phường 2, Tân Bình, Thành phố Hồ Chí Minh',21.2178,105.793,2),('DAD','Đà Nẵng','Nguyễn Văn Linh, Hòa Thuận Tây, Hải Châu, Đà Nẵng',16.0556,108.202,3),('BMV','Buôn Ma Thuột','100 Đam San, Hoà Thắng, Thành phố Buôn Ma Thuột, Đắk Lắk',12.6648,108.118,4),('VCA','Trà Nóc','179B Lê Hồng Phong, Long Hoà, Bình Thủy, Cần Thơ',10.0807,105.712,5),('VCL','Chu Lai','Tam Nghĩa, Núi Thành, Quảng Nam',15.4148,108.704,6),('DLI','Liên Khương','Liên Nghĩa, Đức Trọng, Lâm Đồng',11.7489,108.368,7),('HUI','Phú Bài','TT. Phú Bài, Hương Thủy, Thừa Thiên Huế',16.3979,107.7,8),('CXR','Cam Ranh','Nguyễn Tất Thành, Cam Nghĩa, Cam Lâm, Khánh Hòa',11.9983,109.219,9),('VDO','Vân Đồn','Đoàn Kết, Vân Đồn, Quảng Ninh',21.1205,107.416,10);
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `name` varchar(255) DEFAULT NULL,
  `CCCD` varchar(12) NOT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `birthday` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CCCD` (`CCCD`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('Trịnh Tấn S','012345678910',1,'0987654321','2051052115si@ou.edu.vn','28/11/2002',1),('Hoàng Văn N','001122334455',1,'0123456789','2051052084nam@ou.ed.vn','01/02/2002',2),('Nguyễn Thị N','123412341234',0,'0101012233','2054062133ngan@ou.edu.vn','11/08/2000',3),('Chí Phèo','567856785678',1,'0113114115','duongtambua@gmail.com','09/09/1941',4),('Chị Dậu','000000999999',0,'0555666777','bachthienho@gmail.com','31/03/1958',5);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `start_time` datetime NOT NULL,
  `id_plane` int NOT NULL,
  `id_team_flight` int NOT NULL,
  `id_flight_route` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_plane` (`id_plane`),
  KEY `id_team_flight` (`id_team_flight`),
  KEY `id_flight_route` (`id_flight_route`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`id_plane`) REFERENCES `plane` (`id`),
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`id_team_flight`) REFERENCES `teamflight` (`id`),
  CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`id_flight_route`) REFERENCES `flightroute` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES ('2024-01-30 08:00:00',1,3,1,1),('2024-01-28 09:30:00',1,2,2,2),('2024-01-01 10:45:00',1,3,3,3),('2024-01-31 11:20:00',1,2,4,4),('2024-01-27 12:00:00',1,2,5,5),('2024-01-20 02:00:00',1,3,6,6),('2024-01-17 18:30:00',1,2,7,7),('2024-01-14 22:45:00',1,3,8,8),('2024-01-13 16:20:00',2,3,9,9),('2024-01-21 19:00:00',2,2,10,10),('2024-01-02 08:00:00',2,1,11,11),('2024-01-15 09:30:00',2,2,12,12),('2024-01-11 10:45:00',2,1,13,13),('2024-01-23 11:20:00',2,2,14,14),('2024-01-29 12:00:00',2,1,15,15),('2024-01-03 02:00:00',2,3,16,16),('2024-01-18 18:30:00',3,2,17,17),('2024-01-20 22:45:00',3,2,18,18),('2024-01-13 16:20:00',3,3,19,19),('2024-01-21 19:00:00',3,2,20,20),('2024-01-30 08:00:00',3,2,21,21),('2024-01-28 09:30:00',4,3,22,22),('2024-01-01 10:45:00',4,1,23,23),('2024-01-31 11:20:00',4,2,24,24),('2024-01-27 12:00:00',5,3,25,25),('2024-01-20 02:00:00',5,3,26,26),('2024-01-17 18:30:00',5,2,27,27),('2024-01-14 22:45:00',5,1,28,28),('2024-01-13 16:20:00',5,1,29,29),('2024-01-21 19:00:00',6,2,30,30),('2024-01-30 08:00:00',6,2,31,31),('2024-01-28 09:30:00',7,3,32,32),('2024-01-01 10:45:00',7,1,33,33),('2024-01-31 11:20:00',7,2,34,34),('2024-01-27 12:00:00',7,1,35,35),('2024-01-20 02:00:00',8,2,36,36),('2024-01-17 18:30:00',8,2,37,37),('2024-01-14 22:45:00',9,3,38,38),('2024-01-13 16:20:00',9,1,39,39),('2024-01-21 19:00:00',9,2,40,40),('2024-01-30 08:00:00',9,1,41,41),('2024-01-28 09:30:00',10,3,42,42),('2024-01-01 10:45:00',10,3,43,43);
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightrole`
--

DROP TABLE IF EXISTS `flightrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightrole` (
  `name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `value` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightrole`
--

LOCK TABLES `flightrole` WRITE;
/*!40000 ALTER TABLE `flightrole` DISABLE KEYS */;
INSERT INTO `flightrole` VALUES ('Thời gian bay tối thiểu ','Thời gian máy bay cất cánh tới khi hạ cánh',30,1),('Sân bay trung gian','Sân bay khác với sân bay đi và sân bay đến ',2,2),('Thời gian dừng tối đa','Thời gian máy bay dừng nhiều nhất có thể tại sân bay trung gian',30,3),('Thời gian dừng tối thiểu','Thời gian máy bay dừng ít nhất có thể tại sân bay trung gian',20,4);
/*!40000 ALTER TABLE `flightrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightroleflight`
--

DROP TABLE IF EXISTS `flightroleflight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightroleflight` (
  `id_flight_role` int NOT NULL,
  `id_flight` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_flight_role` (`id_flight_role`),
  KEY `id_flight` (`id_flight`),
  CONSTRAINT `flightroleflight_ibfk_1` FOREIGN KEY (`id_flight_role`) REFERENCES `flightrole` (`id`),
  CONSTRAINT `flightroleflight_ibfk_2` FOREIGN KEY (`id_flight`) REFERENCES `flight` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightroleflight`
--

LOCK TABLES `flightroleflight` WRITE;
/*!40000 ALTER TABLE `flightroleflight` DISABLE KEYS */;
INSERT INTO `flightroleflight` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(1,2,5),(2,2,6),(3,2,7),(4,2,8),(1,3,9),(2,3,10),(3,3,11),(4,3,12),(1,4,13),(2,4,14),(3,4,15),(4,4,16),(1,5,17),(2,5,18),(3,5,19),(4,5,20),(1,6,21),(2,6,22),(3,6,23),(4,6,24),(1,7,25),(2,7,26),(3,7,27),(4,7,28),(1,8,29),(2,8,30),(3,8,31),(4,8,32),(1,9,33),(2,9,34),(3,9,35),(4,9,36),(1,10,37),(2,10,38),(3,10,39),(4,10,40),(1,43,41),(2,43,42),(3,43,43),(4,43,44),(1,42,45),(2,42,46),(3,42,47),(4,42,48),(1,41,49),(2,41,50),(3,41,51),(4,41,52),(1,40,53),(2,40,54),(3,40,55),(4,40,56),(1,39,57),(2,39,58),(3,39,59),(4,39,60),(1,38,61),(2,38,62),(3,38,63),(4,38,64),(1,37,65),(2,37,66),(3,37,67),(4,37,68),(1,36,69),(2,36,70),(3,36,71),(4,36,72),(1,25,73),(2,25,74),(3,25,75),(4,25,76),(1,19,77),(2,19,78),(3,19,79),(4,19,80),(1,28,81),(2,28,82),(3,28,83),(4,28,84);
/*!40000 ALTER TABLE `flightroleflight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightroute`
--

DROP TABLE IF EXISTS `flightroute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightroute` (
  `destination` int NOT NULL,
  `departure` int NOT NULL,
  `id_flight_route_type` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_destination_departure` (`destination`,`departure`),
  KEY `departure` (`departure`),
  KEY `id_flight_route_type` (`id_flight_route_type`),
  CONSTRAINT `flightroute_ibfk_1` FOREIGN KEY (`destination`) REFERENCES `airport` (`id`),
  CONSTRAINT `flightroute_ibfk_2` FOREIGN KEY (`departure`) REFERENCES `airport` (`id`),
  CONSTRAINT `flightroute_ibfk_3` FOREIGN KEY (`id_flight_route_type`) REFERENCES `flightroutetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightroute`
--

LOCK TABLES `flightroute` WRITE;
/*!40000 ALTER TABLE `flightroute` DISABLE KEYS */;
INSERT INTO `flightroute` VALUES (1,2,2,1),(1,3,1,2),(1,4,2,3),(1,5,2,4),(1,6,1,5),(1,7,1,6),(1,8,1,7),(1,9,2,8),(2,1,2,9),(2,3,2,10),(2,4,1,11),(2,6,1,12),(2,7,1,13),(2,8,1,14),(2,9,1,15),(2,10,1,16),(3,1,2,17),(3,2,2,18),(3,4,1,19),(3,5,2,20),(3,7,1,21),(3,9,1,22),(4,1,2,23),(4,2,1,24),(4,3,1,25),(5,1,2,26),(5,3,1,27),(5,7,1,28),(5,9,1,29),(5,10,1,30),(6,1,1,31),(6,2,1,32),(7,1,2,33),(7,2,1,34),(7,3,1,35),(7,5,1,36),(8,1,1,37),(8,2,1,38),(9,1,2,39),(9,2,1,40),(9,3,1,41),(9,5,1,42),(10,2,1,43),(10,5,1,44);
/*!40000 ALTER TABLE `flightroute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightroutetype`
--

DROP TABLE IF EXISTS `flightroutetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightroutetype` (
  `description` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightroutetype`
--

LOCK TABLES `flightroutetype` WRITE;
/*!40000 ALTER TABLE `flightroutetype` DISABLE KEYS */;
INSERT INTO `flightroutetype` VALUES ('Tuyến bay không điểm dừng',1),('Tuyến bay có điểm dừng',2);
/*!40000 ALTER TABLE `flightroutetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightschedule`
--

DROP TABLE IF EXISTS `flightschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightschedule` (
  `id_stop_point` int NOT NULL,
  `id_airport` int NOT NULL,
  `id_flight_route` int NOT NULL,
  `time_stop` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_stop_point` (`id_stop_point`),
  KEY `id_airport` (`id_airport`),
  KEY `id_flight_route` (`id_flight_route`),
  CONSTRAINT `flightschedule_ibfk_1` FOREIGN KEY (`id_stop_point`) REFERENCES `stoppoint` (`id`),
  CONSTRAINT `flightschedule_ibfk_2` FOREIGN KEY (`id_airport`) REFERENCES `airport` (`id`),
  CONSTRAINT `flightschedule_ibfk_3` FOREIGN KEY (`id_flight_route`) REFERENCES `flightroute` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightschedule`
--

LOCK TABLES `flightschedule` WRITE;
/*!40000 ALTER TABLE `flightschedule` DISABLE KEYS */;
INSERT INTO `flightschedule` VALUES (1,4,1,22,'Sài Gòn - Buôn Mê Thuật - Đà Nẵng - Hà Nội',1),(2,3,1,22,'Sài Gòn - Buôn Mê Thuật - Đà Nẵng - Hà Nội',2),(1,3,3,24,'Buôn Mê Thuật - Đà Nẵng - Hà Nội',3),(1,7,4,27,'Cần Thơ - Lâm Đồng - Đà Nẵng - Hà Nội',4),(2,3,4,27,'Cần Thơ - Lâm Đồng - Đà Nẵng - Hà Nội',5),(1,3,8,26,'Nha Trang - Đà Nẵng - Hà Nội',6),(1,3,9,23,'Hà Nội - Đà Nẵng - Lâm Đồng - Sài Gòn',7),(2,7,9,23,'Hà Nội - Đà Nẵng - Lâm Đồng - Sài Gòn',8);
/*!40000 ALTER TABLE `flightschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plane`
--

DROP TABLE IF EXISTS `plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plane` (
  `aircraft_license_plate` varchar(7) NOT NULL,
  `flight_speed` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
INSERT INTO `plane` VALUES ('HAN1111',950,1),('HCM2222',955,2),('DAD3333',920,3),('BMV4444',890,4),('VCA5555',820,5),('VCL6666',835,6),('DLI7777',900,7),('HUI8888',870,8),('CXR9999',900,9),('VDO1234',915,10);
/*!40000 ALTER TABLE `plane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promotions`
--

DROP TABLE IF EXISTS `promotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promotions` (
  `id_flight` int NOT NULL,
  `value` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`,`id_flight`),
  KEY `id_flight` (`id_flight`),
  CONSTRAINT `promotions_ibfk_1` FOREIGN KEY (`id_flight`) REFERENCES `flight` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotions`
--

LOCK TABLES `promotions` WRITE;
/*!40000 ALTER TABLE `promotions` DISABLE KEYS */;
INSERT INTO `promotions` VALUES (1,10,1),(2,15,2),(3,20,3),(4,12,4),(5,18,5),(6,25,6),(7,30,7),(8,22,8),(9,28,9),(10,35,10);
/*!40000 ALTER TABLE `promotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `position` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES ('HRM','Người quản lý tổ đội bay',1),('Flightmanament','Người quản lý chuyến bay',2),('Cashier','Người giữ chức vụ bán vé thu tiền',3),('Flight Attendant','Hướng dẫn cho hành khách các quy tắc, phục vụ và giữ an toàn trên máy bay',4),('Captain','Điều hành tổng thể bộ máy để máy bay được vận hành đúng',5),('Co-pilot','Hỗ trợ cơ trưởng trong suốt chuyến bay',6),('Administrator','Người quản trị có quyền tối cao của hệ thống',7);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seat`
--

DROP TABLE IF EXISTS `seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seat` (
  `id_plane` int NOT NULL,
  `id_type_seat` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_plane` (`id_plane`),
  KEY `id_type_seat` (`id_type_seat`),
  CONSTRAINT `seat_ibfk_1` FOREIGN KEY (`id_plane`) REFERENCES `plane` (`id`),
  CONSTRAINT `seat_ibfk_2` FOREIGN KEY (`id_type_seat`) REFERENCES `typeseat` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
INSERT INTO `seat` VALUES (1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,1,5),(1,1,6),(1,1,7),(1,1,8),(1,1,9),(1,1,10),(1,1,11),(1,1,12),(1,1,13),(1,1,14),(1,1,15),(1,1,16),(1,1,17),(1,1,18),(1,1,19),(1,1,20),(1,2,21),(1,2,22),(1,2,23),(1,2,24),(1,2,25),(1,2,26),(1,2,27),(1,2,28),(1,2,29),(1,2,30),(2,1,31),(2,1,32),(2,1,33),(2,1,34),(2,1,35),(2,1,36),(2,1,37),(2,1,38),(2,1,39),(2,1,40),(2,1,41),(2,1,42),(2,1,43),(2,1,44),(2,1,45),(2,1,46),(2,1,47),(2,1,48),(2,1,49),(2,1,50),(2,2,51),(2,2,52),(2,2,53),(2,2,54),(2,2,55),(2,2,56),(2,2,57),(2,2,58),(2,2,59),(2,2,60),(3,1,61),(3,1,62),(3,1,63),(3,1,64),(3,1,65),(3,1,66),(3,1,67),(3,1,68),(3,1,69),(3,1,70),(3,1,71),(3,1,72),(3,1,73),(3,1,74),(3,1,75),(3,1,76),(3,1,77),(3,1,78),(3,1,79),(3,1,80),(3,2,81),(3,2,82),(3,2,83),(3,2,84),(3,2,85),(3,2,86),(3,2,87),(3,2,88),(3,2,89),(3,2,90),(4,1,91),(4,1,92),(4,1,93),(4,1,94),(4,1,95),(4,1,96),(4,1,97),(4,1,98),(4,1,99),(4,1,100),(4,1,101),(4,1,102),(4,1,103),(4,1,104),(4,1,105),(4,1,106),(4,1,107),(4,1,108),(4,1,109),(4,1,110),(4,2,111),(4,2,112),(4,2,113),(4,2,114),(4,2,115),(4,2,116),(4,2,117),(4,2,118),(4,2,119),(4,2,120),(5,1,121),(5,1,122),(5,1,123),(5,1,124),(5,1,125),(5,1,126),(5,1,127),(5,1,128),(5,1,129),(5,1,130),(5,1,131),(5,1,132),(5,1,133),(5,1,134),(5,1,135),(5,1,136),(5,1,137),(5,1,138),(5,1,139),(5,1,140),(5,2,141),(5,2,142),(5,2,143),(5,2,144),(5,2,145),(5,2,146),(5,2,147),(5,2,148),(5,2,149),(5,2,150),(6,1,151),(6,1,152),(6,1,153),(6,1,154),(6,1,155),(6,1,156),(6,1,157),(6,1,158),(6,1,159),(6,1,160),(6,1,161),(6,1,162),(6,1,163),(6,1,164),(6,1,165),(6,1,166),(6,1,167),(6,1,168),(6,1,169),(6,1,170),(6,2,171),(6,2,172),(6,2,173),(6,2,174),(6,2,175),(6,2,176),(6,2,177),(6,2,178),(6,2,179),(6,2,180),(7,1,181),(7,1,182),(7,1,183),(7,1,184),(7,1,185),(7,1,186),(7,1,187),(7,1,188),(7,1,189),(7,1,190),(7,1,191),(7,1,192),(7,1,193),(7,1,194),(7,1,195),(7,1,196),(7,1,197),(7,1,198),(7,1,199),(7,1,200),(7,2,201),(7,2,202),(7,2,203),(7,2,204),(7,2,205),(7,2,206),(7,2,207),(7,2,208),(7,2,209),(7,2,210),(8,1,211),(8,1,212),(8,1,213),(8,1,214),(8,1,215),(8,1,216),(8,1,217),(8,1,218),(8,1,219),(8,1,220),(8,1,221),(8,1,222),(8,1,223),(8,1,224),(8,1,225),(8,1,226),(8,1,227),(8,1,228),(8,1,229),(8,1,230),(8,2,231),(8,2,232),(8,2,233),(8,2,234),(8,2,235),(8,2,236),(8,2,237),(8,2,238),(8,2,239),(8,2,240),(9,1,241),(9,1,242),(9,1,243),(9,1,244),(9,1,245),(9,1,246),(9,1,247),(9,1,248),(9,1,249),(9,1,250),(9,1,251),(9,1,252),(9,1,253),(9,1,254),(9,1,255),(9,1,256),(9,1,257),(9,1,258),(9,1,259),(9,1,260),(9,2,261),(9,2,262),(9,2,263),(9,2,264),(9,2,265),(9,2,266),(9,2,267),(9,2,268),(9,2,269),(9,2,270),(10,1,271),(10,1,272),(10,1,273),(10,1,274),(10,1,275),(10,1,276),(10,1,277),(10,1,278),(10,1,279),(10,1,280),(10,1,281),(10,1,282),(10,1,283),(10,1,284),(10,1,285),(10,1,286),(10,1,287),(10,1,288),(10,1,289),(10,1,290),(10,2,291),(10,2,292),(10,2,293),(10,2,294),(10,2,295),(10,2,296),(10,2,297),(10,2,298),(10,2,299),(10,2,300);
/*!40000 ALTER TABLE `seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistical`
--

DROP TABLE IF EXISTS `statistical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistical` (
  `link_statistical` varchar(255) DEFAULT NULL,
  `id_user` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `statistical_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistical`
--

LOCK TABLES `statistical` WRITE;
/*!40000 ALTER TABLE `statistical` DISABLE KEYS */;
INSERT INTO `statistical` VALUES ('Tự nhập',1,1);
/*!40000 ALTER TABLE `statistical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stoppoint`
--

DROP TABLE IF EXISTS `stoppoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stoppoint` (
  `description` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stoppoint`
--

LOCK TABLES `stoppoint` WRITE;
/*!40000 ALTER TABLE `stoppoint` DISABLE KEYS */;
INSERT INTO `stoppoint` VALUES ('Point A',1),('Point B',2);
/*!40000 ALTER TABLE `stoppoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teamflight`
--

DROP TABLE IF EXISTS `teamflight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teamflight` (
  `description` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teamflight`
--

LOCK TABLES `teamflight` WRITE;
/*!40000 ALTER TABLE `teamflight` DISABLE KEYS */;
INSERT INTO `teamflight` VALUES ('Team A có 5 thành viên gồm 1 cơ trưởng, 2 cơ phó, cùng 3 tiếp viên',1),('Team C có 7 thành viên gồm 1 cơ trưởng, 2 cơ phó, cùng 4 tiếp viên',2),('Team B có 10 thành viên gồm 1 cơ trường, 3 cơ phó,  cùng 6 tiếp viên',3),('2 nhân viên',4);
/*!40000 ALTER TABLE `teamflight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `id_seat` int NOT NULL,
  `id_buyer` int NOT NULL,
  `id_passenger` int NOT NULL,
  `id_flight` int NOT NULL,
  `id_ticket_status` int NOT NULL,
  `purchase_time` datetime DEFAULT NULL,
  `employee_responsible` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_seat` (`id_seat`),
  KEY `id_buyer` (`id_buyer`),
  KEY `id_passenger` (`id_passenger`),
  KEY `id_flight` (`id_flight`),
  KEY `id_ticket_status` (`id_ticket_status`),
  KEY `employee_responsible` (`employee_responsible`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`id_seat`) REFERENCES `seat` (`id`),
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`id_buyer`) REFERENCES `customer` (`id`),
  CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`id_passenger`) REFERENCES `customer` (`id`),
  CONSTRAINT `ticket_ibfk_4` FOREIGN KEY (`id_flight`) REFERENCES `flight` (`id`),
  CONSTRAINT `ticket_ibfk_5` FOREIGN KEY (`id_ticket_status`) REFERENCES `ticketstatus` (`id`),
  CONSTRAINT `ticket_ibfk_6` FOREIGN KEY (`employee_responsible`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,1,1,1,1,'2024-01-01 08:00:00',3,1),(2,2,2,1,1,'2024-01-02 09:30:00',3,2),(3,3,3,1,1,'2024-01-03 11:20:00',3,3),(4,4,4,1,2,'2024-01-04 12:00:00',3,4),(5,5,5,1,3,'2024-01-05 08:00:00',3,5),(25,2,2,1,1,'2024-01-06 09:30:00',3,6),(26,3,3,1,1,'2024-01-07 10:45:00',3,7),(27,4,4,1,1,'2024-01-08 11:20:00',3,8),(28,5,5,1,2,'2024-01-07 01:45:00',3,9),(29,1,1,1,3,'2024-01-08 06:20:00',3,10),(41,3,3,10,1,'2024-01-01 08:00:00',3,11),(42,4,4,10,1,'2024-01-02 09:30:00',3,12),(43,5,5,10,1,'2024-01-03 11:20:00',3,13),(44,1,1,10,2,'2024-01-04 12:00:00',3,14),(45,2,2,10,3,'2024-01-05 08:00:00',3,15),(55,4,4,10,1,'2024-01-06 09:30:00',3,16),(56,5,5,10,1,'2024-01-07 10:45:00',3,17),(57,1,1,10,1,'2024-01-08 11:20:00',3,18),(58,2,2,10,2,'2024-01-07 01:45:00',3,19),(59,3,3,10,3,'2024-01-08 06:20:00',3,20),(61,5,5,18,1,'2024-01-01 08:00:00',3,21),(62,1,1,18,1,'2024-01-02 09:30:00',3,22),(63,2,2,18,1,'2024-01-03 11:20:00',3,23),(64,3,3,18,2,'2024-01-04 12:00:00',3,24),(65,4,4,18,3,'2024-01-05 08:00:00',3,25),(85,1,1,18,1,'2024-01-06 09:30:00',3,26),(86,2,2,18,1,'2024-01-07 10:45:00',3,27),(87,3,3,18,1,'2024-01-08 11:20:00',3,28),(88,4,4,18,2,'2024-01-07 01:45:00',3,29),(89,5,5,18,3,'2024-01-08 06:20:00',3,30),(101,1,1,22,1,'2024-01-01 08:00:00',3,31),(102,2,2,22,1,'2024-01-02 09:30:00',3,32),(103,3,3,22,1,'2024-01-03 11:20:00',3,33),(104,4,4,22,2,'2024-01-04 12:00:00',3,34),(105,5,5,22,3,'2024-01-05 08:00:00',3,35),(115,2,2,22,1,'2024-01-06 09:30:00',3,36),(116,3,3,22,1,'2024-01-07 10:45:00',3,37),(117,4,4,22,1,'2024-01-08 11:20:00',3,38),(118,5,5,22,2,'2024-01-07 01:45:00',3,39),(119,1,1,22,3,'2024-01-08 06:20:00',3,40),(121,3,3,29,1,'2024-01-01 08:00:00',3,41),(122,4,4,29,1,'2024-01-02 09:30:00',3,42),(123,5,5,29,1,'2024-01-03 11:20:00',3,43),(124,1,1,29,2,'2024-01-04 12:00:00',3,44),(125,2,2,29,3,'2024-01-05 08:00:00',3,45),(145,4,4,29,1,'2024-01-06 09:30:00',3,46),(146,5,5,29,1,'2024-01-07 10:45:00',3,47),(147,1,1,29,1,'2024-01-08 11:20:00',3,48),(148,2,2,29,2,'2024-01-07 01:45:00',3,49),(149,3,3,29,3,'2024-01-08 06:20:00',3,50),(165,5,5,31,1,'2024-01-01 08:00:00',3,51),(166,1,1,31,1,'2024-01-02 09:30:00',3,52),(167,2,2,31,1,'2024-01-03 11:20:00',3,53),(168,3,3,31,2,'2024-01-04 12:00:00',3,54),(169,4,4,31,3,'2024-01-05 08:00:00',3,55),(175,1,1,31,1,'2024-01-06 09:30:00',3,56),(176,2,2,31,1,'2024-01-07 10:45:00',3,57),(177,3,3,31,1,'2024-01-08 11:20:00',3,58),(178,4,4,31,2,'2024-01-07 01:45:00',3,59),(179,5,5,31,3,'2024-01-08 06:20:00',3,60),(181,1,1,34,1,'2024-01-01 08:00:00',3,61),(182,2,2,34,1,'2024-01-02 09:30:00',3,62),(183,3,3,34,1,'2024-01-03 11:20:00',3,63),(184,4,4,34,2,'2024-01-04 12:00:00',3,64),(185,5,5,34,3,'2024-01-05 08:00:00',3,65),(205,2,2,34,1,'2024-01-06 09:30:00',3,66),(206,3,3,34,1,'2024-01-07 10:45:00',3,67),(207,4,4,34,1,'2024-01-08 11:20:00',3,68),(208,5,5,34,2,'2024-01-07 01:45:00',3,69),(209,1,1,34,3,'2024-01-08 06:20:00',3,70),(221,3,3,36,1,'2024-01-01 08:00:00',3,71),(222,4,4,36,1,'2024-01-02 09:30:00',3,72),(223,5,5,36,1,'2024-01-03 11:20:00',3,73),(224,1,1,36,2,'2024-01-04 12:00:00',3,74),(225,2,2,36,3,'2024-01-05 08:00:00',3,75),(235,4,4,36,1,'2024-01-06 09:30:00',3,76),(236,5,5,36,1,'2024-01-07 10:45:00',3,77),(237,1,1,36,1,'2024-01-08 11:20:00',3,78),(238,2,2,36,2,'2024-01-07 01:45:00',3,79),(239,3,3,36,3,'2024-01-08 06:20:00',3,80),(241,5,5,41,1,'2024-01-01 08:00:00',3,81),(242,1,1,41,1,'2024-01-02 09:30:00',3,82),(243,2,2,41,1,'2024-01-03 11:20:00',3,83),(244,3,3,41,2,'2024-01-04 12:00:00',3,84),(245,4,4,41,3,'2024-01-05 08:00:00',3,85),(265,1,1,41,1,'2024-01-06 09:30:00',3,86),(266,2,2,41,1,'2024-01-07 10:45:00',3,87),(267,3,3,41,1,'2024-01-08 11:20:00',3,88),(268,4,4,41,2,'2024-01-07 01:45:00',3,89),(269,5,5,41,3,'2024-01-08 06:20:00',3,90),(285,1,1,42,1,'2024-01-01 08:00:00',3,91),(286,2,2,42,1,'2024-01-02 09:30:00',3,92),(287,3,3,42,1,'2024-01-03 11:20:00',3,93),(288,4,4,42,2,'2024-01-04 12:00:00',3,94),(289,5,5,42,3,'2024-01-05 08:00:00',3,95),(293,2,2,42,1,'2024-01-06 09:30:00',3,96),(294,3,3,42,1,'2024-01-07 10:45:00',3,97),(295,4,4,42,1,'2024-01-08 11:20:00',3,98),(296,5,5,42,2,'2024-01-07 01:45:00',3,99),(297,1,1,42,3,'2024-01-08 06:20:00',3,100);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketrole`
--

DROP TABLE IF EXISTS `ticketrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticketrole` (
  `name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `value` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketrole`
--

LOCK TABLES `ticketrole` WRITE;
/*!40000 ALTER TABLE `ticketrole` DISABLE KEYS */;
INSERT INTO `ticketrole` VALUES ('Nhân viên','Nhân viên đặt vé tại quầy và bán cho khách hàng',4,1),('Khách hàng','Khách hàng tự đặt vé trực tuyến',12,2);
/*!40000 ALTER TABLE `ticketrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketroleticket`
--

DROP TABLE IF EXISTS `ticketroleticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticketroleticket` (
  `id_ticket_role` int NOT NULL,
  `id_ticket` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_ticket_role` (`id_ticket_role`),
  KEY `id_ticket` (`id_ticket`),
  CONSTRAINT `ticketroleticket_ibfk_1` FOREIGN KEY (`id_ticket_role`) REFERENCES `ticketrole` (`id`),
  CONSTRAINT `ticketroleticket_ibfk_2` FOREIGN KEY (`id_ticket`) REFERENCES `ticket` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketroleticket`
--

LOCK TABLES `ticketroleticket` WRITE;
/*!40000 ALTER TABLE `ticketroleticket` DISABLE KEYS */;
INSERT INTO `ticketroleticket` VALUES (1,1,1),(1,2,2),(1,3,3),(1,4,4),(1,5,5),(2,6,6),(2,7,7),(2,8,8),(2,9,9),(2,10,10),(1,11,11),(1,12,12),(1,13,13),(1,14,14),(1,15,15),(2,16,16),(2,17,17),(2,18,18),(2,19,19),(2,20,20),(1,21,21),(1,22,22),(1,23,23),(1,24,24),(1,25,25),(2,26,26),(2,27,27),(2,28,28),(2,29,29),(2,30,30),(1,31,31),(1,32,32),(1,33,33),(1,34,34),(1,35,35),(2,36,36),(2,37,37),(2,38,38),(2,39,39),(2,40,40),(1,41,41),(1,42,42),(1,43,43),(1,44,44),(1,45,45),(2,46,46),(2,47,47),(2,48,48),(2,49,49),(2,50,50),(1,51,51),(1,52,52),(1,53,53),(1,54,54),(1,55,55),(2,56,56),(2,57,57),(2,58,58),(2,59,59),(2,60,60),(1,61,61),(1,62,62),(1,63,63),(1,64,64),(1,65,65),(2,66,66),(2,67,67),(2,68,68),(2,69,69),(2,70,70),(1,71,71),(1,72,72),(1,73,73),(1,74,74),(1,75,75),(2,76,76),(2,77,77),(2,78,78),(2,79,79),(2,80,80),(1,81,81),(1,82,82),(1,83,83),(1,84,84),(1,85,85),(2,86,86),(2,87,87),(2,88,88),(2,89,89),(2,90,90),(1,91,91),(1,92,92),(1,93,93),(1,94,94),(1,95,95),(2,96,96),(2,97,97),(2,98,98),(2,99,99),(2,100,100);
/*!40000 ALTER TABLE `ticketroleticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketstatus`
--

DROP TABLE IF EXISTS `ticketstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticketstatus` (
  `name` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketstatus`
--

LOCK TABLES `ticketstatus` WRITE;
/*!40000 ALTER TABLE `ticketstatus` DISABLE KEYS */;
INSERT INTO `ticketstatus` VALUES ('Loading.........',1),('Loading.........',2),('Loading.........',3);
/*!40000 ALTER TABLE `ticketstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `typeseat`
--

DROP TABLE IF EXISTS `typeseat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `typeseat` (
  `name` varchar(50) NOT NULL,
  `value` float NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `typeseat`
--

LOCK TABLES `typeseat` WRITE;
/*!40000 ALTER TABLE `typeseat` DISABLE KEYS */;
INSERT INTO `typeseat` VALUES ('Hạng 2',1000,1),('Hạng 1',2500,2);
/*!40000 ALTER TABLE `typeseat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `CCCD` varchar(12) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `birthday` varchar(50) NOT NULL,
  `id_role` int NOT NULL,
  `id_team_flight` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `id_role` (`id_role`),
  KEY `id_team_flight` (`id_team_flight`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`id_team_flight`) REFERENCES `teamflight` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('si','1','','Tấn Sĩ','121212343434',1,'0704770906','tansitrinh@gmail.com','28/11/2002',1,1,1),('nam','1','','Hoàng Nam','565656578787',0,'0786452756','hoangvannam27072002@gmail.com','01/01/2000',2,2,2),('khoi','1','','Vỹ Khôi','919191232323',1,'0123123456','user3@example.com','15/07/2005',3,3,3),('ngan','1','','Thu Ngân','454545676767',1,'0202026789','user4@example.com','31/05/2001',4,1,4),('Giang','1','','Lệ Giang','898989010101',0,'0909123445','user5@example.com','10/02/2004',5,2,5),('rwrwrwrwr','4224',NULL,'fmndbfjdf','3535353535',1,'0123456789','hoangvannam27072002@gmail.com','2024-01-10',2,3,6),('namdss','1',NULL,'fmndbfjdf','3535353535',0,'424242','cuongtttt123@gmail.com','2024-01-01',2,2,9),('nam244','1',NULL,'fsfsfsfsf','001122334455',1,'0786452763','2051052084nam@ou.edu.vn','2024-01-11',2,2,12),('Hoang_Nam_IT03','12',NULL,' sdsfsf','001122334455',1,'0786452763','nam001202030355@gmail.com','2024-01-15',2,3,13),('nam4fssfsf','322','https://res.cloudinary.com/del3gk3b3/image/upload/v1705136571/xe839n1bpds6wlbq4xrp.heic','fsfsfsfsf','001122334455',1,'0786452763','2051052084nam@ou.edu.vn','2024-01-17',1,2,14);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-13 20:24:14
