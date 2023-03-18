<?php
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - Logout';
$page_header = NULL;

// Session leeren
$_SESSION = array();
// Session zerstören
if( session_destroy() ) {
    $message = '<p class="alert alert-success">Sie wurden erfolgreich ausgeloggt.</p>';
} else {
    $message = '<p class="alert alert-danger">Ausloggen hat nicht funktioniert... Viel Glück!</p>';
}

include_once '_header.php';

echo $message;

?>
    
<?php get_footer(); ?>