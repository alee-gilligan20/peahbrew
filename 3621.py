import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import math
import time

######################
## Motor Establishment
######################

motorL = 0
motorR = 1
c = 0
motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

front = 16
left = 17
right = 18

while c<15:
        c = c + .1
        time.sleep(0.1)
        sensor_pin = 0
        spd = RPL.analogRead(0)
        speed = int(2*92*math.log10(spd))
	if speed >500:
		speed = 500
	print speed
	RPL.servoWrite(motorL, 2000-speed)
	RPL.servoWrite(motorR, 1000+speed)
RPL.servoWrite(motorL, 1500)
RPL.servoWrite(motorR, 1500)
