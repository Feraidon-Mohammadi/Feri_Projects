<?php 

session_start();
require_once('../includes/functions.inc.php');
$args = array(

    'sessions',
    Null,
    false,
    'sessions-Formular'


);

get_header(...$args );


?>

<h2>Formular</h2>
<form action="03-auswertung.php" method="post">
    <p>Vorname: <input type="text" name="vorname"></p>
    <p>Nachname: <input type="text" name="nachname"></p>
    <p>Wohnort: <input type="text" name="ort"></p>

    <p><input type="submit"value="senden"></p>





    
</form>

<?php get_footer(); ?>