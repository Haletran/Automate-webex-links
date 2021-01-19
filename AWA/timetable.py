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
    table.rows.append(["Anglais-Comp/exp orales",
                       "14:00-15:00", "Kawach Nada"])
    table.rows.append(["Arabe", "15:30-18:00", "Deabes Mohammed Mustapha"])
    table.rows.append(
        ["Russe enjeux socio-eco", "09:00-10:00", "Olga Osinovskaya"])
    table.rows.append(["Economie Francaise", "11:00-12:00", "Cormeau Nicolas"])
    table.rows.append(
        ["Russe langue ecrite", "14:00-15:30", "Olga Osinovsakaya"])
    table.rows.append(["Simple, la phrase", "08:00-10:00",
                       "Dourdet Jean Christophe"])
    table.rows.append(["Arabe", "10:00-11h30", "Deabes Mohammed Mustapha"])
    table.rows.append(
        ["Anglais langue ecrite ", "13:30-15:00", "Robert Jessica"])
    table.rows.append(["Russe culture", "15:30-16:30", "Krauss Charlotte"])
    table.rows.append(["Anglais economie anglosaxone",
                       "08:00-09:00", "Jorge Anita"])
    table.rows.append(
        ["Russe comp/exp orales", "10:00-11:00", "Bondareva Irina"])
    table.rows.append(
        ["Anglais div culturelle", "11:00-12:00", "Peyrol Elodie"])
    table.rows.append(
        ["Anglais div culturelle", "15:00-16:00", "Millon Isabelle"])
    table.rows.header = ["M", "M", "T", "T", "T",
                         "W", "W", "W", "W", "TH", "TH", "TH", "F"]
    table.columns.header = ["Cours", "Heures", "Professeurs"]
    print(table)


agenda()
