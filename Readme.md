
<h1 align="center">AWA</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/Haletran/Automate-webex-links/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/Haletran/Automate-webex-links/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A simple python program to launch your webex classes automatically
    <br> 
</p>

## 📝 Table of Contents

- [à propos](#about)
- [Getting Started](#getting_started)
- [Installation](#deployment)
- [AWA](#usage)
- [Mise en place](#config)
- [Emploi du temps ](#table)
- [Auteurs](#authors)

## 🧐 à propos <a name = "about"></a>

AWA est un programme en python permettant d'automatiser le lancement des cours sur Webex en fonction
de l'heure et du jour qu'il est . Par exemple , si vous avez cours de Maths à 13h , le programme lancera
le cours qui correspond , le rejoindra et vous souhaitera un bon cours .

## 🏁 Getting Started <a name = "getting_started"></a>

Vous aurez besoin de quelques pre-requis pour faire marcher le programme , sans cela il ne marchera pas.

### Prerequis

En premier lieu vous devez installer le language Python 3.9 .

```
https://www.python.org/
```

### Installation

Apres avoir installé Python , vous allez devoir télécharger les modules qui vont avec .
Ouvrer le CMD (touche windows,tapez CMD et lancez).

Il y a en tout 4 modules à installer :

```
pip install schedule
pip install pyautogui
pip install pyttsx3
pip install beautifultable
pip install pyttsx3
```

Les instalations des uns ou des autres peuvent durer quelques minutes , cela depend avant tout de votre connexion.

## AWA <a name = "tests"></a>

Maintenant que l'environnement compatible est pret , vous devez télécharger le fichier "Source code(zip)" situés dans release (en haut à droite).
Une fois le fichier telecharge ,vous devez extraire et lancez le programma AWA.py . Si vous avez tout fait correctement vous devriez voir la fenetre
du programme . Dans ce cas , vous pouvez vous applaudir !

### 🔧 Mise en place <a name = "config"></a>

Maintenant , il va falloir mettre les mains dans le code , je sais que cela peut faire peur mais vous allez voir c'est extremement simple .
Ouvrez search.py avec le bloc-note (ou IDE ).

Vous allez apercevoir des emplacements pour mettre des liens Webex , numeroté de 1 à 11 (vous pouvez en ajouter plus)
Copiez le lien de votre professeur entre les guillemets.

```
url1 = "le_lien_webex_de_votre_professeur"
```

Une fois les liens de vos professeurs recopiés , il va falloir definir les heures et les jours à laquelle ils ont lieu .
Descendez tout en bas du fichier afin d'apercevoir les fonctions schedule .

```
schedule.every().monday.at("14:00").do(a)
```

On peut decomposer la fonction en 3 parties :

- le jour ( ici monday donc lundi )
- l'heure ( ici 14:00 )
- le fonction a lancé ( ici 'a' )

Vous allez donc devoir compléter selon les cours que vous avez .
Les liens correspondent tous à des fonctions , ainsi 'url1' correspond à la fonction 'a' . Compléter donc en fonction de cela .

EXEMPLES :

Ici j'ai cours le mardi( tuesday ) à 9h00 de Philosphie( b = url2 qui correspond au lien du prof de philosphie .

```
schedule.every().tuesday.at("09:00").do(b)
```

### ⛏️ Emploi du temps <a name = "table"></a>

Voici la derniere étape , mettre en place votre emploi du temps . Cette étape n'est pas obligatoire donc vous n'etes pas obligés
de la faire .Elle permet d'afficher votre emploi du temps constitué du nom des cours , des heures de cours et des noms des professeurs . 

Vous allez devoir ouvrir le fichier timetable.py , toujours avec le bloc-note ( ou IDE ).
Vous allez voir différentes fonctions , mais il va falloir devoir modifier ceux appeles 'rows.append' .

```
 table.rows.append([])
```

Entre les crochets , vous allez mettre les informations de cours sous cette forme :

```
 table.rows.append(["nom_du_cour","heures","noms du professeurs"])
```

EXEMPLE :

```
table.rows.append(["Anglais-Comp/exp orales", "14:00-15:00", "Kawach Nada"])
```

## ✍️ Auteurs <a name = "authors"></a>

- [@Haletran](https://github.com/Haletran) - Idée et création

La liste des [contributeurs](https://github.com/Haletran/Automate-webex-links/graphs/contributors) qui ont participés au projet.
