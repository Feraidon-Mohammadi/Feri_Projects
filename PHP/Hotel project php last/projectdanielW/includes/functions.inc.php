<?php
/* 
 pw  !l.rr6N/wZaK9tE]    

 * Schreibt einen HTML-Header und den Kopf-Bereich der Seite.
 * 
 * @param $title string required Titel der Website (im head-Bereich)
 * @param $css string|array optional 
 *      Pfad zu CSS-Datei(en)
 *      default NULL
 * @param $bootstrap bool optional
 *      Bootstrap nutzen oder nicht.
 *      default false
 * @param $header string optional
 *      Ausgabe der Hauptüberschrift im sichtbaren Bereich
 *      default NULL
 * @param $nav array optional
 *      Wird eine Navigation benötigt, wenn ja: welche Nav-Punkte
 *      default NULL
 * @param $fluid bool optional
 *      Regelt, ob eine Bootstrap-Klasse 'container' oder 'container-fluid' benutzt werden soll
 *      default false
 * 
 * @return string HTML-Header und Seiten-Kopfbereich
 */

function get_header(
    string $title,
    string|array $css = NULL,
    bool $bootstrap = false,
    string $header = NULL,
    array $nav = NULL,
    bool $fluid = false
){
    $class_fluid = (false === $fluid)? 'container' :'container-fluid';
?>
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><<?php echo htmlspecialchars($title); ?> </title>
    <!-- CSS only -->
    <!-- Bootstrap-CSS -->
    <?php  if($bootstrap){
  echo'  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'."\r\n";}
  if (is_array($css))   
    {
    foreach($css as $css_link)
      { 
            echo "\t". '<link rel="stylesheet" href="'.  $css_link . '">'. "\r\n";
      }
    }
    elseif ( is_null($css)){
        echo "\t". '<link rel="stylesheet" href="'.  $css . '">'. "\r\n";
    }
  
?>  </head>

<body>
    <?php if(!is_null($nav)) get_nav($nav, $fluid) ;?>

<header class="bg-light bg-gradiant boarder-bottom">
<div class="<?php echo $class_fluid; ?>">
    <h1 class="display-3"> <?php echo is_null($header)? $title:$header; ?></h1>
</div>
</header>
<main class = "<?php echo $class_fluid;?> py-3">





<?php 
}




/* 
 * 
 * Schreibt die Navigationsleiste der HTML-Seite (basierend auf Boostrap 5, nur eine Ebene).
 * 
 * @param $nav array required
 *      $nav[0] = Branding
 *      $nav[1] = array() mit den Menüpunkten (eine Ebene!)
 * @param $fluid bool optional
 *      Regelt, ob eine Bootstrap-Klasse 'container' oder 'container-fluid' benutzt werden soll
 *      default false
 * 
 * @return string Navigationsleiste für die Website
 * 
 * */

function get_nav( array $nav, bool $fluid = false ) {
    $class_fluid = (false === $fluid)? 'container' :'container-fluid';

 ?>
    <nav class="navbar navbar-expand-lg navbar-dark bg-secondary bg-gradient">
    <div class="<?php echo $class_fluid; ?>">
        <a class="navbar-brand" href="index.php"><?php echo $nav[0]; ?></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

        <?php  foreach($nav[1] as $item => $url): ?>
     <?php
        $class_activ ='';
        $current = '';
        if(basename($_SERVER['PHP_SELF']) === $url )
        {
            $class_activ = 'active';
            $current = 'aria-current="page"';
        }       
     ?>
        <li class="nav-item">
            <a href= "<?php echo $url;?>" class="nav-link <?php echo $class_activ?>" <?php echo $current ?>><?php echo $item ?></a>
        </li>
            <?php endforeach; ?>
        </ul>
        </div>
    </div>
    </nav>

<?php    
}



/* 
 * Schreibt einen Fußbereich einer HTML-Seite.
 * 
 * @param $fluid bool optional
 *      Regelt ob eine Bootstrap-Klasse 'container' bzw. 'container-fluid' benutzt werden soll
 *      default false
 * @param $bootstrap_js bool optional
 *      Regelt ob Bootstrap-JS-Dateien eingebunden werden müssen.
 *      default false
 * 
 * @return string Footer-Angaben für die HTML-Seite.
 */

function get_footer( bool $fluid = false, bool $bootstrap_js = false ) {
   
    $class_fluid =(false===$fluid) ? 'container': 'container-fluid';
?>


</main>
<footer class="bg-dark bg-gradiant text-white py-5">
    <div class= "<?php echo  $class_fluid; ?>">
        <p>&copy; <?php echo date('Y') .'seinen-namen-oder-was-weiss-ich'; ?></p>
    </div>
</footer>
<?php if ($bootstrap_js): ?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <?php endif; ?>
</body>
</html>
<?php  
}



/**
 * get_db_error( $db, $sql )
 *
 * Gibt eine formatierte Fehlermeldung zu MySQL-Abfragen aus
 *
 * @param object-mysqli $db Server-Kennung
 * @param string $sql zugehörige SQL-Anweisung
 * 
 * @return string Die formatierte Meldung.
 */
function get_db_error( object $db, string $sql ):string {
    $errnum = mysqli_errno( $db );
    $search = array( ';', 'manual', 'near' );
    $replace = array( ';<br>', '<a href="https://mariadb.com/kb/en/mariadb-error-codes/" target="_blank">manual</a>', 'near<br>' );
    $errmsg = str_replace( $search, $replace, mysqli_error( $db ) );
    $errdisplay  = '<div class="alert alert-danger">';
    $errdisplay .= '<h4 class="alert-heading">SQL-Fehler!</h4>';
    $errdisplay .= "<p><b>Fehler-Code:</b> <code>$errnum</code></p>";
    $errdisplay .= '<hr>';
    $errdisplay .= '<p><b>Der SQL-Server meldet:</b><br>';
    $errdisplay .= "<code>$errmsg</code></p>";
    $errdisplay .= '<hr>';
    $errdisplay .= '<p><b>Die fehlerhafte SQL-Anweisung:</b><br>';
    $errdisplay .= '<code>' . highlightText($sql) . '</code></p>';
    $errdisplay .= '</div>';
    return $errdisplay;
}

/**
 * highlightText($text)
 *
 * Formatiert Code-Ausschnitte
 *
 * @autor Stanislav Eckert stanislav.eckert@viszon.de
 * @url https://www.php.net/manual/de/function.highlight-string.php#118550
 *
 * @param string $text der zu formatierende Code
 * 
 * @return string der formatierte Code.
 */
function highlightText(string $text):string {
    $text = trim($text);
    $text = highlight_string("<?php " . $text, true);  // highlight_string() requires opening PHP tag or otherwise it will not colorize the text
    $text = trim($text);
    $text = preg_replace("|^\\<code\\>\\<span style\\=\"color\\: #[a-fA-F0-9]{0,6}\"\\>|", "", $text, 1);  // remove prefix
    $text = preg_replace("|\\</code\\>\$|", "", $text, 1);  // remove suffix 1
    $text = trim($text);  // remove line breaks
    $text = preg_replace("|\\</span\\>\$|", "", $text, 1);  // remove suffix 2
    $text = trim($text);  // remove line breaks
    $text = preg_replace("|^(\\<span style\\=\"color\\: #[a-fA-F0-9]{0,6}\"\\>)(&lt;\\?php&nbsp;)(.*?)(\\</span\\>)|", "\$1\$3\$4", $text);  // remove custom added "<?php "
    return $text;
}


/**
 * exceptionHandler( $exception )
 *
 * Gibt anstelle der Standard-Ausnahmebehandlung eine formatierte Meldung aus
 *
 * @param Throwable $exception    required abgefangene Ausnahme
 * 
 * @return void
 */
function exceptionHandler(Throwable $exception): void {
    if (ini_get('display_errors')) {
        $errdisplay  = '<div class="alert alert-danger">';
        $errdisplay  .= '<h4 class="alert-heading">SQL-Fehler!</h4>';
        $errdisplay .= '<p><b>Fehler-Code:</b> <code>' . $exception->getCode() . '</code></p>';
        $errdisplay .= '<hr>';
        $errdisplay .= '<p><b>Der SQL-Server meldet:</b><br>';
        $errdisplay .= '<code>' . $exception->getMessage() . '<br>';
        $errdisplay .= 'in ' . $exception->getFile() . ', Zeile ' . $exception->getLine() . '</code><br>';
        $errdisplay .= '<h6 class="alert-heading">Trace:</h6><pre>' . $exception->getTraceAsString() . '</pre></p>';
    } else {
        $errdisplay = '<p>Es ist ein Fehler aufgetreten.</p>';
    }
    $errdisplay .= '</div>';
    echo $errdisplay;
}
/**
 * errorHandler(int $errno, string $errstr, string $errfile = null, int $errline = null)
 *
 * Wandelt die Standard-Fehlermeldung in eine Ausnahme um und wirft eine neue Ausnahme
 * die von der Funktion exceptionHandler übernommen und ausgegeben wird
 *
 * @param int       $errno      required Fehlernummer
 * @param string    $errstr     required Fehlermeldung
 * @param string    $errfile    optional Datei mit Fehler, default null
 * @param int       $errline    optional Zeile in welcher der Fehler festgestellt wurde, default null
 * 
 * @return bool     korrekte Ausführung
 */
function errorHandler(int $errno, string $errstr, string $errfile = null, int $errline = null): bool
{
    $message = $errstr;
    if ($errfile !== null) {
        $message .= " in Datei $errfile";
    }
    if ($errline !== null) {
        $message .= ":$errline";
    }
    $message .= " [Error #$errno]";
    // Umwandlung eines PHP-Fehlers in eine Ausnahme, führt zum Aufruf der Funktion exceptionHandler()
    // und damit einer einheitlichen Behanndlung von PHP-Fehlern und Ausnahmen
    throw new Exception($message);
}

/**
 * is_logged_in()
 * checkt via SESSIN array ob user eingeloggt ist 
 * gibt bool zurück 
 */
function is_logged_in():bool
{
    return isset($_SESSION['user']);
}
/**
 * Format_dateTime(string $dateTime )
 * liefert ein Formatiertes datum + Uhrzeit (deutsches Format)
 * 
 * 
 */
function Format_dateTime(string $dateTime ): string
{
    return(new DateTime($dateTime))->format(' d.m.Y H:i ');
}
/**
 * Format_date(string $dateTime )
 * liefert ein Formatiertes datum(deutsches Format)
 * 
 * 
 */
function Format_date(string $dateTime ): string
{
    return(new DateTime($dateTime))->format('d.m.Y');
}

?>