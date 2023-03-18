<?php
session_start();
require_once '../../includes/functions.inc.php';
$args = array(
    'Kasse',
    NULL,
    true,
    'Honigbestellung - Abschluss'
);
get_header(...$args);

if( empty( $_POST ) ):
    /* Wenn $_POST leer ist: Formular anzeigen */
?>

<p class="lead">Bitte geben Sie noch Ihre Kontaktdaten ein</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    <div class="form-group mb-3">
        <label for="vorname">Vorname</label>
        <input type="text" name="vname" id="vorname" class="form-control">
    </div>

    <div class="form-group mb-3">
        <label for="nachname">Nachname</label>
        <input type="text" name="nname" id="nachname" class="form-control">
    </div>

    <div class="form-group mb-3">
        <label for="ort">Wohnort</label>
        <input type="text" name="ort" id="ort" class="form-control">
    </div>

    <div class="form-group mb-3">
        <label for="email">Mailadresse</label>
        <input type="email" name="email" id="email" class="form-control">
    </div>

    <!-- Emmet-Code -> button:submit.btn.btn-primary -->
    <button type="submit" class="btn btn-primary">Abschicken</button>
</form>

<?php else: ?>

    <p class="lead">Dies sind die in der Session gespeicherten Daten:</p>

    <?php
        
    /* Daten aus dem $_POST-Array zum $_SESSION-Array hinzufügen */
    foreach( $_POST as $key => $value ) {
        $_SESSION[$key] = $value;
    }

    /* Alle Daten aus Session ausgeben */
    echo '<p>';
    foreach( $_SESSION as $key => $value ) {
        echo "$key: <b>$value</b><br>";
    }
    echo '</p>';

    /* Session beenden, Array leeren und Session zerstören */
    $_SESSION = array();
    session_destroy();
        
    ?>

    <p>Damit ist die Session beendet. <a href="u_formular.php">Klicken Sie hier</a>, um eine neue Session zu beginnen.</p>

<?php 
    endif;
    get_footer(true,false); 
?>