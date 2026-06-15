import random
import csv
import time
from datetime import datetime

SAFE_LAT = 8.5241
SAFE_LON = 76.9366
RADIUS = 0.03

def generate_location():
    lat = SAFE_LAT + random.uniform(-0.06, 0.06)
    lon = SAFE_LON + random.uniform(-0.06, 0.06)
    return lat, lon

def geofence(lat, lon):
    return abs(lat - SAFE_LAT) < RADIUS and abs(lon - SAFE_LON) < RADIUS

def maps_url(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"

def log(lat, lon, status, alert):
    with open("data/log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), lat, lon, status, alert])

print("🚗 Vehicle Tracking System Started...\n")

while True:
    lat, lon = generate_location()
    inside = geofence(lat, lon)

    if inside:
        status = "SAFE"
        alert = "NONE"
    else:
        status = "THEFT ALERT"
        alert = "GEOFENCE BREACH"

    print("Location:", lat, lon)
    print("Status:", status)
    print("Alert:", alert)
    print("Map:", maps_url(lat, lon))
    print("-"*40)

    log(lat, lon, status, alert)
    time.sleep(3)