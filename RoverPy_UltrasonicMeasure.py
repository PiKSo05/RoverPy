
# Import required Python libraries
import time
import RPi.GPIO as GPIO

class UltrasonicMeasure:
	# Define GPIO to use on Pi
	GPIO_TRIGGER = 17
	GPIO_ECHO = 27
	MeasureOn = 0

	def init(self):
		# Use BCM GPIO references
		# instead of physical pin numbers
		GPIO.setmode(GPIO.BCM)

	def Measure(self):
		print "Ultrasonic Measurement"
		self.init()
		# Set pins as output and input
		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)  # Trigger
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)      # Echo

		# Set trigger to False (Low)
		GPIO.output(self.GPIO_TRIGGER, False)

		# Allow module to settle
		time.sleep(0.5)

		# Send 10us pulse to trigger
		GPIO.output(self.GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)
		start = time.time()
		while GPIO.input(self.GPIO_ECHO)==0:
		  start = time.time()

		while GPIO.input(self.GPIO_ECHO)==1:
		  stop = time.time()

		distance = self.ComputeDistance(start, stop)

		# Reset GPIO settings
		GPIO.cleanup()
		print "Distance : %.1f" % distance

		return distance

	def ComputeDistance(self, startTime, stopTime):
		# Calculate pulse length
		elapsed = stopTime-startTime

		# Distance pulse travelled in that time is time
		# multiplied by the speed of sound (cm/s)
		distance = elapsed * 34000

		# That was the distance there and back so halve the value
		distance = distance / 2

		return distance

	def MeasureAverage(self, numberOfMeasures):
		distance = 0

		for i in range(0, numberOfMeasures):
			distance = distance + self.Measure()

		distance = distance / numberOfMeasures
		print "Distance moyenne : %.1f" % distance

		return distance

	def MeasureContinueStart(self):
		self.MeasureOn = 1
		while self.MeasureOn == 1:
			self.Measure()

	def MeasureContinueStop(self):
		self.MeasureOn = 0
