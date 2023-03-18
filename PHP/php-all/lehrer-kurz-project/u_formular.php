<?php
session_start();
require_once '../../includes/functions.inc.php';
$args = array(
    'Bestellformular',
    NULL,
    true,
    'Übung: Honigbestellung'
);
get_header(...$args);
?>

<p class="lead">Bitte geben Sie die Bestellmenge an (Einheit: 500-g-Glas)</p>

<form action="u_bestellung.php" method="post">
    
    <table class="table">
        <tr class="table-warning">
            <th>Honig</th>
            <th>Menge</th>
        </tr>

        <tr>
            <td>Akazienhonig</td>
            <td>
                <input class="form-control" type="number" name="Akazienhonig">
            </td>
        </tr>

        <tr>
            <td>Heidehonig</td>
            <td>
                <input class="form-control" type="number" name="Heidehonig">
            </td>
        </tr>

        <tr>
            <td>Kleehonig</td>
            <td>
                <input class="form-control" type="number" name="Kleehonig">
            </td>
        </tr>

        <tr>
            <td>Tannenhonig</td>
            <td>
                <input class="form-control" type="number" name="Tannenhonig">
            </td>
        </tr>

        <tr>
            <td colspan="2">
                <input type="submit" value="Abschicken" class="btn btn-primary">
            </td>
        </tr>
    </table>

</form>

<?php get_footer(true,false); ?>