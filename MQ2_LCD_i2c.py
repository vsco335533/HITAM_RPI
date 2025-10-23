from gpiozero import DigitalInputDevice, Buzzer
import time
import LCD1602  # Using your provided LCD library file

# Pin setup
MQ2_PIN = 17
BUZZER_PIN = 18

# LCD configuration (same as library)
LCD_ADDR = 0x27
BLEN = 1  # Backlight ON

# Initialize devices
mq2 = DigitalInputDevice(MQ2_PIN)
buzzer = Buzzer(BUZZER_PIN)

# Initialize LCD
LCD1602.init(LCD_ADDR, BLEN)
LCD1602.clear()

print("MQ2 Gas Sensor with LCD1602 and Buzzer Started")

try:
    while True:
        sensor_value = mq2.value  # 0 = gas detected, 1 = no gas
        print("Sensor Value:", sensor_value)

        if sensor_value == 0:
            buzzer.on()
            print("Gas detected! Buzzer ON")
            LCD1602.write(0, 0, "GAS: DETECTED   ")
        else:
            buzzer.off()
            print("No gas detected. Buzzer OFF")
            LCD1602.write(0, 0, "GAS: NONE       ")

        LCD1602.write(0, 1, f"Value: {sensor_value}       ")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

finally:
    buzzer.off()
    LCD1602.clear()
    print("Program ended. LCD cleared.")
