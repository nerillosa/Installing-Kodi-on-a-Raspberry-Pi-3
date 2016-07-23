#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 0
frame = bytearray([0,0]) # The first byte is the control byte and in this application is always \x00

#the following while loop will assign values to the second byte of the frame sent to SPI bus
try:
	while True:
		for num in range(60,127):
        		frame[1] = num
			resp = spi.xfer2(frame)
			time.sleep(0.05) # sleep for 0.05 seconds (1/20)
		#end for
        
		time.sleep(0.5) # sleep for 0.5 seconds

        	for num in range(127,60, -1):
        		frame[1] = num
                	resp = spi.xfer2(frame)
                	time.sleep(0.05) # sleep for 0.05 seconds
        	#end for
	#end While

except KeyboardInterrupt: # Ctrl+C pressed, so.
	spi.close() # . close the port before exit
#end try
