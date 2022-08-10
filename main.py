import os             
import pyautogui
import time
from time import sleep
from datetime import datetime

import login, logout

windowsUser = "hassan.aftab" # <-- Enter your Windows User Name here

teamsPath = "C:/Users/{}/AppData/Local/Microsoft/Teams/current/Teams.exe".format(windowsUser)

os.startfile(teamsPath)