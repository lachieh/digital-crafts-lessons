function makeItUppercase(string, callback) {
    // start the function
    console.log('Starting uppercase conversion');

    // start a timeoout
    setTimeout(() => {
        // timeout is done
        console.log('Timeout Finished');

        // make the string uppercase
        const newString = string.toUpperCase();

        //call the function that was passed in as 'callback'
        callback(newString);
    }, 5000);
}

function removeSpaces(string, callback) {
    // start the function
    console.log('Starting space removal');

    // remove spaces
    const newString = string.split(' ').join('');

    //call the function that was passed in as 'callback'
    callback(newString);
}

module.exports = {
    makeItUppercase,
    removeSpaces,
}
