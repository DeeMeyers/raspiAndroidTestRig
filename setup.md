# Setup Guide
This will take you through a headless setup proccess. Headless means that you are not hooking your RaspberyPi up to an external monitor and keyboard.
Considering that many of the tools we will ultimately used also let us set This guide assumes you are using a Windows PC but all of the provided
resources have instructions and software for both mac and linux (debian mainly but there are alternatives for others distros as well)

## Required Hardware
- a raspberrypi 
- a way to connect your raspberrypi to your home network (hardwired, using the built in wifi adapter, or an external wifi adapter)
- a microSD card 8 gigs or larger (you will lose any data stored on this card during setup)
- a laptop
- an android phone or tablet
- a USB cable to connect your device to the raspberrypi
- that's it!

## Before You Start

This project is not intended for use on a network you don't control or for anything other than personal use. If your router is still using the default username and password or if you're unsure I would highly recomend finding out and changing it before starting. 

## Preparing Your RaspberryPi

For this project we are going to use the Raspbian OS. Raspian is a Debian based unix operating system built specifically for the raspberrypi.
I chose it because it has some really great doccumention and a lot support from creaters and community alike. 

I highly recomend downloading the Raspberry Pi Imager for Windows here:

[https://www.raspberrypi.org/downloads/](https://www.raspberrypi.org/downloads/)
The imager will walk you through flashing your microSD card and will download the RaspbianOS image for you as well.

### Adding Configuration Files
Once you are finshed flashing your SD card next we have to enable SSH. SSH is what allows us to connect to the raspi over our nextwork. It is 
by default turned off. To enable it all we need to do is add a blank file titled `ssh` into the boot folder. 

If you are unable to connect to you network via ethernet you will also need to configure in advance aswell. Just follow the directions laid out here:
[https://www.raspberrypi.org/documentation/configuration/wireless/headless.md](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md)

A blank shh file and a copy of the template wpasupplicant.conf file are available in the root of this project. 

## Setting up your PC 

wip

