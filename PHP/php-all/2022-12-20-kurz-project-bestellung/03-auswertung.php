<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'sessions-Auswertung, Daten speichern'


);

get_header(...$args );


?>
<p>Sie haben folgende Daten im Formular übertragen:</p>



<p>Vorname: <?php echo $_POST['vorname']; ?></p>
<p>Nachname: <?php echo $_POST['nachname']; ?></p>
<p>Wohnort: <?php echo $_POST['ort']; ?></p>


<?php 
$_SESSION['vorname'] = $_POST['vorname'];
$_SESSION['nachname'] = $_POST['nachname'];
$_SESSION['ort'] = $_POST['ort'];

$_SESSION['zeit'] = time();
?>


<p>Folgende Daten sind nun im Session-Cookie gespeichert:</p>

   <?php echo   '<pre>', Var_dump($_SESSION) , '</pre>' ?>

   <p>Weiter zur <a href="04-auslesen.php">nächsten Seite.</a></p>

<?php get_footer(); ?>