from microbit import *
import radio


radio.config(channel=7, group=0, queue=1)
radio.on()


leftSpeedPin = pin2
leftDirectionPin = pin12
rightSpeedPin = pin1
rightDirectionPin = pin8

#  deadBand = 5   not used

#  0 turns the motors off; 1023 turns them on at full speed
def stop():
    leftDirectionPin.write_digital(0)
    leftSpeedPin.write_analog(0)
    rightDirectionPin.write_digital(0)
    rightSpeedPin.write_analog(0)
    display.clear()

# Inputs between 0-1023 to control both motors
def drive(L, R):
    #  an adjustment to correct for motor speed discrepancy
    L = int(L * 1)
    R = int(R * 1)
    leftSpeed = abs(L)
    if leftSpeed < 0:
        leftSpeed = 0
    if leftSpeed > 1023:
        leftSpeed = 1023
    rightSpeed = abs(R)
    if rightSpeed < 0:
        rightSpeed = 0
    if rightSpeed > 1023:
        rightSpeed = 1023

    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 5:
        leftDirectionPin.write_digital(0)  # go forwards at speed given
        leftSpeedPin.write_analog(leftSpeed)         # don't go backwards
    elif L < -5:  # and L >= -1023
        leftDirectionPin.write_digital(1)         # don't go forwards
        leftSpeedPin.write_analog(leftSpeed)  # go backwards at speed given
    else:
        leftDirectionPin.write_digital(0)         # stop the left wheel
        leftSpeedPin.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 5:  # and R <= 1023
        rightDirectionPin.write_digital(0)  # go forwards at speed given
        rightSpeedPin.write_analog(rightSpeed)         # don't go backwards
    elif R < -5:  # and R >= -1023
        rightDirectionPin.write_digital(1)         # don't go forwards
        rightSpeedPin.write_analog(rightSpeed)  # go backwards at speed given
    else:
        rightDirectionPin.write_digital(0)         # stop the right wheel
        rightSpeedPin.write_analog(0)


'''
MAIN LOOP
'''
while True:
    message = radio.receive()
    if message is not None:
        message = message.split()
        drive(int(message[0]), int(message[1]))
