import machine
import utime

AO_PIN = 4   # ADC-capable pin

adc = machine.ADC(machine.Pin(AO_PIN))
adc.atten(machine.ADC.ATTN_11DB)    # full range ~0...3.3V
adc.width(machine.ADC.WIDTH_12BIT)  # 0...4095

def read_voltage():
    raw = adc.read()
    v = (raw / 4095.0) * 3.3
    return raw, v

try:
    while True:
        raw, v = read_voltage()
        print("raw:", raw, "voltage:{:.3f}V".format(v))
        utime.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped.")