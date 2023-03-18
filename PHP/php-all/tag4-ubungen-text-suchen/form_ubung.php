<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Addition mit eingebundene Funktion</title>
</head>
<body>

    

    <h1>Addition mit eingebundene Funktion</h1>

        <h2> bitte geben Sie zwei oder drei Zahlen ein und senden Sie das Formular ab</h2>
      
          

       <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">

       <p>Zahl1: <input type="Number" name="zahl1" value="<?php echo $zahl1;  ?>"></p>
       <p>Zahl2: <input type="Number" name="zahl2" value="<?php echo $zahl2;  ?>"></p>
       <p>Zahl3(optional): <input type="Number" name="zahl3" value="<?php echo $zahl3;  ?>"></p>

   
         <p><input type="submit" value="Absenden" name="plus"></p>



    <?php 

       

        if( isset( $_POST['plus']) OR isset( $_POST['mal'] ) ) {
        $erg = 0;
        $op = '';


        $Zahl1 = (double)$_POST['zahl1'];
        $Zahl2 = (double)$_POST['zahl2'];
        $Zahl3 = (double)$_POST['zahl3'];

        if(isset( $_POST['plus'] ) ){
        $erg = $Zahl1 + $Zahl2 + $Zahl3;
        $op = 'Addition';
        } elseif ( isset( $_POST['mal'] ) ) {

        $erg = $zahl1 * $zahl2 * $zahl3;
        $op = 'Multiplikation';

        echo '<pre>', var_dump( $_POST, $Zahl1, $Zahl2, $Zahl3 ), '</pre>';
        }

        echo "<p>Das ergebnis des $op ist $erg (" . gettype($erg) . ").</p>";

        }

    ?>





    </form>


<!--

    

       function addiere( int $zahl1, int $zahl2, int $zahl3 ):int {
        return $zahl1 + $zahl2 + $zahl3;

        }
        echo addiere( 1, 2, 3 ) . '<br>';

        echo addiere( '1', '2', '3' ) . '<br>';

        echo addiere( true, '2abc' ) . '<br>';
    


 -->













    


</body>
</html>