<?php declare(strict_types=1); ?>
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Funktionen</h1>

<?php


/* Eine Funktion wird definiert */
    function hallo() {
        echo '<p>Hallo</p>';
    }


/* Funktion mit Paramer */
    function begruessung( $ausgabe ) {
        if( !empty( $ausgabe ) ){
            return "<p>Hallo $ausgabe!</p>";
        }

/* Anweisungen nach return werder nicht ausfeführt */
        return"<p>Hallo Peter</p>";
    }

/* Eine funktion wird aufgerufen und tut das was sie tut */
        hallo();


       $msg = begruessung( 'Dieter', 'Klaus' );
        echo $msg;


/* optionale Parameter */
/* gehören IMMer ans Ende der Parameter-Kette */
    function gesamtpreis( $anzahl, $preis = 42, $waehrung = 'Euro' ) {
        $erg = $anzahl * $preis;
        return "<p>Ihr einkauf kostet $erg $waehrung.</p>";


}

    echo gesamtpreis( 5, 12.5, 'Euro' );

    echo gesamtpreis( 2, 20, 'Dollar' );



/* beliebig viele Parameter  */

    function viele_Parameter( $a ) {
        $num_args = func_num_args(); /* for numbers to send */
        $args = func_get_args();
        echo "<p>Das erste Paramer ist $a.</p>";
        echo "<p>Es wurden $num_args Parameter übergeben.</p>";

        echo '<pre>';
        var_dump( $args );
        echo '</pre>';
    }
    viele_parameter( 5, 'Wuatsch', true, 12.5 );


/* varidische Parameter */
    function variadische( ...$params) {
        echo '<pre>', print_r( $params, true ), '</pre>';

    }
    variadische( 'Butter', 'Mehl', 'Milch', 'Eier', true, 6.8 );


    function mitarbeiter( $m_name, $m_vorname, $beruf, $alter){
        if( is_array( $m_vorname ) ) {
            $vn = implode( ', ', $m_vorname );
        }
        else {
            $vn = $m_vorname;
        }
        return "<p>$vn $m_name ist $beruf und $alter Jahre alte.</P>";
    }


/* normaler Aufruf  */
    echo mitarbeiter( 'Kenobi', 'Obi-Wan', 'jedi', 185 );


/* variadischer Aufruf */
    $m_array = array(
        'Duck',
        array( 'donald', 'Fauntleroy' ),
        'Ente',
        76
    );
    echo mitarbeiter( ...$m_array );


/* explizirte Datentypen bei Parametern und return  wichtig! vorher declare(strict_types=1) als erste anweisung in der Datei angeben  */
    function addiere( int $a, int $b ):int {
        return $a + $b;

    }
        echo addiere( 1, 2 ) . '<br>';

        echo addiere( '1', '2' ) . '<br>';

        echo addiere( true, '2abc' ) . '<br>'; /* es zeigt ein fehler meldung aber ist richtig  */
        
    ?>

</body>
</html>