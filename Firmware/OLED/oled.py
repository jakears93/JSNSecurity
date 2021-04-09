from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

import os.path
import signal
import sys
import time
import pyrebase
import subprocess

#Pyrebase Config from file
config = {}
conf_file = open("credentials")
for line in conf_file:
    key, value = line.split()
    config[key] = value


# Manage Keyboard Interupt and close program while clearing screen.
def sigint_handler(signal, frame):
    print('Closing Program due to Interupt')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


serial = spi(device=0, port=0)
device = ssd1309(serial)

# Initialize Pyrebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()



i = 1
c = 0
hasDrawn = False

while True:
    # Download temperature data
    storage.child("jacob/BedRoom/sensorReadings.txt").download("sensorReadings.txt")
    
    # File Containing Sensor Data
    fileName = "sensorReadings.txt"

    # Open file reading in lines
    if not os.path.isfile(fileName):
        print("File does not exist.")
    else:
        with open(fileName) as f:
            content = f.readlines()
    #Close file once lines have been read in
    f.close()

    hasDrawn = False
    with canvas(device) as draw:
            print("Data Entry:",i)
            for line in content:
                if c>=((i-1)*6) and c<(i*6):
                    print("Drawing Line:",c)
                    hasDrawn = True
                    draw.text((1, (c%6)*10), line, fill="white")
                c+=1
            if (hasDrawn == True):
                i += 1
    time.sleep(5)
    c = 0
