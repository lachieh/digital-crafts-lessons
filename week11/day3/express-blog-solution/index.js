const express = require('express');
const util = require('util');
const fs = require('fs');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

app.get('/', (request, response) => {
    readFile('data.json')
        .then((data) => {
            response.json(JSON.parse(data));
        });
});

app.get('/:id', (request, response) => {
    const id = Number(request.params.id);

    readFile('data.json')
        .then((data) => {
            const blogData = JSON.parse(data)
            if (blogData[id]) {
                response.json(blogData[id]);
            } else {
                response.json({});
            }
        });
});

app.post('/', (request, response) => {
    readFile('data.json')
        .then((data) => {
            return JSON.parse(data);
        })
        .then((data) => {
            const id = Object.keys(data).length + 1;
            while (data[id]) {
                id++;
            }
            const newEntry = {
                id,
                ...request.body
            };
            data[id] = newEntry;

            return writeFile('data.json', JSON.stringify(data, null, '\t'))
                .then(() => {
                    return newEntry;
                });
        })
        .then((newEntry) => {
            response.json(newEntry);
        })
        .catch((err) => {
            response.status(500).send(err);
        });
})

app.listen(3000, () => {
    console.log('listening on port 3000');
});
