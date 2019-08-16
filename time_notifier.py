import schedule
import subprocess
from subprocess import Popen, PIPE
import datetime
import time
import base64
from io import BytesIO

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def time_noti():
    file_path = 'pic/time.png'
    file_path = resource_path(file_path)
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    img = file_path
    subprocess.Popen(['notify-send', "-i", img, "TIME : "+timestamp])

schedule.every().hour.at(":00").do(time_noti)
schedule.every().hour.at(":30").do(time_noti)
while True:
    schedule.run_pending()
    time.sleep(1)
