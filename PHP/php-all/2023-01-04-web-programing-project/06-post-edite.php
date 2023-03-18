<?php 
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'blog - Artikel bearbeiten ';
$page_header= 'Artikel bearbeiten';
$msg = '';

if( !empty( $_POST ) ){ //falls formular abgeschickt wurde 
    // alle Formularfelder auslesen und den Variablen zuweisen

    $post_id = $_POST['posts_id'] ?? '';
$post_header = $_POST['posts_header'] ?? '';
$post_body = $_POST['posts_body'] ?? '';

$post_img = ( !empty( $_POST['posts_img'] ) ) ? 'images/':'';
$post_img .=  $_POST['posts_img'] ?? '';
$post_img_alt = $_POST['posts_img_alt'] ?? '';
$categ_id = $_POST['categ_id'] ?? '';
$users_id = $_SESSION['user'][ 'user_id'] ?? '';

$sql = 'UPDATE `tbl_posts`
    SET 
        `posts_header` = ? ,
        `posts_body` = ?,
        `posts_img` = ?,
        `posts_img_alt` = ?,
        `posts_categ_id_ref` = ?,
        `posts_users_id_ref` = ?
    WHERE
        `posts_id` = ?';
    $stmt = $db->prepare( $sql);
    $stmt->execute( [
        $post_header,
        $post_body,
        $post_img,
        $post_img_alt,
        $categ_id,
        $users_id,
        $post_id
    ]);

    //prüfe ob Aktion erfolgreich oder nicht 
    if( $stmt->rowCount() === 0 ) {//Artikel-ID existiert nicht
        $msg ='<p class="alert alert-danger">Artikel nicht gefunden<br>';
        $msg .= 'Zurück zur <a class="alert-link" href=04-index.php">Startseite</a></p>';
        
    } else {
        $msg ='<p class="alert alert-success">Artikel angelegt.</p>';
    }
    
    
}else{// Falls formular zur bearbeitung aufgerufen wurde (noch nicht abgesendet ) =>artikel laden

    $post_id = $_GET['post_id'];
    // Aus Zeitgründen * benutzt. Normalerweise benönigen wir die Felder posts_created_at und post_updated_at nicht
    $sql = 'SELECT * FROM `tbl_posts` WHERE `posts_id` = ?';
    $stmt = $db->prepare( $sql );
    $stmt->execute( [$post_id] );

    //prüfe ob Aktion erfolgreich oder nicht 
    if( $stmt->rowCount() === 0 ) {//Artikel-ID existiert nicht
        $msg ='<p class="alert alert-danger">Artikel nicht gefunden</p>';
        
    } else {
        $post = $stmt->fetch();

        $post_header = $post['posts_header'];
        $post_body = $post['posts_body'];
        $post_img =  $post['posts_img'];
        $post_img_alt = $post['posts_img_alt'];
        $categ_id = $post['posts_categ_id_ref'];
        $users_id = $_SESSION['user'][ 'user_id'] ;
    }

}
include_once '_header.php';
echo $msg;
include_once '_post-form.php';

get_footer();