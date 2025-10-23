from gpiozero import DigitalInputDevice, Buzzer
import time

mq2 = DigitalInputDevice(17)  # MQ2 sensor pin
buzzer = Buzzer(18)           # Buzzer pin

while True:
    if mq2.value == 0:        # Gas detected
        buzzer.on()
        print("Gas detected! Buzzer ON")
    else:
        buzzer.off()
        print("No gas. Buzzer OFF")
    time.sleep(1)
