import webbrowser
import datetime
import calendar

now = datetime.datetime.now()
day = datetime.datetime.today().weekday()

i = now.hour
url1 = "https://univ-poitiers.webex.com/meet/sanja.boskovic"
url2 = "https://univ-poitiers.webex.com/meet/irina.bondareva"
url3 = "https://univ-poitiers.webex.com/meet/olga.osinovskaya"
url4 = "https://univ-poitiers.webex.com/meet/raluca.nita"
url5 ="https://univ-poitiers.webex.com/meet/andrew.peterson"
url6 = "https://univ-poitiers.webex.com/meet/anita.jorge"
url7 = "https://univ-poitiers.webex.com/meet/nicolas.cormeau"
url8 = "https://univ-poitiers.webex.com/univ-poitiers/j.php?MTID=m5cc9bbc014e051be70b488afa018712a"
url9 = "https://univ-poitiers.webex.com/univ-poitiers/j.php?MTID=m17b56450e300259c9f9b70d4d98d97dc"
url10 = "https://univ-poitiers.webex.com/meet/alix.tubman"


if day== 0 and  i == 10: 
 print("Russe : Grands reperes culturels")
 webbrowser.open(url1,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 0 and  i == 14: 
 print("Russe : Langue orale et ecrite Irina")
 webbrowser.open(url2,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 0 and  i == 15: 
 print("Russe : Langue orale et ecrite Olga")
 webbrowser.open(url3,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 1 and  i == 9: 
 print("Origines et fonctionnements de l'Anglais")
 webbrowser.open(url4,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 1 and  i == 10: 
 print("Langues et Politiques linguistiques")
 webbrowser.open(url1,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 1 and  i == 11: 
 print("Lire le Monde")
 webbrowser.open(url5,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 2 and  i == 10: 
 print("Traduction Anglais")
 webbrowser.open(url6,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 3 and  i == 10: 
 print("Courants pensees economiques")
 webbrowser.open(url7,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 3 and  i == 11: 
 print("Panorama du monde anglophone")
 webbrowser.open(url9,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 4 and  i == 8: 
 print("Decouverte Entreprise")
 webbrowser.open(url8,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 4 and  i == 9: 
 print("Institutions Francaises et europeenes")
 webbrowser.open(url7,new=0,autoraise=True)
else : 
 print("Pas de cours ")

if day== 4 and  i == 10: 
 print("Francais")
 webbrowser.open(url10,new=0,autoraise=True)
else : 
 print("Pas de cours ")

    
