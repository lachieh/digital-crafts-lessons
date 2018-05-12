const fs = require('fs');

const print = what => 'HEY: ' + what;

const watcher = fs.watch('./README.md', () => {
    console.log(print('Ouch!'));
})

module.exports = { watcher, print };
