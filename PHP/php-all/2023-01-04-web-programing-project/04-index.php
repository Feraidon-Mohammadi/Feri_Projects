<?php 
require_once( '_init.php' );
$database = 'blog';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'blog - Startseite';
$page_header = 'IT-Blog';


include_once '_header.php';

$sql = 'SELECT
    `posts_id`,
    `posts_header`,
    `posts_categ_id_ref`,
    `posts_updated_at`
FROM
    `tbl_posts`
ORDER BY 
    `posts_updated_at` DESC';

$stmt = $db->query($sql);

?>

<h2>Artikel-Übersicht</h2>

<ul>
    <?php while( $row = $stmt->fetch()): ?>
        <li>
            <a href="05-post.php?post_id=<?= $row['posts_id']; ?>">
            <?= $row['posts_header']; ?>
        </a>
        </li>
    <?php endwhile ?>
</ul>

<?php  get_footer(); ?>








