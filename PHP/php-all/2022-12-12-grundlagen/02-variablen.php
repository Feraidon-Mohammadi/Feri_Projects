<!DOCTYPE html>
<html long="de">
    <head>
        <meta charset="UTF-8"
        <meta http-equiv="x-UA-Compatible"
        <meta name="viewport" content="width=device-width, initial-scale=1.0"
        <title>Hallo php</title>
</head>
<body>

    <h1>variablen</h1>

    <?php


        // Vaariablen beginnen mit einem $

        $eine_zahl = 5;
        $keine_ahnung = ' 5 Tassen kaffee';

        echo '<p>' . gettype($keine_ahnung) . '</p>';

        $erg = $eine_zahl + $keine_ahnung;


        echo '<p>Das ergebnis ist: ' .$erg . 'vom Datentyp ' .gettype($erg) . '</p>';



        /* besonderheiten bein zeichenketten */
        /* zeichenketten können in 'single-quotes' oder in "double Quotes" stehen */

        $eine_zeichenkette = 'Hier kommt ein Karton';

        echo '<h2>' . $eine_zeichenkette . '</h2>';

        echo "<h2>$eine_zeichenkette<h2>";

        /*=== Abgekürzte mathematische  opetationen
        ========================================================================================================================*/

        // 1. pre-Inkrement
        $a = 39;
        $b = 2;

        echo "<P>/$a = $b, \$b =$b</p>";

        $erg = ++$a + $b;
        echo "<p>Das Erfgebnis von $a + $b ist <b>$erg</b>.</p>";

        /* was macht PHP?
        1.Das Inkrement wird ausgeführt:39 + 1 = 40
        2.Die Addition wird durchgeführt: 40 + 2 = 42
        3.Das Ergebnis wird der Variable $erg zugewiesen.*/

        // 2. post-Inkrement 
        $a = 39;

        $erg = $a++ + $b;
        echo "<p>Das Ergebnis von $a + $b ist <b>$erg</b> . </p>";
        /* was macht PHP?
        1.Die Additon wird durchgeführt: 39 + 2 = 41 (a + b)
        2.Das Ergebnis wird der Variable $erg zugewiesen
        3.Das Inkrement wird ausgeführt: 39 + 1 = 40 */






       /*=== Abgekürzte mathematische  opetationen
        ========================================================================================================================*/


        $a = 10;
        $b += 5; /* ist das selbe wie &a = $a + 5 */
        echo "<p>Der wert von \$a ist $a.</p>";

        /*=== Daten explizit konvertieren 
        ========================================================================================================================*/

        $z1 = '25.8';
        $z2 = '17';

        $erg = (int)$Z2 + (double)$z1;


        echo "<p>Das Ergebnis $z1 + $z2 ist  $erg</p>";

        $z1 = '25.8';
        $z2 = '17';

        $erg = (double)$z2 + (int)$z1;

        echo "<p>Das Ergebnis $z1 + $z2 ist  $erg</p>";



    ?>

</body>
</html>