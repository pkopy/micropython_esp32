from machine import Pin
from time import sleep
import esp32
import urandom
import urequests
import network

led = Pin(2, Pin.OUT)
def led_connect():
    while True:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)

def do_connect():
    count = 0
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        # led_connect()
        print('connecting to network...')
        wlan.connect('ZyXEL_B6AF', 'Kopycki76')
        while not wlan.isconnected():
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)
    led.off()
    print('network config:', wlan.ifconfig())
    while True:
        led.on()
        rand = urandom.getrandbits(10)
        try:
            response = urequests.post("http://192.168.1.42:5000/hoho", json={"value": rand})
            print(response.json())
            led.off()
            sleep(3)
            count=0
        except:
            print("Error: bad response")
            led.off()
            sleep(2)
            count+=1
            if count > 50:
                break

        # sleep(10)

do_connect()
