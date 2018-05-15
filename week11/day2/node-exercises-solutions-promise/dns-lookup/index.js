const util = require('util');
const readline = require('readline');
const dns = require('dns');

// Create the interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// make resolve into a promise
const dnsResolve = util.promisify(dns.resolve);

// Prompt, then wait for user to type a domain name
rl.question('Domain name: ', (domain) => {
  rl.close();

  // Do the DNS resolve
  dnsResolve(domain)
    .then((address) => {
      console.log(`IP address: ${address}`);
      return true;
    })
    .catch((err) => {
      // if there is an error, then log it and fail
      if (err) { console.log(err.message); return false; }
      // otherwise, log it to the console
    })
});
