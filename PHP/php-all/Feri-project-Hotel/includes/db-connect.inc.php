<?php 

/*   
*Ausgabe von MySQLI Fehlermeldungen erzwingen 
*Der Standard-Wert wurde mit php 8.1 geändert
 */


 mysqli_report( MYSQLI_REPORT_OFF);


 /* Konstanten für die zugangdaten anlegen */
 
define('DB_USER' , 'php-user');
define('DB_PW' , 'w8rkFUE_Ole2n)i2');
define('DB_HOST' , 'localhost');
define('DB_NAME' , $database);



$db = mysqli_connect( DB_HOST, DB_USER, DB_PW )
    or die( '<p class="alert alert-danger">Die DB-Server-Verbidung konnte nicht  hergestellt werden.</p>');

    /* zeichensatz für die DB-Server-Verbindung explizit einstellen  */
    mysqli_set_charset($db, 'urf8mb4');

    /* Datenbank auswählen  */
    mysqli_select_db( $db, DB_NAME)
    or die( '<p class ="alert alert-danger">Die Datenbank <b>' . DB_NAME . '</b>konnte nicht ausgewählt werden.</p>');


