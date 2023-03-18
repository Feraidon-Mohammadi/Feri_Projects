<?php
require_once( '../includes/functions.inc.php' );
$database = 'blog';
 /*get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* )
 */
$args = array(
    `Blog - logout`,
    NULL,
    true   
);
get_header( ...$args );
require_once( '../includes/pdo-connect.inc.php' );
 
// session leeren
$_SESSION = array();

// session zerstören 
if( session_destroy ( ) ) {
    echo '<p class= "alert alert-seccess">Sie wurden erfolgereich ausgeloggt.</p>';

}else{
    echo '<p class="alert alert-danger">Ausloggen hat nicht funktioniert... Viel Glück!</p>';

}



?>
    
<?php get_footer(); ?>