const express = require('express');
const app = express();
const port = 5000;
const cors = require('cors');

const arr=[]
const server = {};
app.use(cors());

app.post('/hoho', (req, res) => {
    req.on('data', (data) => {
        const payload = Buffer.from(data).toString();
        const payloadObject = JSON.parse(payload);
        arr.push(payloadObject.value)
        console.log(arr)
        res.writeHead(200, {
            'Content-Type': 'application/json'
          });
          res.end(JSON.stringify(arr))
    })
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))