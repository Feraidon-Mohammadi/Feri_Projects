<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'Hönig bestellung'


);

get_header(...$args );


?>

<p>Sie haben folgende mengen bestellt</p>

<p>Akazienhoenig:<?php echo $_POST ['akazienhönig'] ; ?> </p>
<p>Heidehoenig:<?php echo $_POST ['heidehönig'] ; ?> </p>
<p>Kleehoenig:<?php echo $_POST ['kleehönig'] ; ?> </p>
<p>Tannenhoenig:<?php echo $_POST ['tannenhönig'] ; ?> </p>

<?php 


$_SESSION['akazienhoenig'] = $_POST['akazienhönig'];
$_SESSION['heidehoenig'] = $_POST['heidehönig'];
$_SESSION['kleehoenig'] = $_POST['kleehönig'];
$_SESSION['tannenhoenig'] = $_POST['tannenhönig'];

?>

<p>weiter zu eingabe persönliche Daten <a href="u_abschluss.php"> nächste page.</a></p>
<p>Folgende Daten sind nun im Session-Cookie gespeichert:</p>

   <?php echo   '<pre>', Var_dump($_SESSION) , '</pre>' ?>



<?php get_footer(); ?>
