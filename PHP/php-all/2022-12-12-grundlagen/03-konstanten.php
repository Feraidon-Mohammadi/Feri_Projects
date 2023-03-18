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

        /*=============================================
        ================*/


        // 1. klassische Variante
        define( 'MWST' , 0.19 );

        echo '<p>Die Mehrwertsteuer in Deutschland beträgt zurzeit '. (MWST * 100) . '%.</p>';

        // 2.alternative Variante (seit PHP 5.3)
        const MWST = 0.07;
        // Hinweis: diese Variante funktioniert nur im Top.Level-Scope!!!

        
        

    ?>

<body>


</html>