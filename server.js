const express = require('express');
const app = express();
const port = 3000;
const cors = require('cors');

const arr=[]
let led = {};

app.use(cors());


app.post('/hoho', (req, res) => {
    req.on('data', (data) => {
        const payload = Buffer.from(data).toString();
        const payloadObject = JSON.parse(payload);
        // arr.push(payloadObject.value)
        if (led.value === undefined) {
            led.value = payloadObject.value
            console.log(led)
        } 
        console.log(led)
        // led = payload
        res.writeHead(200, {
            'Content-Type': 'application/json'
          });
          res.end(JSON.stringify(led))
    })
})

app.get('/switch', (req, res) => {
    
    led.value = !led.value
    console.log('ledyyyyyyyyyy ',led.value)

    res.writeHead(200, {
        'Content-Type': 'application/json'
      });
      res.end(JSON.stringify(led))
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))