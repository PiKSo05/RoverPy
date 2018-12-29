
# Import required Python libraries
import time
from RoverPy_UltrasonicMeasure import UltrasonicMeasure
from RoverPy_command import RoverPyCommand

class UltrasonicFollowMe:
	isStarted = False
	roverPyCommand = RoverPyCommand()
	ultrasonicMeasure = UltrasonicMeasure()
	distanceMin = 10.0 #distance in centimeter
	distanceMax = 20.0 #distance in centimeter
	walkingDuration = 0.5 #duration in seconds
	measureNumber = 3
	
	def __init__(self):
		print 'constructeur'
		
	def start(self):
		isStarted = True
		while isStarted:
			distance = ultrasonicMeasure.MeasureAverage(measureNumber)
			if distance > distanceMin:
				if distance < distanceMax:
					roverPyCommand.stop()
				else:
					roverPyCommand.forward(walkingDuration)
			else:
				roverPyCommand.backward(walkingDuration)					
	
	def stop(self):
		isStarted = False