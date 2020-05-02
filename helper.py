import paramiko
import getpass
import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    return ip


class GetAdresses:

    def localip():
            print('Getting local ip adress:')
            computer = get_ip_address()
            print(computer)
            return computer
    def raspberrypiFind():
            print('Getting local address for raspi:')
            try:
                pi = socket.gethostbyname('raspberrypi.local')
                print(pi)
                return pi
            except: 
                print('raspi not found using raspberrypi.local')
                exit()


class SSHClient:
    def __init__(self, user, password, raspiAdress, localAdress):
        pass


class Helper:   
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()
        SSHClient(self.user, self.password, GetAdresses.raspberrypiFind(), GetAdresses.localip())

Helper()