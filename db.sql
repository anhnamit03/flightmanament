-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: fightmanament
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
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
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
  `CCCD` varchar(12) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `birthday` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_plane` (`id_plane`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`id_plane`) REFERENCES `plane` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightchedules`
--

DROP TABLE IF EXISTS `flightchedules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightchedules` (
  `stop_time` int NOT NULL,
  `notes` varchar(250) DEFAULT NULL,
  `id_the_flight` int NOT NULL,
  `id_multileg_Flight` int NOT NULL,
  `id_flight_number` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_the_flight` (`id_the_flight`),
  KEY `id_multileg_Flight` (`id_multileg_Flight`),
  KEY `id_flight_number` (`id_flight_number`),
  CONSTRAINT `flightchedules_ibfk_1` FOREIGN KEY (`id_the_flight`) REFERENCES `theflight` (`id`),
  CONSTRAINT `flightchedules_ibfk_2` FOREIGN KEY (`id_multileg_Flight`) REFERENCES `multilegflight` (`id`),
  CONSTRAINT `flightchedules_ibfk_3` FOREIGN KEY (`id_flight_number`) REFERENCES `flightnumber` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightchedules`
--

LOCK TABLES `flightchedules` WRITE;
/*!40000 ALTER TABLE `flightchedules` DISABLE KEYS */;
/*!40000 ALTER TABLE `flightchedules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightnumber`
--

DROP TABLE IF EXISTS `flightnumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flightnumber` (
  `description` varchar(50) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightnumber`
--

LOCK TABLES `flightnumber` WRITE;
/*!40000 ALTER TABLE `flightnumber` DISABLE KEYS */;
/*!40000 ALTER TABLE `flightnumber` ENABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightrole`
--

LOCK TABLES `flightrole` WRITE;
/*!40000 ALTER TABLE `flightrole` DISABLE KEYS */;
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
  `notes` varchar(50) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_flight_role` (`id_flight_role`),
  KEY `id_flight` (`id_flight`),
  CONSTRAINT `flightroleflight_ibfk_1` FOREIGN KEY (`id_flight_role`) REFERENCES `flightrole` (`id`),
  CONSTRAINT `flightroleflight_ibfk_2` FOREIGN KEY (`id_flight`) REFERENCES `flight` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightroleflight`
--

LOCK TABLES `flightroleflight` WRITE;
/*!40000 ALTER TABLE `flightroleflight` DISABLE KEYS */;
/*!40000 ALTER TABLE `flightroleflight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `multilegflight`
--

DROP TABLE IF EXISTS `multilegflight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `multilegflight` (
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multilegflight`
--

LOCK TABLES `multilegflight` WRITE;
/*!40000 ALTER TABLE `multilegflight` DISABLE KEYS */;
/*!40000 ALTER TABLE `multilegflight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onewayflight`
--

DROP TABLE IF EXISTS `onewayflight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `onewayflight` (
  `id_the_flight` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_the_flight` (`id_the_flight`),
  CONSTRAINT `onewayflight_ibfk_1` FOREIGN KEY (`id_the_flight`) REFERENCES `theflight` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onewayflight`
--

LOCK TABLES `onewayflight` WRITE;
/*!40000 ALTER TABLE `onewayflight` DISABLE KEYS */;
/*!40000 ALTER TABLE `onewayflight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plane`
--

DROP TABLE IF EXISTS `plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plane` (
  `aircraft_license_plate` varchar(7) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotions`
--

LOCK TABLES `promotions` WRITE;
/*!40000 ALTER TABLE `promotions` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistical`
--

LOCK TABLES `statistical` WRITE;
/*!40000 ALTER TABLE `statistical` DISABLE KEYS */;
/*!40000 ALTER TABLE `statistical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theflight`
--

DROP TABLE IF EXISTS `theflight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theflight` (
  `to_id` int NOT NULL,
  `depart_id` int NOT NULL,
  `distance` float DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `to_id` (`to_id`),
  KEY `depart_id` (`depart_id`),
  CONSTRAINT `theflight_ibfk_1` FOREIGN KEY (`to_id`) REFERENCES `airport` (`id`),
  CONSTRAINT `theflight_ibfk_2` FOREIGN KEY (`depart_id`) REFERENCES `airport` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theflight`
--

LOCK TABLES `theflight` WRITE;
/*!40000 ALTER TABLE `theflight` DISABLE KEYS */;
/*!40000 ALTER TABLE `theflight` ENABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_seat` (`id_seat`),
  KEY `id_buyer` (`id_buyer`),
  KEY `id_passenger` (`id_passenger`),
  KEY `id_flight` (`id_flight`),
  KEY `id_ticket_status` (`id_ticket_status`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`id_seat`) REFERENCES `seat` (`id`),
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`id_buyer`) REFERENCES `customer` (`id`),
  CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`id_passenger`) REFERENCES `customer` (`id`),
  CONSTRAINT `ticket_ibfk_4` FOREIGN KEY (`id_flight`) REFERENCES `flight` (`id`),
  CONSTRAINT `ticket_ibfk_5` FOREIGN KEY (`id_ticket_status`) REFERENCES `ticketstatus` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketrole`
--

LOCK TABLES `ticketrole` WRITE;
/*!40000 ALTER TABLE `ticketrole` DISABLE KEYS */;
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
  `notes` varchar(50) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_ticket_role` (`id_ticket_role`),
  KEY `id_ticket` (`id_ticket`),
  CONSTRAINT `ticketroleticket_ibfk_1` FOREIGN KEY (`id_ticket_role`) REFERENCES `ticketrole` (`id`),
  CONSTRAINT `ticketroleticket_ibfk_2` FOREIGN KEY (`id_ticket`) REFERENCES `ticket` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketroleticket`
--

LOCK TABLES `ticketroleticket` WRITE;
/*!40000 ALTER TABLE `ticketroleticket` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketstatus`
--

LOCK TABLES `ticketstatus` WRITE;
/*!40000 ALTER TABLE `ticketstatus` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `typeseat`
--

LOCK TABLES `typeseat` WRITE;
/*!40000 ALTER TABLE `typeseat` DISABLE KEYS */;
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
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
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

-- Dump completed on 2023-12-28 15:44:46
