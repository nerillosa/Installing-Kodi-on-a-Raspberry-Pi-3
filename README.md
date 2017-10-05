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

Installing the Kodi Media Center on the Raspberry Pi is easy and only requires a couple of commands to install on your system. There will be a few configurations you will have to do after to make it work properly as well as updating Kodi if you would like. Run the following commands one after the other in a terminal window on your Raspberry Pi. 
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

Save the file (Ctrl-x --> Y --> Enter) and exit the nano editor.
Now simply reboot with the command _"sudo reboot now"_ and you have successfully installed Kodi on the Raspberry Pi 3.

**RUN KODI ON STARTUP**

At this point you should see KODI as an installed program under "Sound & Video" in the desktop.
If you want KODI to run on startup instead of the RPI3 booting up on the Desktop you can accomplish this by various ways. The way I did it was to create a launch script to run from the RPI3 startup script. Do the following:
Open a terminal (Ctrl-Alt-T) and create a launch script by typing: _"sudo nano /home/pi/.kodi/system/launch.sh"_ and hitting Enter.
Add the following 2 lines in the nano editor and save the file (Ctrl-x --> Y --> Enter).<br>

<strong>#!/bin/bash<br>
/usr/bin/kodi-standalone</strong><br>

The last line above runs Kodi by calling the command "kodi-standalone", which you can also call from a terminal.
Make the new launch script executable by running the following command:<br>

__sudo chmod 700 /home/pi/.kodi/system/launch.sh__ <br> 

You need to modify the RPI3 startup script next.<br>
You might want to save a copy of this file to your home folder _(sudo cp /home/pi/.config/lxsession/LXDE-pi/autostart ~)_ before modifying it. In case you make a mistake you can always restore the startup file from this copy.
Open the RPI3 startup script by typing: _"sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart"_ and hitting Enter.
Add the following line at the end of the script and save the file. <br>

__/home/pi/.kodi/system/launch.sh__<br>

The startup script always runs on boot-up and the line above will execute last and call the launch.sh script we created in the previous step which will in turn launch Kodi.
Reboot your RPI3 _(sudo reboot now)_. Kodi should launch automatically at the end of boot-up.

## VPN Setup on the RPI3

One of the best ways to secure your data is to use a virtual private network (VPN), which provides greater control of how you're identified online. Simply put, a VPN creates a virtual encrypted "tunnel" between you and a remote server operated by a VPN service. All external internet traffic is routed through this tunnel, so your ISP can't see your data. If the site you're heading to uses HTTPS, your data stays encrypted, too. Best of all, your computer appears to have the IP address of the VPN server, masking your identity. Because you can use a VPN to spoof your location, it's an effective tool for getting around internet censorship. It's also a way to watch region-locked content. If you log in to a VPN server in the UK, you'll be able to watch BBC streams for free.

There are many VPN providers out there. Some better than others. Following advice from a current user, I chose https://www.privateinternetaccess.com/ which charges $3.33 per month if you buy a whole year subscription. The installation instructions are similar for most VPNs as they all implement the OpenVPN suite of virtual private network (VPN) techniques. Once you sign up to your preferred VPN service, they will issue you a userId and a password. They will also give you access to special files (with ovpn extension) which can access specific servers located in different geographical areas.

To install and run VPN in the RPI3, open a terminal and do the following:

* sudo apt-get update
* sudo apt-get install openvpn
* cd /etc/openvpn/
* wget https://www.privateinternetaccess.com/openvpn/openvpn.zip
* sudo unzip openvpn.zip (this will create a lot of ovpn files)
* sudo openvpn "US West.ovpn" 

The last command runs VPN on the "US WEST" server after asking for username and password provided by your VPN service. This means that all your web traffic gets encrypted (and tunnelled through the internet) and goes to and from that server before going out into internet again to fetch the data/webpages requested.
That is all fine and good but the best way to use VPN is to use two servers (one as a backup) and for VPN to run automatically on startup.

**RUN VPN ON STARTUP**

You need to create a password file and to write your username and password on the file. Do the following:

* cd /etc/openvpn
* sudo touch pswfile  (create blank file)
* sudo chmod 700 pswfile (give access only to root, so nobody else can see the password)
* sudo nano pswfile
* Add these two lines with the actual username and passwords: 
  * USERNAME
  * PASSWORD
* Save the file

The next step is to choose the two ovpn files you are going to use and copy/rename them by replacing any spaces with underscores and changing the extesion from ovpn to conf. OpenVPN only recognizes conf files

* sudo cp "US Midwest.ovpn" US_Midwest.conf
* sudo cp "UK London.ovpn" UK_London.conf

The next step is to edit those new conf files and adding the reference to the pswfile in it.
Open each file and look for the line that starts with "auth-user-pass".
Replace that line with "auth-user-pass pswfile".

* sudo nano US_Midwest.conf
* replace "auth-user-pass" with "auth-user-pass pswfile". Omit the double quotes.
* save the file: Ctrl-X -> Y --> Enter

Once you have modified both conf files, you are ready to have openvpn run at boot-up.
In order to run openvpn at startup, you need to add it as a startup service.<br>
Run the following command: _sudo systemctl enable openvpn_ <br>

Edit the openvpn startup file: _sudo nano /etc/init.d/openvpn_

Look for the line:<br>AUTOSTART=ALL<br>
Replace it with:<br> AUTOSTART="US_West.conf US_Silicon_Valley.conf" <br>

The two conf files that you created will be run by openvpn on startup.
save the file: Ctrl-X -> Y --> Enter <br>

You are done. Reboot the RPI3 _(sudo reboot now)_ and VPN should start running on startup under the covers.
The easiest way to check of your VPN is working is to open browser up in the Desktop and going to: <br>
https://www.privateinternetaccess.com/

It will tell you that you are protected and that your webpage is being requested from an IP other than the IP that your ISP provider assigns to you:





















