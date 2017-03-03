# spibox
## Re-installing the SPi-Box scripts on your Raspberry Pi
Note: These steps are only necessary if you have not got a pre-loaded SPi-Box microSD card from SB Components or if you need to reformat your microSD card for any reason.
Pre-requisites and assumptions
You have a clean install of Raspbian (visit https://www.raspberrypi.org/downloads/)
Your Pi is plugged in, powered on and connected to a monitor, keyboard and mouse, your network
You have downloaded and unzipped the spibox.zip file so that the following directories appear:
/home/pi/spibox
/home/pi/spibox/capture
/home/pi/spibox/capture/archive
You have copied the x2 .Desktop files to /home/pi/Desktop
You are using the default user: pi / raspberry
You know how to open command windows and edit files using nano
## Enable the camera and SSH
Open up a LXTerminal session and enter:
        sudo raspi-config
Use the arrow keys to move down to "5 Enable Camera" and press Enter/Return and select <enable>
Back on the main config page use the arrow keys to move down to "8 Advanced Options" and press Enter/Return
Use the arrow keys to scroll down to "A4 SSH" and press Enter/Return and select <enable>
## Install required packages
Open up a LXTerminal session and type:
        sudo apt-get update
        sudo apt-get install ssmtp
        sudo apt-get install mpack
        sudo apt-get update
## Configure your mail account
At a command prompt enter:
        sudo nano /etc/ssmtp/ssmtp.conf
Change the lines:

        mailhub=[your smtp server or smtp.gmail.com:587 if using a gmail account]
        FromLineOverride=YES
        AuthUser=[yourEmail@address]
        AuthPass=[your email address password]
        UseSTARTTLS=YES
Close the file, saving your changes.
## Turn off the camera's LED
At a command prompt type:
        sudo nano /boot/config.txt
And add the following line to the file:
        disable_camera_led=1
Close the file saving your change.
## Change the "From name" that will appear on emails
At a command prompt enter:
        sudo nano /etc/passwd
Edit the line beginning "root" to be:
        root:x:0:0:SPIBOX:/root:/bin/bash
Close the file saving your change.
## Schedule the spiboxmessenger script to run in the background on startup
At a command prompt enter:
        crontab -e
Add the following lines to the end of the file (for messages and to autostart the camera):
        @reboot sudo python /home/pi/spibox/spiboxmessenger.py &
        @reboot sudo python /home/pi/spibox/spibox.py &

Close the file, saving your change.
For additional information regarding running the SPi-Box scripts please refer to the manual.
Original code from http://sb-components.co.uk/resources/spi-box/code-and-config.html
## My version of spibox code with intruder alert
