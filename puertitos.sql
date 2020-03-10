-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-03-2020 a las 19:22:12
-- Versión del servidor: 10.1.39-MariaDB
-- Versión de PHP: 7.1.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `puertitos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bitacora`
--

CREATE TABLE `bitacora` (
  `ip` varchar(20) NOT NULL,
  `puertos` varchar(20) NOT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `servicio` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `bitacora`
--

INSERT INTO `bitacora` (`ip`, `puertos`, `estado`, `servicio`) VALUES
('200.33.171.13', '139/tcp', 'open', 'netbios-ssn'),
('200.33.171.13', '2000/tcp', 'open', 'cisco-sccp'),
('200.33.171.13', '22/tcp', 'open', 'ssh'),
('200.33.171.13', '445/tcp', 'open', 'microsoft-ds'),
('200.33.171.13', '5060/tcp', 'open', 'sip'),
('200.33.171.13', '80/tcp', 'open', 'http');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bitacora`
--
ALTER TABLE `bitacora`
  ADD PRIMARY KEY (`ip`,`puertos`,`servicio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
