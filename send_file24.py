from ftplib import FTP, error_perm
import os

ftp = FTP(user="cameri-service@cameri-tech.com", passwd="Vjz]R6pLoUh,",host="ftp.cameri-tech.com")
hmax_dir = "./imgs/comp/"

dirs = [
    {"HISTORY_PATH" : "./HAIFA/max/", "DIR_NAME_FTP":"HAIFA_HISTORY", "HMAX_NAME":"H_latest.json"},
    {"HISTORY_PATH" : "./ASHDOD/max/", "DIR_NAME_FTP":"ASHDOD_HISTORY", "HMAX_NAME":"A_latest.json"}
]
def placeFiles(ftp, path, dir_name, hmax_name):
    hmax_path = os.path.join(hmax_dir, hmax_name)
    ftp.storbinary('STOR ' + hmax_name, open(hmax_path, 'rb'))
    try:
        ftp.mkd(dir_name)
    except error_perm:
       pass
    ftp.cwd(dir_name)
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        ftp.storbinary('STOR ' + name, open(localpath,'rb'))
    ftp.cwd("..")

for directory in dirs:    
    placeFiles(ftp, directory["HISTORY_PATH"], directory["DIR_NAME_FTP"], directory["HMAX_NAME"])

ftp.quit()
