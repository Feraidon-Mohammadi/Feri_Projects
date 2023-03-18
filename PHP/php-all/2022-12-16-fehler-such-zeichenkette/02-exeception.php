<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- Variable unbekannt -->
<?php 
try {
    if( !isset($x) ) {
        throw new Exception( 'Variable unbekannt' );
    }
echo "Varibale: $x</p>";

} catch ( Exception $e ) {
    echo '<p>' . $e->getMessage() . '</p>';
    echo '<p>' . $e->getMessage( ) . '</P>';

}finally {
    echo '<p> Ende, Variable unbekannt </p>';
}

/* division durch 0 */
$x = 42;
$y = 0; //fehlerhafter Wert

try {
    if( $y === 0)
        throw new Exception( 'Division durch 0 ');
        $z = $x / $y;
        echo "<p>Division $x / $y = $z<br>";
} catch ( Exception $e ) {
        echo '<p>' . $e->getMessage() . '</p>';
} finally {
    echo 'Ende, Division durch 0</p>';
}

/* zugriff auf Funktion  */



    try {
        if(!function_exists( 'testFunktion' ) ) {
            throw new Excepton( 'Fehler: funktion unbekannt');
        } 
        testFunktio();
    } catch(Exception $e){
            echo '<p>' . $e->getMessage() . '<br>';
            echo 'pre', print_r($e, true ), '</pre>';
    }finally {
            echo 'Ende, Funktion unbekannt </p>';
    }
    echo '<p>Ende des programms</p>';


 ?>


</body>
</html>