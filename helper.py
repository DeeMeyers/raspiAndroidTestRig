import paramiko
import getpass
import socket

class SSHCreds:
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    print(ip)
    return ip


class GetAdresses:
    def __init__(self):
        self.computer = ''
        self.raspi = ''

    def localip():
            print('Getting local ip adress:')
            self.computer = get_ip_address()
            print(self.computer)
            return self.computer
    def raspberrypi():
            print('Getting local address for raspi:')
            try:
                self.raspi = socket.gethostbyname('raspberrypi.local')
                print(self.raspi)
                return self.raspi
            except: 
                print('raspi not found using raspberrypi.local')
                exit()


class SSHClient:
    def __init__(self, user, password, raspiAdress, localAdress):
        pass


class Helper:
    def __init__(self):
        SSHClient(SSHCreds().user, SSHCreds().password, GetAdresses.raspberrypi(), GetAdresses.localip())

Helper()