-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Jan 2021 pada 21.52
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `freefire`
--

CREATE TABLE `freefire` (
  `JenisPaket` varchar(50) NOT NULL,
  `Harga` varchar(10) NOT NULL,
  `JumlahDiamond` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `freefire`
--

INSERT INTO `freefire` (`JenisPaket`, `Harga`, `JumlahDiamond`) VALUES
('PaketMill', 'Rp.200.000', '1450Diamond'),
('PaketHangar', 'Rp.500.000', '3640Diamond'),
('PaketKhatulistiwa', 'Rp.1.000.0', '7290Diamond');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `Username` varchar(32) NOT NULL,
  `Password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`Username`, `Password`) VALUES
('HaloPenta51', 'qwerty123'),
('Vieta7521', 'SukaPBO'),
('Anjay000', '123456');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mobile legend`
--

CREATE TABLE `mobile legend` (
  `JenisPaket` varchar(50) NOT NULL,
  `Harga` varchar(10) NOT NULL,
  `JumlahDiamond` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `mobile legend`
--

INSERT INTO `mobile legend` (`JenisPaket`, `Harga`, `JumlahDiamond`) VALUES
('PaketMCL', 'Rp.250.000', '875Diamond'),
('PaketMPL', 'Rp.500.000', '2010Diamon'),
('PaketM1', 'Rp.1.000.0', '4700Diamond');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pubg`
--

CREATE TABLE `pubg` (
  `JenisPaket` varchar(50) NOT NULL,
  `Harga` varchar(20) NOT NULL,
  `JumlahDiamond` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pubg`
--

INSERT INTO `pubg` (`JenisPaket`, `Harga`, `JumlahDiamond`) VALUES
('PaketSCAR', 'Rp.200.000', '660UC'),
('PaketM4', 'Rp.400.000', '1800UC'),
('PaketAWM', 'Rp.800.000', '4000UC');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
