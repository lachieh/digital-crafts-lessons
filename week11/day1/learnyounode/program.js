var fs = require('fs');
var contents = fs.readdir(process.argv[2], (err, data) => {
    if (process.argv[3]) {
        var ext = process.argv[3];
        data.forEach((item, key) => {
            if (item.substr(-ext.length - 1) == '.'+ext) {
                console.log(item)
            }
        })
    } else {
        data.forEach((item) => {
            console.log(item);
        })
    }
});
