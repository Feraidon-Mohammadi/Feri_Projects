<?php
/* get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* )
*/

if( is_logged_in ) {
    $nav = array(
        'Logout' => '033-logout.php'
    );
} else {
    $nav = array(
        'Registrieren' => '011-register.php',
        'Login' => '022-login.php'
    );
}
$args = array(
    $page_title,
    NULL,
    true,
    $page_header,
    array(
        'Mein Blog',
        $nav
    )
);
get_header( ...$args );