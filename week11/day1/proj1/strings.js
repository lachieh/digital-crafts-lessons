class Strings {
    // Reverses a string.
    reverse(toReverse) {
        return toReverse.split('').reverse().join('')
    }

    // Detectes if a string is a pallindrome
    detectPallindrome(toCheck) {
        return toCheck.split('').reverse().join() === toCheck;
    }

    // Shifts every letter forward by one. Z goes
    // to A (wraps around)
    shift(toShift) {
        const alphabet = 'abcdefghijklmnopqrstuvwxyz';
        const letters = [];
        for (let index = 0; index < toShift.length; index++) {
            const letter = toShift[index];
            let newIndex = alphabet.indexOf(letter) + 1;
            if (newIndex >= alphabet.length) {
                newIndex = 0;
            }
            letters.push(alphabet[newIndex]);
        }
        return letters.join('');
    }

    // Checks to see if the target string is a number
    isNumber(toCheck) {

    }
}

module.exports = Strings
