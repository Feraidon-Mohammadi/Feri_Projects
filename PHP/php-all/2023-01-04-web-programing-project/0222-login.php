<?php
session_start();
require_once( '../includes/functions.inc.php' );
$database = 'blog';
/* get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* )
 */
if( !empty( $_POST ) AND $_SESSION['is_logged_in'] === true ){


$args = array(
    'Blog - login',
    NULL,
    true,
    NULL,
    array(
        'Logo',
        array(
            'Logout' => '02-logout.php'
        )
    )


);


} 

#

require_once( '../includes/pdo-connect.inc.php' );

// prüfe, ob Formular abgesendet  ist 
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
        `users_name` = ? ';

        $stmt = $db->prepare( $sql );
        
        if( $stmt->execute( array($users_name) ) ) {
            $row = $stmt->fetch();

            // prüfung auf Übereinstimmung des passwortes
            if( password_verify( $users_password, $row['users_password']  ) ){
                $_SESSION['users_id'] = $row['users_id'];
                $_SESSION['users_name'] = $row['users_name'];
                $_SESSION['is_logged_in'] = true;
               

            }else{
                echo '<p class="alert alert-danger">Login fehlergeschlagen!</p>';
            }
            
        }

        $stmt = NULL;

}
if( !empty( $_SESSION ) AND $_SESSION['is_logged_in'] ) {
    $nav_array = array(
        'logout' => '03-logout.php'
    );



}else {
    $nav_array = array(
        'Registrieren' => '01-register.php',
        'Loging' => '02-login.php'
    );
}



    $args = array(
        'Blog - login',
       
        NULL,
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
    <button type="submit" class="btn btn-primary">Login</button>
</p>


</form>











<?php get_footer(); ?>