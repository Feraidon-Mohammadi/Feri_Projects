<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formatiert Ausgaben mit printf()</title>
</head>
<body>
    

<h1>Formatiert Ausgaben mit printf()</code></h1>

<?php
    
    printf( '<p>Eine normal Ausgabe</p>' );
    
    printf( '<p>Ausgabe Typ b (binär): %b</p>', 125 );
    printf( '<p>Ausgabe Typ c (Zahl als ASCII): %c</p>', 125 );
    printf( '<p>Ausgabe Typ d (Ganzzahl): %d</p>', 125.43 );
    printf( '<p>Ausgabe Typ f (String): %f</p>', 125.43 );
    printf( '<p>Ausgabe Typ s (Zahl als ASCII): %g</p>', 125.43 );
    printf( '<p>Ausgabe Typ x (Hexadezimal): %x</p>', 125 );



?>
<h1>Führende null</h1>


<?php 
 /* maskierte nummber or password */

   $hrs = 4;
    $min = 30;
    printf( '<p>Ausgabe der Uhrzeit: %02d:%02d</p>',$hrs, $min  )
?>

<h2>Zeichenketten auffüllen</h2>

<?php 
printf( "<p>Ein aufgefüllter String: %'*7s</p>", 'TH' );


?>
<h2>Formatierte zahlenwerte</h2>
<?php 


/*  brei moratam kardan adad estefade mishavad  */
$preise = array( 22124.667, 12.8, 234, 53.333337, .5 );

foreach( $preise as $preis ) {
    printf( 'Unser Preis: %03.2f €<br>', $preis );

}



?>


<h2>Formatierte Zahlenwerte mit number_format()</h2>

<?php 

echo '<p>';

foreach ($preise as $preis) {
    echo number_format($preis, 2, ',' ,'' ) .'€<br>';
}

?>






</body>
</html>