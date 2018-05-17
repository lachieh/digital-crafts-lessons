const express = require('express');
const app = express();
const http = require('http').Server(app);

// io is socket.io instance
var io = require('socket.io')(http)

// setting up the static resources
app.use(express.static('public'))

// adding the connection listener
io.on('connection', function(socket) {
  console.log('a user has connected')

  socket.on('digitalcrafts2018', function(message){
    console.log(message)
    io.emit('digitalcrafts2018',message)
  })

  /*
  socket.on('chat message', function(msg){
    console.log(msg)
    io.emit('chat message',msg)
  }) */
})

http.listen(3000, function(){
  console.log('listening on port 3000');
})
