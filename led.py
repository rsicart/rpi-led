#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

class Led:

	def __init__(self):
		# make sure gpio pins are ready
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		# setup led pin
		self.led = 21
		GPIO.setup(self.led, GPIO.OUT)

	def on(self):
		# value 1 represents "on" and 0 "off"
		print('Turn led on')
		GPIO.output(self.led, 1)
		time.sleep(1)

	def off(self):
		print('Turn led off')
		GPIO.output(self.led, 0)
		time.sleep(1)


if __name__ == '__main__':
	try:
		led = Led()
		led.on()
		led.off()
		led.on()
		led.off()
	except:
		pass
	finally:
		print('Finally Cleaning up...')
		GPIO.cleanup()
