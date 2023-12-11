import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
servo_pin = 18
sw1_pin = 16
sw2_pin = 20
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(sw1_pin, GPIO.IN)
GPIO.setup(sw2_pin, GPIO.IN)

servo = GPIO.PWM(servo_pin,50)
servo.start(0)
servo_deg = 0
servo_min_duty = 3
servo_max_duty =12

def set_servo_degree(degree):
	duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180.0)
	servo.ChangeDutyCycle(duty)

try:
	while 1:
		if GPIO.input(sw1_pin):
			servo_deg += 10
			if servo_deg > 180:
				servo_deg = 180
			set_servo_degree(servo_deg)
			print(servo_deg)
			time.sleep(1)
		elif GPIO.input(sw2_pin):
			servo_deg -= 10
			if servo_deg < 0:
				servo_deg = 0
			set_servo_degree(servo_deg)
			print(servo_deg)
			time.sleep(1)
			
finally : GPIO.cleanup
