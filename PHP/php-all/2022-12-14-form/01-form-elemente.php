<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auswertung verschiedener Formular-Elemente</title>
</head>
<body>
    
<h1>Auswertung verschiedener Formular-Elemente</h1>

    <?php 

        if( isset ($_POST['e-mail'] ) ) {
            // ist das pflichfeld (E-Mail) gefüllt
            //empty() prüft , ob das übergebene Element leer, null oder nicht vorhanden ist 
            //trim() entfern leerzeichen, Tab-aprunge etc. (whitespaces ) links undrechts vom
            if( empty( trim( $_POST['e-mail']  ) ) ){
                echo '<p>Mail ist leer</p>';
            } else {
                echo '<p>Mail-Adresse: ' . $_POST['e-mail'] . '</p>';
            }


                // Prüfe ob Eissorte ausgewält wurde
                if( $_POST['eissorte'] == -1 )  {
                    echo '<p>Eissorte wurde nicht gewählt :-( </p>';

                } else {
                    echo '<p>Eissorte: ' .$_POST['eissorte'] . '</p>';
                }


        //Ausgabe der Nachricht 
        // Das zweite argument nl2br() bei gibt an, ob die br-Tags xhtml-konform (true-standard) oder HTML5-konform (false) sind.
        echo '<p>Ihre Nachricht:<br>' . nl2br($_POST['message'] ) . '</p>';
        //echo '<p>Ihre Nachricht:<br>' . nl2br($_POST['message'], true/false) . '</p>';



           echo '<pre>', print_r($_POST, true ), '</pre>';

        } else {
            echo '<p>Diese Seite wurde nicht duch ein Formular aufgerufen. Bitte füllen sie zunächst das <a href="01-form-element.html">Formular </a> aus!</p>';
        }
        




    ?>




</body>
</html>