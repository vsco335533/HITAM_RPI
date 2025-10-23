# File: led_blink.py
import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# Setup pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def turn_off_leds():
    """Turn off all LEDs"""
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def blink_led(pin, duration=1):
    """Blink a single LED"""
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(duration)

def rgb_sequence():
    """Run RGB color sequence"""
    try:
        while True:
            # Red
            GPIO.output(RED_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # Green
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # Blue
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # Yellow (Red + Green)
            GPIO.output(RED_PIN, GPIO.HIGH)
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # Cyan (Green + Blue)
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # Magenta (Red + Blue)
            GPIO.output(RED_PIN, GPIO.HIGH)
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
            # White (All colors)
            GPIO.output(RED_PIN, GPIO.HIGH)
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            time.sleep(1)
            turn_off_leds()
            
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        turn_off_leds()
        GPIO.cleanup()

if __name__ == "__main__":
    print("RGB LED Control Started")
    print("Press Ctrl+C to stop")
    rgb_sequence()
