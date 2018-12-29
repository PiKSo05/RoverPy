
# Import required Python libraries
import time
from RoverPy_UltrasonicMeasure import UltrasonicMeasure
from RoverPy_command import RoverPyCommand

class UltrasonicMazeSolver:
	isStarted = False
	roverPyCommand = RoverPyCommand()
	ultrasonicMeasure = UltrasonicMeasure()
	distanceMin = 10.0 #distance in centimeter
	walkingDuration = 0.5 #duration in seconds
	measureNumber = 3
	turnAngle = 45 #angle in degree
	
	def __init__(self):
		print 'constructeur'
		
	def start(self):
		isStarted = True
		while isStarted:
			distance = ultrasonicMeasure.MeasureAverage(measureNumber)
			if distance > distanceMin:
				roverPyCommand.forward(walkingDuration)
			else:
				roverPyCommand.backward(walkingDuration)
				roverPyCommand.pivotRightAngle(turnAngle)						
	
	def stop(self):
		isStarted = False