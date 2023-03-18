<?php
    
    require_once 'Fahrzeug-class.php';

    $vespa = new Fahrzeug( 'Vespa Piaggio', 25, 'rot' );

    /* Daten des Objektes als Zeichenkette in eine Variable speichern  */

    $s = serialize( $vespa);


    /* Dise zeichenkette zum Test ausgeben  */
    echo "<p> $s</p>";


print_r(   "<p>$s</p>"    );


file_put_contents(    'vespa.dat', $s     );
echo '<p>Objekt serialisiert und in Datei gespeichert.</p>';







?>