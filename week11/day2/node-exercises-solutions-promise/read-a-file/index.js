const util = require('util');
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const readFile = util.promisify(fs.readFile);

rl.question('filename: ', (fname) => {
  // All done with readline. Let's close it up.
  rl.close();

  // fs.readFile(fname, (err, data) => {
  readFile(fname, 'utf8')
    .then((data) => {
      console.log(data.toUpperCase());
    })
    .catch((err) => {
      console.log(err.message);
      return false;
    });
})
