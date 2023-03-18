console.log(Math.trunc(3.14), Math.trunc(-12.755));

function distanceBetween(a, b) {
    // -3, 4 => -3 - 4 = -7
    // 4, -3 => 4 - -3 = 7
    return Math.abs(a - b);
}

function calculateHypothenuse(a, b) {
    return Math.sqrt(a ** 2 + Math.pow(b, 2));
}

function degreesToRadians(degrees) {
    return (degrees / 180) * Math.PI;
}

function radiansToDegree(radians) {
    return (radians / Math.PI) * 180;
}

function randomBetween(min, max) {
    // min=-2, max=3 => -2, -1, 0, 1, 2, 3
    //                   0   1  2  3  4  5
    const diff = max - min + 1;
    return Math.floor(Math.random() * diff + min);
}
