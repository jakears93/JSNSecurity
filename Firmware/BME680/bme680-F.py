#!/usr/bin/env python3
#code is based off of http://www.pibits.net/code/arduino-and-bme680-environmental-sensor-example.php 

import bme680
import time
import sys
import os
import RPi.GPIO as GPIO
from time import sleep

import datetime

#Firebase connection
import pyrebase


config = {}
if not os.path.isfile("credentials"):
	print("Credentials does not exist.")
	sys.exit(0)

else: 
	conf_file = open("credentials")

for line in conf_file:
    key, value = line.split()
    config[key] = value

conf_file.close()


print("""read-all.py - Displays temperature, pressure, humidity, and gas.
Press Ctrl+C to exit!
""")
global PIN_18    
global GPIO_Chan_List

PIN_18=27    #GPIO18  -- this LED is driven by GPIO 18.
GPIO_Out_List=[PIN_18]
 
GPIO.setmode(GPIO.BCM)   # use this BCM (Board GPIO number) instead of using Board Pin numbers. 
GPIO.setwarnings(False)   
GPIO.setup(GPIO_Out_List, GPIO.OUT)  #Initialize the Channel List PIN_17 and PIN_18 as outputs. 

def blinkLED():
  # i = 0; 
   #for i in range (0, 2):   # repeat 1000 times. 
      turnon()
      sleep(0.5)  # delay for 0.5 second.
      turnoff()
      sleep(0.5)   # delay for 0.5 second.
     # i+= 1
      return

def turnon():
   #print("Hello from a function")
   GPIO.output(PIN_18, GPIO.HIGH)# Turn ON the LED connected to GPIO 18.
   print ('turn ON the LED')
   return
def test():
   print("if staement good")

def turnoff():
    GPIO.output(PIN_18, GPIO.LOW)    # Turn OFF the LED connected to GPIO 18.
    print ('turn OFF the LED')
    return
 
try:
 
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These calibration data can safely be commented
# out, if desired.

print('Calibration data:')
for name in dir(sensor.calibration_data):

    if not name.startswith('_'):
        value = getattr(sensor.calibration_data, name)

        if isinstance(value, int):
            print('{}: {}'.format(name, value))

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)

    if not name.startswith('_'):
        print('{}: {}'.format(name, value))

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)

print('\n\nPolling:')
try:
    
    while True:
        f = open("sensorReadings.txt", "a+") #out to file around here
        x = datetime.datetime.now()

	#trying to create the title of the file
        #f = open("temp.txt", "a")
        #print("This file displays the Temperture Pressure, Humidty, and Gas resistance in Ohms")
        #f.close()

        if sensor.get_sensor_data():
            print("")
            print(x) #displays date on terminal 
           
            print(x.strftime("%d-%m-%Y %H:%M:%S")) #displays time on terminal 

            #f = open("temp.txt", "a+") #out to file around here
            
            output = 'Temp: {0:.2f} C\nPressure:{1:.2f} hPa \nHumidity: {2:.2f} %RH \n'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity,)
            					
	#add timestamp/date to files aswell

            if sensor.data.heat_stable:
               
                print('{0}Gas:{1:.2f} Ohms'.format(
                output,
                sensor.data.gas_resistance))
                #print('{0} Ohms'.format(sensor.data.gas_resistance))

                 #writes date to file along with Data readings 
                f.write("Date: "+x.strftime("%d-%m-%Y"))
                f.write("\nTime: "+x.strftime("%H:%M:%S") + "\n")
                f.write(output + "" +'Gas: {0:.2f} Ohms'.format(sensor.data.gas_resistance) + "\n")
                f.close() #closes file

                username = "jacob"
                room = "BedRoom"
                storagepath = username+"/"+room+"/sensorReadings.txt"
                firebase = pyrebase.initialize_app(config)              
                storage = firebase.storage()
                fbupload = storage.child(storagepath).put("sensorReadings.txt")

                storage.child("jacob/BedRoom/temp.txt").put("sensorReadings.txt")

               
                if sensor.data.temperature>=30:
                   #x = datetime.datetime.now()  
                   #test()
                   #blinkLED()
                   turnon()

                if sensor.data.temperature<=29.9:
                  #x = datetime.datetime.now() 
                   #test()
                   #blinkLED()
                   turnoff()

            else:
                print(output)
            time.sleep(4) 
    
                      
except KeyboardInterrupt:
    pass
