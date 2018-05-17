const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.get('/', (req, res) => {
    res.send('hey!');
})

app.get('/contacts', (request, response) => {
    fs.readFile('contacts.json', (err, data) => {
        if (err) { return console.log(err) }
        response.send(JSON.parse(data));
    })
})

app.get('/contact/:id', (request, response) => {
    fs.readFile('contacts.json', (err, data) => {
        if (err) { return console.log(err) }

        // set id to the number that was passed from the URL
        const id = Number(request.params.id);

        //filter the JSON data from our file into the result variable
        const result = JSON.parse(data).filter((entry) => {
            // if the entry.id matches what came from the URL, let it through
            // if it doesn't, then filter it out
            return entry.id === id
        });
        response.send(result);
    })
})

app.post('/new', (request, response) => {
    fs.readFile('contacts.json', (err, data) => {
        if (err) { return console.log(err) }
        if (
            !request.body.first_name ||
            !request.body.last_name ||
            !request.body.email
        ) {
            response.send('Error: missing fields');
        }
        let contacts = JSON.parse(data);
        let newId = contacts.length + 1;
        let newContact = {
            id: newId,
            first_name: request.body.first_name,
            last_name: request.body.last_name,
            email: request.body.email,
        };
        contacts.push(newContact);
        fs.writeFile('contacts.json', JSON.stringify(contacts, null, ' '), () => {
            response.send(newContact);
        });
    });
})

app.listen(3000, () => {
    console.log('listening on port 3000');
})
