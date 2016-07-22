#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 0
try:
	while True:
		for num in range(0,127):
        		frame = bytearray()
        		frame.append(0)
        		frame.append(num)
			resp = spi.xfer2(frame)
			time.sleep(0.05) # sleep for 0.05 seconds
		#end for
        
		time.sleep(0.5) # sleep for 0.5 seconds

        	for num in range(127,0, -1):
                	frame = bytearray()
                	frame.append(0)
                	frame.append(num)
                	resp = spi.xfer2(frame)
                	time.sleep(0.05) # sleep for 0.05 seconds
        	#end for
	#end While

except KeyboardInterrupt: # Ctrl+C pressed, so.
	spi.close() # . close the port before exit
#end try
