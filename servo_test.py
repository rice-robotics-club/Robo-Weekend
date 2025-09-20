# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-servo-motor-micropython/

from machine import Pin, PWM
from time import sleep

# Set up PWM Pin for servo control
servo1_pin = Pin(16)
servo1 = PWM(servo1_pin)
servo2_pin = Pin(17)
servo2 = PWM(servo2_pin)


# Set Duty Cycle for Different Angles
max_duty = 7864 # 9000
min_duty = 1802
half_duty = int(max_duty/2)

#Set PWM frequency
frequency = 50
servo1.freq (frequency)
servo2.freq (frequency)
print("Running Servo Test...")

i = 0
try:
    while i < 2:
        i = i + 1
        #Servo at 0 degrees
        servo1.duty_u16(min_duty)
        servo2.duty_u16(min_duty)
        sleep(2)
        #Servo at 90 degrees
        servo1.duty_u16(half_duty)
        servo2.duty_u16(half_duty)
        sleep(2)
        #Servo at 180 degrees
        servo1.duty_u16(max_duty)
        servo2.duty_u16(max_duty)
        sleep(2)    
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo1.deinit()
    servo1_pin.off()
    servo2.deinit()
    servo2_pin.off()

servo1.deinit()
servo1_pin.off()
servo2.deinit()
servo2_pin.off()

print("Finished.")


