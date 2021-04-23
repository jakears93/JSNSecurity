import os.path
import signal
import sys
import time
import pyrebase
import subprocess
import serial
from serial import Serial

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
    ser = serial.Serial("/dev/ttyACM0",9600)
  
    ser.write('x'.encode())

  #f = os.open("/dev/ttyACM0",os.O_RDWR)
  #f.write(open("sensorReadings.txt","rb").read())
  #f.write(open("sensorReadings.txt").read())
  #f.close()
    print('backup complete') 
    time.sleep(5)
	
# Manage Keyboard Interupt and close program while clearing screen.
def sigint_handler(signal, frame):
    print('Closing Program due to Interupt')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
