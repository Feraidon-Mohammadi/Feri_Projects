<?php 
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'blog - Artikeldetails';
$page_header= '';

// sicherheit, Falls Datei ohne Get-Parameter aufgerufen wird 
if( empty($_GET) ) {
    header( 'Location: 04-index.php');
}



$post_id = $_GET['post_id'];
$sql = 'SELECT * From 
     `tbl_posts`
JOIN `tbl_categories`

ON `posts_categ_id_ref` = `categ_id`

JOIN `tbl_users`

ON `posts_users_id_ref` = `users_id`

WHERE `posts_id` = ?';



$stmt = $db->prepare( $sql);
$stmt->execute( [$post_id] );

echo '<pre>', var_dump( $stmt ), '</pre>';

/* echo '<pre>', var_dump( $stmt->$rowCount() ),'</pre>'; */


if( $stmt->rowCount() !== 1 ){ //falls nicths oder zu viel gefunden, meldung
    include '_header.php';
    echo '<p class="alert alert-danger">kein Artikel gefunden!</p>';
    get_footer();
    exit;

}

$post = $stmt->fetch();


$post_title = $post['posts_header'];
$page_header = $post_title;


include_once '_header.php';
?>

<article>
    <header>
        <p>
            <!-- kopfbereich des Artikels mit Erstellungs- und Änderungsdatum, Autor und Kategorie -->

            <?=formatDatetime( $post['posts_created_at']); ?> | 
            <?=formatDatetime( $post['posts_updated_at']); ?> | 
            <?= $post['posts_created_at']; ?> | 
            <?= $post['posts_updated_at']; ?> |
            <?= $post['users_name']; ?> |
            <?= $post['categ_name']; ?> 
        </p>
    </header>

    <main>
        <figure calss="figure">
            <img 
            class="figure-img img-fluid"
            src="<?= $post['posts_img']; ?>" 
            alt="<?= $post['posts_img_alt']; ?>">
        </figure>

        <p>
         <?=nl2br( $post['posts_body']); ?>
        </p>
        </main>

<?php if( is_logged_in() ): ?>
    <footer>
        <p>
            <a href="06-post-edite.php?post_id=<?= $post['posts_id']; ?>">Artikel
            bearbeiten</a> |
            <a href="07-post-created.php">neue Artikel </a>


        </p>

     
</footer>
<?php endif; ?>   











</article>