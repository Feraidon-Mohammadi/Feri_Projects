<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
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

<?php  

$str = '$Message';
echo '<p>';
echo 'suche nach: <b>' . strchr( $str, 'i' , true) . '</b><br>';
echo 'suche nach: <b>' . strrchr( $str, 'i') . '</b><br>';
echo '</p>';
echo "<p>$str</p>";

?>

















</body>
</html>