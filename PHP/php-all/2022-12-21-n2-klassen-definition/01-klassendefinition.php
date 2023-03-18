<?php 
class Mensch {
    /* Lisste der Eigenschaften */

    /* Sichtbarkeitsstufen:
    *privat:        steht nur innerhalb der Klasse zur Verfugung
    *protected:     wie private-aber Zugriff aus der erbendn Klasse möglich
    *public:        überall suchtbar und verwendbar
     */
    private $arme = 2;
    private $beine = 2;
    private $name = '';
    public $augenfarbe = '';
}
$anna = new Mensch();

$anna->augenfarbe = 'blue';

echo' <pre>', var_dump($anna),'</pre>';

$paul = new Mensch();

/* $paul ->name = 'paul'; */

echo '<pre>', var_dump( $paul ), '</pre>';


?>