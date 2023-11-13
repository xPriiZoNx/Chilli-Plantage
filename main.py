#import needed packages 
import machine
from machine import ADC, Pin  
import time
import sys
import errno
#import itertools
#import numpy as np

#define Pin & create object
led_pin = machine.Pin(2,machine.Pin.OUT)
led_pin.value(0)
# create an ADC object acting on a pin
soil_sensor = ADC(Pin(34))
soil_sensor.atten(ADC.ATTN_11DB)
soil_sensor.width(ADC.WIDTH_12BIT)






#define relais
relais = machine.Pin(32,machine.Pin.OUT)
relais.value(0)

#define vlaues 
#pos_values = [range(10,50,1)]
pos_values = list(range(10, 100))
counter = 0
x = 1
 
#def soil_value(moisture):
#    moisture = map(soil_sensor.read_u16(),(0,100),(0,65000))
#    return moisture
moisture = soil_sensor.read_u16()
print(pos_values)

while True:
    #led_pin.value(1)
    #time.sleep(1)
    #led_pin.value(0)
    time.sleep(1)
    #print(soil_sensor.read_u16())
    #print(moisture)
    #check mesured value
   # print(soil_sensor.read_u12())
    print(soil_sensor.read())
   # if soil_sensor.read_u16() < 10000:
      # led_pin.value(1)
      # relais.value(1)
        #counter = x + 1
        #print(counter)
        #if counter > 10 :
            #relais.value(0)
            #exit programm 
            #quit()
            #exc.StopIteration
        #else:
           # counter = 0
           # continue
    #led_pin.value(0)
   # relais.value(0)

        
