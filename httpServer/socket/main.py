import network
import esp32
import machine
from time import sleep
import uhashlib
import ubinascii



import gc
gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
led = machine.Pin(2, machine.Pin.OUT)

wlan.connect('RADWAG', 'rdg37gh213vbk')
while not wlan.isconnected():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
print('Conected ', wlan.ifconfig())
led.off()

import socket
addr = socket.getaddrinfo('0.0.0.0', 7000)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(10)
print('listening on', addr)

while True:
    import test
    cl, addr = s.accept()
    req = cl.recv(1024)
    reqToObj = test.requestParse(req)
    magicString = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    test = uhashlib.sha1(reqToObj['Sec-WebSocket-Key']+magicString)
    # print('test xxxxxx', uhashlib.sha1("dGhlIHNhbXBsZSBub25jZQ==258EAFA5-E914-47DA-95CA-C5AB0DC85B11").digest())
    accept = test.digest()
    # print('SHA1AAAAAAAAAAAAAAAAAAAAAAAA',accept)
    # print('SHA1AAAAAAAAAAAAAAAAAAAAAAAA',accept)
    a1 = ubinascii.b2a_base64(accept)
    b1 = a1.decode()
    # print('xxxxxxxxxxxxxxx', a1.decode())
    # print(reqToObj)
    print('client connected from', addr)
    cl.send('HTTP/1.1 101 Switching Protocols\n')
    cl.send('Upgrade: websocket\n')
    cl.send('Connection: Upgrade\n')
    cl.send('Sec-WebSocket-Accept: '+ b1 + '\n\n')
    # www = cl.read()
    while True:
        www = cl.recv(4096)
        print('ddddddddddd ',ubinascii.hexlify(www))
        # cl.write(www)
            
    # cl.close()