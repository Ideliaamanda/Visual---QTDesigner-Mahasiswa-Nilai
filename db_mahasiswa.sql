-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2025 at 11:50 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `mhs`
--

CREATE TABLE `mhs` (
  `npm` varchar(100) NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `nama_panggilan` varchar(100) NOT NULL,
  `telepon` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `kelas` varchar(100) NOT NULL,
  `mata_kuliah` varchar(50) NOT NULL,
  `lokasi_kampus` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mhs`
--

INSERT INTO `mhs` (`npm`, `nama_lengkap`, `nama_panggilan`, `telepon`, `email`, `kelas`, `mata_kuliah`, `lokasi_kampus`) VALUES
('2310010271', 'idelia amanda putri', 'idelia', '081928939', 'idelia@gmail.com', '4m reguler pagi', 'visual 2', 'uniska');

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `field_id` varchar(100) NOT NULL,
  `id_mahasiswa` varchar(100) NOT NULL,
  `nilai_harian` varchar(100) NOT NULL,
  `nilai_tgs` varchar(100) NOT NULL,
  `nilai_uts` varchar(100) NOT NULL,
  `nilai_uas` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nilai`
--

INSERT INTO `nilai` (`field_id`, `id_mahasiswa`, `nilai_harian`, `nilai_tgs`, `nilai_uts`, `nilai_uas`) VALUES
('F001', 'MHS001', '95', '90', '80', '90'),
('F002', 'MHS090', '75', '80', '70', '70'),
('F003', 'MHS091', '85', '90', '90', '85'),
('F004', 'MHS085', '70', '80', '80', '75'),
('F005', 'MHS066', '90', '100', '95', '90');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mhs`
--
ALTER TABLE `mhs`
  ADD PRIMARY KEY (`npm`);

--
-- Indexes for table `nilai`
--
ALTER TABLE `nilai`
  ADD PRIMARY KEY (`field_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
