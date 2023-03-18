<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    




<h1>Paramere-übergabe per referenz</h1>

<?php 
/* barai tavan adad masalan 3²=9 ya har adade dige ke lazem darim estefade mishavad (just need to change $wert = 1... than answer will be validated) */ 
function quadrat( $zahl ) {
    echo "<p>Das Quadrat von $zahl ist: ";
    $zahl *= $zahl;
    echo "$zahl.</p>";

}


function quadrat_ref( &$zahl ) {
    echo "<p>Das Quadrat von $zahl ist: ";
    $zahl *= $zahl;
    echo "$zahl.</p>";

}

$wert = 3;

echo "<b>Der Ausgangswert von \$wert ist </b>.</p>";
echo '<h2>call-by-value (Standardverhalten)</h2>';
for( $i = 1; $i <4; $i++ ) {

    quadrat( $wert );
}
echo "<p>Der Wert von \$wert nach call-by value: <b>$wert</b>.</p>";




echo '<h2>call-by-reference</h2>';
for( $i = 1; $i <4; $i++ ) {

    quadrat_ref( $wert );
}
echo "<p>Der Wert von \$wert nach call-by value: <b>$wert</b>.</p>";













?>
</body>
</html>