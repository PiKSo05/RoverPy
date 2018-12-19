import RoverPyCommand from RoverPy_command
  
class KeyBoardControl:
  
  sleepTime = 0.030
  forwardKey = 'z'
  backwardKey = 's'
  stopKey = 'space'
  turnRightKey = 'd'
  turnLeftKey = 'q'
  pivotRightKey = 'c'
  pivotLeftKey = 'w'

  def __init__(self):
      print 'constructeur'
    
  def keyInput(self, event):
	print 'key: ', event.name
	keyPress = event.name
	if keyPress.lower() == self.forwardKey:
		self.forward(self.sleepTime)
	elif keyPress.lower() == self.backwardKey:
		self.backward(self.sleepTime)
	elif keyPress.lower() == self.turnLeftKey:
		self.turnLeft(self.sleepTime)
	elif keyPress.lower() == self.turnRightKey:
		self.turnRight(self.sleepTime)
	elif keyPress.lower() == self.pivotLeftKey:
		self.pivotLeft(self.sleepTime)
	elif keyPress.lower() == self.pivotRightKey:
		self.pivotRight(self.sleepTime)
	elif keyPress.lower() == self.stopKey:
		self.stop()
	else:
		pass
