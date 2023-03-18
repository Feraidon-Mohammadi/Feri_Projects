<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zeichenkettenfunktionen</title>
</head>
<body>
    
<h1>zeichenkettenfunktionen</h1>

<?php 
$e_mail = 'Brigitte.B@abc.com';
echo "<p>Original-Zeichenkette: <b>$e_mail</b></p>";


/* zeichenkette finden */

echo '<p>';


echo 'suche nach B@ ergibt: <b>' . strstr( $e_mail, 'B@' ) . '</b><br>';
echo 'suche nach B@ ergibt: <b>' . strstr( $e_mail, 'B@', true ) . '</b><br>';

echo 'suche nach b@ ergibt: <b>' . stristr( $e_mail, 'b@'  ) . '</b>';

echo '</p>';


/* Einzelne zeichen finden */

echo '<p>';

echo 'suche nach i ergibt: <b>' . strchr( $e_mail, 'i') . '</b><br>';

echo 'suche nach i ergibt: <b>' . strrchr( $e_mail, 'i') . '</b><br>';

echo '</p>';




/* Neue zeichenketten-Funktionen seit PHP 8 */

echo '<p>';
echo 'Suche nach g ergibt: <b>' . str_contains( $e_mail, 'g') . '</b><br>';
echo 'Suche nach g ergibt: <b>' . str_contains( $e_mail, 'z') . '</b><br>';

echo '</p>';

echo '<p>';

echo 'Suche nach Bri ergibt: <b>' . str_starts_with( $e_mail, 'Bri') . '</b><br>';
echo 'Suche nach Bri ergibt: <b>' . str_ends_with( $e_mail, 'Bri') . '</b><br>';
echo 'Suche nach .com ergibt: <b>' . str_starts_with( $e_mail, 'com') . '</b><br>';
echo 'Suche nach .com ergibt: <b>' . str_ends_with( $e_mail, 'com') . '</b><br>';

echo '</p>';

/* einzeln Zeichen finden, position zurückliefren */
/* ep+ will be add start ende paragraph */

echo '<p>';
echo 'Suche nach i ergibt: <b>' . strpos( $e_mail, 'i') . '</b><br>';
echo 'Suche nach i ergibt: <b>' . strrpos( $e_mail, 'i') . '</b><br>';
echo 'Suche nach b ergibt: <b>' . stripos( $e_mail, 'b') . '</b><br>';
echo 'Suche nach b ergibt: <b>' . strpos( $e_mail, 'b') . '</b><br>';

/* beginen der suche angeben ein buchtstabe finden in nächste gleiche buchtstabe */
echo 'Suche nach i ergibt: <b>' . strpos( $e_mail, 'i' , 3) . '</b><br>';

echo '</p>';

/* Teilestrings extragieren*/
$e_mail = 'meister.nadeloerhr@wie-ist-meine-ip.de';
echo "<p>Die neue Original-Zeichenkette: <b>$e_mail</b></p>";

echo '<p>';

 echo 'Domainnamen extrahieren: <b>' . substr( $e_mail, 18 ) . '</b><br>';
 echo 'Domainnamen extrahieren: <b>' . substr( $e_mail, -19 ) . '</b><br>';

echo '</p>';


$adressen = array(
    'Brigitte.B@abc.de',
    'meister.nadeloehr@wie-ist-meine-ip.de',
    'ben.a@gmx.de'

);

echo '<p>';

foreach( $adressen as $adresse ) {
    $pos = strpos( $adresse, '@' );
    echo 'Domainname: <b>' . substr( $adresse, $pos + 1 ) . '</b><br>';

}

echo '</p>';

/*  Anzahl der gefundenen Suchzeichen Treffer */

echo '<p>Gefudene Traffer für <i>ei</i> in <b>' . $e_mail . '</b> genau <b>' .
substr_count( $e_mail, 'ei') . '-mal</b> vor.</p>';


/*  Suchen und Ersetzen Z:B ersetze uh statt ak  */
$str = 'Buch buchen';
echo '<p>' . strtr( $str, 'uh', 'ak' ) . '</p>';

/* oder dieser */
$str = 'Buch buchen';

$tausch = array( 'u' => 'au', 'ch' => 'sch');

echo '<p>' . strtr( $str, $tausch ) . '</p>';


/* oder */
$str = 'Main Tante lebt in Frankreich. Meine Tante ist noch nicht so alt:';

$str = str_replace( 'Tante', '<i>nichte</i>', $str );
$str = str_replace( 'Frankreich', '<b>Italian</b>', $str );

echo "<p>$str</p>";


/* Anzahl der bytes einer Zeichenkette */
$str1 = 'Hauser';
$str2 = 'Häuser';

echo '<p>Die zeichenkette <i>' . $str1 . '</i>besteht aus <b>' . strlen( $str1 ) .'</b> Bytes.</p>';

echo '<p>Die zeichenkette <i>' . $str2 . '</i>besteht aus <b>' . strlen( $str2 ) .'</b> Bytes.</p>';



/* seit php 7 neue multible -funktionen */
echo '<p>Die zeichenkette <i>' . $str1 . '</i>besteht aus <b>' . mb_strlen( $str1 ) .'</b> Bytes.</p>';

echo '<p>Die zeichenkette <i>' . $str1 . '</i>besteht aus <b>' . mb_strlen( $str2 ) .'</b> Bytes.</p>';









?>














</body>
</html>