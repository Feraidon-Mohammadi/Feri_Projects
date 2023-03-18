<?php
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'Blog - Login';
$page_header = NULL;
$message = '';

// Prüfe ob Formular gesendet ist
if( !empty( $_POST ) ) {
    // Variablen anlegen
    $users_name = $_POST['users_name'];
    $users_password = $_POST['users_password'];

    $sql = 'SELECT
        `users_id`,
        `users_name`,
        `users_password`
    FROM
        `tbl_users`
    WHERE
        `users_name` = ?';

    $stmt = $db->prepare( $sql );

    if( $stmt->execute( array($users_name) ) ) {
        $row = $stmt->fetch();

        
        
        // Prüfung auf Übereinstimmung des Passwortes
        if( password_verify( $users_password, $row['users_password'] ) ) {
            $_SESSION['user'] = array(
                'user_id' => $row['users_id'],
                'user_name' => $row['users_name']
            );

            $message = '<p class="alert alert-success">Login erfolgreich!</p>';
        } else {
            $message = '<p class="alert alert-danger">Login fehlgeschlagen!</p>';
        }
    }
    
    $stmt = NULL;
}

include_once '_header.php';


    echo $message;



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
        <button type="submit" class="btn btn-primary">Login</button>
    </p>

</form>

<?php get_footer(); ?>