from RoverPy_command import RoverPyCommand
from RoverPy_UltrasonicFollowMe import UltrasonicFollowMe
from RoverPy_UltrasonicMazeSolver import UltrasonicMazeSolver
  
class KeyBoardControl:
  
  sleepTime = 0.030
  forwardKey = 'z'
  backwardKey = 's'
  stopKey = 'space'
  turnRightKey = 'd'
  turnLeftKey = 'q'
  pivotRightKey = 'c'
  pivotLeftKey = 'w'
  mazeSolverModeKey = '1'
  followMeModeKey = '2'
  roverPyCommand = RoverPyCommand()
  ultrasonicMazeSolver = UltrasonicMazeSolver()
  ultrasonicFollowMe = UltrasonicFollowMe()

  def __init__(self):
	print 'constructeur'

  def keyInput(self, event):
	print 'key: ', event.name
	keyPress = event.name
	
	if keyPress.lower() != self.mazeSolverModeKey:
		self.ultrasonicMazeSolver.stop()
		self.ultrasonicMazeSolver.join()
	if keyPress.lower() != self.followMeModeKey:
		self.ultrasonicFollowMe.stop()
		self.ultrasonicFollowMe.join()
		
	if keyPress.lower() == self.forwardKey:
		self.roverPyCommand.forward(self.sleepTime)
	elif keyPress.lower() == self.backwardKey:
		self.roverPyCommand.backward(self.sleepTime)
	elif keyPress.lower() == self.turnLeftKey:
		self.roverPyCommand.turnLeft(self.sleepTime)
	elif keyPress.lower() == self.turnRightKey:
		self.roverPyCommand.turnRight(self.sleepTime)
	elif keyPress.lower() == self.pivotLeftKey:
		self.roverPyCommand.pivotLeft(self.sleepTime)
	elif keyPress.lower() == self.pivotRightKey:
		self.roverPyCommand.pivotRight(self.sleepTime)
	elif keyPress.lower() == self.stopKey:
		self.roverPyCommand.stop()
	elif keyPress.lower() == self.mazeSolverModeKey:
		self.ultrasonicMazeSolver.start()
	elif keyPress.lower() == self.followMeModeKey:
		self.ultrasonicFollowMe.start()
	else:
		pass
