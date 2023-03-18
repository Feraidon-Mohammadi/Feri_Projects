<?php
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'Blog - Registrierung';
$page_header = NULL;

include_once '_header.php';

// Prüfe, ob das Formular gesendet wurde
if( !empty($_POST) ) {
    // Variablen definieren
    $users_name = $_POST['users_name'] ?? NULL;
    $users_password = password_hash( $_POST['users_password'], PASSWORD_DEFAULT );

    // SQL-Anweisung vorbereiten, Platzhalter (?) für Werte werden benutzt
    $sql = 'INSERT INTO `tbl_users`
    (
        `users_name`,
        `users_password`
    )
    VALUES
    ( ?, ? );';

    // SQL-Anweisung an den Datenbankserver senden
    $stmt = $db->prepare( $sql );

    // Datenbankserver anweisen die vorbereitete SQL-Anweisung mit den ersetzten Platzhaltern auszuführen
    if( $stmt->execute( array( $users_name, $users_password ) ) ) {
        echo '<p class="alert alert-success">Der Benutzer ' . $users_name . ' wurde angelegt</p>'; 
    } else {
        echo '<p class="alert alert-danger">Benutzer konnte nicht angelegt werden.</p>';
    }

    $stmt = NULL;
}
?>

<p class="lead">Bitte geben Sie einen Benutzernamen und ein Passwort ein.</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
    <p>
        <input type="text" name="users_name" placeholder="Benutzername eintragen">
    </p>

    <p>
        <input type="password" name="users_password" placeholder="Passwort">
    </p>

    <p>
        <button type="submit" class="btn btn-primary">Registrieren</button>
    </p>

</form>

<?php get_footer(); ?>