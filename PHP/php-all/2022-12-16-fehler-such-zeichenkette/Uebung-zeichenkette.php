<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Begriff in einer textpassage suchen</title>
    <style>
        
    



    </style>
</head>
<body>
    
    <h1>Begriff in einer textpassage suchen</h1>


    <form action="Uebung-zeichenkette.php" method="post">
       
    <p><marquee bgcolor=#ddbbee;> wikipedia</marquee></p>

<table>
<tr>

        
<p>Original Text
    <textarea name='$Message' cols="75" rows="8">
    'Im Februar 2002 entschied sich Bomis, nicht länger einen Chefredakteur zu beschäftigen,
    und kündigte den Vertrag mit Larry Sanger, der wenig später seine Mitarbeit bei Nupedia 
    und Wikipedia aufgab. Als eine der Ideen, Autoren zu motivieren, hochwertige Artikel zu 
    schreiben, wurde am 27. August 2002 die Bewertungsstufe „exzellent“ eingeführt, mit der 
    nach einer Abstimmung herausragende Artikel bewertet werden konnten; am 22. März 2005 
    folgte die in der Wertigkeit darunterliegende Stufe „lesenswert“. Bis Anfang 2016 wuchs
    deren Zahl in der deutschsprachigen Wikipedia auf über 3800 an, die der „exzellenten“ 
    Artikel auf über 2400.'; </textarea> </p>    
</tr>

   <tr>
        <td>suche nach</td>

        <td><input type="text" name="suchtext"></td>

   </tr>
</table>





    <input type="text" value="zeichenkette suchen">
    




</form>
    <?php 
            
$Anzahl= '';
           
            if(isset(($_POST['suchtext'])) && $_POST['suchtext'] != ''){
                $anzahl = substr_count( $_POST['eingabe'], $_POST['suchtext'] );
                echo '<p>suche nach <b><fort style="color: red;">' . $_POST['suchtect']. '"</font></b>: <b><font style="color:blue</b>"';

               
        
        
        
 /*    echo str_replace(['suchtext'], '<font style="background-color:orange">' . $_POST['suchtext'] . '</font></b>"': );
                    echo '<br>';
                } else {
        
          echo '<p> ffffff ffffffffffff</p>'; */
        }

?> 


    
</body>
</html>