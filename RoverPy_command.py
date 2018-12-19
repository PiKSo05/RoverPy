import RPi.GPIO as GPIO
import time
import sys

class RoverPyCommand:
	GPIO_LEFT_FORWARD = 22
	GPIO_LEFT_BACKWARD = 23
	GPIO_RIGHT_FORWARD = 25
	GPIO_RIGHT_BACKWARD = 24	
	
	def __init__(self):
		print 'constructeur'
		self.init()

	def test(self):
		print 'test roverPy'

	def init(self):
		print 'Initialisation'
		GPIO.setmode(GPIO.BCM)
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.GPIO_LEFT_FORWARD, GPIO.OUT)
		GPIO.setup(self.GPIO_LEFT_BACKWARD, GPIO.OUT)
		GPIO.setup(self.GPIO_RIGHT_FORWARD, GPIO.OUT)
		GPIO.setup(self.GPIO_RIGHT_BACKWARD, GPIO.OUT)

	def stop(self):
		print 'Stoppe'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.LOW)
		GPIO.cleanup()

	def forward(self, tf):
		print 'Avance pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.LOW)
		time.sleep(tf)
		GPIO.cleanup()

	def backward(self, tf):
		print 'Recule pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.HIGH)
		time.sleep(tf)
		GPIO.cleanup()

	def turnRight(self, tf):
		print 'Tourne a droite pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.LOW)
		time.sleep(tf)
		GPIO.cleanup()

	def turnLeft(self, tf):
		print 'Tourne a gauche pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.LOW)
		time.sleep(tf)
		GPIO.cleanup()

	def pivotRight(self, tf):
		print 'Pivote a droite pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.HIGH)
		time.sleep(tf)
		GPIO.cleanup()

	def pivotLeft(self, tf):
		print 'Pivote a gauche pendant ', tf, 's'
		self.init()
		GPIO.output(self.GPIO_LEFT_FORWARD, GPIO.LOW)
		GPIO.output(self.GPIO_LEFT_BACKWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_RIGHT_FORWARD, GPIO.HIGH)
		GPIO.output(self.GPIO_RIGHT_BACKWARD, GPIO.LOW)
		time.sleep(tf)
		GPIO.cleanup()

#	def keyInput(self, event):
#		print 'key: ', event.name
#		keyPress = event.name
#		sleepTime = 0.030
#		if keyPress.lower() == 'z':
#			self.forward(sleepTime)
#		elif keyPress.lower() == 's':
#			self.backward(sleepTime)
#		elif keyPress.lower() == 'q':
#			self.turnLeft(sleepTime)
#		elif keyPress.lower() == 'd':
#			self.turnRight(sleepTime)
#		elif keyPress.lower() == 'w':
#			self.pivotLeft(sleepTime)
#		elif keyPress.lower() == 'c':
#			self.pivotRight(sleepTime)
#		elif keyPress.lower() == 'space':
#			self.stop()
#		else:
#			pass

	
