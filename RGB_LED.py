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

def set_color(r, g, b):
    GPIO.output(RED, GPIO.HIGH if r else GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH if g else GPIO.LOW)
    GPIO.output(BLUE, GPIO.HIGH if b else GPIO.LOW)

while True:
    set_color(1, 0, 0)   # Red
    time.sleep(1)
    set_color(0, 1, 0)   # Green
    time.sleep(1)
    set_color(0, 0, 1)   # Blue
    time.sleep(1)
    set_color(1, 1, 0)   # Yellow (Red + Green)
    time.sleep(1)
    set_color(0, 1, 1)   # Cyan (Green + Blue)
    time.sleep(1)
    set_color(1, 0, 1)   # Magenta (Red + Blue)
    time.sleep(1)
    set_color(1, 1, 1)   # White (Red + Green + Blue)
    time.sleep(1)
    led_off()
    time.sleep(0.5)
