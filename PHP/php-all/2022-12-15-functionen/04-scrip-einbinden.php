<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Externs PHP-Script einbinden</title>
</head>
<body>

    <h1>Externs PHP-Script einbinden</h1>

    <?php 
    
    
    /* Zum Einbinden von Skripten kannt PHP vier Befehle:
    *
    * include => bei fehlenden inclide -Datei  wird Folge-code ausgeführt 
    * require => bei fehlenden inclide -Datei  wird folge-code nicht  ausgeführt (FAtal-Error)
    * 
    *
    * include_once =>
    * require-once =>
    *
    *  */
    
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';
    include_once '04-extenes-script.inc.php';

    //echo gib_mir( 'Kirk', 'james T.', 65 );

    
    echo '<p>Das ist eine folgende Ausgabe</p>';

    
    
    
    
    
    ?>






</body>
</html>