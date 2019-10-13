# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:33:22 2019

@author: Marco Menezes
"""

lvlList = ("Expert","Medium","Easy")

#--------------------- DATA ABOUT SUBSTANTIVE CLASS----------------------------#

listCases = ["Nominativ", "Akkusativ","Dativ"]
listGenres = ["Männlich","Neutral","Weiblich","Plural"]
adjWeakDek = [['e','e','e','en'],['en','e','e','en'],['en','en','en','en']]
adjMixedDek = [['er','es','e','e'],['en','es','e','e'],['en','en','en','en']]
adjStrongDek = [['er','es','e','e'],['en','es','e','e'],['em','em','er','en']]

#----------------------- DATA ABOUT VERB CLASS --------------------------------#

listTense = ["Präsens","Perfekt","Präteritum","Futur I","Plasquamperfekt",
             "Futur II","Konjunktiv II + Vergangenheit",
             "Konjunktiv II + Futur I","Konjunktiv II + Futur II",
             "Passiv Vergangenheit","Passiv Präsen"]
listTense2 = ("Präsens","Perfekt","Präteritum")
modalVerbs = ("Können","Sollen","Dürfen","Müssen","Wollen")
bitteVerbs = ("Möchten","Würden gern")
untrennbarePrefix = ("be","emp","ent","er","miss","ver","zer")
trennbarePrefix = ("ab","an","auf","aus","bei","ein","mit",
                   "her","hin","vor","weg","zu","zurück")
vetPrasens1 = ['e','st','t','t','en']
vetPrasens2 = ['e','est','et','et','en']
vetPrasens3 = ['e','t','t','t','en']
finalCase2 = ["t","d","m","n"]
finalCase3 = ["s","x","z","ß"]
vetPrateritum = ['te','test','te','tet','ten'] 
trennUntrennPrefix = ("durch","hinter","über","um","unter")


NomPerson = ['Ich','Du','Er/Sie/Es','Ihr','Wir/Sie/sie']
AkkPerson = ['mich','dich','ihn/sie/es','uns','euch, Sie/sie']
DatPerson = ['mir','dir','ihm/ihr/ihm','uns','euch, Ihnen/ihnen']
RefPerson = ['mich','dich','sich','uns','euch, sich']
#-------------------- DATA ABOUT THE GAME INTERFACE ---------------------------#

invalidInput = "Bitte geben Sie eine gültige Nummer ein!\n"
difficultyMsg = "Wählen Sie eine Schwierigkeitsgrad (Nummer) für das VerbenSpiel:\n\n"
mutterspracheMsg = "\nWählen Sie bitte eine Muttersprache für die Übersetzung:\n\n"
subThemaMsg = "\nWählen Sie bitte eine Nummer für das Untertitel des Spiels:\n\n"
themaMsg = "\nWählen Sie bitte eine Nummer für das Thema des Spiels:\n\n"
introdMsg1 = "\n\nHallo mein Freund! Herzlich Willkommen zum Spiel von Marco"
introdMsg2 = " Menezes. Diese Software hat eine glorreiche Zukunft.\n\n"
introdMsg = introdMsg1 + introdMsg2
tenseMsg1 = "\n\nWählen Sie die im Spiel verfügbaren Zeiten! Geben Sie "
tenseMsg2 = "Kommagetrennte Zahlen, z.B '2,4' for Perfekt und Futur I.\n"
tenseMsg = tenseMsg1 + tenseMsg2