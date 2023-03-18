<?php  
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - Login';
$page_header = NULL;
$message = '';

if( !empty( $_POST ) ) {
    // Variablen anlegen
    $users_email = $_POST['users_email'];
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

    if( $stmt->execute( array($users_email) ) ) {
        $row = $stmt->fetch();

        $stmt = $db->prepare( $sql );

        if( $stmt->execute( array($users_email) ) ) {
            $row = $stmt->fetch();
    
            
            
            // passwort reinstimmung konrolliern
            if( password_verify( $users_password, $row['users_password'] ) ) {
                $_SESSION['user'] = array(
                    
                    'user_id' => $row['users_id'],
                    'user_email' => $row['users_email']
                   
                );
    
             }
                $message = '<p class="alert alert-success">Login erfolgreich!</p>';
            } else {
                $message = '<p class="alert alert-danger">Login fehlgeschlagen!</p>';
            }
        }
        
        $stmt = NULL;
}
    

    include_once '_header.php';
    
    
       /*  echo $message; */
    
    
    ?>
    <p class="lead">Bitte geben Sie einen Benutzernamen und ein Passwort ein.</p>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
    <p>
        <input type="text" name="users_email" placeholder="Benutzername eintragen">
    </p>

    
<p>
        <input type="password" name="users_password" placeholder="Passwort">
    </p>

    
   

    <p>
        <button type="submit" class="btn btn-primary">Login</button>
    </p>



    <?php 

if( isset ($_POST['e-mail'] ) ) {
    // ist das pflichfeld (E-Mail) gefüllt
    //empty() prüft , ob das übergebene Element leer, null oder nicht vorhanden ist 
    //trim() entfern leerzeichen, Tab-aprunge etc. (whitespaces ) links undrechts vom
    if( empty( trim( $_POST['e-mail']  ) ) ){
        echo '<p>Mail ist leer</p>';
    } else {
        echo '<p>Mail-Adresse: ' . $_POST['e-mail'] . '</p>';
    }


        // Prüfe ob Eissorte ausgewält wurde
        if( $_POST['password'] == -1 )  {
            echo '<p>password wurde nicht eingegeben :-( </p>';

        } else {
            echo '<p>passowrd: ' .$_POST['passwort'] . '</p>';
        }


//Ausgabe der Nachricht 
// Das zweite argument nl2br() bei gibt an, ob die br-Tags xhtml-konform (true-standard) oder HTML5-konform (false) sind.
echo '<p>Ihre Nachricht:<br>' . nl2br($_POST['message'] ) . '</p>';
//echo '<p>Ihre Nachricht:<br>' . nl2br($_POST['message'], true/false) . '</p>';



   echo '<pre>', print_r($_POST, true ), '</pre>';

} else {
    echo '<p>Haben sie sich noch  nicht angemeldet. Bitte füllen sie zunächst das <a href="register.php">Formular </a> aus!</p>';
}





?>





    
</form>

<?php get_footer(); ?>