<?php 

class Fahrzeug {

    function __construct(private $bezeichnung = 'unbekannt', private $geschwindigkeit = 0) {}

    function beschleunigen($wert) {
        $this->geschwindigkeit += $wert;

    }

    function __toString() {
        return "$this->bezeichnung, $this->geschwindigkeit km/h<br>";

    }
    /* methode zum klonen eines objektes  */
    function __clone() {

        $this->bezeichnung = 'Klon von ' . $this->bezeichnung;
        $this->geschwindigkeit = $this->geschwindigkeit + 1;

    }

/* Methode zum kopieren eines objectes */
static function kopieVon($original) {

$new = new Fahrzeug();
$new->bezeichnung = 'kopie von ' . $original->bezeichnung;
$new->geschwindigkeit = $original->geschwindigkeit + 1;
return $new;


}







}
/* Originalobjekt */
$vespa = new Fahrzeug('Vespa Piaggio', 25);

/* Referenz auf Originalobjekt  */
$suzuki = $vespa;


/* Klonen eines Objektes */
$yamaha = clone $vespa;

/* Kopie eines Objektes  */
$honda = Fahrzeug::kopieVon($vespa);

/* Auswirkung  auf die zweite Referenz  */
$vespa->beschleunigen(20);
echo 'suzuki: ';/* verknupfung */

echo $suzuki;




/* Ausgabe des Klons  */
echo 'yamaha: ';/* verknupfung */
echo $yamaha;



/* ändern und ausgabe der kopie  */
$honda->beschleunigen(30);
echo 'honda: ';/* verknupfung */
echo $honda;


echo 'honda: ';
echo $honda;





?>