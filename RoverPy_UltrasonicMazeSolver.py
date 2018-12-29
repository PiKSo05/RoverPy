
# Import required Python libraries
import time
from StoppableThread import StoppableThread
from RoverPy_UltrasonicMeasure import UltrasonicMeasure
from RoverPy_command import RoverPyCommand

class UltrasonicMazeSolver(StoppableThread):
	roverPyCommand = RoverPyCommand()
	ultrasonicMeasure = UltrasonicMeasure()
	distanceMin = 10.0 #distance in centimeter
	walkingDuration = 0.5 #duration in seconds
	measureNumber = 3
	turnAngle = 45 #angle in degree
	
	def __init__(self):
		print 'constructeur'
		StoppableThread.__init__(self)
		
	def run(self):
		while True:
			if StoppableThread.stopped():
				self.roverPyCommand.stop()
				break
			self.distance = self.ultrasonicMeasure.MeasureAverage(self.measureNumber)
			if self.distance > self.distanceMin:
				self.roverPyCommand.forward(self.walkingDuration)
			else:
				self.roverPyCommand.backward(self.walkingDuration)
				self.roverPyCommand.pivotRightAngle(self.turnAngle)						
	