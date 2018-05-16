const readline = require('readline');
const dns = require('dns');
const util = require('util');

// Create the interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lookup = util.promisify(dns.lookup);

// Prompt, then wait for user to type a domain name
rl.question('Domain name: ', (domain) => {
  rl.close();

  lookup(domain)
    .then((address) => {
      console.log(`IP address: ${address}`);
    })
    .catch((err) => {
      return console.log(err)
    })
});
