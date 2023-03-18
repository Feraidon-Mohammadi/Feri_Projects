<?php 
class Mensch {
    // eigenschaften 
    Private $arme = 2;
    Private $beine = 2;
    Private $erschoepfung = 0;
    Private $zufriedneheit= 0;
    Private $name= '';
 
    Private $geschlecht = '';
    Private $augenfarbe= '';
    Private $haarfarbe = '';
    
//methoden 
        function __construct( $name, $geschlecht, $augenfarbe, $haarfarbe ) {
        $this->name = $name;
        $this->geschlecht = $geschlecht;
        $this->augenfarbe= $augenfarbe;
        $this->haarfarbe = $haarfarbe;

        }


        function __destruct() {
            echo '<p>'.$this->name.'wird  gelöscht </p>';

        }
        
 }
//..weitere Methoden 

$anna = new Mensch('Anna' , 'Weiblich', 'blue', 'schwarz');
$Paul = new Mensch('Paul' , ';Mänlich', 'braun', 'blond');


echo '<pre>', print_r( $anna ), '</pre>';
echo '<pre>', print_r( $Paul ), '</pre>';


echo '<p>';

echo '</p>';

?>