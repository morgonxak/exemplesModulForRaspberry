'''
Модуль работы со светодиодом
'''
i = 0
import RPi.GPIO as GPIO
import time
LED = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

i = 0
while (i < 5):
    i = i + 1
    time.sleep(0.5)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)

GPIO.cleanup()