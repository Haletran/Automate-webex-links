import webbrowser
import datetime
import calendar
import subprocess
import schedule
import time

"""Add your webex link"""
url1 = "YOUR WEBEX LINK ..."
url2 = "YOUR WEBEX LINK ..."


"""Instructions to launch WEBEX link"""


def rcr():
    print("Starting Lecture " + rcr.__name__)
    webbrowser.open(url1)


def lrm():
    print("Starting Lecture " + rcr.__name__)
    webbrowser.open(url2)


"""Schedule classes at a certain day and time"""
russe = schedule.every().monday.at("10:00").do(rcr)
informatique = schedule.every().tuesday.at("10:00").do(lrm)
entreprise = schedule.every().wednesday.at("10:00").do()
anglais = schedule.every().thursday.at("10:00").do()
francais = schedule.every().saturday.at("10:00").do()


while True:
    schedule.run_pending()
    time.sleep(1)

