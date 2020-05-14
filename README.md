# raspiAndroidTestRig
test your current project on multiple androiod devices connected locally to a raspi

## Goal
after spending too much time deploying and reloading a recent project on my cellphone (chrome browser for android) and a tablet (silk browser for android) I decided I wanted a better way to test projects. After seeing a hardware test rack during a tour of a local Google office I thouguht I might be able to make something similar for myself. 

At the end of the day I hope to able to run my project on a local server on my desktop, load that project on to 2 or more android devices, run a test on each device, and return those results to the desktop. 

## Plan
using gtihub as a sort of engineering journal I will document my progress and keep track of the resources I use to accomplish my goal. 

## Current State
5/14/20

helper.py can see if adb is installed and tell the user how to install it without leaving the script. it's not perfect but it saves some extra steps in the directions. Getting the script and its dependency packaged up and updating the instructions. My hope is to be able to package up as an .exe and a .deb to make this more system agnostic. Also stumbled across how to add color to error messages and might do that just to make things more legible for the user.  

5/13/20

  helper scripts works consistently and well. I'm going to rely on the user to provide the port information. I was able to find it but my method (using nmap in python) was too slow to be practically. I'm sure there's an easier way to to do this and if I find it I will add it. Next step is to add a check to see if ADB is installed on the raspi and let the user install it while using the script. After that I want to package this all up in it's  own exe or deb package so the user can use the tool standalaone. 

5/6/20

  Made a helper script that can find the ip of a raspi connected to local network, find your local ip adress, and open and close an ssh connection to the raspi. Now i need to have the script send a terminal command which should not be chalenging. The question I am facing now is should I have the user preinstall ADB on the raspi or use the script to check if it exists and install it if it does not exist. Or look into using adb python tools that already exist. Also I need to figure out if I can consistently detect the port a user is running their local server on or if I should ask for that information from the user directly. Considering that I am assuming the user can set up their own local server it may be practical to just ask for the information. 

4/23/20

  Currently I am able to use putty on my desktop to load webpages onto a single device attached to the raspi. Next steps are to attach a second device via usb to the raspi and see if I can push the same command to both devices at the same time. I also plan on documenting how I got to here so anyone can also start the same setup. As it stands I'm simply using putty to use the raspi's command line to run ADB to communicate with an old amazon fire tablet. 
