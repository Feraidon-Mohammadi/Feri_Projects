<?php 
class Mensch {
    static $count; //Klassenvariablen
    const MAX_ALTER = 122; // ältesster Mensch

// eigenschaften 
private $zufriedenheit = 0;

//methoden
function arbeiten($dauer) {
    self::$count++; //Zugriff auf Klassenvariable


    //$this: Referenz auf das aktuelle object
    $this->zufriedenheit += $dauer/4;
    echo '<p>(' .self::$count.') Arbeit macht zufrieden...</p>';

    echo '<p>Zufriedenheit: '.$this->zufriedenheit.'</p>';

}

function ausruhen($dauer){

    self::$count++;

    $this->zufriedenheit+=$dauer/2;

    echo '<p>(' .self::$count.') Ausruhen ist besser...</p>';

    echo '<p>Zufriedenheit: '.$this->zufriedenheit.'</p>';



    }
}


$anna = new Mensch();
$anna->arbeiten(8);
$anna->ausruhen(6);
$anna->arbeiten(4);

$paul = new Mensch();
$paul->arbeiten(3);
$paul->ausruhen(7);
$paul->arbeiten(9);

echo '<p> Instesamt sind die Methoden der Klasse Mensch  '. Mensch::$count . ' Mal 
aufgerugen worden .</p>';

echo '<p>Der älteste Mensch, eine französische Frau, wurde ' . Mensch::MAX_ALTER . ' jahre alt.</p>'



?>