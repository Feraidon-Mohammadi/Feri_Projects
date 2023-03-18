<?php
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - Buchung';
$page_header = NULL;

include_once '_header.php';

// Prüfe, ob das Formular gesendet wurde
if( !empty($_POST) ) {
    // Variablen definieren
    $bkngs_num_persons = $_POST['bkngs_num_persons'] ?? NULL;
    $bkngs_arr_day = $_POST['bkngs_arr_day'] ?? NULL;
    $bkngs_dep_day = $_POST['bkngs_dep_day'] ?? NULL;

  





    // SQL-Anweisung vorbereiten, Platzhalter (?) für Werte werden benutzt
    $sql = 'INSERT INTO `tbl_bookings`
    (
        `bkngs_num_persons`,
        `bkngs_arr_day`,
        `bkngs_dep_day`
        
       
       
    )
    VALUES
    ( ?, ?, ? );';

    // SQL-Anweisung an den Datenbankserver senden
    $stmt = $db->prepare( $sql );

    // Datenbankserver anweisen die vorbereitete SQL-Anweisung mit den ersetzten Platzhaltern auszuführen
    if( $stmt->execute( array( $bkngs_num_persons, $bkngs_arr_day, $bkngs_dep_day ) ) ) {
        echo '<p class="alert alert-success">Der Benutzer hat ' . $bkngs_num_persons . ' buchung Erfolgreich angelegt</p>'; 
    } else {
        echo '<p class="alert alert-danger">buchung konnte nicht angelegt werden.</p>';
    }

    $stmt = NULL;
}
?>

<p class="lead">Buchungs Formular.</p>



<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    

    <p>
        <input type="text" name="bkngs_num_persons" placeholder="bkngs_num_persons eintragen" size="45" >
    </p>

     <p>
        <input type="date" name="bkngs_arr_day" placeholder="bkngs_arr_day eintragen"size="45">
    </p> 

    <p>
        <input type="date" name="bkngs_dep_day" placeholder="bkngs_dep_day eintragen" size="45">
    </p>
    
    <p>
        <button type="submit" class="btn btn-primary">buchen</button>
    </p>

</form>

<?php get_footer(); ?>

