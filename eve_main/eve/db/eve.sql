-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 24, 2022 at 09:37 AM
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
(3, '3', '2', '3', '19-09-2022', '19-09-2022', '1', '2', '5', '100');

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
(1, '2', '3', 'brakes not working', 'P', NULL);

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
(2, 'UoG point', '55.872614', '-4.290292', 'G12 8QQ');

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
(3, '3', '5', '100', '2', 'S', NULL);

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
  `sos_contact` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `firstname`, `lastname`, `username`, `password`, `email`, `age`, `phone`, `user_address`, `user_pincode`, `user_type_id`, `driving_license`, `license_status`, `rides`, `wallet_money`, `sos_contact`) VALUES
(1, 'John', 'Doe', 'JohnD', 'john@doe123', 'john.doe@gmail.com', '27', '9876543210', 'Buchanan View, 33-35 Calgary Street, Glasgow', 'G4 0XG', '2', 'AB12JN31', 'P', '0', '15', '7871230856'),
(2, 'Maria', 'Hill', 'Mhill', 'mhill@123', 'm.hill@gmail.com', '35', '8787676546', 'avenue Building, Glasgow', 'G12 8QQ', '1', 'POI1JJD1', 'S', '3', '20', '');

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
  `status` varchar(1) DEFAULT 'A',
  `service` varchar(1) DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`veh_id`, `veh_name`, `veh_type_id`, `vehicles_kms_run`, `charge_left`, `license_plate`, `station_id`, `status`, `service`) VALUES
(1, 'model car 01', '1', '0', '100', 'ABC123', '1', 'A', 'N'),
(2, 'model car 02', '1', '124', '45', 'NBCH123', '1', 'C', 'N'),
(3, 'model car 03', '1', '15', '90', 'OP123O', '2', 'I', 'Y'),
(4, 'model car 04', '1', '0', '100', 'JUK123J', '2', 'A', 'N'),
(5, 'model cycle 01', '2', '8', '100', 'KIA123K', '1', 'A', 'N'),
(6, 'model cycle 02', '2', '0', '100', 'IUI12J', '2', 'A', 'N'),
(7, 'model sports 01', '3', '35', '100', 'KINF12', '1', 'A', 'N');

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
(3, 'bike sports', 'eve', 'model bike', '2', '15', '12', '15');

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
  `status` varchar(1) DEFAULT 'P'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wallet`
--

INSERT INTO `wallet` (`wid`, `uid`, `card_no`, `cvv`, `exp_date`, `amount`, `status`) VALUES
(1, '2', '1234567890123846', '474', '11-11-2025', '300', 'S'),
(2, '2', '1234567890123846', '474', '11-11-2025', '250', 'P');

--
-- Indexes for dumped tables
--

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
-- AUTO_INCREMENT for table `ongoing_rides`
--
ALTER TABLE `ongoing_rides`
  MODIFY `ride_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `past_rides`
--
ALTER TABLE `past_rides`
  MODIFY `p_ride_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `stations`
--
ALTER TABLE `stations`
  MODIFY `station_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `t_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_type`
--
ALTER TABLE `user_type`
  MODIFY `user_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `veh_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vehicle_type`
--
ALTER TABLE `vehicle_type`
  MODIFY `veh_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `wallet`
--
ALTER TABLE `wallet`
  MODIFY `wid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
