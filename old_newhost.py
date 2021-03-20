from apscheduler.schedulers.background import BlockingScheduler
import subprocess, sys
#from elevate import elevate
import logging


logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

def activar_hosts():
#elevate(show_console=False)
    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\AddToHosts.ps1 -Hostname www.youtube.com -DesireIP 127.0.0.1"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\AddToHosts.ps1 -Hostname www.juegosdechicas.com -DesireIP 127.0.0.1"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\AddToHosts.ps1 -Hostname www.juegos.com -DesireIP 127.0.0.1"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\AddToHosts.ps1 -Hostname amongusplay.online -DesireIP 127.0.0.1"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\AddToHosts.ps1 -Hostname web.roblox.com -DesireIP 127.0.0.1"], 
                  stdout=sys.stdout)
    p.communicate()        


def desactivar_hosts():
#elevate(show_console=False)
    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\RemoveFromHosts.ps1 -Hostname www.youtube.com"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\RemoveFromHosts.ps1 -Hostname www.juegosdechicas.com"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\RemoveFromHosts.ps1 -Hostname www.juegos.com"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\RemoveFromHosts.ps1 -Hostname amongusplay.online"], 
                  stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe", 
                  "D:\\MyDesktop\\manolix\\hoststime\\RemoveFromHosts.ps1 -Hostname web.roblox.com"], 
                  stdout=sys.stdout)
    p.communicate() 


sched = BlockingScheduler()

sched.add_job(activar_hosts, 'cron', day_of_week='0-4', hour=8, minute=20,replace_existing=True)
sched.add_job(desactivar_hosts, 'cron', day_of_week='0-4', hour=13, minute=0,replace_existing=True)
sched.start()