import paramiko
import getpass
import socket

class GetAdresses:
    def localip():
            print('Getting local ip adress:')
            temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp.connect(("8.8.8.8", 80))
            computer = temp.getsockname()[0]
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
    def __init__(self, user, psword, raspiAdress, localAdress, port):
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(raspiAdress, username=user, password=psword)
                print('i connect')
                stdin,stdout,stderr = client.exec_command(f'adb shell am start -a android.intent.action.VIEW -d http://{localAdress}:{port}/')
            except paramiko.ssh_exception.NoValidConnectionsError:
                print("!!!Connection failed!!!")
            except paramiko.ssh_exception.AuthenticationException:
                print("!!!Username or password incorrect!!!")
            client.close()
            print('i close')


class Helper:   
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()
        print("What port is your local server running on?")
        self.port = input("Port: ")
        SSHClient(self.user, self.password, GetAdresses.raspberrypiFind(), GetAdresses.localip(), self.port)


Helper()