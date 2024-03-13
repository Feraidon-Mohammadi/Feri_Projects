 <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $user_vor_name = $_POST['user_vor_name'];
        $user_nach_name = $_POST['user_nach_name'];
        echo "Hello User, bitte Eingabe ausfüllen,<br>Vorname: $user_vor_name,<br>Nachname: $user_nach_name";
    } else {
        echo "Form not submitted.";
    }
    ?>