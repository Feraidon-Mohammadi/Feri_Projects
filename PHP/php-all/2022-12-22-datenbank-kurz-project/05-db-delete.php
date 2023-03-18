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
* )
 */
$args = array(
'Daten Löschen',
NULL,
true,
'Ausgewählte Datensätze löschen'


);
get_header( ...$args );
require_once( '../includes/db-connect.inc.php' );


$sql = ' DELETE FROM `tbl_bestellungen`
    WHERE `bstlg_id` = 13';

if( $result = mysqli_query( $db, $sql ) ){

    $anzahl = mysqli_affected_rows( $db );
    echo "<p>$anzahl Datensätze wurden geändert .</p>";

}else {
    echo get_db_error( $db, $sql );


}


mysqli_close( $db );
?>
    
<?php get_footer(); ?>