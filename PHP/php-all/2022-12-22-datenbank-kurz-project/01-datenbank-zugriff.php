<?php 

require_once( '../includes/functions.inc.php' );
/*
* get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* )
*/
$args = array(
'Datenbank-zugriff',
    NULL,
    true,
    'Zugriff auf den MariaDB-Server'


);
get_header( ...$args );


define('DB_USER' , 'php-user');
define('DB_PW' , 'w8rkFUE_Ole2n)i2');
define('DB_HOST' , 'localhost');
define('DB_NAME' , 'obstladen');



//Verbindung zum datenbankserver herstellen und Datenbank auswählen
$db = mysqli_connect(DB_HOST, DB_USER, DB_PW, DB_NAME );

// Prüfen, ob die verbindung hergestellt werden konnte 
if( !$db ) {
     exit( '<p>Datenbankverbindung konnte nicht hergestellt werden</p>' );
}
   
/* Verbindung wrude hergestellt. DB-Skripte können ausgeführt werden */
echo '<p>Die DB-Server-Verbindung wurde erfolgreich hergestellt, Die Datenbank '.DB_NAME . 'wurde ausgewählt.</p>';


// Am Ende der Skript-Ausführung muss Die DB-Server-Verbindung geschlossen werden.
mysqli_close( $db );









?>





