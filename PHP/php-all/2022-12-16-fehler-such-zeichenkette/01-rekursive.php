<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>rekursive funktionen</h1>


<?php 
function halbieren( &$z ) {
    $z = $z / 2;
    if( $z > 0.1 ){
        echo "z: $z<br>";
        halbieren( $z);
    }
}



$x = 1.5;
echo "<p>x: $x</p><p>";

halbieren( $x );

echo "</p><p>x nach halbieren: $x</p>";



?>


</body>
</html>