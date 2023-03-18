<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> mehrdimensionale Ferlder</title>
</head>
<body>
    <h1>mehrdimensionale felder</h1>
    <?php
        
        $personen = array(
            array(
                'Manfred',
                'deutsch',
                53,
                'männlich',
            ),

            array(
                'Cindy',
                'englisch',
                23,
                'weiblich',
      
            ),

            array(
                'Carlos',
                'spaniesch',
                23,
                'Männlich',
      
            ),

        );

//Werte ausgeben 
            echo '<p>'
                . $personen[2][0] . ' ist '
                . $personen[2][2] . ' jahr alt , spricht '
                . $personen[2][1] . ' und ist '
                . $personen[2][3] . ' </p>';


            // ändern 
            $personen[2][2] = 35;

         echo '<pre>', print_r( $personen ), '</pre>';

            // Hizufügen
            $personen[] = array(
                'Ursula',
                'schwedisch',
                47,
                'weiblich',



            );



            $personen[4][0] = 'johanna';
            $personen[4][1] = 'dämnisch';
            $personen[4][2] =  22;
            $personen[4][3] = 'weiblich';
           
          echo '<pre>', print_r( $personen ), '</pre>';
    

    ?>

            <h2>ausgabe der personalliste mit verschachtelter foreach-Schleife</h2>

            <table style="border: 1px solid gray">
        <tr>
            <th>Name</th>
            <th>Geschlecht</th>
            <th>Sprache</th>
            <th>Alter</th>
        </tr>
        <!-- Schleife für das äußere Array (Zeilen) -->
        <?php foreach( $personen as $person ): ?>
            <tr>
                <?php foreach( $person as $eigenschaft ): ?>
                    <td><?php echo $eigenschaft; ?></td>
                <?php endforeach; ?>
            </tr>
        <?php endforeach; ?>
    </table>

    <h2>Ausgabe der personalliste mit der list ()-Funktion</h2>
                <table style="border: 1px solid gray;">
                        <tr>
                            <th>Name</th>
                            <th>Gechlecht</th>
                            <th>Alter</th>
                            <th>Sprache</th>
                        </tr>

                        <!--schleife für das äußere Array (Zeilen)-->


                        <?php foreach( $personen as $person ): ?>
                        <tr>
                            <!-- list()-funktion für das innere Array (spalten) --> 
                            <?php list( $pname, $sprache, $alter, $geschlecht ) = $person ?>


                            <td><?php echo $pname; ?></td>
                            <td><?php echo $geschlecht; ?></td>
                            <td><?php echo $sprache; ?></td>
                            <td><?php echo $alter; ?></td>


                        </tr>
                    <?php endforeach; ?>

                </table>


        <h2>mehrdimensionale assoziative Arrays</h2>
                    <?php
                        
                        $laender = array(
                            'Spanien' => array(

                                'Hauptstadt' => 'Madrid',
                                'Sprache' => 'spanisch',
                                'Währung' => 'Euro',
                                'Fläche' => '504.645 qkm'
                            ),

                            'England' => array(

                                'Hauptstadt' => 'London',
                                'Sprache' => 'englisch',
                                'Währung' => 'pfund Sterling',
                                'Fläche' => '130.395 qkm'
                            ),

                            'Portugal' => array(

                                'Hauptstadt' => 'Lissabon',
                                'Sprache' => 'portugiesisch',
                                'Währung' => 'Euro',
                                'Fläche' => '92.345 qkm'
                            )

                        );


                        // zugriff

                        $land = 'England';

                        echo "<p>Angabe tu $land<br>";
                        echo 'Hauptstadt: ' . $laender[$land]['Hauptstadt'] . '<br>';
                        echo 'Fläche: ' . $laender[$land]['Fläche'] . '<br>';
                        echo 'Sprachet: ' . $laender[$land]['Sprache'] . '<br>';
                        echo 'Währung: ' . $laender[$land]['Währung'] . '</p>';


                    ?>


             <table>
                    <tr>
                        <th>Land</th>
                        <th>Hauptstadt</th>
                        <th>Sprache</th>
                        <th>Währung</th>
                        <th>Fläche</th>
                    </tr>
    
            </table>

        <?php foreach( $laender as $land => $infos): ?>
             <tr>
                 <!--Land ist der schlüssel des äußeren Arrays, weshalb er hier bereits
                 ausgegeben wereden muss-->
                 <td><?php echo $land; ?></td>

                <!--Diese reslichen Infors kommen aus dem inneren Array -->
                <?php foreach( $infos as $info ): ?>
                <td><?php echo $info; ?></td>
            
            <?php endforeach; ?>
            </tr>







        <?php endforeach; ?>


</body>
</html>