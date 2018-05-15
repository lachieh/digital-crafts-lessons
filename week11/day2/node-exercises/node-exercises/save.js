const fs = require('fs');
const readline = require('readline');
const http = require('http');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('What is the URL: ', (url) => {
    rl.question('What is the output:', (outputFilename) => {
        rl.close();

        http.get(url, (response) => {
            let outputData = '';
            response.on('data', (data) => {
                outputData += data;
            })
            response.on('end', () => {
                fs.writeFile(outputFilename, outputData, (outputErr) => {
                    if (outputErr) { return console.log(outputErr)}
                    return console.log('Saving ' + url + ' was successful');
                })
            })
        })
    })
});
