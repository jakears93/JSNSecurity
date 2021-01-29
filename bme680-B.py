#!/usr/bin/env python3

import bme680
import time
import sys
import os
import RPi.GPIO as GPIO
from time import sleep

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
        if sensor.get_sensor_data():
            output = '{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity,)

            if sensor.data.heat_stable:
                print('{0},{1} Ohms'.format(
                output,
                sensor.data.gas_resistance))

                if sensor.data.temperature>=30:
                   #test()
                   #blinkLED()
                   turnon()

                if sensor.data.temperature<=29.9:
                   #test()
                   #blinkLED()
                   turnoff()

            else:
                print(output)

        time.sleep(1)

except KeyboardInterrupt:
    pass