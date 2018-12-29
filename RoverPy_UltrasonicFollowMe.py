
# Import required Python libraries
import time
from StoppableThread import StoppableThread
from RoverPy_UltrasonicMeasure import UltrasonicMeasure
from RoverPy_command import RoverPyCommand

class UltrasonicFollowMe(StoppableThread):
	roverPyCommand = RoverPyCommand()
	ultrasonicMeasure = UltrasonicMeasure()
	distanceMin = 10.0 #distance in centimeter
	distanceMax = 20.0 #distance in centimeter
	walkingDuration = 0.5 #duration in seconds
	measureNumber = 3
	
	def __init__(self):
		print 'constructeur'
		StoppableThread.__init__(self)
		
	def run(self):
		while True:
			self.distance = self.ultrasonicMeasure.MeasureAverage(self.measureNumber)
			if self.distance > self.distanceMin:
				if self.distance < self.distanceMax:
					self.roverPyCommand.stop()
				else:
					self.roverPyCommand.forward(self.walkingDuration)
			else:
				self.roverPyCommand.backward(self.walkingDuration)					
	