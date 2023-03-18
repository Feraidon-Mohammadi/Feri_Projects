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