<?php
    require_once('includes/_init.inc.php');

    $page_title ='Hote Home';
    $page_header = 'Hotel Home';
    require_once('includes/_header.inc.php');    
    
   const categories = array('einzel','doppel','palace');
       
   $sql = 'SELECT DISTINCT `rooms_typ`  FROM `tbl_rooms`';
   $stmt= $db->query($sql);

  
?>

    <form action="details.php" method="get">
        <div class="my-2">
    
            <label for="rooms_typ">Zimmer kategorie</label>
            <select name="rooms_typ" class="form-control" id ="rooms_typ">
    
    
                <?php while($row= $stmt->fetch()):?>
                <option value="<?= $row['rooms_typ'] ?>"><?= $row['rooms_typ'] ?> </option>
    
                <?php endwhile; ?>
            </select>
    
            <input type="hidden" name="rooms_id">
        </div>
        <input type="submit" value="ok" class="btn btn-primary">
    </form>


<?php get_footer() ?>