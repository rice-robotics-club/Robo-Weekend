# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-dc-motor-micropython/
from machine import Pin, PWM
from time import sleep

# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-dc-motor-micropython/

class DCMotor:
    def __init__(self, pin1, pin2, enable_pin, min_duty=15000, max_duty=65535):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

    def forward(self, speed):
        print('Motor Forwards')
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def backwards(self, speed):
        print('Motor Backwards')
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        print('Motor Stop')
        self.enable_pin.duty_u16(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * (speed / 100))
        return duty_cycle

frequency = 1000

pin1 = Pin(4,Pin.OUT)
pin2 = Pin(3,Pin.OUT) # TODO FIXME
enable = PWM(Pin(2, Pin.OUT))
enable.freq(frequency)

dc_motor = DCMotor(pin1, pin2, enable, min_duty=0)

# Set min duty cycle (15000) and max duty cycle (65535) 
# dc_motor = DCMotor(pin1, pin2, enable, 15000, 65535)




try:
    print('Forward with speed: 50%')
    dc_motor.forward(50)
    sleep(2)
    dc_motor.stop()
    sleep(2)
    print('Backwards with speed: 100%')
    dc_motor.backwards(100)
    sleep(2)
    print('Forward with speed: 5%')
    dc_motor.forward(5)
    sleep(2)
    dc_motor.stop()
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor.stop()