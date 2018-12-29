
# Import required Python libraries
import time
from threading import Thread
from RoverPy_UltrasonicMeasure import UltrasonicMeasure
from RoverPy_command import RoverPyCommand

class UltrasonicMazeSolver(Thread):
	roverPyCommand = RoverPyCommand()
	ultrasonicMeasure = UltrasonicMeasure()
	distanceMin = 10.0 #distance in centimeter
	walkingDuration = 0.5 #duration in seconds
	measureNumber = 3
	turnAngle = 45 #angle in degree
	
	def __init__(self):
		print 'constructeur'
		Thread.__init__(self)
		
	def run(self):
		while True:
			self.distance = self.ultrasonicMeasure.MeasureAverage(self.measureNumber)
			if self.distance > self.distanceMin:
				self.roverPyCommand.forward(self.walkingDuration)
			else:
				self.roverPyCommand.backward(self.walkingDuration)
				self.roverPyCommand.pivotRightAngle(self.turnAngle)						
	