/*
  SD card file dump

  This example shows how to read a file from the SD card using the
  SD library and send it over the serial port.
The circuit:
   SD card attached to SPI bus as follows:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 4 (for MKRZero SD: SDCARD_SS_PIN)

  created  22 December 2010
  by Limor Fried
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.
*/


#include <SPI.h>
#include <SD.h>

File dFile; 

const int chipSelect = 4;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.setTimeout(5000);

  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
}
void loop() {
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
String str = Serial.readString();                     
 
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.                       
  // will write a new file if doesnt exist
  //File dataFile = SD.open("sensor2.txt",FILE_WRITE);
  // reads a file if it exists                         
  File dFile  = SD.open("sensor2.txt",FILE_READ);
  // if the file is available, write to it:
  if (dFile) {
    while (dFile.available()) {
      Serial.write(dFile.read());
    }
    dFile.close();
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening sensor2.txt");
   }                          
   exit(0);    
} 
                                     
