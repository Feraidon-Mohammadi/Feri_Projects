<?php
    require_once('includes/_init.inc.php');

    $page_title ='Hote requests';
    $page_header = 'Hotel requests';
    require_once('includes/_header.inc.php');    

    //vorbereitung aufabfrage
    $sql = 'SELECT `rooms_typ`,`bkngs_arr_day`,`bkngs_dep_day`,`bkngs_status`,`bkngs_id`  From `tbl_boockings` 
            JOIN `tbl_rooms` ON `bkngs_rooms_id_ref` = `rooms_id`';
   

    // Auswertung der einstellungen
    if(!empty($_POST))
    {      
        $sql_update = "UPDATE `tbl_boockings`
                        SET bkngs_status = ? 
                       WHERE bkngs_id = ?";

        $stmt_update= $db->prepare($sql_update);

        foreach( $_POST as $key=> $val )
        {
        $stmt_update->execute([$val, $key]);
        }

        echo '<p class= "alert alert-success" >' . ' Einstellungen gespeichert '  . '</p>';
        unset($stmt_update);
    }

 $stmt = $db->query($sql);
?>

<!-- Formular mitden daten der abfrage -->
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">

<table class= "table">
    <tr>
        <th>Zimmertyp</th>
        <th>Anreise</th>
        <th>Abreise</th>
        <th>anfrage Bestätigt?</th>
    </tr>

    <?php
    $id_status = array();
     while($row = $stmt->fetch()): ?>
        <!-- daten in tabelle eintragen -->
        <tr>
            <td><?=$row['rooms_typ'] ?></td>
            <td><?= Format_date( $row['bkngs_arr_day']) ?></td>
            <td><?= Format_date( $row['bkngs_dep_day']) ?></td>

            <td>
            <select name="<?=$row['bkngs_id']?>" id="bkngs_status">
                <option value="a" <?= $row['bkngs_status']=='a'? 'selected':'';?> >angefragt</option>
                <option value="b" <?= $row['bkngs_status']=='b'? 'selected':'';?> >bestätigt</option>
            </select>
            </td>        
        </tr>
   
        
    
    <?php endwhile;  unset($stmt)?>
   
  
</table>



<input type="submit" value="speichern" class= "btn btn-primary">
</form>
