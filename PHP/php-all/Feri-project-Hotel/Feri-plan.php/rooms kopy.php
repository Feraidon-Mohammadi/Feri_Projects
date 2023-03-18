<?php 
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - 5sterne';
$page_header= '';

// sicherheit, Falls Datei ohne Get-Parameter aufgerufen wird 
#meine spaziele fehler zu unexistierte seite

/* if( empty($_GET) ) {
    header( 'Location: _index.php');
} */


/* 
$rooms_id = $_GET['room_id'];
$sql = 'SELECT * From 
     `tbl_rooms`
JOIN `tbl_bookings`

ON `rooms_bkngs_rooms_id_ref` = `bkngs_id`

JOIN `tbl_users`

ON `rooms_users_id_ref` = `users_id`

WHERE `rooms_id` = ?';



$stmt = $db->prepare( $sql);
$stmt->execute( [$room_id] ); */

/* echo '<pre>', var_dump( $stmt ), '</pre>'; */

/* echo '<pre>', var_dump( $stmt->$rowCount() ),'</pre>'; */


/* if( $stmt->rowCount() !== 1 ){ //falls nicths oder zu viel gefunden, meldung
    include '_header.php';
    echo '<p class="alert alert-danger">kein Artikel gefunden!</p>';
    get_footer();
    exit;

} */

$sql = 'SELECT
    `rooms_id`,
    `rooms_typ`
FROM
    `tbl_rooms`';

$stmt = $db->query($sql);
$room = $stmt->fetch();


$room_title = $post['rooms_typ'];
$page_header = $room_title; 


include_once '_header.php';
?>

<article>
    <header>
        <p>
            <!-- kopfbereich des Artikels mit Erstellungs- und Änderungsdatum, Autor und Kategorie -->

            <?=formatDatetime( $post['rooms_created_at']); ?> | 
            <?=formatDatetime( $post['rooms_updated_at']); ?> | 
            <?= $post['rooms_created_at']; ?> | 
            <?= $post['rooms_updated_at']; ?> |
            <?= $post['users_forename']; ?> |
            <?= $post['categ_name']; ?> 
        </p>
    </header>

    <main>
        <figure calss="figure">
            <img 
            class="figure-img img-fluid"
            src="<?= $post['rooms_img']; ?>" 
            alt="<?= $post['rooms_img_alt']; ?>">
        </figure>

        <p>
         <?=nl2br( $post['rooms_details']); ?>
        </p>
        </main>

<?php if( is_logged_in() ): ?>
    <footer>
        <p>
            <a href="rooms.php?room_id=<?= $post['rooms_id']; ?>">kategorie auswählen</a> 
            
            
            |
            <a href="buchungs.php">neue booking </a>


        </p>

        <a href="https://simplexitytravel.com/wp-content/plugins/phastpress/phast.php/c2VydmljZT1pbWFnZXMmc3JjPWh0dHBzJTNBJTJGJTJGc2ltcGxleGl0eXRyYXZlbC5jb20lMkZ3cC1jb250ZW50JTJGdXBsb2FkcyUyRjIwMjAlMkYwNyUyRnJhZmZsZXMtc2luZ2Fwb3JlLXNjYWxlZC5qcGcmY2FjaGVNYXJrZXI9MTYwMTE5NTE4NS04ODA3NjcmdG9rZW49NjE2ZTNjMjllYTkyNTYxNw.q.jpg"></a>






     
</footer>
<?php endif; ?> 


<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
<div class="mb-3">
    <!-- Ausgabe der Blog-Kategorien -->
    <select name="categ_id" class="form-select">
        <optgroup label="Kategorie">

            <?php 
            $sql = 'SELECT * FROM  `tbl_categories`;';
            $stmt = $db->query( $sql );
            while( $row = $stmt->fetch() ): 
                $selected = '';
                if( $row['categ_id'] === $categ_id ) $selected = 'selected';
            ?>

                <option value="<?= $row['categ_id']; ?>"><?= $row['categ_name']; ?></option>

             <?php endwhile ?> 

            </optgroup>
    </select>
</div>