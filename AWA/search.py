import webbrowser
import datetime
import calendar
import schedule
import time
import pyautogui
import os
import pyttsx3
import random
import sys
from beautifultable import BeautifulTable
from subprocess import call

"""Add your webex link - You can add as many as you want"""
url1 = "https://univ-poitiers.webex.com/meet/nada.kawach"
url2 = "https://univ-poitiers.webex.com/meet/mohamed.mustapha.deabes"
url3 = "https://univ-poitiers.webex.com/meet/olga.osinovskaya"
url4 = "https://univ-poitiers.webex.com/meet/nicolas.cormeau"
url5 = "https://univ-poitiers.webex.com/meet/jean.christophe.dourdet"
url6 = "https://univ-poitiers.webex.com/meet/anita.jorge"
url7 = "https://univ-poitiers.webex.com/meet/jessica.robert"
url8 = "https://univ-poitiers.webex.com/meet/charlotte.krauss"
url9 = "https://univ-poitiers.webex.com/meet/irina.bondareva"
url10 = "https://univ-poitiers.webex.com/meet/ariane.le.moing"
url11 = "https://univ-poitiers.webex.com/meet/isabelle.millon.zumstein"

"""Text-to-speech"""
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)

"""Quotes"""

name = "Baptiste"
QUOTES_CLASSES = [
    "Bonne Chance " + name,
    "Travaillez bien !",
    "Passez un bon cours !",
    "Bonne journée " + name,
    "Profitez bien de votre journée",
    "Cent pour cent Utah",
]
quote = QUOTES_CLASSES[random.randint(0, len(QUOTES_CLASSES)-1)]


def a():
    webbrowser.open(url1)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Arabe"""


def b():
    webbrowser.open(url2)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Russe appliquee"""


def c():
    webbrowser.open(url3)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Economie fr"""


def d():
    webbrowser.open(url4)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Russe langue ecrite"""


def e():
    webbrowser.open(url3)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Simple, la phrase"""


def f():
    webbrowser.open(url5)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Anglais langue ecrite"""


def g():
    webbrowser.open(url7)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Russe histoire"""


def h():
    webbrowser.open(url8)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Economie anglosaxone"""


def i():
    webbrowser.open(url6)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Russe COM/EXP orale"""


def j():
    webbrowser.open(url9)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Anglais diversite culturelle CM"""


def k():
    webbrowser.open(url10)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""Anglais diversite culturelle TD"""


def l():
    webbrowser.open(url11)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


"""debug schedule"""


def debug():
    print("Bonjour")
    time.sleep(2)


schedule.every().monday.at("14:00").do(a)
schedule.every().monday.at("15:30").do(b)
schedule.every().tuesday.at("09:00").do(c)
schedule.every().tuesday.at("11:00").do(d)
schedule.every().tuesday.at("14:00").do(e)
schedule.every().wednesday.at("08:00").do(f)
schedule.every().wednesday.at("10:00").do(b)
schedule.every().wednesday.at("13:30").do(g)
schedule.every().wednesday.at("15:30").do(h)
schedule.every().thursday.at("08:00").do(i)
schedule.every().thursday.at("10:00").do(j)
schedule.every().thursday.at("11:00").do(k)
schedule.every().friday.at("15:00").do(l)


while True:
    schedule.run_pending()
    time.sleep(1)
