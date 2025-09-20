from machine import Pin
import time

button = Pin(13, Pin.IN, Pin.PULL_UP)
i = 0
last = 0
while i < 100:
    i = i+1
    val = button.value()
    if last is 1 and last != val:
        print("Button is Pressed")
    last = val
    time.sleep(0.1)