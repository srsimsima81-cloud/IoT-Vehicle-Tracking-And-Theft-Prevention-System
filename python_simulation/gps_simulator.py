import random
import time

SAFE_LAT = 8.5241
SAFE_LON = 76.9366

def generate_gps():
    lat = SAFE_LAT + random.uniform(-0.05, 0.05)
    lon = SAFE_LON + random.uniform(-0.05, 0.05)
    return round(lat, 6), round(lon, 6)

while True:
    lat, lon = generate_gps()
    print(f"GPS DATA → Latitude: {lat}, Longitude: {lon}")
    time.sleep(2)