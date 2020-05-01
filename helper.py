import paramiko
import python-nmap
import getpass

class SSHCreds:
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()
    def __str__(self): 
        return self.user, self.password

