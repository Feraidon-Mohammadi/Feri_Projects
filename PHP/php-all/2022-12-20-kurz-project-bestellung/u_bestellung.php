<?php
session_start();
require_once '../../includes/functions.inc.php';
$args = array(
    'Bestellübersicht',
    NULL,
    true,
    'Honigbestellung'
);
get_header(...$args);
?>

<p class="lead">Sie haben folgende Mengen bestellt.</p>

<p>

<?php
    
if( !empty( $_POST ) ) {
    foreach( $_POST as $artikel => $menge ) {
        if( is_numeric( $menge ) && (int)$menge > 0 ) {
            $_SESSION[$artikel] = (int)$menge;
            echo "$artikel: <b>$menge Gläser</b></br>";
        }
    }
}
    
?>

</p>

<p>Die Session-ID lautet: <?php echo session_id(); ?></p>

<p><a href="u_abschluss.php">Weiter zur Eingabe persönlicher Daten</a> und dem Abschluss der Bestellung.</p>

<?php get_footer(true, false); ?>