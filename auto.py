import webbrowser
import datetime
import calendar
import subprocess
import schedule
import time

day = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour
drive = "https://drive.google.com/drive/folders/1Pw3IrUWfMep7SzaudP9mUhFDaL4ttfhf"
url1 = "https://univ-poitiers.webex.com/meet/sanja.boskovic"
url2 = "https://univ-poitiers.webex.com/meet/irina.bondareva"
url3 = "https://univ-poitiers.webex.com/meet/olga.osinovskaya"
url4 = "https://univ-poitiers.webex.com/meet/raluca.nita"
url5 = "https://univ-poitiers.webex.com/meet/andrew.peterson"
url6 = "https://univ-poitiers.webex.com/meet/anita.jorge"
url7 = "https://univ-poitiers.webex.com/meet/nicolas.cormeau"
url8 = "https://univ-poitiers.webex.com/univ-poitiers/j.php?MTID=m5cc9bbc014e051be70b488afa018712a"
url9 = "https://univ-poitiers.webex.com/univ-poitiers/j.php?MTID=m17b56450e300259c9f9b70d4d98d97dc"
url10 = "https://univ-poitiers.webex.com/meet/alix.tubman"
drive = "https://drive.google.com/drive/folders/1Pw3IrUWfMep7SzaudP9mUhFDaL4ttfhf"

"""Instructions to launch WEBEX link"""


def rcr():
    print("Starting Lecture " + rcr.__name__)
    webbrowser.open(url1)


def lrm():
    print("Starting Lecture " + rcr.__name__)
    webbrowser.open(url2)


"""Schedule classes at a certain day and time"""
russe = schedule.every().monday.at("10:00")
informatique = schedule.every().tuesday.at("10:00")
entreprise = schedule.every().wednesday.at("10:00")
anglais = schedule.every().thursday.at("10:00").do(lrm)
francais = schedule.every().saturday.at("21:46").do(rcr)

while True:
    schedule.run_pending()
    time.sleep(1)
