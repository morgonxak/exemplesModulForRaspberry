'''
Модуль работы с дачиком растояния
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 38
GPIO.setup(TRIG, GPIO.OUT, initial=0)
GPIO.setup(ECHO, GPIO.IN)

# Minimum delay between measurements is 50ms. 100ms is fine:
time.sleep(0.1)

# Send a probe signal to the sensor. Signal should be 10 micro sec long.
GPIO.output(TRIG,1)
time.sleep(0.00001)
GPIO.output(TRIG,0)
print "ok"
while GPIO.input(ECHO) == 0:
    pass
    start = time.time()

while GPIO.input(ECHO) == 1:
    pass
    stop = time.time()

# Print distance to object in santimeters. Sound speed = 340 m/s
print "Distance = ", (stop - start) * 17000, "sm"
print "start time = ", start
print "stop time = ", stop

GPIO.cleanup()