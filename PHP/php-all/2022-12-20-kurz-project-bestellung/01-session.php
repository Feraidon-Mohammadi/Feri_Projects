<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'sessions-Startseite'


);

get_header(...$args );


?>

<h2>Die Session wurde gestartet</h2>

<p>Session-ID: <?php echo session_id(); ?><br>
Name der Session:<?php echo session_name(); ?></p>

<p>Weiter zu <a href="02-formular.php">nächsten Seite.</a></p>

<?php get_footer(); ?>