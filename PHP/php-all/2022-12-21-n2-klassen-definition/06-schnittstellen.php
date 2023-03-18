<?php 

interface iFahrbar {
    function rollen();
    function reifernwechsel();

}

interface iSchwimmfaehig {

function anlegen();
function kentern();


}


class AmphiCar implements iFahrbar, iSchwimmfaehig {
    /* Methoden, die aufgrund iFahrbar implementiert werden müssen */
    function rollen() { echo 'Es rollt<br>'; }
    function reifernwechsel() { echo 'Es werden Reifen gewechselt <br>'; }


    /* Methoden die aufgrund iSchwimmfaehig implementiert werden Müssen */
    function anlegen() { echo 'Es legt an <br>';  }
    function kentern() { echo 'Es kentert <br>'; }


/* eigen methode */
function bewegen() { echo 'Es bewegt sich (doch)<br>'; }


}

$VwType166 = new AmphiCar();
$VwType166->rollen ();
$VwType166->reifernwechsel ();
$VwType166->anlegen ();
$VwType166->kentern();
$VwType166->bewegen ();


?>