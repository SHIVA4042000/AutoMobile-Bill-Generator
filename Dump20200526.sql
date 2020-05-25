-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: bill
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `bike_parts`
--

DROP TABLE IF EXISTS `bike_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bike_parts` (
  `S_No` int DEFAULT NULL,
  `Part_No` int NOT NULL,
  `Model` varchar(150) DEFAULT NULL,
  `part_Name` varchar(90) DEFAULT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Part_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bike_parts`
--

LOCK TABLES `bike_parts` WRITE;
/*!40000 ALTER TABLE `bike_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `bike_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_details` (
  `S_no` int DEFAULT NULL,
  `Registration_No` varchar(10) NOT NULL,
  `Customer_Name` char(30) DEFAULT NULL,
  `Phone_No` bigint DEFAULT NULL,
  `Address` varchar(150) DEFAULT NULL,
  `Vehical_Sn` int DEFAULT NULL,
  PRIMARY KEY (`Registration_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT INTO `customer_details` VALUES (6,'MP14MG9875','Robert Thomas',9876543210,'H-764,police colony,mandsaur, m.p, 458001\n',9),(5,'MP14MH5469','Gurjar Singh',9876543210,'D-09,kityani mandsaur m.p 458001\n',10),(3,'MP14MJ4578','Jon Thomas',9876543210,'S-67,Pihor Colony, indore M.P 458001\n',10),(8,'MP14MK2325','Manoj Reddi',9876543210,'A-876,Gandhi Choraha Mandsaur M.P 458001\n',25),(4,'MP14MK9523','Jon Watson',9876543212,'A-43,pihor colony, mandsaur , m.p 458001\n',10),(1,'MP14MK9564','Ayush Sharma',9826204582,'A-34,Gandhi Nagar,Mandsaur,MP,458001',51),(2,'MP14MK9988','Jeff Bezos',9876543210,'A-32,jagah khedi, mandsaur, m.p 458001\n',13),(7,'MP14MY5687','Mahesh Joshi',9876543210,'D-56,Ram Tekri, Mandsaur, M.P, 458001\n',10),(9,'MP65MJ5487','Shiva Hari V Mohan',0,'Haveli Mandsaur M.P 458001\n',13);
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hatchback_car_parts`
--

DROP TABLE IF EXISTS `hatchback_car_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hatchback_car_parts` (
  `S_No` int DEFAULT NULL,
  `Part_No` int NOT NULL,
  `Model` varchar(150) DEFAULT NULL,
  `part_Name` varchar(90) DEFAULT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Part_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hatchback_car_parts`
--

LOCK TABLES `hatchback_car_parts` WRITE;
/*!40000 ALTER TABLE `hatchback_car_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `hatchback_car_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_card`
--

DROP TABLE IF EXISTS `job_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_card` (
  `S_No` int DEFAULT NULL,
  `Registration_No` varchar(10) DEFAULT NULL,
  `Total_Km` int DEFAULT NULL,
  `Part_S_No` varchar(20) DEFAULT NULL,
  `Hour` varchar(20) DEFAULT NULL,
  `Quantity` varchar(20) DEFAULT NULL,
  `Invoice_NO` int NOT NULL,
  `Bill_Date` date DEFAULT NULL,
  `Bill_Time` time DEFAULT NULL,
  `job_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Invoice_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_card`
--

LOCK TABLES `job_card` WRITE;
/*!40000 ALTER TABLE `job_card` DISABLE KEYS */;
INSERT INTO `job_card` VALUES (8,'MP14MJ4578',15878,'6,','9,','1,',12569,'2020-05-19','18:55:19','1,'),(3,'MP14MK9564',8000,'4,1,','5,','1,1,1,',21258,'2019-11-21','17:38:50','1,'),(1,'MP14MK9564',12000,'1,4,3,','5,','1,1,1,',21548,'2020-05-19','17:38:50','1,'),(2,'MP14MK9564',10000,'1,4,1,','5,','1,1,1,',21958,'2020-01-21','17:38:50','1,'),(5,'MP14MK9988',19500,'','6,','',23222,'2020-05-19','09:18:05','1,'),(12,'MP14MY5687',14658,'3,1,','6,','1,1,',29374,'2020-05-19','19:38:08','1,'),(14,'MP65MJ5487',5487,'6,3,','10,','1,1,',31219,'2020-05-25','16:58:56','1,'),(10,'MP14MH5469',14879,'3,','9,','1,',32536,'2020-05-19','19:08:40','1,'),(13,'MP14MK2325',8254,'','5,','',66329,'2020-05-25','16:52:50','1,'),(6,'MP14MK9988',20000,'1,','6,','1,',75619,'2020-05-19','09:22:18','1,'),(11,'MP14MG9875',2564,'6,','6,','1,',84722,'2020-05-19','19:24:11','1,'),(4,'MP14MK9988',15480,'3,1,','9,','1,1,',87824,'2020-05-19','09:12:06','1,'),(9,'MP14MK9523',14769,'3,','9,','1,',98693,'2020-05-19','18:58:33','1,'),(7,'MP14MK9988',26546,'9,','9,','1,',99021,'2020-05-19','09:35:14','1,');
/*!40000 ALTER TABLE `job_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_performed`
--

DROP TABLE IF EXISTS `job_performed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_performed` (
  `S_No` int DEFAULT NULL,
  `Job_Name` varchar(50) NOT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Job_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_performed`
--

LOCK TABLES `job_performed` WRITE;
/*!40000 ALTER TABLE `job_performed` DISABLE KEYS */;
INSERT INTO `job_performed` VALUES (1,'Labour',70.00);
/*!40000 ALTER TABLE `job_performed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `S_No` int DEFAULT NULL,
  `User_ID` varchar(20) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'login','2736fab291f04e69b62d490c3c09361f5b82461a');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marketed_vehical`
--

DROP TABLE IF EXISTS `marketed_vehical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marketed_vehical` (
  `S_No` int NOT NULL,
  `Class` char(10) DEFAULT NULL,
  `Brand` char(10) DEFAULT NULL,
  `Model` varchar(50) DEFAULT NULL,
  `Year` int DEFAULT NULL,
  `Colour` varchar(50) DEFAULT NULL,
  `Fuel` char(10) DEFAULT NULL,
  `Wheels` int DEFAULT NULL,
  `CC` decimal(6,2) DEFAULT NULL,
  `Gear` char(10) DEFAULT NULL,
  `Power_HP` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`S_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marketed_vehical`
--

LOCK TABLES `marketed_vehical` WRITE;
/*!40000 ALTER TABLE `marketed_vehical` DISABLE KEYS */;
INSERT INTO `marketed_vehical` VALUES (1,'Scooter','Honda','Activa 6G',2020,'Black','Petrol',2,109.00,'Automatic',7.79),(2,'Scooter','Honda','Activa 6G',2020,'Pearl Precious White','Petrol',2,109.00,'Automatic',7.79),(4,'Scooter','Honda','Activa 6G',2020,'Matte Axis Grey','Petrol',2,109.00,'Automatic',7.79),(5,'Scooter','Honda','Activa 6G',2020,'Pearl Spartan Red','Petrol',2,109.00,'Automatic',7.79),(6,'Scooter','Honda','Activa 6G',2020,'Glitter Blue','Petrol',2,109.00,'Automatic',7.79),(7,'Scooter','Honda','Activa 5G',2018,'Glitter Blue','Petrol',2,109.00,'Automatic',7.79),(8,'Scooter','Honda','Activa 5G',2018,'Pearl Spartan Red','Petrol',2,109.00,'Automatic',7.79),(9,'Scooter','Honda','Activa 5G',2018,'Black','Petrol',2,109.00,'Automatic',7.79),(10,'Scooter','Honda','Activa 5G',2018,'Matte Selene Silver','Petrol',2,109.00,'Automatic',7.79),(11,'Scooter','Honda','Activa 5G',2018,'Trance Blue Metallic','Petrol',2,109.00,'Automatic',7.79),(12,'Scooter','Honda','Activa 5G',2018,'Pearl Precious White and Matte Selene Silver','Petrol',2,109.00,'Automatic',7.79),(13,'Scooter','Honda','Activa 5G',2018,'Majestic Brown Metallic','Petrol',2,109.00,'Automatic',7.79),(14,'Scooter','Honda','Activa 5G',2018,'Dazzle Yellow Metallic','Petrol',2,109.00,'Automatic',7.79),(15,'Scooter','Honda','Activa 5G',2018,'Pearl Amazing White','Petrol',2,109.00,'Automatic',7.79),(16,'Scooter','Honda','Activa 5G',2018,'Silver and black','Petrol',2,109.00,'Automatic',7.79),(17,'Scooter','TVS','Jupiter STD BS6',2020,'Tech Blue','Petrol',2,109.70,'Automatic',7.99),(18,'Scooter','TVS','Jupiter STD BS6',2020,'Autumn Brown','Petrol',2,109.70,'Automatic',7.99),(19,'Scooter','TVS','Jupiter STD BS6',2020,'Sunlit Ivory','Petrol',2,109.70,'Automatic',7.99),(20,'Scooter','TVS','Jupiter STD BS6',2020,'Volcano Red','Petrol',2,109.70,'Automatic',7.99),(21,'Scooter','TVS','Jupiter STD BS6',2020,'Titanium Grey','Petrol',2,109.70,'Automatic',7.99),(22,'Scooter','TVS','Jupiter STD BS6',2020,'Mystic Gold','Petrol',2,109.70,'Automatic',7.99),(23,'Scooter','TVS','Jupiter STD BS6',2020,'Midnight Black','Petrol',2,109.70,'Automatic',7.99),(24,'Scooter','TVS','Jupiter STD BS6',2020,'Matte Silver','Petrol',2,109.70,'Automatic',7.99),(25,'Scooter','TVS','Jupiter STD BS6',2020,'Matte Blue','Petrol',2,109.70,'Automatic',7.99),(26,'Scooter','TVS','Jupiter STD BS6',2020,'Starlight Blue','Petrol',2,109.70,'Automatic',7.99),(27,'Scooter','TVS','Jupiter STD BS6',2020,'Royal Wine','Petrol',2,109.70,'Automatic',7.99),(28,'Scooter','TVS','Jupiter ZX BS6',2020,'Starlight Blue','Petrol',2,109.70,'Automatic',7.99),(29,'Scooter','TVS','Jupiter ZX BS6',2020,'Royal Wine','Petrol',2,109.70,'Automatic',7.99),(30,'Scooter','TVS','Jupiter Grande Edition BS6',2020,'Tech Blue','Petrol',2,109.70,'Automatic',7.99),(31,'Scooter','TVS','Jupiter Grande Edition BS6',2020,'Autumn Brown','Petrol',2,109.70,'Automatic',7.99),(32,'Scooter','TVS','Jupiter Grande Edition BS6',2020,'Sunlit Ivory','Petrol',2,109.70,'Automatic',7.99),(33,'Scooter','Hero','Maestro Edge VX',2018,'Techno Blue','Petrol',2,110.90,'Automatic',8.15),(34,'Scooter','Hero','Maestro Edge VX',2018,'Shooting Night Star','Petrol',2,110.90,'Automatic',8.15),(35,'Scooter','Hero','Maestro Edge VX',2018,'Pearl Silver White','Petrol',2,110.90,'Automatic',8.15),(36,'Scooter','Hero','Maestro Edge VX',2018,'Panther Black','Petrol',2,110.90,'Automatic',8.15),(37,'Scooter','Hero','Maestro Edge VX',2018,'Matte Vernier Grey','Petrol',2,110.90,'Automatic',8.15),(38,'Scooter','Hero','Maestro Edge VX',2018,'Matte Blue','Petrol',2,110.90,'Automatic',8.15),(39,'Scooter','Hero','Maestro Edge VX',2018,'Candy Blazing Red','Petrol',2,110.90,'Automatic',8.15),(40,'Scooter','Hero','Maestro Edge VX',2018,'Sporty Matte Grey And Red','Petrol',2,110.90,'Automatic',8.15),(41,'Scooter','Hero','Maestro Edge VX',2018,'Active Matte Grey And Blue','Petrol',2,110.90,'Automatic',8.15),(42,'Bike','Bajaj','Pulsar 125 Neon',2020,'Black Blue','Petrol',2,124.40,'Manual',12.00),(43,'Bike','TVS','Apache RTR 160',2018,'Grey','Petrol',2,159.70,'Manual',15.11),(44,'Bike','TVS','Apache RTR 160',2018,'Pearl White','Petrol',2,159.70,'Manual',15.11),(45,'Bike','TVS','Apache RTR 160',2018,'Matte Red','Petrol',2,159.70,'Manual',15.11),(46,'Bike','TVS','Apache RTR 160',2018,'Matte Blue','Petrol',2,159.70,'Manual',15.11),(47,'Bike','TVS','Apache RTR 160',2018,'Gloss Black','Petrol',2,159.70,'Manual',15.11),(48,'Bike','TVS','Apache RTR 160 4V',2018,'Blue','Petrol',2,159.70,'Manual',16.70),(49,'Bike','TVS','Apache RTR 160 4V',2018,'Black','Petrol',2,159.70,'Manual',16.70),(50,'Bike','TVS','Apache RTR 160 4V',2018,'Red','Petrol',2,159.70,'Manual',16.70),(51,'Bike','TVS','Apache RR 310',2018,'Phantom Black','Petrol',2,312.20,'Manual',34.00),(52,'Bike','TVS','Apache RR 310',2018,'Racing Red','Petrol',2,312.20,'Manual',34.00),(53,'Scooter','TVS','Jupiter STD BS6',2020,'Pristine White','Petrol',2,109.70,'Automatic',7.99);
/*!40000 ALTER TABLE `marketed_vehical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scooter_parts`
--

DROP TABLE IF EXISTS `scooter_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scooter_parts` (
  `S_No` int DEFAULT NULL,
  `Part_No` int NOT NULL,
  `Model` varchar(150) DEFAULT NULL,
  `Part_Name` varchar(90) DEFAULT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Part_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scooter_parts`
--

LOCK TABLES `scooter_parts` WRITE;
/*!40000 ALTER TABLE `scooter_parts` DISABLE KEYS */;
INSERT INTO `scooter_parts` VALUES (1,10011,'Activa 5G','Side Stand',315.00),(2,10012,'Activa 5G','Leg Guard',530.00),(3,10013,'Activa 5G','Grip Set',57.00),(4,10014,'Activa 5G','Silencer Assly',1656.00),(5,10015,'Activa 5G','Rider Foot Rest',99.00),(6,10016,'Activa 5G','No Plate',100.00),(7,10017,'Activa 5G','Meter Cover',284.00),(8,10018,'Activa 5G','Inner Cover',1117.00),(9,10019,'Activa 5G','Horn',203.00);
/*!40000 ALTER TABLE `scooter_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sedan_car_parts`
--

DROP TABLE IF EXISTS `sedan_car_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sedan_car_parts` (
  `S_No` int DEFAULT NULL,
  `Part_No` int NOT NULL,
  `Model` varchar(150) DEFAULT NULL,
  `part_Name` varchar(90) DEFAULT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Part_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sedan_car_parts`
--

LOCK TABLES `sedan_car_parts` WRITE;
/*!40000 ALTER TABLE `sedan_car_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `sedan_car_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suv_car_parts`
--

DROP TABLE IF EXISTS `suv_car_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suv_car_parts` (
  `S_No` int DEFAULT NULL,
  `Part_No` int NOT NULL,
  `Model` varchar(150) DEFAULT NULL,
  `part_Name` varchar(90) DEFAULT NULL,
  `Rate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Part_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suv_car_parts`
--

LOCK TABLES `suv_car_parts` WRITE;
/*!40000 ALTER TABLE `suv_car_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `suv_car_parts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-26  5:11:08
