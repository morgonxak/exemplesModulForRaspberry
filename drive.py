'''
Модуль работы с моторами на Raspberry
'''

#!/usr/bin/env python
#from settings import GPIO,PIN_EN_A,PIN_EN_B,PIN_IN_1_A,PIN_IN_1_B,PIN_IN_2_A,PIN_IN_2_B
import time
import RPi.GPIO as GPIO
PIN_IN_1_A = 4  # pin11
PIN_IN_2_A = 17  # pin12
PIN_EN_A = 23  # pin13

PIN_IN_1_B = 27   # pin11
PIN_IN_2_B = 22  # pin12
PIN_EN_B = 24  # pin13

def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    #GPIO.setwarnings(False)

    GPIO.setup(PIN_IN_1_A, GPIO.OUT)  # mode --- output motor A
    GPIO.setup(PIN_IN_2_A, GPIO.OUT)
    GPIO.setup(PIN_EN_A, GPIO.OUT)

    GPIO.setup(PIN_IN_1_B, GPIO.OUT)  # mode --- output motor B
    GPIO.setup(PIN_IN_2_B, GPIO.OUT)
    GPIO.setup(PIN_EN_B, GPIO.OUT)

    pwm_A = GPIO.PWM(PIN_EN_A,10)
    pwm_A.start(0)

    pwm_B = GPIO.PWM(PIN_EN_B, 10)
    pwm_B.start(0)

    return (pwm_A,pwm_B)


def loop():
    i = 10
    while True:
        print 'Press Ctrl+C to end the program...'

        print ("i= ", i)

        pwm[0].ChangeDutyCycle(i)
        pwm[1].ChangeDutyCycle(i)
        GPIO.output(PIN_IN_1_A, GPIO.HIGH)  # clockwise
        GPIO.output(PIN_IN_2_A, GPIO.LOW)
        time.sleep(5)
        i=i+10

        if i == 100:
            break

def go_forward(spead=50):
    pwm[0].ChangeDutyCycle(spead)
    pwm[1].ChangeDutyCycle(spead)

    GPIO.output(PIN_IN_1_A, GPIO.HIGH)  # clockwise
    GPIO.output(PIN_IN_2_A, GPIO.LOW)

    GPIO.output(PIN_IN_1_B, GPIO.HIGH)  # clockwise
    GPIO.output(PIN_IN_2_B, GPIO.LOW)
    time.sleep(5)


def go_back(spead=50):
    pwm[0].ChangeDutyCycle(spead)
    pwm[1].ChangeDutyCycle(spead)

    GPIO.output(PIN_IN_1_A, GPIO.LOW)  # clockwise
    GPIO.output(PIN_IN_2_A, GPIO.HIGH)

    GPIO.output(PIN_IN_1_B, GPIO.LOW)  # clockwise
    GPIO.output(PIN_IN_2_B, GPIO.HIGH)
    time.sleep(5)


def go_left(spead_A=50,spead_B=50):
    pwm[0].ChangeDutyCycle(spead_A)
    pwm[1].ChangeDutyCycle(spead_B)

    GPIO.output(PIN_IN_1_A, GPIO.LOW)  # clockwise
    GPIO.output(PIN_IN_2_A, GPIO.HIGH)

    GPIO.output(PIN_IN_1_B, GPIO.HIGH)  # clockwise
    GPIO.output(PIN_IN_2_B, GPIO.LOW)
    time.sleep(5)


def go_right(spead_A=50,spead_B=50):
    pwm[0].ChangeDutyCycle(spead_A)
    pwm[1].ChangeDutyCycle(spead_B)

    GPIO.output(PIN_IN_1_A, GPIO.HIGH)  # clockwise
    GPIO.output(PIN_IN_2_A, GPIO.LOW)

    GPIO.output(PIN_IN_1_B, GPIO.LOW)  # clockwise
    GPIO.output(PIN_IN_2_B, GPIO.HIGH)
    time.sleep(5)

def test():
    while True:
        go_forward()
        go_back()
        go_left()
        go_right()

def destroy(pwm):
    GPIO.output(PIN_EN_A, GPIO.LOW)  # motor stop
    GPIO.output(PIN_EN_B, GPIO.LOW)

    pwm[0].stop()
    pwm[1].stop()

    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    pwm = setup()
    try:
        #loop()
        test()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy(pwm)