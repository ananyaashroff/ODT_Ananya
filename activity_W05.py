from machine import Pin, PWM
import time
import neopixel
import random

np = neopixel.NeoPixel(Pin(5),16)
pb1 = Pin(4, Pin.IN, Pin.PULL_UP)
pb2 = Pin(12, Pin.IN, Pin.PULL_UP)
white = [255,200,100]
pink = [255,51,153]


while True :
    pb1_val = pb1.value()
    print("01")
    time.sleep(0.1)
    pb2_val = pb2.value()
    print("02")
    time.sleep(0.1)
    
    
    if pb1_val == 0:
        print("01")
        for i in range(0,16):
             np[i] = white
             np.write()
             time.sleep(0.01)
             
             
    if pb2_val == 0:
        print("02")
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = [r, g, b]
        
        for y in range(0,16):
            np[y]= x
            np.write()
            time.sleep(0.01)
            
            
            
#left button white light. right button random color generated
