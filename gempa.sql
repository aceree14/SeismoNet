-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Jun 2024 pada 11.54
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gempa`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `earthquake`
--

CREATE TABLE `earthquake` (
  `id` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL,
  `Jam` varchar(255) DEFAULT NULL,
  `DateTime` varchar(255) DEFAULT NULL,
  `Coordinates` varchar(255) DEFAULT NULL,
  `Lintang` varchar(255) DEFAULT NULL,
  `Bujur` varchar(255) DEFAULT NULL,
  `Magnitude` varchar(255) DEFAULT NULL,
  `Kedalaman` varchar(255) DEFAULT NULL,
  `Wilayah` varchar(255) DEFAULT NULL,
  `Potensi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `earthquake`
--

INSERT INTO `earthquake` (`id`, `Tanggal`, `Jam`, `DateTime`, `Coordinates`, `Lintang`, `Bujur`, `Magnitude`, `Kedalaman`, `Wilayah`, `Potensi`) VALUES
(1, '15 Jun 2024', '20:08:15 WIB', '2024-06-15T13:08:15+00:00', '3.16,127.27', '3.16 LU', '127.27 BT', '5.7', '10 km', '112 km BaratLaut PULAUDOI-MALUT', 'Tidak berpotensi tsunami'),
(2, '14 Jun 2024', '15:18:46 WIB', '2024-06-14T08:18:46+00:00', '2.26,128.14', '2.26 LU', '128.14 BT', '5.0', '151 km', '29 km BaratLaut DARUBA-MALUT', 'Tidak berpotensi tsunami'),
(3, '14 Jun 2024', '02:44:01 WIB', '2024-06-13T19:44:01+00:00', '5.65,126.22', '5.65 LU', '126.22 BT', '5.0', '93 km', '137 km BaratLaut PULAUKARATUNG-SULUT', 'Tidak berpotensi tsunami'),
(4, '13 Jun 2024', '00:01:23 WIB', '2024-06-12T17:01:23+00:00', '4.36,126.65', '4.36 LU', '126.65 BT', '6.0', '30 km', '40 km BaratLaut MELONGUANE-SULUT', 'Tidak berpotensi tsunami'),
(5, '12 Jun 2024', '10:45:23 WIB', '2024-06-12T03:45:23+00:00', '-3.33,142.43', '3.33 LS', '142.43 BT', '5.1', '10 km', '132 km BaratLaut WEWAK-PNG', 'Tidak berpotensi tsunami'),
(6, '09 Jun 2024', '08:04:46 WIB', '2024-06-09T01:04:46+00:00', '4.88,126.24', '4.88 LU', '126.24 BT', '5.1', '54 km', '94 km BaratLaut PULAUKARATUNG-SULUT', 'Tidak berpotensi tsunami'),
(7, '07 Jun 2024', '23:31:06 WIB', '2024-06-07T16:31:06+00:00', '-2.86,139.37', '2.86 LS', '139.37 BT', '5.8', '45 km', '95 km TimurLaut KOBAGMA-PAPUAPGNGN', 'Tidak berpotensi tsunami'),
(8, '07 Jun 2024', '05:00:52 WIB', '2024-06-06T22:00:52+00:00', '-2.72,142.32', '2.72 LS', '142.32 BT', '5.1', '10 km', '170 km BaratLaut WEWAK-PNG', 'Tidak berpotensi tsunami'),
(9, '06 Jun 2024', '20:15:40 WIB', '2024-06-06T13:15:40+00:00', '-9.11,116.94', '9.11 LS', '116.94 BT', '5.1', '10 km', '40 km Tenggara SUMBAWABARAT-NTB', 'Tidak berpotensi tsunami'),
(10, '05 Jun 2024', '18:16:14 WIB', '2024-06-05T11:16:14+00:00', '0.42,98.50', '0.42 LU', '98.50 BT', '5.7', '57 km', '78 km Tenggara NIASSELATAN-SUMUT', 'Tidak berpotensi tsunami'),
(11, '05 Jun 2024', '09:20:28 WIB', '2024-06-05T02:20:28+00:00', '-3.76,100.54', '3.76 LS', '100.54 BT', '5.7', '34 km', '146 km BaratDaya MUKOMUKO-BENGKULU', 'Tidak berpotensi tsunami'),
(12, '03 Jun 2024', '04:43:44 WIB', '2024-06-02T21:43:44+00:00', '-2.77,138.89', '2.77 LS', '138.89 BT', '5.0', '31 km', '77 km Tenggara MAMBERAMOTENGAH-PAPUAPGNGN', 'Tidak berpotensi tsunami'),
(13, '02 Jun 2024', '16:22:04 WIB', '2024-06-02T09:22:04+00:00', '2.02,127.71', '2.02 LU', '127.71 BT', '5.1', '222 km', '30 km BaratDaya PULAUDOI-MALUT', 'Tidak berpotensi tsunami'),
(14, '01 Jun 2024', '18:01:40 WIB', '2024-06-01T11:01:40+00:00', '-1.51,134.53', '1.51 LS', '134.53 BT', '5.2', '11 km', '41 km Tenggara RANSIKI-PAPUABRT', 'Tidak berpotensi tsunami'),
(15, '07 Jun 2024', '01:57:39 WIB', '2024-06-06T18:57:39+00:00', '-7.36,121.04', '7.36 LS', '121.04 BT', '5.3', '537 km', '133 km Tenggara SELAYAR-SULSEL', 'Tidak berpotensi tsunami');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `earthquake`
--
ALTER TABLE `earthquake`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `earthquake`
--
ALTER TABLE `earthquake`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
