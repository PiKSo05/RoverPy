
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
		self.isStarted = True
		while self.isStarted:
			self.distance = self.ultrasonicMeasure.MeasureAverage(self.measureNumber)
			if self.distance > self.distanceMin:
				self.roverPyCommand.forward(self.walkingDuration)
			else:
				self.roverPyCommand.backward(self.walkingDuration)
				self.roverPyCommand.pivotRightAngle(self.turnAngle)						
	
	def stop(self):
		self.isStarted = False