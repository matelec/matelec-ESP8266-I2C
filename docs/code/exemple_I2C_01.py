from machine import Pin, I2C
import time

#configuration du bus I2C sur l'ESP8266
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000, timeout=5000)

print ("san du bus i2c")
devices = i2c.scan()

if len(devices) == 0:
    print("aucun périphérique sur le bus I2C")
else :
    print("périphérique trouvé:",len(devices))
    for i in devices:
        print("decimal", i)
        print("hexadecimal", hex(i))
