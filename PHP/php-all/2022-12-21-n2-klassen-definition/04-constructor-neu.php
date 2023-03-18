<?php 
class Fahrzeug {
    function __construct( private $bezeichnung, private $geschwindigkeit ) {}


    function beschleunigen($wert) {
        $this->geschwindigkeit += $wert;
    }
    /* -this gehört dazu - dass ich nur noch echo $objekt ausführen muss, um  sie aufzurufen..... */
    function __toString() {
        return $this->bezeichnung . ', ' . $this->geschwindigkeit . ' km/h<br>';


    }
}

// objekte erzeugen
$vespa = new Fahrzeug('Vespa Piaggio', 25);
$scania = new Fahrzeug('Scania Ts 360', 62);


//Objekt ausgeben
echo $vespa;
echo $scania;

$vespa->beschleunigen(20);

echo $vespa;


?>