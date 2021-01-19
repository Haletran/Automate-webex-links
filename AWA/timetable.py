import webbrowser
import datetime
import calendar
import schedule
import time
import pyautogui
import os
import pyttsx3
import sys
from beautifultable import BeautifulTable
from subprocess import call


def agenda():
    table = BeautifulTable()
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.append([""])
    table.rows.header = ["M", "M", "T", "T", "T",
                         "W", "W", "W", "W", "TH", "TH", "TH", "F"]
    table.columns.header = ["Cours", "Heures", "Professeurs"]
    print(table)


agenda()
