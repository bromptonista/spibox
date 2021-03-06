#!/bin/sh
# spiboxmessenger.py
# look for files in the capture directory then process them
import os
import subprocess
import ConfigParser
import time

class spiboxMessenger:

    def init(self):
        spiboxConf = ConfigParser.ConfigParser()
        spiboxConf.read('/home/pi/spibox/spibox.conf')
        self.emailsubject = spiboxConf.get('email','emailsubject')
        self.emailrecipient = spiboxConf.get('email','emailrecipient')
        self.emailon = spiboxConf.get('email','on')

    def getFileList(self):
       self.filelist = []
       i = 0
       for file in os.listdir("/home/pi/spibox/capture"):
          if file.endswith(".jpg"):
             self.filelist.extend([None])
             self.filelist[i] = file
             i = i+1

    def moveFiles(self):
        for filename in self.filelist:
            print('moving'+filename)
            pid = subprocess.call(['sudo','mv','/home/pi/spibox/capture/'+filename,'/home/pi/spibox/capture/archive/'])

    def emailFiles(self):
        print(len(self.filelist))
        for filename in self.filelist:
            print('emailing'+filename)
            cmd = 'mpack -s "'+self.emailsubject+'" -c image/jpeg /home/pi/spibox/capture/'+filename + ' '+self.emailrecipient
            pid = subprocess.call(cmd, shell=True)


messenger = spiboxMessenger()
while True:
   time.sleep(10)
   messenger.init()
   messenger.getFileList()
   if messenger.emailon == "YES":
      messenger.emailFiles()
   messenger.moveFiles()
