<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'sessions-Auswertung, Daten zerstoeren'



);

get_header(...$args );

/* EINZELN einträge aus session -Array loschen */



echo '<pre>', print_r( $_SESSION, true ), '</pre>';
unset ($_SESSION ['vorname'] );
echo '<pre>', print_r( $_SESSION, true ), '</pre>';

//1 .Session Array leeren /*======================================================================================================================================================================================= */
$_SESSION = array();

echo '<p>Die Session mit der ID: ' . session_id( ) . ' wurde ';
/* 2.Session zerstoeren  */
if(session_destroy() ) {
    echo '<b>erfolgreich zerstört</b>';

} else {
    echo '<b>nicht terstört</b>';
}
echo '</p>';
get_footer();

?>