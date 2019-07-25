import machine
from time import sleep
import urandom
import urequests
import network
import esp32
import ubinascii
from machine import Timer


led = machine.Pin(2, machine.Pin.OUT)
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 4, 5, 12, 13, 14, 15)]
nets = []
import gc
gc.collect()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def do_connect():
    wlan_ap = network.WLAN(network.AP_IF)
    wlan_ap.active(True)
    wlan_ap.config(essid='ESP32 - PK')
    print('AP config:', wlan_ap.ifconfig())
    # print(wlan_ap.ifconfig()[0])


    

    



    # if not wlan.isconnected():
    #     # led_connect()
    #     print('connecting to network...')
    #     wlan.connect('RADWAG', 'rdg37gh213vbk')
    #     while not wlan.isconnected():
    #         led.on()
    #         sleep(0.5)
    #         led.off()
    #         sleep(0.5)
    # led.off()
    # print('network configGGGGGGGGGGGGGGGGGGGGGGG:', wlan.status('rssi'))
    net = wlan.scan()
    print(net)
    
    for i in net:
        # print(i[0].decode())
        obj = {}
        obj['name'] = i[0].decode()
        obj['mac'] = ubinascii.hexlify(i[1]).decode()
        obj['rssi'] = str(i[3])
        obj['channel'] = str(i[2])
        obj['auth'] = i[4]
        nets.append(obj)
        # print(ubinascii.hexlify(i[1]))
    # print('Networks: ', ubinascii.hexlify(net[0][1]))

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
        <form action="/test" method="POST">
            First name:<br>
            <input type="text" name="firstname">
            <br>
            
            <input type="submit" value="Submit">
        </form>
        <h1>END</h1>
    </body>
</html>
"""

html1 = """<!DOCTYPE html>
<html>
    
    <head>
    <link rel="stylesheet" href="app.css">
    <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <form action="/test" method="POST">
            First name:<br>
            <input type="text" name="firstname">
            <br>
            <input type="submit" value="Submit">
        </form>
        <table><tr><th>Value</th></tr> %s </table>
        <h1>END</h1>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(10)
print('listening on', addr)

while True:
    import test 
    cl, addr = s.accept()
    req = cl.recv(1024)
    x = test.requestParse(req)
    # test1 = 'ooooooooooooooo'
    print("Request:")
    # print(x)
    # lines = x.splitlines()
    # print(lines[len(lines) - 1])
    # for line in lines:
    #     print(line)
    url = ''
    method = x['method'].split(' ')
    if len(method) > 1:
        url = method[1][1:]
    mimetype = 'text.plain'
    data = ''
    try:
        file = open(url)
        data = file.read()
        file.close()
    except:
        print('could not open')

    if '.' in url: 
        mimetype = {
            '.html' : 'text/html',
            '.ico' : 'image/x-icon',
            '.jpg' : 'image/jpeg',
            '.png' : 'image/png',
            '.gif' : 'image/gif',
            '.css' : 'text/css',
            '.js' : 'text/javascript'
        }[url[url.find('.'):]]

    # print(mimetype)
    # print(data)
    # xx = file.read()


    # print(xx)
    # print()

    print('client connected from', addr)
    # print(str(req).find('/?kotlet'))
    # if x['method'].find('/test') and 'firstname' in x['body'].keys():


    # Timer runs a function every set period #################################################

    # tim = Timer(0)
    # def xmann(tim):
    #     try:
    #         response = urequests.post("http://104.248.23.119:3000/hoho", json={"value": led.value()})
    #         print(response.json())
    #         test = response.json()
            
    #         led.value(test['value'])
    #         # sleep(1)
    #     except:
    #         print("Error: bad response")
    #         # led.off()
    #         sleep(2)

    # tim.init(period=1000, mode=Timer.PERIODIC, callback=xmann)

    #########################################################################

    # cl_file = cl.makefile('rwb', 0)
    # while True:
    #     line = cl_file.readline()
    #     if not line or line == b'\r\n':
    #         break
    # for i in nets:
    #     print(i)
        # print(ubinascii.hexlify(i[1]))
    
    rows = ['<tr><td>%s</td></tr>'  % p for p in nets]
    response = html1 % '\n'.join(rows)
    # cl.send(response)
    # if wlan_ap.ifconfig()[0] 
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: ' + mimetype +'\n')
    cl.send('Connection: close\n\n')
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:', url.find('onoffled'))
    tim = Timer(0)
    if url=='onled':
        # print('ledddddddd', led.value)
        # led.value( not led.value())
        # led_value = ''
        # if led.value() == 0:
        #     led_value = 'OFF'
        # else:
        #     led_value = 'ON'
        # cl.sendall('<h1> LED IS ' + led_value + '</h1>')
        def xmann(tim):
            try:
                response = urequests.post("http://104.248.23.119:3000/hoho", json={"value": led.value()})
                print(response.json())
                test = response.json()
                
                led.value(test['value'])
                # sleep(1)
            except:
                print("Error: bad response")
                # led.off()
                sleep(2)

        tim.init(period=200, mode=Timer.PERIODIC, callback=xmann)
    elif url=='offled':
        tim.deinit()
    elif url=='login':
        count = 0
        if not wlan.isconnected():
            # led_connect()
            print('connecting to network...')
            wlan.connect(x['body']['wifi'], x['body']['pass'])
            while not wlan.isconnected():
                # print('STAT_WRONG_PASSWORD ', network.STAT_WRONG_PASSWORD )
                # print('STAT_CONNECTING ', network.STAT_CONNECTING )
                # print('STAT_IDLE ', network.STAT_IDLE )
                # print('STAT_NO_AP_FOUND ', network.STAT_NO_AP_FOUND )
                # # print('STAT_CONNECT_FAIL ', network.STAT_CONNECT_FAIL )
                # print('STAT_GOT_IP ', network.STAT_GOT_IP )
                print('xxxxxxxxxxxxxxx ', wlan.status())
                led.on()
                sleep(0.5)
                led.off()
                sleep(0.5)
                if wlan.status() != 1010:
                    count = count + 1
                    print('count ', count)
                if count > 10:
                    wlan.disconnect()
                    cl.sendall('Can not connect with ' + x['body']['wifi'])
                    break
                    
            # except:
            #     print('Cannot connect with ' + x['body']['wifi'])
            #     cl.sendall('Cannot connect with ' + x['body']['wifi'])
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # print('STAT_WRONG_PASSWORD ', network.STAT_WRONG_PASSWORD )
        # print('STAT_CONNECTING ', network.STAT_CONNECTING )
        # print('STAT_IDLE ', network.STAT_IDLE )
        # print('STAT_NO_AP_FOUND ', network.STAT_NO_AP_FOUND )
        # # print('STAT_CONNECT_FAIL ', network.STAT_CONNECT_FAIL )
        # print('STAT_GOT_IP ', network.STAT_GOT_IP )
        led.off()
        cl.sendall('<h1>Connect with ' + x['body']['wifi'] + ' ' + str(wlan.ifconfig()[0]) + '</h1>')
        


    elif url == 'config.html' and len(data) > 0 and not wlan.isconnected():
        # for i in nets:
        #     print(i[name])
        led.on()
        rows = []
        for net in nets:
            # if net['name'] == wlan.config('essid'):
            #     row = '<tr class="connected"><td class="name">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'  % (net['name'], net['mac'], net['rssi'], net['channel'], net['auth'])
            #     rows.append(row)
            # else:
            row = '<tr><td class="name">%s</td><td class="bssid">%s</td><td class="signal">%s</td><td class="channel">%s</td><td class="auth">%s</td></tr>'  % (net['name'], net['mac'], net['rssi'], net['channel'], net['auth'])
            rows.append(row)

        response = data % '\n'.join(rows)
        cl.sendall(response)
    elif len(data) > 0:
        cl.sendall(data)
    elif not wlan.isconnected():
        try:
            file = open('config.html')
            data = file.read()
            file.close()
        except:
            print('could not open')

        rows = []
        for net in nets:
            # if net['name'] == wlan.config('essid'):
            #     row = '<tr class="connected"><td class="name">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'  % (net['name'], net['mac'], net['rssi'], net['channel'], net['auth'])
            #     rows.append(row)
            # else:
            row = '<tr><td class="name">%s</td><td class="bssid">%s</td><td class="signal">%s</td><td class="channel">%s</td><td class="auth">%s</td></tr>'  % (net['name'], net['mac'], net['rssi'], net['channel'], net['auth'])
            rows.append(row)
        response = data % '\n'.join(rows)
        cl.sendall(response)
    else:
        # tim = Timer(0)
        # count = 0
        # def uuu(tim):
        #     res =+ count
        #     # print(res)
        #     cl.sendall(str(res))
        #     # return res

        # tim.init(period=2000, mode=Timer.PERIODIC, callback=uuu)
        cl.sendall('NOT FOUND')
    cl.close()
