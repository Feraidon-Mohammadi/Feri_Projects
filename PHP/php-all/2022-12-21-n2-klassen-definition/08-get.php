<?php
require_once 'Fahrzeug-class.php';

if( !file_exists('vespa.dat' )) {
    exit( 'Datei kann nicht gefunden werden ');
} 

$s = file_get_contents( 'vespa.dat');
$vespa = unserialize($s);

    echo 'Objekt aus Datei gelesen und deserializiert<br>';
    echo $vespa;

    
?>