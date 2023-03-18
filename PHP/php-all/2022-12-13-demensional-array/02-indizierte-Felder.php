<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>indizierte Fehler (arrays)</h1>


    <?php

        $staedte = array(
            'Erfurt',
            'Jena',
            'frankfurt',
            'paris',
            'London',
        );

        echo "<p>$staedte[2]</p>";

        // kurzschreibweise seit php 5.4
        $laender = [
            'Deutschland',
            'schweiz',
            'Frankreich',
        ];

        // während der Entwicklungsphase: Ausgabe eines Arrays zu Testzwecken 
        // 1. mit print_r()

        echo '<pre>';
        print_r( $staedte );
        echo '</pre>';


        echo '<pre>', print_r( $laender ), '</pre>';

        // 2. mit var_dump()

        echo '<pre>' , var_dump($laender, $staedte ), '</pre>';

        // anfügen eines wertes an ein indiziertes Array 
        $laender[] = 'Belgien';

        // Ändern eines wertes 
        $laender[2] = 'Luxxembourgh';
        // Löschen eines Wertes
        unset( $laender[1]);
    

        echo '<pre>', var_dump( $laender ), '</pre>';

        // Index neu  belegen 
        $laender[1] = 'Portugal';

        $laender[] = 'Lichtenstein';

        echo '<pre>', print_r( $laender ), '</pre>';

        // sortiere das Array nach seinen Indizes aufsteigend 
        ksort( $laender );

        echo '<pre>', print_r( $laender ), '</pre>';

        // ausgabe für den produktiven Einsatz
        echo '<p>';

        foreach( $staedte as $stadt ) {
            echo "$stadt, ";

        }
        
        echo '</p>';

        //ausgabe der Anzahl der Array-Einträge
        echo '<p>Das Array $laender hat ' . count($laender ) . ' Einträge.</p>';



    ?>







</body>
</html>