import request from 'request';
import fs from 'fs';

export default function saveWebPage(url, filename, cb) {
  request.get(url, (err, response, html) => {
    if (err) {
      console.log(err.message);
      return;
    }
    fs.writeFile(filename, html, cb);
  });
}
