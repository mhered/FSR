# analog.py

from machine import ADC, Pin
from utime import sleep

AO_PIN = 4   # ADC-capable pin where A0 is connected

adc = ADC(Pin(AO_PIN))
adc.atten(ADC.ATTN_11DB)    # full range ~0...3.3V
adc.width(ADC.WIDTH_12BIT)  # 0...4095

def read_voltage():
    raw = adc.read()
    v = (raw / 4095.0) * 3.3
    return raw, v

def loop(delay = 0.1):
    try:
        while True:
            raw, v = read_voltage()
            print("raw:", raw, "voltage:{:.3f}V".format(v))
            sleep(delay)
    except KeyboardInterrupt:
        print("Stopped.")


if __name__ == "__main__":
    print("Polling AO pin. Press Ctrl-C to stop.")
    loop()
