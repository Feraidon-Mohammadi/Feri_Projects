
<?php 
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - Startseite';
$page_header = '5sterne-hotel';


include_once '_header.php';


$sql = 'SELECT
    `rooms_id`,
    `rooms_typ`,
    `rooms_num_beds`,
    `rooms_img`,
    `rooms_extrabed`,
    `rooms_equipment`,
    `rooms_price_overnight`,
    `rooms_price_breakfest`,
    `rooms_price_halfboard`
   
FROM
    `tbl_rooms`
ORDER BY 
    `rooms_price_overnight` DESC';

$stmt = $db->query($sql);

?>
<table>
<h2>buchung-Übersicht</h2>


<p>

    <form action="rooms.php" method="post"><input type="submit" value="kategories" class="btn btn-primary"></form> 
</p>

<!-- <p>
    <form action="rooms.php" method="post"><input type="submit" value="Komfortklasse" class="btn btn-primary"></form> 
</p>

 <p>
  <form action="rooms.php" method="post"><input type="submit" value="luxusklasse" class="btn btn-primary"> </form>  
</p>
 -->
<form action="img">

<div>
 <img src="img\hotel.jpg" alt="hotel übersicht" width="500" height="400" location="center" />
 </div>
<a href="img\hotel.jpg">Hotel Übersicht-foto</a>

</form>
</table>








<?php  get_footer(); ?>



