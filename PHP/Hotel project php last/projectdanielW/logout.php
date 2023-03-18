<?php

require_once('includes/_init.inc.php');

$page_title ='Hote Home';
$page_header = 'Hotel Home';




$page_title = 'Hotel - Logout';
$page_header = 'Hotel logout';

// Session leeren
$_SESSION = array();
// Session zerstören
if( session_destroy() ) {
    $message = '<p class="alert alert-success">Sie wurden erfolgreich ausgeloggt.</p>';
} else {
    $message = '<p class="alert alert-danger">Ausloggen hat nicht funktioniert... Viel Glück!</p>';
}

require_once('includes/_header.inc.php');    

echo $message;

?>
    
<?php get_footer(); ?>