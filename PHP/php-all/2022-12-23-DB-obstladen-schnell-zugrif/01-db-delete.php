<?php
require_once( '../includes/functions.inc.php' );
$database = 'obstladen';
/* * /get_header(
*	string $title,
*	string/array $css=NULL,
*	bool $bootstrap=false,
*	string $header=NULL,
*	array $nav=NULL,
*	bool $fluid=false
* ) */

$args = array(

    'Formular zur Datenbank',
    Null,
    true
    
);
get_header( ...$args );
require_once( '../includes/db-connect.inc.php' );


if(!empty( $_POST)) {
    $sql = "DELETE FROM `tbl_bestellungen`
        WHERE `bstlg_id` = {$_POST['auswahl'] } ;";

/* echo $sql . '<br>'; */

if( $result = mysqli_query( $db, $sql ) ) {
    $anzahl = mysqli_affected_rows($db );
    echo "<p class=\"alert alert-success\">$anzahl Datensätze wurden gelöcht.</p>";

    }else {
        echo get_db_error( $db, $sql );
    }

}









?>
    
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
        
<table class="table">

<tr>

<th>Auswahl</th>
<th>Kunde</th>
<th>Ort</th>


</tr>



<?php 

$sql = 'SELECT
    `bstlg_id`,
    `bstlg_vorname`,
    `bstlg_nachname`,
    `bstlg_ort`
    
    FROM
    
    `tbl_bestellungen`';

    if( $result = mysqli_query($db, $sql ) ){
        while( $row = mysqli_fetch_assoc ( $result)): ?>

        <tr>
                <td>
                    <input type="radio" name="auswahl" value="<?php echo $row['bstlg_id']; ?>">
                </td>

                <td>
                    <?php echo $row['bstlg_vorname'] . '' . $row['bstlg_nachname']; ?>
                </td>

                <td>
                    <?php echo $row['bstlg_ort'];  ?>
                </td>



        </tr>

<?php endwhile; ?>
    <tr>

            <td colspan="3">
                <button type="submit" class="btn btn-primary">Auswahl löschen </button>

            </td>

    </tr>


<?php } else {
    echo get_db_error( $db, $sql );

}

mysqli_close( $db );

?>
</table>

    </form>





<?php get_footer(); ?>