<?php 


// konstanten für die zugangsdaten anlegen 
define('DB_DSN', 'mysql:host=localhost;port=3306;dbname=' . $database . ';charset=utf8');
define('DB_USER', 'php-user');
define('DB_PW', 'w8rkFUE_Ole2n)i2');


//  verbindung zum Datenbank-Server aufnehmen
$db = new PDO( DB_DSN, DB_USER, DB_PW);















?>