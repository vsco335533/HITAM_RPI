from gpiozero import DigitalInputDevice, Buzzer
import time
import LCD1602  # Import your LCD library file

MQ2_PIN = 17
BUZZER_PIN = 18
I2C_ADDR = 0x27
BACKLIGHT = 1

mq2 = DigitalInputDevice(MQ2_PIN)
buzzer = Buzzer(BUZZER_PIN)

LCD1602.init(I2C_ADDR, BACKLIGHT)
LCD1602.clear()

print("MQ2 Gas Sensor with LCD and Buzzer Started")

try:
    while True:
        val = mq2.value  # 0 or 1
        print("Sensor Value:", val)

        if val == 0:
            buzzer.on()
            print("Gas Detected! Buzzer ON")
            LCD1602.write(0, 0, "GAS: DETECTED   ")
        else:
            buzzer.off()
            print("No Gas. Buzzer OFF")
            LCD1602.write(0, 0, "GAS: NONE       ")

        LCD1602.write(0, 1, f"Value: {val}         ")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    buzzer.off()
    LCD1602.clear()
    print("Program ended, LCD cleared.")
