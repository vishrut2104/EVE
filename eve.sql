-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2022 at 10:01 PM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eve`
--

-- --------------------------------------------------------

--
-- Table structure for table `damages`
--

CREATE TABLE `damages` (
  `damage_id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `amount` int(5) NOT NULL,
  `veh_id` int(11) NOT NULL,
  `comments` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `damages`
--

INSERT INTO `damages` (`damage_id`, `uid`, `amount`, `veh_id`, `comments`, `status`) VALUES
(1, 4, 150, 2, 'pedals are hard', 'S'),
(2, 4, 150, 4, 'adding again.. breaks not working', 'S'),
(3, 2, 150, 3, 'breaks are bad', 'P'),
(4, 4, 200, 5, 'seat cover is torn', 'S'),
(5, 4, 900, 4, 'adding again.. breaks not working', 'P');

-- --------------------------------------------------------

--
-- Table structure for table `ongoing_rides`
--

CREATE TABLE `ongoing_rides` (
  `ride_id` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `veh_id` varchar(20) NOT NULL,
  `curr_lat` varchar(10) NOT NULL,
  `curr_long` varchar(10) NOT NULL,
  `date_of_booking` varchar(20) NOT NULL,
  `date_of_return` varchar(20) DEFAULT NULL,
  `start_station_id` varchar(5) NOT NULL,
  `end_station_id` varchar(5) NOT NULL,
  `hours` varchar(3) NOT NULL,
  `estimated_price` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `past_rides`
--

CREATE TABLE `past_rides` (
  `p_ride_id` int(11) NOT NULL,
  `ride_id` varchar(20) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `veh_id` varchar(20) NOT NULL,
  `date_of_booking` varchar(20) NOT NULL,
  `date_of_return` varchar(20) NOT NULL,
  `start_station_id` varchar(5) NOT NULL,
  `end_station_id` varchar(5) NOT NULL,
  `hours_rided` varchar(3) NOT NULL,
  `price` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `past_rides`
--

INSERT INTO `past_rides` (`p_ride_id`, `ride_id`, `uid`, `veh_id`, `date_of_booking`, `date_of_return`, `start_station_id`, `end_station_id`, `hours_rided`, `price`) VALUES
(1, '1', '2', '1', '12-09-2022', '12-09-2022', '1', '2', '4', '80'),
(2, '2', '2', '1', '13-09-2022', '13-09-2022', '2', '1', '5', '100'),
(3, '3', '2', '3', '19-09-2022', '19-09-2022', '1', '2', '5', '100'),
(4, '1', '2', '5', '2022-09-25 08:19:30', '2022-09-25 08:19:42', '1', '2', '2', '8'),
(5, '2', '4', '7', '2022-09-25 08:22:09', '2022-09-25 08:22:14', '1', '2', '4', '40'),
(6, '1', '5', '6', '2022-09-29 09:45:26', '2022-09-29 09:45:48', '2', '2', '2', '6'),
(7, '4', '4', '4', '2022-10-27 09:20:42', '2022-10-27 09:21:35', '2', '1', '10', '210'),
(10, '9', '4', '4', '2022-10-27 09:53:30', '2022-10-27 09:55:22', '1', '1', '0.0', '1'),
(11, '10', '4', '4', '2022-10-27 09:57:08', '2022-10-27 09:59:31', '1', '2', '1', '21'),
(12, '11', '4', '8', '2022-10-27 10:24:34', '2022-10-27 10:25:21', '1', '1', '1', '21'),
(13, '12', '4', '8', '2022-10-27 10:26:35', '2022-10-27 10:26:56', '1', '1', '1', '21'),
(14, '13', '4', '2', '2022-10-27 10:39:11', '2022-10-27 10:41:10', '1', '1', '1', '21'),
(15, '14', '4', '8', '2022-10-27 10:48:10', '2022-10-27 10:48:48', '1', '1', '1', '21'),
(16, '1', '2', '5', '2022-10-31 20:03:04', '2022-10-31 20:03:24', '2', '3', '1', '4'),
(17, '2', '2', '6', '2022-10-31 20:10:05', '2022-10-31 20:10:11', '2', '1', '0', '0'),
(18, '3', '2', '1', '2022-10-31 20:11:14', '2022-10-31 20:11:18', '1', '3', '0', '0'),
(19, '5', '2', '4', '2022-10-31 20:11:46', '2022-10-31 20:11:47', '2', '3', '0', '0'),
(20, '6', '2', '9', '2022-10-31 20:12:16', '2022-10-31 20:12:34', '3', '1', '1', '50'),
(21, '4', '4', '1', '2022-10-31 20:11:36', '2022-10-31 20:15:39', '1', '1', '1', '21'),
(22, '7', '4', '2', '2022-10-31 20:16:22', '2022-10-31 20:16:28', '1', '3', '0', '0'),
(23, '8', '2', '10', '2022-10-31 20:29:43', '2022-10-31 20:29:45', '4', '2', '0', '0'),
(24, '9', '2', '1', '2022-10-31 20:29:59', '2022-10-31 20:30:03', '1', '1', '0', '0'),
(25, '10', '2', '6', '2022-10-31 20:30:13', '2022-10-31 20:31:17', '1', '1', '1', '4'),
(26, '1', '4', '5', '2022-11-02 16:12:34', '2022-11-02 18:23:17', '3', '1', '3', '9'),
(27, '1', '4', '8', '2022-11-03 08:50:20', '2022-11-03 10:31:24', '1', '1', '2', '42'),
(28, '2', '2', '9', '2022-11-03 10:31:51', '2022-11-03 10:35:15', '1', '1', '1', '50'),
(29, '3', '4', '5', '2022-11-03 10:38:12', '2022-11-03 10:48:07', '1', '1', '1', '3'),
(30, '4', '4', '1', '2022-11-03 10:51:22', '2022-11-03 10:51:38', '1', '1', '0', '0'),
(31, '1', '2', '1', '2022-11-03 19:37:16', '2022-11-03 19:37:24', '1', '1', '0', '0'),
(32, '2', '2', '4', '2022-11-03 19:37:23', '2022-11-03 19:37:50', '3', '2', '1', '25'),
(33, '3', '2', '6', '2022-11-03 19:38:53', '2022-11-03 19:38:56', '1', '1', '0', '0'),
(34, '4', '2', '8', '2022-11-03 19:42:30', '2022-11-03 19:50:25', '1', '1', '1', '25'),
(35, '5', '2', '3', '2022-11-03 19:53:53', '2022-11-03 19:56:18', '2', '4', '1', '25'),
(36, '7', '4', '9', '2022-11-04 17:13:41', '2022-11-04 17:29:23', '1', '1', '1', '42'),
(37, '8', '4', '12', '2022-11-04 21:00:07', '2022-11-04 21:00:32', '4', '1', '1', '21'),
(38, '6', '2', '5', '2022-11-03 20:05:01', '2022-11-04 21:00:42', '1', '3', '25', '100');

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `r_id` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `veh_id` varchar(20) NOT NULL,
  `comments` varchar(50) DEFAULT NULL,
  `status` varchar(1) DEFAULT 'P',
  `fix_uid` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` (`r_id`, `uid`, `veh_id`, `comments`, `status`, `fix_uid`) VALUES
(1, '2', '3', 'brakes not working', 'F', NULL),
(2, '4', '7', 'pedals are hard', 'R', NULL),
(3, '5', '6', 'breaks are bad', 'R', NULL),
(4, '4', '7', 'adding again.. breaks not working', 'R', NULL),
(5, '4', '8', 'seat cover is torn', 'F', NULL),
(6, '2', '6', 'very nice vehicle good job ', 'P', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `stations`
--

CREATE TABLE `stations` (
  `station_id` int(11) NOT NULL,
  `station_name` varchar(20) NOT NULL,
  `latidute` varchar(10) NOT NULL,
  `longitude` varchar(10) NOT NULL,
  `pincode` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stations`
--

INSERT INTO `stations` (`station_id`, `station_name`, `latidute`, `longitude`, `pincode`) VALUES
(1, 'Buchanan point', '55.865905', '-4.252024', 'G4 0LU'),
(2, 'UoG point', '55.872614', '-4.290292', 'G12 8QQ'),
(3, 'hillhead', '55.875404', '-4.293552', 'G12 8SH'),
(4, 'Firhill Stadium', '55.881595', '-4.270718', 'G20 7AH');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `t_id` int(11) NOT NULL,
  `p_ride_id` varchar(20) NOT NULL,
  `hours_rided` varchar(3) NOT NULL,
  `price` varchar(5) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `payment_status` varchar(1) DEFAULT 'P',
  `comments` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`t_id`, `p_ride_id`, `hours_rided`, `price`, `uid`, `payment_status`, `comments`) VALUES
(1, '1', '4', '80', '2', 'S', NULL),
(2, '2', '5', '100', '2', 'S', NULL),
(3, '3', '5', '100', '2', 'S', NULL),
(4, '4', '2', '8', '2', 'P', 'testing'),
(5, '5', '4', '40', '4', 'P', 'testing'),
(6, '6', '2', '6', '5', 'P', 'testing'),
(7, '7', '10', '210', '4', 'P', 'testing'),
(8, '10', '0.0', '1', '4', 'P', 'testing'),
(9, '11', '1', '21', '4', 'P', 'testing'),
(10, '12', '1', '21', '4', 'P', 'testing'),
(11, '13', '1', '21', '4', 'P', 'testing'),
(12, '14', '1', '21', '4', 'P', 'testing'),
(13, '15', '1', '21', '4', 'P', 'testing'),
(14, '16', '1', '4', '2', 'P', 'testing'),
(15, '17', '0', '0', '2', 'P', 'testing'),
(16, '18', '0', '0', '2', 'P', 'testing'),
(17, '19', '0', '0', '2', 'P', 'testing'),
(18, '20', '1', '50', '2', 'P', 'testing'),
(19, '21', '1', '21', '4', 'P', 'testing'),
(20, '22', '0', '0', '4', 'P', 'testing'),
(21, '23', '0', '0', '2', 'P', 'testing'),
(22, '24', '0', '0', '2', 'P', 'testing'),
(23, '25', '1', '4', '2', 'P', 'testing'),
(24, '26', '3', '9', '4', 'P', 'testing'),
(25, '27', '2', '42', '4', 'P', 'testing'),
(26, '28', '1', '50', '2', 'P', 'testing'),
(27, '29', '1', '3', '4', 'P', 'testing'),
(28, '30', '0', '0', '4', 'P', 'testing'),
(29, '31', '0', '0', '2', 'P', 'testing'),
(30, '32', '1', '25', '2', 'P', 'testing'),
(31, '33', '0', '0', '2', 'P', 'testing'),
(32, '34', '1', '25', '2', 'P', 'testing'),
(33, '35', '1', '25', '2', 'P', 'testing'),
(34, '36', '1', '42', '4', 'P', 'testing'),
(35, '37', '1', '21', '4', 'P', 'testing'),
(36, '38', '25', '100', '2', 'P', 'testing');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `uid` int(11) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  `email` varchar(25) NOT NULL,
  `age` varchar(3) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `user_address` varchar(50) NOT NULL,
  `user_pincode` varchar(7) NOT NULL,
  `user_type_id` varchar(1) NOT NULL,
  `driving_license` varchar(14) DEFAULT NULL,
  `license_status` varchar(1) DEFAULT 'P',
  `rides` varchar(3) DEFAULT '0',
  `wallet_money` varchar(7) DEFAULT '0',
  `sos_contact` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `firstname`, `lastname`, `username`, `password`, `email`, `age`, `phone`, `user_address`, `user_pincode`, `user_type_id`, `driving_license`, `license_status`, `rides`, `wallet_money`, `sos_contact`) VALUES
(1, 'John', 'Doe', 'JohnD', 'john@doe123', 'john.doe@gmail.com', '27', '9876543210', 'Buchanan View, 33-35 Calgary Street, Glasgow', 'G4 0XG', '2', 'AB12JN31', 'P', '0', '15', '7871230856'),
(2, 'Maria', 'Hill', 'Mhill', 'mhill@123', 'm.hill@gmail.com', '35', '8787676546', 'avenue Building, Glasgow', 'G12 8QQ', '1', 'POI1JJD1', 'S', '19', '29', ''),
(4, 'satwik', 'ghanta', 'yasat', '1234', 'satwik.ynghanta@gmail.com', '24', '7442243720', 'Buchanan View, 33-35 Calgary Street, Glasgow', 'G40XG', '2', '', 'P', '16', '982', 'ghantasat007@gmail.com'),
(6, 'danni', 'summers', 'dannix', '1234', 'danni@gmail.com', '22', '7788776622', 'foundary court, 37 Calgary Street, Glasgow', 'G4 0XG', '2', '', 'P', '0', '0', ''),
(7, 'Adam', 'Smith', 'asmith', '1234', 'asmith@gmail.com', '34', '07896578272', 'Bridle Works, Buchanan Galleries', 'G10XG', '3', '998788982617', 'S', '0', '0', NULL),
(8, 'john', 'doe', 'jd', '1234', 'jd@gmail.com', '44', '07867568162', 'Bridle Works, Buchanan Galleries', 'G10XG', '4', NULL, 'P', '0', '0', NULL),
(9, 'Mingrui', 'Fang', 'FMingrui', '123456', '', '', '', '', '', '2', '', 'P', '0', '50', ''),
(10, 'vishrut', 'jain', 'vishrut_j', 'vishrutjain', 'vishrutjain.8k@gmail.com', '22', '7741540140', '123 cathedral street', 'G1 2BQ', '1', 'as dads', 'P', '0', '0', 'vishrutjain.8k@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `user_type`
--

CREATE TABLE `user_type` (
  `user_type_id` int(11) NOT NULL,
  `user_type_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_type`
--

INSERT INTO `user_type` (`user_type_id`, `user_type_name`) VALUES
(1, 'common'),
(2, 'student'),
(3, 'operator'),
(4, 'manager'),
(5, 'repair');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `veh_id` int(11) NOT NULL,
  `veh_name` varchar(20) NOT NULL,
  `veh_type_id` varchar(3) NOT NULL,
  `vehicles_kms_run` varchar(5) DEFAULT '0',
  `charge_left` varchar(3) DEFAULT '100',
  `license_plate` varchar(8) DEFAULT NULL,
  `station_id` varchar(5) DEFAULT NULL,
  `status` varchar(3) DEFAULT 'A',
  `service` varchar(3) DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`veh_id`, `veh_name`, `veh_type_id`, `vehicles_kms_run`, `charge_left`, `license_plate`, `station_id`, `status`, `service`) VALUES
(1, 'model car 01', '1', '0', '100', 'ABC123', '1', 'C', 'N'),
(2, 'model car 02', '1', '124', '100', 'NBCH123', '3', 'A', 'N'),
(3, 'model car 03', '1', '15', '100', 'OP123O', '4', 'A', 'N'),
(4, 'model car 04', '1', '0', '96', 'JUK123J', '2', 'C', 'N'),
(5, 'model cycle 01', '2', '8', '-21', 'KIA123K', '3', 'C', 'N'),
(6, 'model cycle 02', '2', '0', '100', 'IUI12J', '2', 'I', 'Y'),
(7, 'model sports 01', '3', '35', '100', 'KINF12', '3', 'I', 'Y'),
(8, 'zoomer car 1', '1', '0', '100', '1adws121', '1', 'A', 'N'),
(9, 'fsx1-01', '5', '0', '100', '7uyy6h1u', '3', 'A', 'N'),
(10, 'model car 01', '1', '0', '100', '110', '2', 'C', 'N'),
(11, 'zoomer car 2', '1', '0', '100', '11331231', '4', 'A', 'N'),
(12, 'zoomer car 3', '1', '0', '96', '53453356', '1', 'C', 'N'),
(13, 'zoomer car 4', '1', '0', '100', 'h6rg5rtw', '4', 'A', 'N');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_type`
--

CREATE TABLE `vehicle_type` (
  `veh_type_id` int(11) NOT NULL,
  `vehicle_type_name` varchar(15) NOT NULL,
  `vehicle_company` varchar(15) NOT NULL,
  `vehicle_model` varchar(15) NOT NULL,
  `vehicle_seating_capacity` varchar(2) NOT NULL,
  `kms_charge` varchar(3) NOT NULL,
  `price_hour` varchar(3) NOT NULL,
  `student_discount` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle_type`
--

INSERT INTO `vehicle_type` (`veh_type_id`, `vehicle_type_name`, `vehicle_company`, `vehicle_model`, `vehicle_seating_capacity`, `kms_charge`, `price_hour`, `student_discount`) VALUES
(1, 'car sedan', 'eve', 'model car', '5', '30', '25', '15'),
(2, 'bike cycle', 'eve', 'model cycle', '1', '8', '4', '15'),
(3, 'bike sports', 'eve', 'model bike', '2', '15', '12', '15'),
(4, 'car suv', 'eve', 'model suv', '7', '35', '28', '15'),
(5, 'Fast Series X', 'RF', 'model X1', '2', '22', '50', '15'),
(6, 'car sedan', 'Tesla', 'model car 01', '5', '20', '30', '10');

-- --------------------------------------------------------

--
-- Table structure for table `wallet`
--

CREATE TABLE `wallet` (
  `wid` int(11) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `card_no` varchar(16) NOT NULL,
  `cvv` varchar(5) NOT NULL,
  `exp_date` varchar(12) NOT NULL,
  `amount` varchar(5) NOT NULL,
  `status` varchar(1) DEFAULT 'P',
  `date_of_adding` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wallet`
--

INSERT INTO `wallet` (`wid`, `uid`, `card_no`, `cvv`, `exp_date`, `amount`, `status`, `date_of_adding`) VALUES
(1, '2', '1234567890123846', '474', '11-11-2025', '300', 'S', '2022-10-15'),
(2, '2', '1234567890123846', '474', '11-11-2025', '250', 'S', '2022-10-15'),
(3, '4', '1234123412341234', '112', '11-11-2025', '300', 'S', '2022-10-15'),
(4, '5', '21314432132', '2131', '12-11-2000', '100', 'S', '2022-10-15'),
(5, '4', '123123123124', '123', '2024-06-11', '150', 'S', '2022-10-15'),
(6, '4', '123123123124', '123', '2024-06-11', '150', 'S', '2022-10-15'),
(7, '4', '123123123124', '123', '2022-10-19', '130', 'S', '2022-10-15'),
(8, '4', '123123123124', '123', '2022-10-13', '123', 'S', '2022-10-15'),
(9, '4', '', '', '', '', 'R', '2022-10-15'),
(10, '4', '1234', '123', '2022-10-19', '123', 'S', '2022-10-15'),
(11, '4', '1231231231', '123', '2022-10-25', '100', 'S', '2022-10-15'),
(12, '4', '12311231231', '123', '2022-10-25', '150', 'S', '2022-10-15'),
(13, '2', '23453465456', '122', '2022-11-10', '50', 'S', '2022-10-15'),
(14, '', '1234567890123456', '123', '2019-08-02', '', 'S', '2022-10-15'),
(15, '', '1234567890123456', '123', '2019-08-02', '', 'S', '2022-10-15'),
(16, '9', '1234567890123456', '123', '2026-06-26', '50', 'S', '2022-10-15'),
(17, '4', '12351341123', '111', '2022-12-03', '300', 'S', '2022-11-04 20:11:38');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `damages`
--
ALTER TABLE `damages`
  ADD PRIMARY KEY (`damage_id`);

--
-- Indexes for table `ongoing_rides`
--
ALTER TABLE `ongoing_rides`
  ADD PRIMARY KEY (`ride_id`);

--
-- Indexes for table `past_rides`
--
ALTER TABLE `past_rides`
  ADD PRIMARY KEY (`p_ride_id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`r_id`);

--
-- Indexes for table `stations`
--
ALTER TABLE `stations`
  ADD PRIMARY KEY (`station_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`t_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `user_type`
--
ALTER TABLE `user_type`
  ADD PRIMARY KEY (`user_type_id`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`veh_id`);

--
-- Indexes for table `vehicle_type`
--
ALTER TABLE `vehicle_type`
  ADD PRIMARY KEY (`veh_type_id`);

--
-- Indexes for table `wallet`
--
ALTER TABLE `wallet`
  ADD PRIMARY KEY (`wid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `damages`
--
ALTER TABLE `damages`
  MODIFY `damage_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `ongoing_rides`
--
ALTER TABLE `ongoing_rides`
  MODIFY `ride_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `past_rides`
--
ALTER TABLE `past_rides`
  MODIFY `p_ride_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `stations`
--
ALTER TABLE `stations`
  MODIFY `station_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `t_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user_type`
--
ALTER TABLE `user_type`
  MODIFY `user_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `veh_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `vehicle_type`
--
ALTER TABLE `vehicle_type`
  MODIFY `veh_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `wallet`
--
ALTER TABLE `wallet`
  MODIFY `wid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
