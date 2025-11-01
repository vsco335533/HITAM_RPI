import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 17
GREEN = 27
BLUE = 22

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def led_off():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)

while True:
    GPIO.output(RED, GPIO.HIGH)     # Red light
    time.sleep(3)
    led_off()
    
    GPIO.output(RED, GPIO.HIGH)     # Red + Green = Yellow
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    led_off()
    
    GPIO.output(GREEN, GPIO.HIGH)   # Green light
    time.sleep(3)
    led_off()
    
    GPIO.output(BLUE, GPIO.HIGH)    # Blue for pedestrian (optional)
    time.sleep(1)
    led_off()









https://deploy-formpage.vercel.app/