# Detailed procedure I used to install Kodi on my new RPI3. 
The RPI3 is one of the newest versions of RPI. It has support for internal WiFi and bluetooth which the previous version B+ did not have.
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
There are several Operating Systems of choice, which you can select by running the NOOBS operating system installation manager. I chose to load the Raspberry Pi desktop OS directly. The desktop OS allows you easy configuration of WiFi, Bluetooth, general settings, as well as access to different programs (browser) and utilities. <br> Go to https://www.raspberrypi.org/downloads/ and click on the RASPBERRY PI DESKTOP link and then on the "Download ISO" link. This will download the OS image onto your computer. <br>
![ISO download link](images/iso_download.JPG?raw=true "ISO download") <br>
As of this writing the ISO file name is: rpd_x86-2017-06-23/2017-06-22-rpd-x86-jessie.iso<br>
Don't be confused with the x86 in the name. The RPI3 is a 64 bit computer running a 32 bit operating system.
You will need to write this image file to the blank SD card.

__WRITING AN ISO IMAGE TO THE SD CARD__ <br>

You will need to use an ISO image writing tool to install the image you have downloaded on your SD card. Once you write this binary image to the SD card and insert it in the Raspberry Pi, the Pi will boot up to the desktop operating system.
There are many Image writing programs out there. I chose Etcher which is free and can be downloaded at https://etcher.io/ <br>
Etcher is a graphical SD card writing tool that works on Mac OS, Linux and Windows, and is the easiest option for most users. If your computer does not have an SD card port, you will need to acquire a SD card USB adapter like this one: https://www.amazon.com/gp/product/B006T9B6R2/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1 <br>

To write your image with Etcher:
* Download Etcher and install it.
* Connect an SD card reader with the SD card inside.
* Open Etcher and select from your hard drive the Raspberry Pi iso image you downloaded previously.
* Select the SD card you wish to write your image to.
* Review your selections and click 'Flash!' to begin writing data to the SD card.

__BOOTING UP THE RASPBERRY PI FOR THE FIRST TIME__ <br>

Once the ISO image file has been written to the SD card, it is time to boot up the RPI3. 
Do the following in order, plugging in the power last. 
* Insert the micro SD card into the memory card slot of the RPI3.
* Plug in a HDMI cable between the RPI3 and your TV and turn on the TV.
* Plug in a USB mouse and keyboard to your RPI3.
* Plug in the power supply between the your RPI3 and a power outlet.

The RPI3 should boot up and you should see a blank linux desktop. The first thing you need to do before installing Kodi is to configure basic settings like your timezone, the keyboard type, WiFi, password, and the language to use. Hover your mouse over the raspberry icon on the top left of the screen and select "Preferences" from the ensuing dropdown and then "Raspberry Pi Configuration":
<br><br>
<img src="https://github.com/nerillosa/Installing-Kodi-on-a-Raspberry-Pi-3/blob/master/images/linux_desktop.jpg" width="750">

You should see the following screen. For security purposes you should always change the default password which is normally "raspberry". Click on "Change Password" button and change the password to something of your choice. 
<br><br>
<img src="https://github.com/nerillosa/Installing-Kodi-on-a-Raspberry-Pi-3/blob/master/images/password.jpg" width="500">

Click on "Localization" and configure Locale, Timezone, Keyboard, and WiFi country to your respective preferences. 
In my case I have:

* Locale: Language-en(English), Country-US(United States), Character Set- UTF-8
* Timezone: Area-America, Location-Phoenix
* Keyboard: Country-United States, Variant-English(US, international)
* WiFi Country: US United States

Last but not least, you need to connect the RPI3 to your internal home WiFi network. Make sure you have your WiFi password handy and click on the WiFi icon at the top right of the RPI3 screen and choose your WiFi SSID from the list that appears. It will ask for the password to connect. Enter your WiFi password and you are connected to the Internet.

__For advanced users:__ <br>
To connect to your RPI3 remotely from any other computer on your same home WiFi network using SSH (putty or bitvise for windows), you will need to enable SSH.
To do this go to the "Raspberry Pi Configuration" popup again and instead of clicking on "Localization", click on "Interfaces". Hit the enable radio button for the SSH entry and then click on "Ok". You can now connect to your RPI3 using the IP address that your router has assigned to your RPI3: pi@192.168.0.8 in my case. An easy way to find out the IP address that your RPI3 has is to open a terminal (click on the black terminal icon on the top of the screen) and type ifconfig.
You should see your IP address next to the wlan0 entry as inet: 192.168.0.8  (in my case):
<br><br>
<img src="https://github.com/nerillosa/Installing-Kodi-on-a-Raspberry-Pi-3/blob/master/images/terminal.jpg" width="500">


## Installing Kodi on a RPI3 running the Raspbian desktop OS

Installing the Kodi Media Center on the Raspberry Pi is super easy and only requires one command to install it on your system. There will be a few configurations you will have to do after to make it work properly as well as updating Kodi if you would like. Run the following commands one after the other in a terminal window on your Raspberry Pi. 
<p align="center"> <strong>sudo apt-get update<br>sudo apt-get install kodi</strong> </p>

That’s basically it. This will grab the latest stable compiled version of Kodi built for Raspbian. It grabs the files from the official Raspbian Repositories. The download should be around 200MB so it will take a while. It will also download some dependencies and install them.

**IMPORTANT RASPBERRY PI BOOT CONFIGS FOR KODI**

The following steps are crucial and need to be done to get proper playback on the Raspberry Pi. If you are having Kodi performance issues or Kodi is only playing audio and the video is black then it could be because of these settings in the Raspberry Pi’s /boot/config.txt file. Type the following command to edit the Raspberry Pi’s configuration file.

<p align="center"> <strong>sudo nano /boot/config.txt</strong> </p>

This file contains some important configurations for our Raspberry Pi. Scroll all the way to the bottom of the file and create 2 new settings. One for GPU_MEM and one for Start_X.

GPU_MEM is the GPU memory in megabytes. This value sets the memory split between the CPU and GPU. The CPU will get the remainer of the unused memory. We will be setting our value to 256 MB.
Start_X will allow codec’s to be enable so that you can playback video’s in Kodi.
Let’s go to the bottom of the configuration file and add the following 2 lines:

<strong>gpu_mem=256 <br>start_x=1</strong>

Now simply reboot with "sudo reboot now" and you have successfully installed Kodi on the Raspberry Pi 3.



