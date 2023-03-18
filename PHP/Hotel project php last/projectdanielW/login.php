<?php

require_once('includes/_init.inc.php');

$page_title ='Hote login';
$page_header = 'Hotel login';


$message = '';

// kpt-metalls daten = Kpt-Metall@kpt.mtl 
// rootys daten (admin) = rooty@adm.co
// Prüfe ob Formular gesendet ist
if( !empty( $_POST ) ) {
    // Variablen anlegen
    $users_email    = $_POST['users_email'];
    $users_password = $_POST['users_password'];

    $sql = 'SELECT
        `users_id`,
        `users_email`,
        `users_password`
    FROM
        `tbl_users`
    WHERE
        `users_email` = ?';

    $stmt = $db->prepare( $sql );

    if(( $stmt->execute( array($users_email)) && ($row = $stmt->fetch()) ) ) {
      
        // Prüfung auf Übereinstimmung des Passwortes
            if( password_verify( $users_password, $row['users_password'] ) ) {
                $_SESSION['user'] = array(
                    'user_id' => $row['users_id'],
                    'user_email' => $row['users_email']
                );

                $message = '<p class="alert alert-success">Login erfolgreich!</p>';
            } else {
                $message = '<p class="alert alert-danger">Login fehlgeschlagen!</p>';
            }
        

    }
    else 
    {
            $message = '<p class="alert alert-danger">Login fehlgeschlagen!</p>';
    }
    
    $stmt = NULL;
}

require_once('includes/_header.inc.php');   
echo $message;

?>

<p class="lead">Bitte geben Sie einen Benutzernamen und ein Passwort ein.</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
    <p>
        <input type="text" name="users_email" placeholder="email eintragen">
    </p>

    <p>
        <input type="password" name="users_password" placeholder="Passwort">
    </p>

    <p>
        <button type="submit" class="btn btn-primary">Login</button>
    </p>

</form>

<?php get_footer(); ?>