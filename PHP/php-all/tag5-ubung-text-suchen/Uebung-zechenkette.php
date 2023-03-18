<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Begriff in einer textpassage suchen</title>
    <style>
        
    .$str {
        height: 30px ;
        padding: 4px ;
        border: 1px solid #dddddd;


    }




    </style>
</head>
<body>
    
    <h1>Begriff in einer textpassage suchen</h1>


    <form action="Uebung-zeichenkette.php" method="post">
        



        <p><marquee> wikipedia</marquee></p>
<p>Original Text</p>
<textarea name='$Message'>'Im Februar 2002 entschied sich Bomis, nicht länger einen Chefredakteur zu beschäftigen,
und kündigte den Vertrag mit Larry Sanger, der wenig später seine Mitarbeit bei Nupedia 
und Wikipedia aufgab. Als eine der Ideen, Autoren zu motivieren, hochwertige Artikel zu 
schreiben, wurde am 27. August 2002 die Bewertungsstufe „exzellent“ eingeführt, mit der 
nach einer Abstimmung herausragende Artikel bewertet werden konnten; am 22. März 2005 
folgte die in der Wertigkeit darunterliegende Stufe „lesenswert“. Bis Anfang 2016 wuchs
 deren Zahl in der deutschsprachigen Wikipedia auf über 3800 an, die der „exzellenten“ 
 Artikel auf über 2400.';
                

          </textarea>     

            </p>

        </p>



    
    </form>




<form action="Uebung-zechenkette.php" method="post">suche nach:<input type="text" name="suchbegriff"/><br>
<p></p>
  <input type="submit" value="Zeichenkette suchen" name="Zeichenkette_suchen"/>
</form>
<?php  


$str = '$Message';
echo '<p>';
echo 'suche nach: <b>' . strchr( $str, 'i' , true) . '</b><br>';
echo 'suche nach: <b>' . strrchr( $str, 'i') . '</b><br>';
echo '</p>';
echo "<p>$str</p>";



$str = '$Message:';

$str = str_replace( 'Tante', '<i>nichte</i>', $str );
$str = str_replace( 'Frankreich', '<b>Italian</b>', $str );

echo "<p>$str</p>";





?>

<form action="Uebung-zechenkette.php" method="post">
            zeichenkette suchen:
            <input type=text name="$Message">
            <br>
<?php  
            $str = '$Message';
  
    ?>         
            <textarea name='$Message'>'Im Februar 2002 entschied sich Bomis, nicht länger einen Chefredakteur zu beschäftigen,
            und kündigte den Vertrag mit Larry Sanger, der wenig später seine Mitarbeit bei Nupedia 
            und Wikipedia aufgab. Als eine der Ideen, Autoren zu motivieren, hochwertige Artikel zu 
            schreiben, wurde am 27. August 2002 die Bewertungsstufe „exzellent“ eingeführt, mit der 
            nach einer Abstimmung herausragende Artikel bewertet werden konnten; am 22. März 2005 
            folgte die in der Wertigkeit darunterliegende Stufe „lesenswert“. Bis Anfang 2016 wuchs
             deren Zahl in der deutschsprachigen Wikipedia auf über 3800 an, die der „exzellenten“ 
             Artikel auf über 2400.';
                            
            
                      </textarea>     
            
                        </p>
        
                    </p>
            
            
            
                
               
            





















            
            <br>
            <input type=submit name="$suchbegriff">
            <?php
if(isset($_POST['$suchbegriff']))
{
    $suchbegriff=$_POST['$Message'];
    echo "suche nach:" ,$suchbegriff;
}
            ?>
        </form>









        echo str_replace($_POST['serch'], '<b style="background-color:#ffa500 ;">' .$_POST['serch'].'</b>', $_POST['message']);












</body>
</html>