This project follows what was done here : http://www.learningaboutelectronics.com/Articles/MCP4131-digital-potentiometer-circuit.php.
The main differences being that I am using a Raspberry Pi instead of an Arduino and I am programming in Python as opposed to C.
Another difference is that since my digital pot is rated at 100k, I used a transistor in the output wired as a voltage follower. 
Since there is a threshold of voltage that needs to be overcome before the LED starts lighting, the program loops between the values 
of 45 and 127 and back.

Follow the instructions to install spidev here: http://tightdev.net/SpiDev_Doc.pdf

