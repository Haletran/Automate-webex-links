from os import system
from beautifultable import BeautifulTable
from subprocess import call


def logo():
    print("""
 
 __      __      ___.                
/  \    /  \ ____\_ |__   ____ ___  ___
\   \/\/   // __ \| __ \_/ __ \\  \/  /  
 \        /\  ___/| \_\ \  ___/ >    <  
  \__/\  /  \___  >___  /\___  >__/\_ \ 
       \/       \/    \/     \/      \/ 

""")


def clear_screen():
    system('cls')


def search():
    clear_screen()
    logo()
    print("Searching...")
    call(["python", "search.py"])


def timetable():
    clear_screen()
    logo()
    call(["python", "timetable.py"])
    op = int(input(("1. Start Bot\nEnter option : ")))
    if(op == 1):
        search()


if __name__ == "__main__":

    logo()
    op = int(input(("1. Start Bot\n2. Emploi du temps\n\nEnter option : ")))

    if(op == 1):
        search()
    if(op == 2):
        timetable()
