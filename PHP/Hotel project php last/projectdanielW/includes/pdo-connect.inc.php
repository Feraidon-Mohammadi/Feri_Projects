<?php
define('DB_DSN','mysql:host=localhost;port=3306;dbname=' . $database .';charset =utf8');
define ('DB_USER' , 'php-user');
define( 'DB_PW' , '!l.rr6N/wZaK9tE]');
#const DB_NAME = $database;



mysqli_report(MYSQLI_REPORT_OFF);//erzwingt sql fehlermeldungen
//connect 
$db = new PDO(DB_DSN, DB_USER, DB_PW);
    
?>