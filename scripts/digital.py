# fsr_digital_poll.py
import machine
import utime

DO_PIN = 18   # change to the pin you connect DO to

do = machine.Pin(DO_PIN, machine.Pin.IN)  # no pull configured; module drives the pin

def loop(delay=0.1):
    try:
        while True:
            state = 1 - do.value()   #1 when pressed, 0 otherwise
            print(state)
            utime.sleep(delay)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    print("Polling DO pin. Press Ctrl-C to stop.")
    loop()
