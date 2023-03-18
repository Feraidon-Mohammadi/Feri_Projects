<?php 
 class  Fahrzeug {


    
        function __construct( private $bezeichnung, private $geschwindigkeit ) {}
    
    
        function beschleunigen($wert) {
            $this->geschwindigkeit += $wert;
        }
        /* -this gehört dazu - dass ich nur noch echo $objekt ausführen muss, um  sie aufzurufen..... */
        function __toString() {
            return $this->bezeichnung . ', ' . $this->geschwindigkeit . ' km/h<br>';
    
    
        }
    }




















?>