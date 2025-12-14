# digital.py

from machine import Pin
from utime import sleep

D0_PIN = 18   # pin where D0 is connected

led = Pin(2, Pin.OUT)
d0 = Pin(D0_PIN, Pin.IN)  # no pull configured; module drives the pin

def loop(delay=0.1):
    try:
        while True:
            state = not d0.value()   # True when pressed, False otherwise
            led.value(state) # LED on when pressed
            print( "Pressure detected" if state else "No Pressure detected")
            sleep(delay)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    print("Polling DO pin. Press Ctrl-C to stop.")
    loop()
