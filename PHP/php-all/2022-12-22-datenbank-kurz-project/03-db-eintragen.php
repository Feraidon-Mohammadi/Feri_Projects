<?php
require_once( '../includes/functions.inc.php' );
$database = 'obstladen';
/* get_header(
*   string $title,
*   string/array $css=NULL,
*   bool $bootstrap=false,
*   string $header=NULL,
*   array $nav=NULL,
*   bool $fluid=false
* )
*/
$args = array(
    'DB eintragen',
    NULL,
    true,
    'Neue Datensätze eintragen'
);
get_header( ...$args );
require_once( '../includes/db-connect.inc.php' );
$sql = 'INSERT INTO `tbl_bestellungen`
    (
        `bstlg_vorname`,
        `bstlg_nachname`,
        `bstlg_ort`,
        `bstlg_sorte`,
        `bstlg_menge`
    )
    VALUES
    (
        "Heinz",
        "Müller",
        "Gotha",
        "Boskoop",
        8
    )';
if( $result = mysqli_query( $db, $sql ) ) {
    // Anzahl der betroffenen Datensätze liefern
    $anzahl = mysqli_affected_rows( $db );
    echo "<p>$anzahl Datensätze wurden hinzugefügt.</p>";
} else {
    echo get_db_error( $db, $sql );
}
mysqli_close( $db );
?>
<?php get_footer(); ?>