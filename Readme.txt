

This project follows what was done here : 
http://www.learningaboutelectronics.com/Articles/MCP4131-digital-potentiometer-circuit.php
It has a very concise and good explanation of SPI serial bus communication.

The ultimate objective of this project is to use the digital pot to mute and change the volume of a speaker attached to an Epson projector. 
This is basically the proof of concept of the functionality. Very impressed with the simplicity and power of the serial SPI bus. 

The main differences between this project and the url referenced above is that I am using a Raspberry Pi instead of an Arduino.
I am also programming in Python as opposed to C. Another difference is that since my digital pot is rated at 100k, 
I used a transistor in the output wired as a voltage follower to avoid non-linear behavior due to impedance mismatching. 
Since there is a threshold of voltage that needs to be overcome (~2.4v -> 1.8v of Led plus 0.6v of transistor) 
before the LED starts lighting, the program loops between the values of 60-127 instead of the full range of 0-127.

Follow the instructions to install spidev here: http://tightdev.net/SpiDev_Doc.pdf

You can see a demo of this project at : https://www.youtube.com/watch?v=p5YHSxK8M4E

