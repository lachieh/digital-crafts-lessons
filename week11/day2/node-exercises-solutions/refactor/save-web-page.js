const request = require('request');
const fs = require('fs');

function saveWebPage(url, filename, callback) {
  request.get(url, (err, response, html) => {
    if (err) {
      console.log(err.message);
      return;
    }
    fs.writeFile(filename, html, (err) => {
      if (err) {
        console.log(err.message);
        return;
      }
      console.log('It worked');
      callback();
    });
  });
}

module.exports = { saveWebPage }
