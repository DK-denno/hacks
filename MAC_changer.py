#!/usr/bin/env python
import subprocess
import optparse

parser=optparse.OptionParser()

parser.add_option("-i","--interface",dest="option",help="Inteface whose MAC_address is to be changed")
parser.add_option("-m","--mac",dest="value",help="MAC address to change to")
(options,arguments) = parser.parse_args()



option = input('Interface > ')
value = input('New MAC > ')
if option=="wlan0"or "etho" and type(value)==int and len(value)==5 : 

    print('[+] loading,please wait')
    subprocess.call("ifconfig " + option + " down",shell=True)
    subprocess.call("ifconfig " + option + " hw ether " + value,shell=True)
    subprocess.call("ifconfig " + option + " up",shell=True)
    print(' changed '+option+' to '+value)
else:
    print("Interface and New MAC address needed ")

#using the above code in list form is more secure against hackers

# subprocess.call(["ifconfig",option,"down"])
# subprocess.call(["ifconfig",option,"hw","ether",value])
# subprocess.call(["ifconfig",option,"up"])
