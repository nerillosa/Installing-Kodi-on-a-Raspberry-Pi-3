#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 0
frame = [0, 0] # initialize list to be sent to spi bus

try:
	while True:
		for num in range(45,127):
        		frame[1]=num
			resp = spi.xfer2(frame)
			time.sleep(0.05) # sleep for 0.1 seconds
		#end for
        
		time.sleep(0.5) # sleep for 0.5 seconds

        	for num in range(127,45, -1):
        		frame[1]=num
                	resp = spi.xfer2(frame)
                	time.sleep(0.05) # sleep for 0.1 seconds
        	#end for
	#end While

except KeyboardInterrupt: # Ctrl+C pressed, so.
	spi.close() # . close the port before exit
#end try
