<?php
require_once( '../includes/functions.inc.php' );
$database = 'blog';
/* * /get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* )
*/
$args = array(
    'Blog - Registerieren',
    null,
    true,
    NULL,
    array(
        'Logo',
        array(
            'Registrieren' => '01-register.php',
            'Loging' => '02-login.php'
        )
    )

);


get_header( ...$args );
require_once( '../includes/pdo-connect.inc.php' );

//prüfe, ob das Formular gesendet wurde 
if( !empty($_POST) ) {
    //Variablen deninieren 
    $users_name = $_POST['users_name'] ?? NULL;
    $users_password = password_hash( $_POST['users_password'], PASSWORD_DEFAULT );




    // SQL-Anweisung vorbereiten, pLatzhalter (?) für Werte werden benutzt 
    $sql = 'INSERT INTO `tbl_users`
    (

        `users_name`,
        `users_password`
    )
    VALUES
    ( ?, ?);';

    // SQL-Anweisung an den Datenbankserver senden
    $stmt = $db->prepare($sql );


    // Datenbankserver anweisen die vorbereitete  SQL-Anweisung mit den ersetzten Platzhaltern auszuführen
    if($stmt->execute( array( $users_name, $users_password ) ) ) {
        echo '<p class="allart alert-danger">Der Benutzer ' . $users_name . 'wurde angelegt</p>';

    }else {
        echo '<p class="alert alert-danger">Benutzer konnte nicht angelegt werden.</p>';
    }
    $stmt = NULL;
}
?> 


<p class="Lead"><marquee direction="left" bgcolor="#f3d3g3">Bitte geben sie einen Benutzernamen und ein passwort ein.</marquee></p>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
<p>
<input type="text" name="users_name" placeholder="Benutzername eintragen">
</p>

<p>
<input type="password" name="users_password" placeholder="passwort">
</p>


<p>
    <button type="submit" class="btn btn-primary">Registerieren</button>
</p>


</form>













<?php get_footer(); ?>