
<?php 
require_once( '_init.php' );
$database = 'hotel';
require_once( '../includes/pdo-connect.inc.php' );

$page_title = 'hotel - 5sterne';
$page_header= '';

include_once '_header.php';



if(!empty( $_POST)) {
    $sql = "SELECT FROM `tbl_rooms`
        WHERE `rooms_typ` = {$_POST['auswahl'] } ;";
/* echo $sql . '<br>'; */

if( $result = mysqli_query( $db, $sql ) ) {
    $anzahl = mysqli_affected_rows($db );
    echo "<p class=\"alert alert-success\">$anzahl Datensätze wurden gelöcht.</p>";

    }else {
        echo get_db_error( $db, $sql );
    }

}


?>

    
        
<table class="table" style="img" >

<tr>
<th>Auswahl</th>
<th>rooms_typ</th>
<th>rooms_id</th>
<th>rooms_img</th>
<th>rooms_extrabed</th>
<th>rooms_price_overnight</th>
<th>rooms_price_breakfest</th>
<th>rooms_price_halfboard</th>


</tr>



<?php 

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
    
    `tbl_rooms`';
    $stmt = $db->query($sql); 

    
        while( $row = $stmt->fetch()): ?>

        <tr>
               <td>
                    <input type="radio" name="auswahl" value="<?php echo $row['rooms_id']; ?>">
                </td>
 

                


                <td>
                    <?php echo $row['rooms_typ'] . '' ; ?>
                </td>

                <td>
                    <?php echo $row['rooms_id'];  ?>
                </td>




                <td>
                    <img class="img-fluid" src="<?php echo $row['rooms_img'];  ?>" alt="">
                    
                </td>

                <td>
                    <?php echo $row['rooms_equipment'];  ?>
                    
                </td>
                
                <td>
                    <?php echo $row['rooms_price_overnight'];  ?>
                </td>
                <td>
                    <?php echo $row['rooms_price_breakfest'];  ?>
                </td>
                <td>
                    <?php echo $row['rooms_price_halfboard'];  ?>
                </td>
                
                
        

        </tr>


<?php endwhile; ?>




























    


    

</table>
    <td colspan="3">
            <p>
                
                <form action="bookings.php" method="post"value="buchen">
                <input type="submit"  class="btn btn-primary"></form>  
            </p>
            </td>
    </form>

    <?php  get_footer(); ?>
















