function printTypeInformation(x) {
    console.log(`${x} hat den Datentyp "${typeof x}"`);
}

function printDaysHoursMinutesAndSeconds(totalSeconds) {
    const secondsPerMinute = 60;
    const secondsPerHour = secondsPerMinute ** 2; // 2 ** 3 => 2 * 2 * 2
    const secondsPerDay = secondsPerHour * 24;

    const days = Math.trunc(totalSeconds / secondsPerDay);
    let remainingSeconds = totalSeconds % secondsPerDay;

    const hours = Math.trunc(remainingSeconds / secondsPerHour);
    remainingSeconds %= secondsPerHour;
    // remainingSeconds = remainingSeconds % secondsPerHour

    const minutes = Math.trunc(remainingSeconds / secondsPerMinute);
    const seconds = remainingSeconds % secondsPerMinute;

    console.log(
        `${totalSeconds} Sekunden sind ${days} Tage, ${hours} Stunden, ${minutes} Minuten und ` + `${seconds} Sekunden`
    );
}

printTypeInformation(3);
printTypeInformation("abc" * 3);
printTypeInformation(`${1 + 1}`);
printTypeInformation(null);
printTypeInformation(undefined);
printTypeInformation(false);
printTypeInformation(24 * 60 * 60);

printDaysHoursMinutesAndSeconds(90_450);
printDaysHoursMinutesAndSeconds(90_000);
printDaysHoursMinutesAndSeconds(86_400);
printDaysHoursMinutesAndSeconds(95);
