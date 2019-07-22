import machine
from time import sleep
import urandom
import urequests
import network
import esp32

led = machine.Pin(2, machine.Pin.OUT)
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 4, 5, 12, 13, 14, 15)]

import gc
gc.collect()

def do_connect():
    wlan_ap = network.WLAN(network.AP_IF)
    wlan_ap.active(True)
    print('AP config:', wlan_ap.ifconfig())


    

    


    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        # led_connect()
        print('connecting to network...')
        wlan.connect('RADWAG', 'rdg37gh213vbk')
        while not wlan.isconnected():
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
    led.off()
    print('network config:', wlan.ifconfig())

    # try:
    #     import usocket as socket
    # except:
    #     import socket

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('', 80))
    # s.listen(5)

    # while True:
    #     conn, addr = s.accept()
    #     print('Got a connection from %s' % str(addr))
    #     request = conn.recv(1024)
    #     request = str(request)
    #     print('Content = %s' % request)
    #     led_on = request.find('/?led=on')
    #     led_off = request.find('/?led=off')
    #     if led_on == 6:
    #         print(led_on)
    #         led.value(1)
    #     if led_off == 6:
    #         print(led_off)
    #         led.value(0)
    #     response = web_page()
    #     conn.send('HTTP/1.1 200 OK\n')
    #     conn.send('Content-Type: text/html\n')
    #     conn.send('Connection: close\n\n')
    #     conn.sendall(response)
    #     conn.close()
    # # while True:
    # # led.on()
    # # rand = urandom.getrandbits(10)
    


def web_page():
    if led.value() == 1:
        gpio_state="ON"
    else:
        gpio_state="OFF"

    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
    <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    
    return html



# web_page()
do_connect()



html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        <h1>END</h1>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    req = cl.recv(1024)
    test = 'ooooooooooooooo'
    print("Request:")
    print(str(req))
    print('client connected from', addr)
    print(str(req).find('/?kotlet'))
    if str(req).find('/?kotlet') == 6:
        try:
            response = urequests.post("http://104.248.23.119:3000/hoho", json={"value": 'fddfdf'})
            print(response.json())
            test = str(response.json())
            led.off()
            sleep(3)
        except:
            print("Error: bad response")
            led.off()
            sleep(2)


    # cl_file = cl.makefile('rwb', 0)
    # while True:
    #     line = cl_file.readline()
    #     if not line or line == b'\r\n':
    #         break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    # cl.send(response)
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(test)
    cl.close()
