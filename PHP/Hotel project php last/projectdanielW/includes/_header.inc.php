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



if( is_logged_in())
{
$sql = "SELECT `users_status` FROM `tbl_users`
WHERE `users_email` = '" . $_SESSION['user']['user_email'] . "'" ;

$stmt = $db->query($sql);
  $status = $stmt->fetch()['users_status'];

    if ( $status ==='a')
   {
    $nav = array
        (
        'Home'=> 'index.php',
        'Logout' => 'logout.php',
        'Anfragen' => 'requests.php'   
        );
    }
    else
    {$nav = array
        (
        'Home'=> 'index.php',
        'Logout' => 'logout.php'     
        );
    }
    
    unset($status);
    
} else
{
    $nav = array(
        'Home'=> 'index.php',
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
        'Hotel',
        $nav
    )
);
get_header( ...$args );