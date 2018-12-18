import RPi.GPIO as GPIO
import time
import sys

class RoverPyCommand:

	def init():
		GPIO.setmode(GPIO.BCM)
	    	#GPIO.setmode(gpio.BOARD)
		GPIO.setup(22, GPIO.OUT)
    		GPIO.setup(23, GPIO.OUT)
	    	GPIO.setup(24, GPIO.OUT)
    		GPIO.setup(25, GPIO.OUT)

	def forward(tf):
		init()GPIO.output(22, GPIO.HIGH)
    		GPIO.output(23, GPIO.LOW)
    		GPIO.output(25, GPIO.HIGH)
    		GPIO.output(24, GPIO.LOW)
    		time.sleep(tf)
    		GPIO.cleanup()

	def backward(tf):
    		init()
    		GPIO.output(22, GPIO.LOW)
    		GPIO.output(23, GPIO.HIGH)
    		GPIO.output(25, GPIO.LOW)
    		GPIO.output(24, GPIO.HIGH)
    		time.sleep(tf)
    		GPIO.cleanup()

	def turnRight(tf):
    		init()
    		GPIO.output(22, GPIO.HIGH)
		GPIO.output(23, GPIO.LOW)
    		GPIO.output(25, GPIO.LOW)
    		GPIO.output(24, GPIO.LOW)
    		time.sleep(tf)
    		GPIO.cleanup()
	def turnLeft(tf):
		init()
		GPIO.output(22, GPIO.LOW)
    		GPIO.output(23, GPIO.LOW)
    		GPIO.output(25, GPIO.HIGH)
    		GPIO.output(24, GPIO.LOW)
    		time.sleep(tf)
    		GPIO.cleanup()

	def pivotRight(tf):
    		init()
    		GPIO.output(22, GPIO.HIGH)
    		GPIO.output(23, GPIO.LOW)
    		GPIO.output(25, GPIO.LOW)
    		GPIO.output(24, GPIO.HIGH)
    		time.sleep(tf)
    		GPIO.cleanup()

	def pivotLeft(tf):
    		init()
    		GPIO.output(22, GPIO.LOW)
    		GPIO.output(23, GPIO.HIGH)
    		GPIO.output(25, GPIO.HIGH)
    		GPIO.output(24, GPIO.LOW)
    		time.sleep(tf)
    		GPIO.cleanup()

	def keyInput(event):
    		init()
    		print 'key: ', event.char
    		keyPress = event.char
    		sleepTime = 0.030
		if keyPress.lower() == 'z':
        		forward(sleepTime)
    		elif keyPress.lower() == 's':
        		backward(sleepTime)
    		elif keyPress.lower() == 'q':
        		turnLeft(sleepTime)
    		elif keyPress.lower() == 'd':
        		turnRight(sleepTime)
    		elif keyPress.lower() == 'w':
        		pivotLeft(sleepTime)
    		elif keyPress.lower() == 'c':
        		pivotRight(sleepTime)
    		else:
        		pass
