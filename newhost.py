import logging
import os
import subprocess, sys
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    #scheduler.add_jobstore('mongodb', collection='example_jobs', host='192.168.0.108', port=27017)

    def activar_hosts():
#elevate(show_console=False)
        print("ejecuntando activate")
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
        print("ejecuntando deactivate")
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

    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        scheduler.remove_all_jobs()

    

    scheduler.add_job(activar_hosts, 'cron', day_of_week='0-4', hour=8, minute=20,id="act_host",replace_existing=True, misfire_grace_time=1000)
    scheduler.add_job(desactivar_hosts, 'cron', day_of_week='0-4', hour=13, minute=0,id="deact_host",replace_existing=True, misfire_grace_time=1000)
    print('To clear the alarms, run this example with the --clear argument.')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    scheduler.start()