<?php  
session_start();
require_once( '../includes/functions.inc.php' );
set_exception_handler( 'exceptionHandler' );
set_error_handler( 'errorHandler');
