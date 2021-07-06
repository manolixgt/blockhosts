import datetime
import logging
import os, subprocess, sys


logging.basicConfig()
logging.getLogger('activar_hosts').setLevel(logging.DEBUG)

#project dir
PROJ_DIR="D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts"

#current time variable
now = datetime.datetime.now()

#new line var
newline = '\n'

#open file to register task execution
file1 = open(os.path.join(PROJ_DIR, 'log.log'),'a') 
file1.write("blocked at "+str(now)+newline) 
file1.close()


def activar_hosts():

    print('adding domains to host file')
    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname www.youtube.com -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname www.juegosdechicas.com -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname www.juegos.com -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname amongusplay.online -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname www.roblox.com -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()        

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname www.minijuegos.com -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()        

    p = subprocess.Popen(["powershell.exe", 
                "D:\\MyDesktop\\manolix\\biggtronic.com\\app_blockhosts\\AddToHosts.ps1 -Hostname betrayal.io -DesireIP 127.0.0.1"], 
                stdout=sys.stdout)
    p.communicate()        


if __name__ == '__main__':
    activar_hosts()