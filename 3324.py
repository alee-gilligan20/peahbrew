import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import time

######################
## Motor Establishment
######################

motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

front = 16
left = 17
right = 18

c = 0

while c < 30:
        c = c + 1
	time.sleep(0.5)
	RPL.pinMode(front, RPL.INPUT)
	fr = RPL.digitalRead(front)
	print fr
	if fr == 1:
		RPL.servoWrite(motorL, 1000)
		RPL.servoWrite(motorR, 1000)
	if fr == 0:
		RPL.servoWrite(motorL, 2000)
		RPL.servoWrite(motorR, 2000)
RPL.servoWrite(motorL, 1500)
RPL.servoWrite(motorR, 1500)
