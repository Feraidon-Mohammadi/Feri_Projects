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

if( is_logged_in())  {
    $nav = array(
        'Home'=> '04-index.php',
        'Logout' => '03-logout.php'
    );
} else {
    $nav = array(
        'Home'=> '04-index.php',
        'Registrieren' => '01-register.php',
        'Login' => '02-login.php'
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