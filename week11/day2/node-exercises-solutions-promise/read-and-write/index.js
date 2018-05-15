const util = require('util');
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

rl.question('Input file: ', (input) => {
  rl.question('Output file: ', (output) => {
    rl.close();

    readFile(input, 'utf8')
      .then((data) => {
        return writeFile(output, data.toUpperCase())
      })
      .then(() => {
        console.log(`Wrote to file: ${output}`);
      })
      .catch((err) => {
        console.log(err);
        return false;
      });
  });
});
