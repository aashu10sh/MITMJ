def makeInstall():
  rootval = os.getuid()
    if  str(rootval) != "0":
        print("Please use this script as root, Permission Denied")
        exit
    else:
        print("Installing necessary modules via pip3,make sure you have pip3 installed")
        try:
          subprocess.call(["pip3","install","scapy","scapy.layers","argparse","colorama"])
         except:
          print("Something went wrong, please manually install all pacakges")

  

try:
  import os
  import scapy.all
  import scapt.layers
  import argparse
  import optparse
  import time
  import sys
  import subprocess
  print("Everything seems to be already installed")
except ModuleNotFoundError:
  makeInstall()
