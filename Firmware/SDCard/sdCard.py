import os.path
import signal
import sys
import time
import pyrebase
import subprocess

#Import Pyrebase Config from file
config = {}
if not os.path.isfile("../credentials"):
    print("Credentials does not exist.")
    sys.exit(0)
else:
    conf_file = open("../credentials")

for line in conf_file:
    key, value = line.split()
    config[key] = value

conf_file.close()

# Initialize Pyrebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Download Sensor Data
while True:
    # Download temperature data
    storage.child("jacob/BedRoom/sensorReadings.txt").download("sensorReadings.txt")
    time.sleep(30)
	
# Manage Keyboard Interupt and close program while clearing screen.
def sigint_handler(signal, frame):
    print('Closing Program due to Interupt')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
