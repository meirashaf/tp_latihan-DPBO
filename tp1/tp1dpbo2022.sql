-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2022 at 06:37 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tp1dpbo2022`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `nama` varchar(1024) NOT NULL,
  `jumlah_buku` int(11) NOT NULL,
  `foto` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `penulis` varchar(1024) DEFAULT NULL,
  `penerbit` varchar(1024) DEFAULT NULL,
  `foto` blob DEFAULT NULL,
  `desc` varchar(1024) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
