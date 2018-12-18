import RPi.GPIO as GPIO
import time
import sys

class RoverPyCommand:
	def __init__(self):
		print 'constructeur'
		self.init()

	def test(self):
		print 'test roverPy'

	def init(self):
		print 'Initialisation'
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(22, GPIO.OUT)
		GPIO.setup(23, GPIO.OUT)
		GPIO.setup(24, GPIO.OUT)
		GPIO.setup(25, GPIO.OUT)

	def stop(self):
		print 'Stoppe'
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		#GPIO.cleanup()

	def forward(self, tf):
		print 'Avance pendant ', tf, 's'
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.LOW)
		time.sleep(tf)
		#GPIO.cleanup()

	def backward(self, tf):
		print 'Recule pendant ', tf, 's'
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(tf)
		#GPIO.cleanup()

	def turnRight(self, tf):
		print 'Tourne a droite pendant ', tf, 's'
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		time.sleep(tf)
		#GPIO.cleanup()

	def turnLeft(self, tf):
		print 'Tourne a gauche pendant ', tf, 's'
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.LOW)
		time.sleep(tf)
		#GPIO.cleanup()

	def pivotRight(self, tf):
		print 'Pivote a droite pendant ', tf, 's'
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(tf)
		#GPIO.cleanup()

	def pivotLeft(self, tf):
		print 'Pivote a gauche pendant ', tf, 's'
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.LOW)
		time.sleep(tf)
		#GPIO.cleanup()

	def keyInput(self, event):
		print 'key: ', event.name
		keyPress = event.name
		sleepTime = 0.030
		if keyPress.lower() == 'z':
			self.forward(sleepTime)
		elif keyPress.lower() == 's':
			self.backward(sleepTime)
		elif keyPress.lower() == 'q':
			self.turnLeft(sleepTime)
		elif keyPress.lower() == 'd':
			self.turnRight(sleepTime)
		elif keyPress.lower() == 'w':
			self.pivotLeft(sleepTime)
		elif keyPress.lower() == 'c':
			self.pivotRight(sleepTime)
		elif keyPress.lower() == 'space':
			self.stop()
		else:
			pass

	
