
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
		self.isStarted = True
		while self.isStarted:
			self.distance = self.ultrasonicMeasure.MeasureAverage(self.measureNumber)
			if self.distance > self.distanceMin:
				if self.distance < self.distanceMax:
					self.roverPyCommand.stop()
				else:
					self.roverPyCommand.forward(self.walkingDuration)
			else:
				self.roverPyCommand.backward(self.walkingDuration)					
	
	def stop(self):
		self.isStarted = False