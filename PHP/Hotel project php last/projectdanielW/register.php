<?php
    require_once('includes/_init.inc.php');

    $page_title ='Hotel Registrierung';
    $page_header = 'Hotel Registrierung';
    require_once('includes/_header.inc.php');    


$page_title = 'Blog - Registrierung';
$page_header = NULL;


// kpt-metalls daten = Kpt-Metall@kpt.mtl 
// Prüfe, ob das Formular gesendet wurde
if( !empty($_POST) ) {
    // Variablen definieren
    $users_forname = $_POST['users_forname'] ?? NULL;
    $users_lastname = $_POST['users_lastname'] ?? NULL;
    $users_salutation = $_POST['users_salutation'] ?? NULL;
    $users_email = $_POST['users_email'] ?? NULL;
    $users_company = $_POST['users_company'] ?? NULL;
    $users_street = $_POST['users_street'] ?? NULL;
    $users_city = $_POST['users_city'] ?? NULL;
    $users_tel = $_POST['users_tel'] ?? NULL;

    $users_password = password_hash( $_POST['users_password'], PASSWORD_DEFAULT );

    // SQL-Anweisung vorbereiten, Platzhalter (?) für Werte werden benutzt
    $sql = 'INSERT INTO `tbl_users`
    (
        `users_forname`,
        `users_lastname`,
        `users_salutation`,
        `users_email`,
        `users_password`,
        `users_company`,
        `users_street`,
        `users_city`,
        `users_tel`
    )
    VALUES
    ( ?,?,?,?,?,?,?,?,? );';

    // SQL-Anweisung an den Datenbankserver senden
    $stmt = $db->prepare( $sql );

    // Datenbankserver anweisen die vorbereitete SQL-Anweisung mit den ersetzten Platzhaltern auszuführen
    if( $stmt->execute( array( 

        $users_forname,
        $users_lastname,
        $users_salutation,
        $users_email,
        $users_password,
        $users_company,
        $users_street,
        $users_city,
        $users_tel
        ))) 
    {
        echo '<p class="alert alert-success">Der Benutzer ' . $users_forname.' ' .$users_lastname . ' wurde angelegt</p>'; 
    } else {
        echo '<p class="alert alert-danger">Benutzer konnte nicht angelegt werden.</p>';
    }

    $stmt = NULL;
}
?>

<p class="lead">Gegben sie ihre daten an</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
<select name="users_salutation" id="users_salutation" class="form-control mb-2">
    <option value="Herr">Herr</option>
    <option value="Frau">Frau</option>
    <option value="Lord">Lord</option>
    <option value="Lady">Lady</option>
    <option value="Dr.">Dr.</option>
    <option value="Mayonaise.">Mayonaise</option>
</select>

   <div class="row">
 <div class="col-6 mr-2">
        <input type="text" name="users_forname" placeholder="Vorname" class="form-control mb-2" required>
         <input type="text" name="users_street" placeholder="Straße" class="form-control mb-2" required>
        <input type="text" name="users_company" placeholder="Firma" class="form-control mb-2" required>
        <input type="email" name="users_email" placeholder="email" class="form-control mb-2" required>
      
    </div>
    <div class="col-6">
        <input type="text" name="users_lastname" placeholder="Nachname" class="form-control mb-2" required>       
        <input type="text" name="users_city" placeholder="Ort" class="form-control mb-2" required>
        <input type="text" name="users_tel" placeholder="Telefonnummer" class="form-control mb-2" required>
         <input type="password" name="users_password" placeholder="Passwort" class="form-control mb-2" required>
   </div>
   
        <button type="submit" class="btn btn-primary">Registrieren</button>
   
</div>
</form>

<?php get_footer(); ?>