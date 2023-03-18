
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
       <?php

        


             /*
             ist gleich ==
             nicht gleich !=
             größer als >
             kleiner als <
             größer gleich >=
             kleiner gleich <=

             ist identisch ===
             ist nicht identisch  !==
             */

             //ist gleich 

             if( 6 == '6') {
                echo 'wahr<br>';
            
             } else {
                echo 'falsh<br>';

             }

             // ist identisch 
             // vergleicht Wert UND Datentyp

             if( 6 === '6') {
                echo 'wahr<br>';
             } else {
                echo 'falsch<br>';

             }
             

             //Trenär-Operator 
             $schlalter = true;


             $licht = ( $schalter === true ) ? 'AN' : 'AUS';




            /* === mehrfachverzweigungen 
            =====================================================================================================*/

             $status = 200;
             switch ($status) {
                    case 200:
                        $erg = 'okay';
                    case 300:
                        $erg = 'Zugriff verweigert';
                        break;
                    case 400:
                        $erg = 'datei nicht gefunden';
                        break;


                    case 500:
                        $erg = 'Server-Ferhler';
                        break;
                    Degault:
                    $erg = 'ungültiger status-Code';

             }

            echo "<p>Server-status: $erg ($status)</p>";

            // Mehrfachverzweigung mit match seit PHP 8.0


            $erg2 = match($status) {
                200 => 'okay',
                300 => 'Zugriff verweigert',
                400 => 'Datei nicht gefunden',
                500 => 'Server-Fehler',
                default => 'Ungültiger Status-Code',//maybe not needed  ,


            };
            
            echo "<p>Server-Status: $erg2 ($status)</p>";


            // spaceship-Operator

            $a = 14;
            $b = 9;

            echo $a <=> $b;


            /*
            ergibt 
            -1 wenn a < b 
            0 wenn a = b 
            1 wenn a > b
            */

            // koaleszenz-Operatoren seit PHP 7

            echo $t ?? '$t nicht vorhanden';

            $t = 42;

            echo $t ?? '<br>$t nicht vorhanden<br>';


            //$l = NULL;



            $l ??= '$l nicht vorhanden<br>';
            echo $l;

            $l = 4200;
            $l ??= '$l nicht vorhanden<br>';
            echo $l;




        ?>
</body>
</html>