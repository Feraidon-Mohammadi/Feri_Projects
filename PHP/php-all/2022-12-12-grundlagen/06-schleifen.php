<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<h1>schleifen</h1>
<h2>while (kopfgesteurt)</h2>

    	<?php
            	$z = $x = 5;

             while( $z <= 10 ) {
                 echo "$z<br>";
                 $z++;

             }


        ?>
        <h2>do-while (fußgesteurt)</h2>
             
             <?php


                	do {
                        echo  "$x<br>";
                        $x++;



                    } while( $x <= 10 );

                    echo "x = $x<br>(nach der schleife),";


             ?>

            <h2>for-shleife</h2>

            <?php


                for( $i = 1; $i <= 10; $i++)
                    echo "$i<br>";
                    













            ?>













    
</body>
</html>