<!DOCTYPE html>
<html long="de">
    <head>
        
        <title>Hallo php</title>
</head>
<body>

    <h1>variablen</h1>

    <?php

        // Fehlerausgaben im Script regeln
         error_reporting(E_ALL);




        // Erzeugt Warnun 
         echo "<p>Der wert der Variable i ist : $i</p>";


        // Erzeugt einen Fatal Error. Folge-Anweisungen werden nicht mehr durschgefpührt
        #echo 4 / 0;


        // Tippfehler bei Funktionsname
        print_r($i);



        echo '<p>weitere Anweisungen</p>';


    ?>


<body>
</html>