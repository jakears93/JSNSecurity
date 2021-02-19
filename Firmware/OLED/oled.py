import os.path
import signal
import sys
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess


# Manage Keyboard Interupt and close program while clearing screen.
def sigint_handler(signal, frame):
    print('Closing Program due to Interupt')
    disp.clear()
    disp.display()
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


# Raspberry Pi pin configuration:
RST = 25
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

while True:

    # File Containing Sensor Data
    fileName = "textFile"

    # Open file reading in lines
    if not os.path.isfile(fileName):
        print("File does not exist.")
    else:
        with open(fileName) as f:
            content = f.readlines()
    # Close file once lines have been read in
    f.close()
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # 
    i = 0
    for line in content:
        draw.text((x, top+int(i)), str(line), font=font, fill=255)
        i = i + 8


    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
