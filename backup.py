import os
import shutil
from datetime import datetime,timedelta
#Create a backup_folder

backup_dir = "Backup"
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

# Calculate time threshold (7 days ago)
now = datetime.now()
cut_off = now - timedelta(days=7)

try:
 for file in os.listdir():
    if os.path.isfile(file):
        mod_time = datetime.fromtimestamp(os.path.getmtime(file))
        if mod_time>cut_off:
            shutil.copy(file,backup_dir)
            print(f"Backup successfully {file}")
 print("SUcess")
except Exception as e:
   print(f"Error {e} ")

