-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 11. Jan 2023 um 09:54
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
-- Datenbank: `hotel`
--
CREATE DATABASE IF NOT EXISTS `hotel` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `hotel`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tbl_bookings`
--

CREATE TABLE `tbl_bookings` (
  `bkngs_id` int(11) NOT NULL,
  `bkngs_num_persons` tinyint(1) NOT NULL,
  `bkngs_rooms_id_ref` int(11) NOT NULL,
  `bkngs_users_id_ref` int(11) NOT NULL,
  `bkngs_arr_day` date NOT NULL COMMENT 'Anreisetag',
  `bkngs_dep_day` date NOT NULL COMMENT 'Abreistag',
  `bkngs_status` varchar(1) NOT NULL COMMENT 'Mögl.Wert:a=angefragt, b=bestätigt'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `tbl_bookings`
--

INSERT INTO `tbl_bookings` (`bkngs_id`, `bkngs_num_persons`, `bkngs_rooms_id_ref`, `bkngs_users_id_ref`, `bkngs_arr_day`, `bkngs_dep_day`, `bkngs_status`) VALUES
(1, 4, 1, 2, '0000-00-00', '0000-00-00', ''),
(2, 4, 0, 0, '0000-00-00', '0000-00-00', ''),
(3, 4, 0, 0, '0000-00-00', '0000-00-00', ''),
(4, 4, 0, 0, '0000-00-00', '0000-00-00', ''),
(5, 4, 0, 0, '0000-00-00', '0000-00-00', ''),
(6, 6, 0, 0, '2023-01-12', '2023-01-28', ''),
(7, 7, 0, 0, '2023-01-20', '2023-02-04', '');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tbl_rooms`
--

CREATE TABLE `tbl_rooms` (
  `rooms_id` int(11) NOT NULL,
  `rooms_typ` varchar(10) DEFAULT NULL,
  `rooms_num_beds` tinyint(4) NOT NULL,
  `rooms_img` varchar(100) DEFAULT NULL,
  `rooms_extrabed` tinyint(1) NOT NULL,
  `rooms_equipment` varchar(255) NOT NULL,
  `rooms_price_overnight` decimal(6,0) NOT NULL COMMENT 'Preis pro Übernachtung',
  `rooms_price_breakfest` decimal(6,0) NOT NULL COMMENT 'Preis Frühstück',
  `rooms_price_halfboard` decimal(6,0) NOT NULL COMMENT 'Preis Halbpension'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `tbl_rooms`
--

INSERT INTO `tbl_rooms` (`rooms_id`, `rooms_typ`, `rooms_num_beds`, `rooms_img`, `rooms_extrabed`, `rooms_equipment`, `rooms_price_overnight`, `rooms_price_breakfest`, `rooms_price_halfboard`) VALUES
(1, 'standard', 2, 'img\\standard.jpg\r\n', 2, 'Einzelzimmer 12 qm, Doppelzimmer 16 qm\r\nFrühstücksbuffet\r\nSitzgelegenheit pro Bett\r\nNachttischlampe \r\nWäschefächer\r\n', '100', '20', '70'),
(2, 'komfort', 2, 'img\\komfort.jpg', 2, 'Einzelzimmer 14 qm, Doppelzimmer 20 qm\r\n10% Nichtraucherzimmer\r\n14 Stunden besetzte separate Rezeption, \r\n', '150', '40', '100'),
(3, 'luxus', 3, 'img\\luxus.jpg', 4, 'Einzelzimmer 18 qm, Doppelzimmer 26 qm,\r\nSuiten\r\nmehrsprachige Mitarbeiter\r\nWagenmeisterservice\r\n', '200', '50', '150');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tbl_users`
--

CREATE TABLE `tbl_users` (
  `users_id` int(11) NOT NULL,
  `users_forename` varchar(50) DEFAULT NULL,
  `users_lastname` varchar(50) NOT NULL,
  `users_salutation` varchar(10) NOT NULL COMMENT 'Anrede',
  `users_email` varchar(100) NOT NULL,
  `users_password` varchar(255) NOT NULL,
  `users_company` varchar(50) DEFAULT NULL,
  `users_street` varchar(70) NOT NULL COMMENT 'inkl. Hausnummer',
  `users_city` varchar(40) NOT NULL,
  `users_tel` varchar(20) NOT NULL,
  `users_status` varchar(1) NOT NULL COMMENT 'mögl. Werte: a=Admin, c=Customer'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `tbl_users`
--

INSERT INTO `tbl_users` (`users_id`, `users_forename`, `users_lastname`, `users_salutation`, `users_email`, `users_password`, `users_company`, `users_street`, `users_city`, `users_tel`, `users_status`) VALUES
(5, 'roy', 'ley', '1111', 'roy@gmail.com', '$2y$10$sDh2n3czo.d/O.2y2RDTLuZQAo/AB.csVx46.KMI2zMGCAGpgKp4q', 'comp', 'robin', 'saale', '123345', 'c'),
(8, 'saman', 'mohama', '1245', 'saman@gmail.com', '$2y$10$/VsFqzZr43kwrylrcS4V5eAqF7oYCcPcUtg5gNDaai1kQJVvZ2aO2', 'comp', 'rieth', 'erfurt', '2342', 'a'),
(9, 'feraidon', 'moham', 'f1234', 'feri@gmail.com', '$2y$10$OiGie15njXru8Y35Jot3ouX6vEmadG9jXy.UaUnPTxCQs0yYjckNO', 'comp', 'rieth', 'erfurt', '012345678', 'a'),
(10, '3saman', 'mohama', '34', 'saman3@gmail.com', '$2y$10$kPA2IQYENcckg/w77mntD.OqfCU4gb6izXOgvCPmCU86tFJdvnhw2', 'comp', 'rieth', 'erfurt', '2342', 'c');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `tbl_bookings`
--
ALTER TABLE `tbl_bookings`
  ADD PRIMARY KEY (`bkngs_id`);

--
-- Indizes für die Tabelle `tbl_rooms`
--
ALTER TABLE `tbl_rooms`
  ADD PRIMARY KEY (`rooms_id`);

--
-- Indizes für die Tabelle `tbl_users`
--
ALTER TABLE `tbl_users`
  ADD PRIMARY KEY (`users_id`),
  ADD UNIQUE KEY `users_email` (`users_email`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `tbl_bookings`
--
ALTER TABLE `tbl_bookings`
  MODIFY `bkngs_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT für Tabelle `tbl_rooms`
--
ALTER TABLE `tbl_rooms`
  MODIFY `rooms_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT für Tabelle `tbl_users`
--
ALTER TABLE `tbl_users`
  MODIFY `users_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
