
from RoverPy_UltrasonicMeasure import UltrasonicMeasure

ultrasonicMeasure = UltrasonicMeasure()

distance = ultrasonicMeasure.Measure()
distance = ultrasonicMeasure.MeasureAverage(3)

ultrasonicMeasure.MeasureContinueStart()
