<?php
    require_once('includes/_init.inc.php');

    $page_title ='details';
    if(!empty($_GET))
    {
      $rooms_typ = $_GET['rooms_typ'];
    }
    elseif(!empty($_POST))
    {      
        $rooms_typ = $_POST['rooms_typ'];
    }

    $page_header = 'details: ' . $rooms_typ;
    require_once('includes/_header.inc.php');   

// query für die detailansicht
$sql = "SELECT `rooms_id`, `rooms_num_beds`,`rooms_img`,`rooms_equpment`,`rooms_price_overnight` ,`rooms_price_breakfest`,`rooms_price_halfoard`
        FROM `tbl_rooms`
        WHERE `rooms_typ` = '". $rooms_typ . "'";
  

$stmt = $db->query($sql);
//detailansicht
    ?> 
     
            <?php $row = $stmt->fetch() ?>
       <div class="card">
           
           <img src="<?=$row['rooms_img'];?>" alt="bild vom zimmer" class="card-img-top">
           <table class= "table card-text">
               <tr><td>verfügbare zimmer :</td> <td><?= $stmt->rowCount() ?></td></tr>
               <tr><td>betten :</td> <td><?= $row['rooms_num_beds']; ?></td></tr>
               <tr><td>ausstattung :</td> <td><?= $row['rooms_equpment']; ?></td></tr>
               <tr><td>Übernachtung :</td><td> <?= $row['rooms_price_overnight']; ?></td></tr>
               <tr><td>mit Frühstück :</td> <td><?= $row['rooms_price_breakfest']; ?></td></tr>
               <tr><td>Halbpension :</td> <td><?= $row['rooms_price_halfoard']; ?></td></tr>
           </table>
       </div>
   
<!-- quary für Buchung -->
 <?php 
 if(!empty($_POST))
 {
    $sql_insert = 'INSERT INTO `tbl_boockings` 
      (`bkngs_num_persons`,`bkngs_rooms_id_ref`,`bkngs_users_id_ref`,`bkngs_arr_day`,`bkngs_dep_day` )
      VALUES
     (?,?,?,?,?)';
 


    $stmt= $db->prepare($sql_insert);
    if ($stmt->execute([$_POST['bkngs_num_persons'],$_POST['rooms_id'],$_SESSION['user']['user_id'],$_POST['bkngs_dep_day'],$_POST['bkngs_dep_day']]))
    {
    echo '<p class="alert alert-success">' . 'buchung erfolgreich'  . '</p>';
    }
    else{echo '<p class = "alert alert-danger">' . 'buchng fehlgeschlagen' . '</p>';}
 }
 ?>  
<!-- Formular für buchung -->
<?php if(!empty($_SESSION)) :?>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" require>
<label for="bkngs_arr_day">Anreise</label>
    <input type="date" name="bkngs_arr_day" id="bkngs_arr_day">

<label for="bkngs_dep_day">Abreise</label>
    <input type="date" name="bkngs_dep_day" id="bkngs_dep_day" require>

    <label for="bkngs_num_persons">personen</label>    
    <input type="number" name="bkngs_num_persons" id="bkngs_num_persons">
    
    <input type="hidden" name ="rooms_typ" value="<?= $rooms_typ ?>">
    <input type="hidden" name ="rooms_id" value="<?= $row['rooms_id'] ?>">
    

    <input type="submit" value="buchen" class="btn btn-success">
</form>
<?php else: ?>
<p><a href="login.php">login</a></p>
<a href="register.php">Registrieren</a>

<?php endif; ?>
    <?php get_footer() ?>