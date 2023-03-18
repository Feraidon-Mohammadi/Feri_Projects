<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Formular Auswertung</h1>

    <?php 

    echo 'Vorname: ' . $_POST['vorname'] . '<br>';
    echo 'Nachname: ' . $_POST['nachname'] . '<br>';
    echo 'E-Mail: ' . $_POST['email'] . '<br>';

        echo '<pre>', print_r( $_POST ), '</pre>';

        








    ?>

    <?php 

        echo 'Vorname: ' . $_POST['vorname'] . '<br>';
        echo 'Nachname: ' . $_POST['nachname'] . '<br>';
        echo 'Wohnort: ' . $_POST['wohnort'] . '<br>';
        echo 'E-Mail: ' . $_POST['email'] . '<br>';

            echo '<pre>', print_r( $_POST ), '</pre>';


    ?>



</body>
</html>