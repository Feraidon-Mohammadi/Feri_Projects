<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ein kleines Rechenbeispiel</title>
</head>
<body>

<h1>Ein kleines Rechenbeispiel</h1>

<?php
    
        $zahl1 = 0;
        $zahl2 = 0;

    if( isset( $_POST['plus']) OR isset( $_POST['mal'] ) ) {
        $erg = 0;
        $op = '';


    $zahl1 = (double)$_POST['zahl1'];
    $zahl2 = (double)$_POST['zahl2'];

    if(isset( $_POST['plus'] ) ){
        $erg = $zahl1 + $zahl2;
        $op = 'Addition';
    } elseif ( isset( $_POST['mal'] ) ) {

    $erg = $zahl1 * $zahl2;
    $op = 'Multiplikation';

    echo '<pre>', var_dump( $_POST, $zahl1), '</pre>';
    }
    
    echo "<p>Das ergebnis de $op ist $erg (" . gettype($erg) . ").</p>";

    #echo '<pre>' var_dump($_POST, $zahl1), '</pre>';
    }








   /*  $zahl1 = 0;
    $zahl2 = 0;

if( isset( $_GET['plus']) OR isset( $_GET['mal'] ) ) {
    $erg = 0;
    $op = '';


$zahl1 = (double)$_GET['zahl1'];
$zahl2 = (double)$_POST['zahl2'];

if(isset( $_POST['plus'] ) ){
    $erg = $zahl1 + $zahl2;
    $op = 'Addition';
} elseif ( isset( $_POST['mal'] ) ) {

$erg = $zahl1 * $zahl2;
$op = 'Multiplikation';

echo '<pre>', var_dump( $_POST, $zahl1), '</pre>';
}

echo "<p>Das ergebnis de $op ist $erg (" . gettype($erg) . ").</p>";

#echo '<pre>' var_dump($_POST, $zahl1), '</pre>';
}
 */



?>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">


    <p>erste zahl: <input type="text" name="zahl1" value="<?php echo $zahl1;  ?>"></p>
    <p>zweite zahl: <input type="text" name="zahl2" value="<?php echo $zahl2;  ?>"></p>

    <p>
        <p><input type="submit" value="+" name="plus"></p>
        <p><input type="submit" value="x" name="plus"></p>
    </p>






</form>


</body>
</html>