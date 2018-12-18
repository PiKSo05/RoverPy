import sys
#import RoverPy_command
from RoverPy_command import RoverPyCommand

roverPyCommand = RoverPyCommand()

#roverPyCommand.test()

roverPyCommand.forward(1)
roverPyCommand.backward(1)
roverPyCommand.turnLeft(0.5)
roverPyCommand.turnRight(1)
roverPyCommand.pivotLeft(1)
roverPyCommand.pivotRight(0.3)
roverPyCommand.stop()

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(22, GPIO.OUT)
##GPIO.setup(23, GPIO.OUT)
##GPIO.setup(24, GPIO.OUT)
##GPIO.setup(25, GPIO.OUT)
##     
##GPIO.output(22, GPIO.HIGH)
####GPIO.output(23, GPIO.HIGH)
##GPIO.output(25, GPIO.HIGH)
####GPIO.output(24, GPIO.LOW)
##time.sleep(1)
##GPIO.cleanup()
