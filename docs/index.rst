********************************
matelec-ESP8266-BUS I2C
********************************

Sources documentaires:
 * https://docs.micropython.org/en/latest/esp32/quickref.html#software-i2c-bus
 * https://docs.micropython.org/en/latest/esp8266/quickref.html#i2c-bus
 * https://github.com/mcauser/micropython-lm75a

Matériels:
  * https://fr.aliexpress.com/item/32689349400.html?spm=a2g0o.cart.0.0.2849378dny4KPH&mp=1&gatewayAdapt=glo2fra
  * https://fr.aliexpress.com/item/32643950109.html?spm=a2g0o.order_list.order_list_main.17.21ef5e5b4c1HLe&gatewayAdapt=glo2fra


--------------------
script python n°1:
--------------------
Il permet d'initialiser le bus I2C et de scanner le bus pour récupérer les adresses des esclaves.

.. literalinclude:: ./code/exemple_I2C_01.py
