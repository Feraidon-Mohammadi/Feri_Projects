-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 23. Dez 2022 um 11:13
-- Server-Version: 10.4.27-MariaDB
-- PHP-Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `obstladen`
--
CREATE DATABASE IF NOT EXISTS `obstladen` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `obstladen`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tbl_bestellungen`
--

CREATE TABLE `tbl_bestellungen` (
  `bstlg_id` int(11) NOT NULL,
  `bstlg_vorname` varchar(50) DEFAULT NULL,
  `bstlg_nachname` varchar(50) NOT NULL,
  `bstlg_email` varchar(150) NOT NULL,
  `bstlg_ort` varchar(50) NOT NULL,
  `bstlg_sorte` varchar(20) NOT NULL,
  `bstlg_menge` tinyint(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `tbl_bestellungen`
--

INSERT INTO `tbl_bestellungen` (`bstlg_id`, `bstlg_vorname`, `bstlg_nachname`, `bstlg_email`, `bstlg_ort`, `bstlg_sorte`, `bstlg_menge`) VALUES
(2, 'Corinna', 'Delphi', 'Corinna_dephi@abcd.de', 'Hamburg', 'Jonagold', 3),
(4, 'Peter', 'Schmidt', 'peter_schmidt@web.de', 'Berlin', 'Eistar', 25),
(14, 'Heinz', 'Müller', 'Henz_müller@gmail.com', 'Gotha', 'Boskoop', 8);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `tbl_bestellungen`
--
ALTER TABLE `tbl_bestellungen`
  ADD PRIMARY KEY (`bstlg_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `tbl_bestellungen`
--
ALTER TABLE `tbl_bestellungen`
  MODIFY `bstlg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
