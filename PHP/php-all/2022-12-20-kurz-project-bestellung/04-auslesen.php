<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'sessions-Daten auslesen'


);

get_header(...$args );


?>

<p>Die Daten aus dem session-Cookie:</p>
<ul>
    <?php 
     foreach( $_SESSION as $key => $value ) {
     echo "<li>$key: $value</li>";

     }

    ?>

</ul>
<?php echo '<pre>' , print_r($_POST, true ), '</pre>'; ?>
<p>Weiter zur <a href="05-session-zerstoern.php">nächste Seite</a>.</p>

<?php get_footer(); ?>

