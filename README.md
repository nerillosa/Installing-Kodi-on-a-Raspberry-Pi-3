# I will detail what I used to install Kodi on my new RPI3. 
The RPI3 is one of the newest versions of RPI. It has support for internal wifi and bluetooth which the previous version B+ did not have.
Kodi provides access to streaming media content, including videos and music. It allows users to play and view most videos, music, podcasts, and other digital media files from local and network storage media and the internet. Kodi also accesses content over the internet using various “add-ons” created by members of the Kodi open source community. Therefore, add-ons do not come “out of the box” with any official version of Kodi.<br>
Things you will need:
* A raspberry pi 3 kit. A kit, at a minimum should contain the RPI3 itself, a case, a 2.5A power supply, and the heatsinks for the two processors.
I bought this one from amazon: https://www.amazon.com/gp/product/B01D92SSX6/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1
* Some kits come with preloaded SD memory cards. I bought a empty 32 G card and loaded the OS from the internet -- as I will explain later. The SD card should be a good quality card. I bought this one: https://www.amazon.com/gp/product/B010Q57T02/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1
* For initial setup you will need a USB keyboard and mouse. After setup, you can control Kodi from your smartphone using free apps like Kodi Remote on Android which will run on your internal WiFi network.
* Finally, you will need to have an HDMI TV (plus HDMI cable) and a Wifi home network up and running to which the RPI3 can connect in order to download videos and music and stream live to your TV.
## This is how a connected RPI3 inside a clear case looks like:
The top two connectors are the HDMI cable to TV and the USB power supply cord. The two connectors on the side (one on top of the other) are the USB keyboard and mouse. 
<br><br>
<img src="https://github.com/nerillosa/Installing-Kodi-on-a-Raspberry-Pi-3/blob/master/images/raspberrypi_connected.jpg" width="500">
## Loading of the Raspbian desktop Operating System (OS) on the SD card
There are several Operating Systems of choice, which you can choose by running the NOOBS operating system installation manager. I chose to load the Raspberry Pi desktop OS directly. The desktop OS allows you easy configuration of WiFi, Bluetooth, general settings, as well as access to different programs (browser) and utilities. Go to https://www.raspberrypi.org/downloads/ and click on the RASPBERRY PI DESKTOP link and then on the "Download ISO" link. This will download the OS image onto your computer. <br>
![ISO download link](images/iso_download.JPG?raw=true "ISO download") <br>
As of this writing the ISO file name is: rpd_x86-2017-06-23/2017-06-22-rpd-x86-jessie.iso<br>
Don't be confused with the x86 in the name. The RPI3 is a 64 bit computer running a 32 bit operating system.
You will need to write this image file to the blank SD card.
_WRITING AN IMAGE TO THE SD CARD_ <br>

You will need to use an image writing tool to install the image you have downloaded on your SD card.
There are many Image writing programs out there. I chose Etcher which is free and can be downloaded at https://etcher.io/ <br>
Etcher is a graphical SD card writing tool that works on Mac OS, Linux and Windows, and is the easiest option for most users. To write your image with Etcher:
* Download Etcher and install it.
* Connect an SD card reader with the SD card inside.
* Open Etcher and select from your hard drive the Raspberry Pi iso image you downloaded previously.
* Select the SD card you wish to write your image to.
* Review your selections and click 'Flash!' to begin writing data to the SD card.

## More to come, work in progress.....
