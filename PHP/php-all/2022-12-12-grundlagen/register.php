<?php
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - Registrierung';
$page_header = NULL;

include_once '_header.php';

// Prüfe, ob das Formular gesendet wurde
if( !empty($_POST) ) {
    // Variablen definieren
    $users_forename = $_POST['users_forename'] ?? NULL;
    $users_password = password_hash( $_POST['users_password'], PASSWORD_DEFAULT );

   
    $users_lastname = $_POST['users_lastname'] ?? NULL;
    $users_salutation = $_POST['users_salutation'] ?? NULL;
    $users_email = $_POST['users_email'] ?? NULL;
    $users_company = $_POST['users_company'] ?? NULL;
    $users_street = $_POST['users_street'] ?? NULL;
    $users_city = $_POST['users_city'] ?? NULL;
    $users_tel = $_POST['users_tel'] ?? NULL;
    $users_status = $_POST['users_status'] ?? NULL;





    // SQL-Anweisung vorbereiten, Platzhalter (?) für Werte werden benutzt
    $sql = 'INSERT INTO `tbl_users`
    (
        `users_forename`,
        `users_lastname`,
        `users_salutation`,
        `users_email`,
        `users_password`,
        `users_company`,
        `users_street`,
        `users_city`,
        `users_tel`,
        `users_status`
       
    )
    VALUES
    ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);';

    // SQL-Anweisung an den Datenbankserver senden
    $stmt = $db->prepare( $sql );

    // Datenbankserver anweisen die vorbereitete SQL-Anweisung mit den ersetzten Platzhaltern auszuführen
    if( $stmt->execute( array( $users_forename, $users_lastname, $users_salutation, $users_email, $users_password, $users_company, $users_street, $users_city, $users_tel, $users_status  ) ) ) {
        echo '<p class="alert alert-success">Der Benutzer ' . $users_forename . ' wurde angelegt</p>'; 
    } else {
        echo '<p class="alert alert-danger">Benutzer konnte nicht angelegt werden.</p>';
    }

    $stmt = NULL;
}
?>

<p class="lead">Registerierungs Formular.</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
    <p>
        <p>Anrede :</p>
        <input type="Radio" name="1"  value="0"> Frau
        <input type="Radio" name="1"  value="1"> Herr
    </p>

    <p>
        <input type="text" name="users_forename" placeholder="vorname eintragen" size="45" >
    </p>
    <p>
        <input type="text" name="users_lastname" placeholder="nachname eintragen" size="45" >
    </p>
    <p>
        <input type="text" name="users_salutation" placeholder="salutatuion eintragen" size="45" >
    </p>
    <p>
        <input type="text" name="users_email" placeholder="Benutzername eintragen,  z.b...@gmail.com" size="45">
    </p>
     <p>
        <input type="password" name="users_password" placeholder="Passwort"size="45">
    </p>
    <p>
        <input type="text" name="users_company" placeholder="companyname eintragen" size="45">
    </p>
    <p>
        <input type="text" name="users_street" placeholder="streetname eintragen" size="45">
    </p>
    <p>
        <input type="text" name="users_city" placeholder="cityname eintragen" size="45">
    </p>
    <p>
        <input type="number" name="users_tel" value="nummer" placeholder="telephonenummer eintragen" size="30">
    </p>

    
    
   

    <p>
        <button type="submit" class="btn btn-primary">Abschicken</button>
    </p>

</form>



<?php get_footer(); ?>

