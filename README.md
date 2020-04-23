# raspiAndroidTestRig
test your current project on multiple androiod devices connected locally to a raspi

## Goal
after spending too much time deploying and reloading a recent project on my cellphone (chrome browser for android) and a tablet (silk browser for android) I decided I wanted a better way to test projects. After seeing a hardware test rack during a tour of a local Google office I thouguht I might be able to make something similar for myself. 

At the end of the day I hope to able to run my project on a local server on my desktop, load that project on to 2 or more android devices, run a test on each device, and return those results to the desktop. 

## Plan
using gtihub as a sort of engineering journal I will document my progress and keep track of the resources I use to accomplish my goal. 

## Current State
4/23/20
  Currently I am able to use putty on my desktop to load webpages onto a single device attached to the raspi. Next steps are to attach a second device via usb to the raspi and see if I can push the same command to both devices at the same time. I also plan on documenting how I got to here so anyone can also start the same setup. As it stands I'm simply using putty to use the raspi's command line to run ADB to communicate with an old amazon fire tablet. 
