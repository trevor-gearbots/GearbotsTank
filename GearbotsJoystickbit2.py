from microbit import *
import radio

radio.config(channel=7, group=0, queue=1)
radio.on()

buttons = {2: 'A',
           516: 'B',
           684: 'C',
           768: 'D',
           853: 'E',
           819: 'F'}

def button_press():
    press = pin2.read_analog()
    if press < 900:
        for number in range(press-5, press+5):
            if number in buttons:
                return buttons[number]

def joystick_push():
    x = pin0.read_analog() - 522
    y = pin1.read_analog() - 514
    leftMotor = y + x
    rightMotor = y - x
    leftMotor = (leftMotor * 2)
    rightMotor = (rightMotor * 2)
    return leftMotor, rightMotor

while True:
    joystick = joystick_push()
    message = str(joystick[0]) + " " + str(joystick[1])
    radio.send(message)
    print(joystick)
    sleep(10)


