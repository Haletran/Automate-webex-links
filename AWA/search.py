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
url1 = ""
url2 = ""
url3 = ""
url4 = ""
url5 = ""
url6 = ""
url7 = ""
url8 = ""
url9 = ""
url10 = ""
url11 = ""

"""Text-to-speech"""
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)

"""Quotes"""

name = ""
QUOTES_CLASSES = [
    "Bonne Chance " + name,
    "Travaillez bien !",
    "Passez un bon cours !",
    "Bonne journée " + name,
    "Profitez bien de votre journée",
    "Cent pour cent Utah",
]
quote = QUOTES_CLASSES[random.randint(0, len(QUOTES_CLASSES)-1)]

"""Fonctions do"""

def a():
    webbrowser.open(url1)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


def b():
    webbrowser.open(url2)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def c():
    webbrowser.open(url3)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def d():
    webbrowser.open(url4)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def e():
    webbrowser.open(url3)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def f():
    webbrowser.open(url5)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def g():
    webbrowser.open(url7)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def h():
    webbrowser.open(url8)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()



def i():
    webbrowser.open(url6)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


def j():
    webbrowser.open(url9)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


def k():
    webbrowser.open(url10)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()


def l():
    webbrowser.open(url11)
    time.sleep(8)
    pyautogui.click(620, 1000)
    pyautogui.click(1100, 1020)
    engine.say('Votre cours est prêt !')
    engine.say(quote)
    engine.runAndWait()




schedule.every().monday.at("10:00").do(a)
schedule.every().monday.at("10:00").do(b)
schedule.every().tuesday.at("10:00").do(c)
schedule.every().tuesday.at("10:00").do(d)
schedule.every().tuesday.at("10:00").do(e)
schedule.every().wednesday.at("10:00").do(f)
schedule.every().wednesday.at("10:00").do(b)
schedule.every().wednesday.at("10:00").do(g)
schedule.every().wednesday.at("10:00").do(h)
schedule.every().thursday.at("10:00").do(i)
schedule.every().thursday.at("10:00").do(j)
schedule.every().thursday.at("10:00").do(k)
schedule.every().friday.at("10:00").do(l)


while True:
    schedule.run_pending()
    time.sleep(1)
