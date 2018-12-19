from RoverPy_command import RoverPyCommand
  
class KeyBoardControl:
  
  sleepTime = 0.030
  forwardKey = 'z'
  backwardKey = 's'
  stopKey = 'space'
  turnRightKey = 'd'
  turnLeftKey = 'q'
  pivotRightKey = 'c'
  pivotLeftKey = 'w'
  roverPyCommand = RoverPyCommand()

  def __init__(self):
	print 'constructeur'

  def keyInput(self, event):
	print 'key: ', event.name
	keyPress = event.name
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
	else:
		pass
