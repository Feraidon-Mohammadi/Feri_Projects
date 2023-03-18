<?php  
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'blog - neue Artikel erstellen';
$page_header= '';
$msg = '';
/* Variblen für jedes Formularfeld initionalisieren ...#
*
* ... leer,falls POST-Formular noch nicht abgeschickt 
*...grfüllt mit Formularewert, falls Formular abgeschickt 
*/
$post_id = $_POST['posts_id'] ?? '';
$post_header = $_POST['posts_header'] ?? '';
$post_body = $_POST['posts_body'] ?? '';

$post_img = ( !empty( $_POST['posts_img'] ) ) ? 'images/':'';
$post_img .=  $_POST['posts_img'] ?? '';
$post_img_alt = $_POST['posts_img_alt'] ?? '';
$categ_id = $_POST['categ_id'] ?? '';
$users_id = $_POST['user'] [ 'user_id'] ?? '';


if( !empty( $_POST) ) {
    $sql = 'INSERT INTO `tbl_posts`
        (`posts_header`, `posts_body`, `posts_img`, `posts_img_alt`, `posts_categ_id_ref`, `posts_users_id_ref` )  
        VALUES 
        ( ?, ?, ?, ? ,? ,?)';
        $stmt = $db->prepare($sql );
        $stmt->execute( [$post_header, $post_body, $post_img, $post_img_alt, $categ_id, $users_id ] ) ;
        if( $stmt ) {
            $msg ='<p class="alert alert-success">Artikel angelegt.</p>';
            

        }else{$msg ='<p class="alert alert-danger">Artikel konnte nicht angelegt werden.</p>';

        }
}



include_once '_header.php';
echo $msg;
include_once '_post-form.php';

get_footer();