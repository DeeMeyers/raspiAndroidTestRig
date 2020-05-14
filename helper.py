import getpass
import socket
import paramiko

try:
    import interactive
except ImportError:
    from . import interactive

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
                print('connected client')
                print('opening local server in browswer with ADB')
                stdin,stdout,stderr = client.exec_command(f'adb shell am start -a android.intent.action.VIEW -d http://{localAdress}:{port}/')
                err = stderr.readlines()
                if err == ['error: no devices/emulators found\n']:
                    print('!!!No Android devices found. Check they are plugged in and in developer mode!!!\n')
                elif err != []:
                    print('!!!There was an error while trying to run adb (Android Debug Bridge)!!!')
                    print('You can install adb by running in the terminal below:\n')
                    print('sudo apt-get install adb')
                chan = client.invoke_shell()
                print(repr(client.get_transport()))
                print("*** opening shell on client ***\n")
                interactive.interactive_shell(chan)
                chan.close()
            except paramiko.ssh_exception.NoValidConnectionsError:
                print("!!!Connection failed!!!")
            except paramiko.ssh_exception.AuthenticationException:
                print("!!!Username or password incorrect!!!")
            client.close()
            print('client closed')


class Helper:   
    def __init__(self):
        print('Please enter the SSH credentials for your RaspberryPi')
        self.user = input("Username: ")
        self.password = getpass.getpass()
        if (self.user == 'pi' and self.password == 'raspberry'):
            print("it looks like you're using the default username and password. It's recomended that you change them to something unique.")
        print("What port is your local server running on?")
        self.port = input("Port: ")
        SSHClient(self.user, self.password, GetAdresses.raspberrypiFind(), GetAdresses.localip(), self.port)


Helper()