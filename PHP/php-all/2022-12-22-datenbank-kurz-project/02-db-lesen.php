<?php
require_once( '../includes/functions.inc.php' );
$database = 'obstladen';
/* * get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* ) */

$args = array(
    'DB-lesen',
    NULL,
    true,
    'Informationen aus einer Datenbank lesen'
    
);

get_header( ...$args );
require_once( '../includes/db-connect.inc.php' );



/* Eine abfrage tum lesen erstellen  */
    $sql = "SELECT `bstlg_nachname`, `bstlg_sorte`, `bstlg_menge` FROM `tbl_bestellungen`;";






    /* /////////test fehler instead of the last text in 27 switch need to see fehler or error//////// */

    /* $sql = "SELECT `bstlg_nachname`,. `bstlg_sorte`, `bstlg_menge` FROM `tbl_bestellungen`;"; */



/* abfrage and den DB-Server senden  */
    if( $result = mysqli_query( $db, $sql ) ) {


/* abgrage war korrekt Ausgabe der  Anzahl der gefundenen Datensätze  */
    $anzahl = mysqli_num_rows( $result );
    echo "<p class=\"alert alert-success\">Es wurden <b>$anzahl</b> Datensätze gefunden.</p>";



    while($erg = mysqli_fetch_array( $result, MYSQLI_ASSOC) ) {  
    
        echo '<p>NAME: ' . $erg['bstlg_nachname'] . ',<br>
                Sorte: ' . $erg['bstlg_sorte'] . ',<br>
                Menge: ' . $erg['bstlg_menge'] . 'kg</p>';
    }

}else {


    /* Abfrage war nicht korrekt  */
    echo '<p calss=alert aler-danger">Fehlerhafte Abfrage<br>';



/*  Fehlernummer und -medlung von DB-Server */
$errnum = mysqli_errno( $db);
$errmsg = mysqli_errno( $db);

echo "Fehler-Nr: <b>$errnum</b><br>Fehler-Meldung: <b>$errmsg</b></p> ";

 echo get_db_error($db, $sql );


}



mysqli_close($db );

?>

   
<?php get_footer(); ?>