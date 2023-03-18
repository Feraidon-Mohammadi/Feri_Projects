<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    

    <h1>assoziative Felder</h2>

    <?php

        // Array anlegen 
        $hauptstaedte = Array(
            'schweiz' => 'Bern',
            'Frankreich' => 'Paris',
            'spanien' => 'Madrid',

        );

        // Array-Werte Ausgeben

        echo "<p>{$hauptstaedte['schweiz']}";

        // Hinzufügen 
        $hauptstaedte['poldand']  = 'Warschau';

        echo '<pre>', print_r( $hauptstaedte ), '</pre>';

        //Löschen
        unset( $hauptstaedte['Spanien'] );
        
        echo '<pre>', print_r( $hauptstaedte ), '</pre>';


        //produktiver Einsatz




    ?>

<table style="border: 1px solid gray">
        <tr>
        <th>Land</th>
        <th>Hauptstadt</th>
        </tr>

        <?php
        //syntax für ass . Arrays foreach( $array as $key => $value )

        foreach( $hauptstaedte as $land => $stadt ) {
                echo '<tr>';
                    echo "<td>$land</td>";
                    echo "<td>$stadt</td>";

                
                echo '</tr>';


        }
        ?>

    </table>



</body>
</html>