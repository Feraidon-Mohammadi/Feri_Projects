
<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'Hönig bestellung'


);     

get_header(...$args );


?>
<tr>Bitte geben Sie die bestellmenge an (Einheit:500 g-Glas)</tr>

<!-- <table>

<ul>
<tr>
<tr><h4>Bitte geben Sie die bestellmenge an (Einheit:500 g-Glas)</h4></tr>


<tr><td><h1>Hönig</h1></td><td><h1>menge</h1></td></tr>

<tr>
<p><td>Akazienhoenig<input type="Text"name="Akazienhönig"></td></p>
</tr>

<tr>
<p><td>Heidehoenig<input type="Text"name="heidhönig"></td></p>
</tr>

<tr>
<p><td>Kleehoenig<input type="Text"name="kleehönig"></td></p>
</tr>

<tr>
<p><td>Tannenhoenig<input type="Text"name="tannenhönig"></td></p>
</tr>

</tr>

<ul>
</table> -->

<form action="u_bestellung.php" method="post">
<table> <tr>
         <tr><td><h1>Hönig </h1></td><td><h1> menge</h1></td></tr>
        </tr>
</table>
    <p>Akazenhoenig: <input type="text" name="akazienhönig"></p>
    <p>Heidehoenig: <input type="text" name="heidehönig"></p>
    <p>Kleehoenig: <input type="text" name="kleehönig"></p>
    <p>Tannenhoenig: <input type="text" name="tannenhönig"></p>






    <p><input type="submit"value="Abschicken"></p>


    
</form>














