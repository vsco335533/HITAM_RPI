import smbus
import time
import RPi.GPIO as GPIO

# Setup LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Red LED for X-axis
GPIO.setup(27, GPIO.OUT)  # Green LED for Y-axis
GPIO.setup(22, GPIO.OUT)  # Blue LED for Z-axis

# MPU6050 addresses
Device_Address = 0x68
PWR_MGMT_1 = 0x6B

# Create I2C bus
bus = smbus.SMBus(1)

# Wake up MPU6050
bus.write_byte_data(Device_Address, PWR_MGMT_1, 0)

def read_sensor(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

print("MPU6050 is ready! Tilt the sensor to light up LEDs!")

try:
    while True:
        # Read accelerometer values
        acc_x = read_sensor(0x3B) / 16384.0
        acc_y = read_sensor(0x3D) / 16384.0
        acc_z = read_sensor(0x3F) / 16384.0
        
        # Control LEDs based on tilt
        # Red LED lights when tilted forward/backward (X-axis)
        if abs(acc_x) > 0.5:
            GPIO.output(17, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.LOW)
        
        # Green LED lights when tilted left/right (Y-axis)
        if abs(acc_y) > 0.5:
            GPIO.output(27, GPIO.HIGH)
        else:
            GPIO.output(27, GPIO.LOW)
        
        # Blue LED lights when moved up/down (Z-axis)
        if abs(acc_z - 1) > 0.3:  # Z is normally 1g (gravity)
            GPIO.output(22, GPIO.HIGH)
        else:
            GPIO.output(22, GPIO.LOW)
        
        print(f"X: {acc_x:.2f}g, Y: {acc_y:.2f}g, Z: {acc_z:.2f}g")
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Goodbye!")
