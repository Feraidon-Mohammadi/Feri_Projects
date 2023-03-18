<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datumsfunktionen</title>
</head>
<body>
    <h1>Datumsfunktionen</h1>



<?php 


echo '<pre>', var_dump( getdate() ), '</pre>';

$zeitstempel = getdate();
printf( '<p>Datum: %s, %d. %s %d</p>', $zeitstempel['weekday'], $zeitstempel['mday'],
 $zeitstempel['month'], $zeitstempel['year'] );

/* ===funktionen zur formatierten Datumsausgabe
================== */


/* 1. date() */
echo '<pre>', print_r(  time(), true ), '</pre>';



echo '<p>'; 
echo date('d,m.Y H:i:s');
echo '</p>';


echo '<p>'; 
echo date('l, d.m.Y H:i \U\h\r' );
echo '</p>';


/* zeitmessugn mit microtime() */


echo '<p>'; 
echo 'microtime(): ' . microtime() . '<br>';
echo 'microtime( true):' . microtime( true );
echo '</p>';

$start = microtime(true);

for( $i = 1; $i < 1000; $i++ ) {
    $quadrat = sqrt($i);

}

$end = microtime(true);


echo '<p>Die Ausgührungsdauer: ' . ($end - $start) . ' Sekunden.</p>';
?>


<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
<p>Geben Sie bitte das Datum in der form tt.mm.jjjj ein !</p>
<input type="date" name="datum">
<!--####1 self <input type="text" name="datum"> -->

    <input type="submit" value="Prüfen" name="senden" >
</form>

<?php 

if( isset( $_POST['senden'])){
    /* zum ptügrn der korrekten Datumsangabe mit der funktion checkdate()benötigen wir 
    das Datum in seine einzelnen Teile zerlegt. */
}

/* ####1 self$datum = explode( '.', $_POST['datum'] ); */
$datum = explode( '-', $_POST['datum'] );

echo '<pre>',var_dump( $datum ), '</pre>';

/* ####1 self$check = checkdate( (int)$datum[1], (int)$datum[0], (int)$datum[2] ); */
$check = checkdate( (int)$datum[1], (int)$datum[2], (int)$datum[0] );


if($check) {
    echo '<p>' . $_POST['datum'] . ' ist korrekt.</p>';

}else {
    echo '<p>' . $_POST['datum'] . ' ist <b>nicht </b> korrekt.</p>';
}




?>







</body>
</html>