<?php   
    session_start();
    require_once('functions.inc.php');
    set_exception_handler('exceptionHandler');
    set_error_handler('errorHandler');
    $database = 'hotel';
    require_once('pdo-connect.inc.php');
?>
<style>
    .main
    {
        min-hight: 100vh;
    }
</style>