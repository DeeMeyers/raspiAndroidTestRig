import paramiko
import nmap
import getpass
import socket

class SSHCreds:
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()
    def __str__(self): 
        return self.user, self.password

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    print(ip)
    return ip


class GetAdresses:
    def __init__(self):
        nm = nmap.PortScanner()
        self.computer = {}
        self.raspi = {}
        print('Getting local ip adress:')
        self.ip = get_ip_address()
        print('Getting local address for raspi:')
        try:
            self.raspi = socket.gethostbyname('raspberrypi.local')
            print(self.raspi)
        except: 
            print('raspi not found using raspberrypi.local')

GetAdresses()