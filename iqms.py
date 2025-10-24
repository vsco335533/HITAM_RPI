import time
import random
import paho.mqtt.client as mqtt
import json

# 🎯 PUT YOUR TOKEN HERE (the one you copied)
THINGSBOARD_HOST = 'thingsboard.cloud'  # Don't change this!
ACCESS_TOKEN = 'PASTE_YOUR_TOKEN_HERE'  # ← PASTE YOUR TOKEN HERE!

# Create MQTT client
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

print("🌈 My Air Quality Monitor Started!")
print("📡 Sending data to the cloud...")

while True:
    # Create pretend sensor data
    air_data = {
        'temperature': round(random.uniform(20, 35), 2),
        'humidity': round(random.uniform(30, 80), 2),
        'pm25': random.randint(10, 150),
        'pm10': random.randint(20, 200),
        'air_quality': random.choice(['Good', 'Moderate', 'Poor'])
    }
    
    # Send to ThingsBoard
    client.publish('v1/devices/me/telemetry', json.dumps(air_data))
    print("✅ Data sent:", air_data)
    
    # Wait 5 seconds
    time.sleep(5)
