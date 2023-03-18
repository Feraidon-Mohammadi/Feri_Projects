<?php 

require_once( '../includes/functions.inc.php' );

$database = 'homepage';



$args = array(
    'Newsletter-Eintragung',
        NULL,
        true,
        'Newsletter php homepage'
    
    
    );
    get_header( ...$args );



    define('DB_NAME' , 'php-user');
    define('DB_PW' , 'w8rkFUE_Ole2n)i2');
    define('DB_HOST' , 'localhost');
    define('DB_NAME' , 'homepage');
    

    $db = mysqli_connect(DB_HOST, DB_USER, DB_PW, DB_NAME );
   /*  $db = mysqli_connect(DB_HOST, DB_USER, DB_PW, DB_NAME ); */
    
    
    if( !$db ) {
        exit( '<p>Datenbankverbindung konnte nicht hergestellt werden</p>' );
   }
      
   echo '<p>Die DB-Server-Verbindung wurde erfolgreich hergestellt, Die Datenbank '.DB_NAME . 'wurde ausgewählt.</p>';


   mysqli_close( $db );












?>