# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-servo-motor-micropython/

from machine import Pin, PWM
from time import sleep

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
        # print('Motor Stop')
        self.enable_pin.duty_u16(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * (speed / 100))
        return duty_cycle


# MOTOR CONFIG
frequency = 1000
# Set min duty cycle (15000) and max duty cycle (65535) 
# dc_motor = DCMotor(pin1, pin2, enable, 15000, 65535)
motorpin1 = Pin(3, Pin.OUT)
motorpin2 = Pin(4, Pin.OUT)
motorpwm = PWM(Pin(2, Pin.OUT))
motorpwm.freq (frequency)

dc_motor = DCMotor(motorpin1, motorpin2, motorpwm, min_duty=0)

# SERVO CONFIG
# Set up PWM Pin for servo/motor control
servo1_pin = Pin(16)
servo1_L1 = PWM(servo1_pin)
servo2_pin = Pin(17)
servo2_L2 = PWM(servo2_pin)


# BUTTON CONFIG
switch_button = Pin(13, Pin.IN, Pin.PULL_UP)
pos_button = Pin(14, Pin.IN, Pin.PULL_UP)
neg_button = Pin(15, Pin.IN, Pin.PULL_UP)
# Set Duty Cycle for Different Angles
max_duty = 7864 # 9000
# min_duty = 1802
# half_duty = int(max_duty/2)
servo_incr = 500
#Set PWM frequency
frequency = 50
servo1_L1.freq(frequency)
servo2_L2.freq(frequency)
print("Running Teleop...")

i = 0
last_switch = 0
last_pos = 0
last_neg = 0
selected_motor = 0

curr_L1 = 0
curr_L2 = 0

while i < 200:
    i = i + 1

    # button logic
    val = switch_button.value()
    if last_switch is 1 and last_switch != val:
        print("Switch Button is Pressed")
        selected_motor = (selected_motor + 1) % 3
    last_switch = val

    pos_pressed = 0
    neg_pressed = 0

    val = pos_button.value()
    if last_pos is 1 and last_pos != val:
        print("Pos Button is Pressed")
        pos_pressed = 1
    last_pos = val

    val = neg_button.value()
    if last_neg is 1 and last_neg != val:
        print("Neg Button is Pressed")
        neg_pressed = 1
    last_neg = val


    if (selected_motor == 0):
        # Base Motor
        if (pos_pressed):
            dc_motor.forward(80)
        elif (neg_pressed):
            dc_motor.backwards(80)
        else:
            dc_motor.stop()
    elif (selected_motor == 1):
        # L1 lower arm servo
        if (pos_pressed):
            curr_L1 = curr_L1 + servo_incr
            if (curr_L1 > max_duty):
                curr_L1 = max_duty
            servo1_L1.duty_u16(curr_L1)
        elif (neg_pressed):
            curr_L1 = curr_L1 - servo_incr
            if curr_L1 < 0:
                curr_L1 = 0
            servo1_L1.duty_u16(curr_L1)
    elif (selected_motor == 2):
        # L2 upper arm servo
        if (pos_pressed):
            if (curr_L2 > max_duty):
                curr_L2 = max_duty
            curr_L2 = curr_L2 + servo_incr
            servo2_L2.duty_u16(curr_L2)
        elif (neg_pressed):
            curr_L2 = curr_L2 - servo_incr
            if curr_L2 < 0:
                curr_L2 = 0
            servo2_L2.duty_u16(curr_L2)

    sleep(0.1)

servo1_L1.deinit()
servo1_pin.off()
servo2_L2.deinit()
servo2_pin.off()
dc_motor.stop()

print("Finished.")


