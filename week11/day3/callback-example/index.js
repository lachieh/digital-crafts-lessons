const utils = require('./utils');
const string = 'make this string do some stuff';
let string1 = '';
let string2 = '';

utils.makeItUppercase(string, (uppercaseString) => {
    console.log(uppercaseString);
    string1 = uppercaseString;

    console.log(string1)

    utils.removeSpaces(string1, (noSpacesString) => {
        console.log(noSpacesString);
        string2 = noSpacesString;

        console.log(string2);
    });
});

makeItUppercase(string)
    .then((uppercaseString) => {
        console.log(uppercaseString);
        string1 = uppercaseString;

        console.log(string1)
        return removeSpaces(string1)
            .then((noSpacesString) => {
                console.log(noSpacesString);
                string2 = noSpacesString;
                console.log(string2);
            });
    })
    .then(() => {
        console.log('promise finished');
    });
