<?php 
class Fahrzeug {
    function __construct(
        private $bezeichnung = 'unbekannt ',
        private $geschwindigkeit = 0,
        private $farbe = 'unbekannt' 
    ){}

function __toString(){

    return "$this->bezeichnung, $this->geschwindigkeit km/h, $this->farbe";

}




}






?>