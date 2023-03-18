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
       
        'Home'=> 'index.php',
        'Logout' => 'logout.php'
    );
} else {
    $nav = array(
        'Home'=> 'index.php',
        'buchung'=> 'bookings.php',

        'Registrieren' => 'register.php',
        'Login' => 'login.php'
    );
}
$args = array(
    $page_title,
    NULL,
    true,
    $page_header,
    array(
        'Mein hotel',
        $nav
    )
);
get_header( ...$args );