#!/usr/src/python3.7 # Emplacement de Python
#-*-coding:Utf-8 #Sélection de l'encodage pour les accents


"""
    Fichier à titre d'information. Utilisé uniquement pour répertorier les leçons
    "Apprenez à programmer en Python" du site OpenclassRooms
"""


# Creation de fonction

def maFonction(para1, para2, ...):

# Appel de fonction

maFonction(para1, para2, ...)

# Fonction lambda. 1 seule ligne

lambda para1, para2, ...: operation

# Appel de la fonction lambda

f = lambda para1, para2, ...: operation
f(para1, para2, ...)

# Importation de module

import math
# Peut être renommé
import math as mathematiques


# Appel de fonction dans le module math

math.sqrt(nb)
# Appel de la fonction dans le module renommé
mathematiques.sqrt(nb)

# Obtenir de l'aide sur un module

help("math")
help("math.sqrt")

# Importation d'une fonction unique d'un module

from math import fabs
from math import * # Fera un check up de toutes les fonctions

# Appel de la fonction unique d'un module

fabs(nb)

# Importation de Packages

import nom_bibliotheque

# Accéder à des sous parties du Package

nom_bibliotheque.sous_partie.sous_sous_partie

# Schema de Package

"""

nom_bibliotheque
|
|_module_1
|
|_module_2
|
|_sous_partie
  |
  |_module_1
  |
  |_module_2
  |
  |_sous_sous_partie
    |
    |_module_1
    |
    |_module_2

"""

 # Importation d'un unique module/fonction dans un Package

from nom_bibliotheque.sous_partie import module

# Gestion des exceptions

# FORME MINIMALE (A éviter)

annee = input()

try:
    annee = int(annee)

except:
    print("Erreur lors de la conversion de l'année")

# FORME UN PEU PLUS COMPLETE

""" Exemple d'une gestion des exceptions pour une division sans variable créée, sans changement de type de variable et avec risque de division par 0 """

try:
    resultat = numerateur / denominateur

except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0")

""" Bonus """

except type_de_l_exception as exception_retournee:
    print("Voici l'erreur :", exception_retournee)
else:
    print("Le résultat obtenu est", resultat)

""" Bloc finally """

finally:
    # Instruction(s) exécutée(s) peu importe si il y a des erreurs ou non

""" Bloc pass """ # Préférable de ne jamais l'utiliser

try:
    # Test
    except type_de_l_exception:
        pass # Rien ne doit se passer en cas d'erreur

# Assertion

""" Test de condition avec assert """

var = 5

assert var == 5 # True
assert var == 8 # False

# Lever une exception

annee = input()

try:
    annee = int(annee)
    if annee <= 0:
        raise ValueError("L'année saisie est négative ou nulle")
    # Lève une exception de type ValueError si l'utilisateur saisit une année négative ou nulle
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")


while input() != "Q":
    input("Appuyez sur \" Q \" pour fermer ce programme...")
# Afin de mettre fin au programme


#   -- Les méthodes de classe str  --

# Mettre une phrase en minuscule

# Methode ASCII

"""
Méthode dans laquelle on change chaque lettre majuscule ASCII par son équivalence en minuscule ASCII une par une en incrémentant le processus

Méthode longue, mais qui a l'avantage de prouver que l'on peut faire un programme sans utiliser les PACKAGES déjà dispo

"""

# Methode simple

chaine = "JE NE SUIS PAS FACHE!"
chaine.lower()
> "je ne suis pas faché!"

# Exemple d'utilisation

chaine = str () # Création d'un chaine de caractères vide
# On peut utiliser chaine = ""

while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()

# Mettre une phrase en majuscule

chaine = "J'aimerais pouvoir crier..."
chaine.upper()
> "J'AIMERAIS POUVOIR CRIER..."

# Mettre une majuscule à la première lettre

chaine = "pour. ceux. qui. ne. savent. pas. mettre. des. majuscules."
chaine.capitalize()
> "Pour. Ceux. Qui. Ne. Savent. Pas. Mettre. Des. Majuscules."

# Retirer les espaces en trop en début et en fin de phrase.

chaine = "  Trop d'espace, tue l'espace  "
chaine.strip()
> "Trop d'espace, tue l'espace"

# Un objet à plusieurs méthodes
# Objet.methode_1().methode_2()

chaine = "introduction"
chaine.upper().center(20)
> "    INTRODUCTION    "

# py help(str) pour d'autres méthodes

# Approfondissement de la fonction print()

prenom = "Axel"
nom = "Pion"
age = 27

print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age))
> "Je m'appelle Axel Pion et j'ai 27 ans."

# Autre méthode

adresse = """
{no_rue} {nom_rue}
{code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Doucettes", code_postal=95140, nom_ville="Garges les Gonesse", pays="France")
print(adresse)
> "5, rue des Doucettes
95140 Garges les Gonesse (France)"

# Concaténation de chaînes

prenom = "Axel"
nom = "Pion"
age = 27
chaine = "Je m'appelle " + prenom + " " + nom + " et j'ai " + str(age) + " ans."
> "Je m'appelle Axel Pion et j'ai 27 ans."

# Parcours dans une chaine

chaine = "Salut les amis !"
chaine[0]
> "S"
chaine[3]
> "u"
chaine[-1]
> "!"

# Connaitre la taille d'une chaîne de caractères

chaine = "Salut"
len(chaine)
> 5

# Parcours avec un while

chaine = "Salut"
i = 0

while i < len(chaine):
    print(chaine[i])
    i++

# Selection de chaînes

chaine = "Salut"
chaine[0:2] # Selection des deux premières lettres
> "Sa"
chaine[2:len(presentation)] # Sélection de toute la chaine sauf les deux premières lettres
> "lut"
chaine[:2] # Sélection du début jusqu'à la 3ème lettre (non comprise)
> "Sa"
chaine[2:] # Selection à partir de la 3ème lettre (comprise)
> "lut"

# Utilisation

chaine = "Salut"
chaine = chaine[:2] + "laud"
print(chaine)
> "Salaud"

#  -- Les Listes --

# Création d'une liste

liste = [] # Création d'une liste vide
liste = [1, 'a', "Salut", 123123] # Une liste peut être remplie avec tout style d'objet

print(liste)
> 1, 'a', "Salut", 123123

# Accéder aux éléments d'une liste

liste = ['S', 'a', "lut", 123]
print(liste[3])
> 123
print(liste[0])
> 'S'
liste[0] = "Ch"
print(liste)
> "Ch" 'a' "lut" 123

# Ajouter des éléments à la fin d'une liste

liste = [1, 2, 3]
liste.append(4) # Ajout de 4 à la fin de la liste
print(liste)
> [1, 2, 3, 4]

# Insérer un élément dans la liste

liste = ['a', 'b', 'd', 'e']
liste.insert(2, 'c') # Insertion de l'élément 'c' à la 3ème place
print(liste)
> ['a', 'b', 'c', 'd', 'e']

# Concaténation des listes

liste1 = [1, 2, 3]
liste2 = [5, 6, 7]
liste1.extend(liste2) # Insertion de la liste2 à la fin de la liste1
print(liste1)
> [1, 2, 3, 5, 6, 7]

# Ou

liste1 = liste1 + liste2

# Ou encore

liste1 += liste2

# Suppression d'éléments d'une liste

# del

variable = 1
print(variable)
> 1

del variable
print(variable)
> Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'variable' is not defined

liste = [1, 2, 3, 4]
del liste[3]
print(liste)
> [1, 2, 3]

# remove

liste = ['a', 'b', "Salut", 'c']
liste.remove("Salut")
print(liste)
> ['a', 'b', 'c']


# Parcours d'une liste

# Méthode while

liste = [1, 2, 3, 4, 5]
i = 0

while i < len(liste[i]):
    print(liste[i])
    i++
>1
>2
>3
>4
>5

# Méthode for (préférable)

for elmt in liste: # elmt va prendre les valeurs successives des éléments
    print(elmt)
>1
>2
>3
>4
>5

# Fonction enumerate

liste = ['a', 'b', 'c']

for i, elmt in enumerate(liste):
    print("A l'indice {}, se trouve {}.".format(i, elmt))

> "A l'indice 0 se trouve a."
> "A l'indice 1 se trouve b."
> "A l'indice 2 se trouve c."

# plus clair

for i, elmt in enumerate(liste):
    print(elt)

> (0, 'a') # Cet élément est appelé un TUPLES
> (1, 'b') # Contenant d'abord l'indice puis l'objet se trouvant à cet indice
> (2, 'c')

# Exemple d'utilisation

liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
    ] # Possibilité d'étaler la liste

for nb, lettre in liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

> "La lettre a est la 1e de l'alphabet."
> "La lettre d est la 4e de l'alphabet."
> "La lettre g est la 7e de l'alphabet."
> "La lettre z est la 26e de l'alphabet."

# Les tuples

" Les tuples sont des listes immuables (elles ne peuvent pas être modifiées). On ne peut rien y ajouter ou retirer"

# Exemples de tuples

tuple_vide = ()
tuple_Nonvide = (1,)
tuple_multiple = (1, 2, 3)

# ou

tuple_Nonvide = 1, # La virgule est essentielle dans la création du tuple sinon Python les considèrera comme des variables lambda

# Renvoyer plusieurs valeurs

def decomposer(entier, divise_par):
    partie_entiere = entier // divise_par
    reste = entier % divise_par
    return partie_entiere, reste

partie_entiere, reste = decomposer(20, 3)
print(partie_entiere)
> 6
print(reste)
> 2

# py help(list) pour en savoir plus

# Passer d'une chaîne de caractères à une liste

chaine = "Salut tout le monde"
chaine.split(" ") # Séparation des mots entre chaque espace
# chaine.split(" ") = chaine.split()
print(chaine)
> ['Salut', 'tout', 'le', 'monde']

# Passer d'une liste à une chaîne de caractères

liste = ['Salut', 'tout', 'le', 'monde']
" ".join(liste)
print(liste)
> "Salut tout le monde"

# Exemple d'utilisation

def aff_float(flottant):
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    part_entiere, part_float = flottant.split(".") # Definition des "cases" de la liste.
    return ",".join([part_entiere, part_float[:3]]) # Mise en place de la virgule entre part_entiere et part_float. part_float, n'affiche que les 3 premiers chiffres

aff_float(3.9999999998)
> '3,999'

# Fonction à paramêtres variables

def fonction(*parametre):
    print("J'ai reçu : {}.".format(parametre))

fonction('a', 'e', 'i', 'o', 'u', 'y')
> "J'ai reçu : ('a', 'e', 'i', 'o', 'u', 'y')."
fontion(1)
> "J'ai reçu : (1,)." # Python va automatiquement placer chaque paramêtres rentrés dans un tuple

# Autre exemple

def fonction(nom, prenom, *parametre)

# Transformer une liste en paramêtre de fonctions

liste_parametres = [2, 4, 6, 8, 10]
print(*liste_parametre)
> 2 4 6 8 10

#  -- Compréhension de liste --

# Parcours simple

liste = [0, 1, 2, 4]
[nb * nb for nb in liste]
> [0, 1, 4, 16]

# Filtrage avec un branchement conditionnel

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste if nb % 2 == 0]
> [2, 4, 6, 8, 10]

# Exemple d'utilisation

quantite_a_retirer = 7
fruits_stockes = [15, 3, 18, 21]
[nb_fruits - quantite_a_retirer for nb_fruits in fruits_stockes if nb_fruits > quantite_a_retirer]
> [8, 11, 14]

#  -- Les dictionnaires --

# Créer un dictionnaire

dictionnaire = dict() # Dictionnaire vide

# Ou

dictionnaire = {} # Dictionnaire vide

type(dictionnaire) # Nous montre que c'est bien un dictionnaire
> <class 'dict'>

"""

() = tuples
[] = listes
{} = dictionnaires

"""

# Ajouter des clefs et des valeurs dans le dictionnaire

dictionnaire = {}
dictionnaire["pseudo"] = "Haneul"
dictionnaire["mot de passe"] = "12345"
print(dictionnaire)
> {'mot de passe': '12345', 'pseudo': 'Haneul'}

# Si on fait

dictionnaire = {}
dictionnaire["pseudo"] = "Haneul"
dictionnaire["mot de passe"] = "*"
dictionnaire["pseudo"] = "Maengdok"
print(dictionnaire)
> {'mot de passe': '*', 'pseudo': 'Maengdok'} # Python remplace la nouvelle valeur par l'ancienne

# Accéder à une valeur précise du dictionnaire

print(dictionnaire["mot de passe"])

# Autre possibilité d'utilisation

dictionnaire = {}
dictionnaire[0] = "a"
dictionnaire[1] = "b"
print(dictionnaire)
> {0: 'a', 1: 'b'}

# Possibilité d'utilisation avec des tuples

echiquier = {}
echiquier['a', 1] = "tour blanche"
echiquier['h', 8] = "tour noire"

# Création de dictionnaire déjà rempli

placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}

# La création d'un dictionnaire avec des clefs, sans valeur, s'appelle un set

dictionnaire = {'pseudo', 'mot de passe'} # == set
# Comme pour le reste, il ne peut pas avoir deux fois le même objet
# Revoir le dictionnaire avec les deux entrées de "pseudo"

# Supprimer des clefs d'un dictionnaire

# del

placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}
del placard["chemise"]

# pop

placard.pop("chemise")
> 3 # La méthode pop supprime la clef mais renvoie la valeur supprimée

# Stocker des fonctions dans un dictionnaire

def manger():
    print("Allons manger des Kimbap!")

def faim():
    print("J'ai faim!")

fonction = {}
fonction["manger"] = manger # Sans les paranthèses
fonction["faim"] = faim
fonction["faim"]
> <function faim at 0x00BA5198> # Nous indique que la fonction faim est bien présente à un endroit donné
fonction["faim"]() # Ajout des parenthèses pour l'appeler
> "J'ai faim!"

# Les méthodes de parcours

# Parcours des clefs

fruits = {"pommes": 21, "melons": 3, "poires": 31}

for clef in fruits:
    print(clef)

> pommes
> poires
> melons

# Ou (question de sureté au niveau de l'ordre d'affichage)

for clef in fruits.keys():
    print(clef)

> pommes
> melons
> poires

# Parcours des valeurs

for valeurs in fruits.values():
    print(valeurs)

> 21
> 3
> 31

# Obtenir une valeur via condition

if 21 in fruits.values():
    print("Un des fruits possède la valeur 21.")

> "Un des fruits possède la valeur 21.")

# Parcours des clefs et des valeurs simultanément

for clef, valeur in fruits.items():
    print("La clef {} contient la valeur {}.".format(clef, valeur))

> "La clef pommes contient la valeur 21."
> "La clef melons contient la valeur 3."
> "La clef poires contient la vlaeur 31."

# Les dictionnaires et paramêtres de fonction

# Récupérer les paramêtres nommés dans un dictionnaire

def fonction(**parametres_nommes): # fonction permettant de récupérer les paramètres nommés d'un dictionnaire
    print("J'ai reçu en paramètres nommés: {}".format(parametres_nommes))

fonction() # Appel vide de la fonction
> "J'ai reçu en paramètres nommés: {}" # Nous montre que la fonction est vide
fonction(p=4, j=8) # Appel avec des paramètres nommés
> "J'ai reçu en paramètres nommés: {'p':4, 'j':8}" # Nous montre tous les paramètres nommés

def fonction(*liste, **dictionnaire) # Tous les paramètres non nommés sont mis dans la liste (*liste) et tous les paramètres nommés sont mis dans le dictionnaire (**dictionnaire)

# Transformer un dictionnaire en paramètres nommés d'une fonction

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres) # Fait passer parametre en tant que dictionnaire et ses paramètres en paramètres de dictionnaire
> "Voici >> un >> exemple >> d'appel -"

# Equivalence

print("Voici", "un", "exemple", "d'appel", sep = " >> ", end = " -\n")
> "Voici >> un >> exemple >> d'appel -"

#  -- Utiliser les fichiers  --

## Lecture et écriture dans un fichier

### Ouverture d'un fichier

# fonction open

open("fichier.extension", "r")

# "r" = read
# "w" = write - Contenu du fichier écrasé. S'il n'existe pas, il est créé
# "a" = append - Ecriture à la fin du fichier sans l'écraser. S'il n'existe pas, il est créé

### fermer le fichier

# close

fichier = open("fichier.txt", "r")
fichier = <_io.TextIOWrapper name='fichier.txt' mode='r' encoding='UTF-8'>
fichier.close()

### Lire l'intégralité du fichier

# read

contenu = fichier.read()
print(contenu)
> "Contenu à afficher"

## Ecrire dans le fichier

# write

fichier = open("fichier.txt", "a")
fichier.write("Contenu à écrire") # N'écrit que des chaînes de caractères
fichier.close() # Toujours fermer le fichier après y avoir écrit

''' help(os) '''

# Fermeture ~forcée du fichier après l'instruction demandée (Evite les pertes de mémoires)

# with

with open("fichier.txt", "w") as fichier:
    contenu = fichier.read()
    # Fermeture du fichier ~forcée après cette instruction


## Enregistrer des objets dans un fichier

# pickle

import pickle

# pickler + dump

score = {
    "Joueur 1": 5,
    "Joueur 2": 35,
    "Joueur 3": 20,
    "Joueur 4": 2,
    }

with open("donnees", "wb") as fichier: # "wb" : Write + Binary
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score) # Enregistrement de l'objet score dans le fichier
    # Possibilité d'ajouter d'autres objets en rappelant mon_pickler.dump(objet) et seront placés dans l'ordre inscrit.
    # Peut être plus opti de place les objets dans des fichiers différents

## Récupérer les objets enregistrés

# unpickler + load

with open("donnees", "rb") as fichier: # "rb" : Read + Binary
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()


# AUTRE

ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print(ma_liste2)
> [1, 2, 3, 4]
print(ma_liste1)
> [1, 2, 3, 4]
# ma_liste1 et ma_liste2 sont liées

ma_liste1 = [1, 2, 3]
ma_liste2 = list(ma_liste1) # copie de la liste 1 dans liste 2, si liste 2 modifiée, cela ne modifiera pas la liste 1

# fonctionne aussi avec les dictionnaires > mon_dict2 = dict(mon_dict1)

ma_liste1 = [1, 2]
ma_liste2 = [1, 2]
ma_liste1 == ma_liste2 # Compare le contenu
> True
ma_liste1 is ma_liste2 # Compare leur référence
> False

# Utiliser concrètement les variables globales

i = 4
def inc_i():
    global i # Python recherche i en dehors de l'espace local de la fonction
    i += 1

print(i)
> 4
inc_i()
print(i)
> 5

# CLASSE

# Définition de classe et constructeur

class Personne: # Définition de la classe Personne
"""
 Classe définissant une personne caractérisée par :
  - Son nom
  - Son prénom
  - Son âge
  - Son lieu de résidence
"""

    def __init__(self, nom, prenom): # Methode constructeur
        self.nom = nom # Attribut nom
        self.prenom = prenom
        self.age = 28
        self.lieu_residence = "Val d'Oise"

axel = Personne("Pion", "Axel")
print(axel.nom)
> 'Pion'

# Attributs de classe

class Compteur:

    objets_crees = 0
    def __init__(self):
        """ A chaque qu'un objet est créé, le compteur incrémente """
        Compteur.objets_crees += 1

print(Compteur.objets_crees)
> 0
a = Compteur() # Création d'un premier objet
print(Compteur.objets_crees)
> 1
b = Compteur() # Création d'un second objet
print(Compteur.objets_crees)
> 2

# Les méthodes

class TableauNoir:
    """
        Classe définissant une surface sur laquelle on peut écrire,
        que l'on peut lire et effacer, par jeu de méthodes.
        L'attribut modifié est 'surface'
    """

    def __init__(self):
        """
            Par défaut, notre surface est vide
        """
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """
            Méthode permettant d'écrire sur la surface du tableau.
            Si la surface n'est pas vide, on saute une ligne avant de rajouter
            le message à écrire
        """

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """
            Cette méthode se charge d'afficher, grâce à print,
            la surface du tableau
        """

        print(self.surface)

    def effacer(self):
        """
            Cette méthode permet d'efface la surface du tableau
        """

        if self.surface != "":
            self.surface= ""
        else:
            print("Le tableau est déjà propre")

tab = TableauNoir()
print(tab.surface)
> ''
tab.ecrire("Cool! Ce sont les vacances!")
print(tab.surface)
> "Cool! Ce sont les vacances!")
tab.ecrire("Joyeux Noël!")
print(tab.ecrire)
> "Cool! Ce sont les vacances!"
> "Joyeux Noël!"

# Paramêtre self

    """
        L'attribut self permet de travailler dans une méthode de l'objet ou sur
        l'objet lui-même
    """

# Exemple

>>> tab.ecrire
> <bound method TableauNoir.ecrire of <__main__.TableauNoir object at 0x00B3F3F0>>
>>> TableauNoir.ecrire
> <function ecrire at 0x00BA5810>
>>> help(TableauNoir.ecrire)
> Help on function ecrire in module __main__:
ecrire(self, message_a_ecrire):
    """
        Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire
    """
>>> TableauNoir.ecrire(tab, "essai")
>>> tab.surface
> 'essai'

# Méthodes de classe et méthode statiques

# Méthode de classe

class Compteur:
    """
        Cette classe possède un atrribut de classe qui s'incrémente à chaque
        fois que l'on crée un objet de ce type
    """

    objets_crees = 0
    def __init__(self):
        """
            A chaque qu'un objet est créé, le compteur incrémente
        """
        Compteur.objets_crees += 1

    def combien(cls):
        """
            Méthode de classe affichant combien d'objets ont été créés
        """
        print("Jusqu'à présent, {} objets on été créés.".format(cls.objets_crees))
    combien = classmmethod(combien)

>>> Compteur.combien()
> "Jusqu'à présent, 0 objets ont été créés."
>>> a  = Compteur()
>>> a.combien()
> "Jusqu'à présent, 1 objets ont été créés."

# Méthode statique

class TestStaticMethod:
    """
        Une classe de test tout simplement
    """

    def afficher():
        """
            Fonction chargée d'afficher quelque chose
        """
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe")
    afficher = staticmethod(afficher)

# INTROSPECTION

# Fonction dir

"""
    La fonction dir renvoie une liste comprenant le nom des attributs et
    méthodes de l'objet qu'on lui passe en parametre.
"""

class Test:
    """
        Une classe de test tout simplement
    """
    def __init__(self):
        """
            On définit dans le constructeur un unique attribut
        """
        self.mon_attribut = "ok"

    def afficher_attribut(self):
        """
            Méthode affichant l'attribut 'mon_attribut'
        """
        print("Mon attribut est {}.".format(self.mon_attribut))

>>> un_test = Test() # Création d'un objet de la classe Test
>>> un_test.afficher_attribut()
"Mon attribut est ok"
>>> dir(un_test)
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'afficher_attribut', 'mon_attribut']

# L'attribut spécial __dict__

"""
    Par défaut, tous les objets construits depuis une classe posséderont un
    attribut spécial __dict__.
    C'est un dictionnaire que contient en guise de clefs les noms des attributs
    et, en tant que valeurs, les valeurs des attributs
"""

>>> un_test = Test()
>>> un_test.__dict__
> {'mon_attribut': 'ok'}

>>> un_test.__dict__["mon_attribut"] = "plus ok"
>>> un_test.afficher_attribut()
> "Mon attribut est plus ok"


# Définir des propriétés

    """
        Les propriétés permettent de contrôler l'accès à certains attributs d'une instance

        nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide)

        Chaque paramêtre est optionnel

        On y accède simplement grâce à objet.nom_propriete comme pour n'importe quel autre attribut

    """

# ENCAPSULATION

class Personne: # Définition de la classe Personne
    """
     Classe définissant une personne caractérisée par :
      - Son nom
      - Son prénom
      - Son âge
      - Son lieu de résidence
  """

    def __init__(self, nom, prenom): # Methode constructeur
        """
            Constructeur de notre classe
        """
        self.nom = nom # Attribut nom
        self.prenom = prenom
        self.age = 28
        self.lieu_residence = "Val d'Oise"

    def _get_lieu_residence(self): # Accesseur
        """
            Méthode qui sera appelée quand on souhaitera accéder en lecture
            à l'attribut 'lieu_residence'
        """

        print("On accède à l'attribut lieu_residence!")
        return self._lieu_residence # _ devant l'attribut est une convention pour dire
        # que l'on accède pas à cet attribut via l'extérieur de la classe

    def _set_lieu_residence(self, nouvelle_residence): # Mutateur
        """
            Méthode appelée quand on souhaite modifier le lieu de résidence
        """

        print("Attention, il semble que {} déménage à {}."format(self.prenom,
                nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

>>> axel = Personne("Pion", "Axel")
>>> axel.nom
> 'Pion'
>>> axel.prenom
> 'Axel'
>>> axel.lieu_residence
> "On accède à l'attribut lieu_residence !"
> 'Paris'
>>> axel.lieu_residence = "Séoul"
> "Attention, il semble que Axel déménage à Séoul."
>>> axel.lieu_residence
> 'Séoul'

# METHODES SPECIALES

# Constructeurs

# Edition de l'objet

class Exemple:
    """
        Un petit exemple de classe
    """

    def __init__(self, nom):
        """
            Exemple de constructeur
        """
        self.nom = nom
        self.autre_attribut = "valeur"

>>> mon_objet = Exemple("un premier exemple")

# Suppression de l'objet
    # Pas très utile ...

def __del__(self):
    """
        Méthode appelée quand l'objet est supprimé
    """
    print("C'est la fin! On me supprime!")

# Représentation de l'objet. Méthode __repr__

class Personne: # Définition de la classe Personne
    """
     Classe définissant une personne caractérisée par :
      - Son nom
      - Son prénom
      - Son âge
      - Son lieu de résidence
  """

    def __init__(self, nom, prenom): # Methode constructeur
        """
            Constructeur de notre classe
        """
        self.nom = nom # Attribut nom
        self.prenom = prenom
        self.age = 28
        self.lieu_residence = "Val d'Oise"

    def __repr__(self):
        """
            Quand on entre notre objet dans l'interpréteur
        """
        return "Personne: nom({}), prenom({}), âge({})".format(
                self.nom, self.prenom, self.age)

>>> p1 = Personne("Pion", "Axel")
>>> p1
> 'Personne: nom(Pion), prénom(Axel), âge(28)'

# Ou

>>> p1 = Personne("Pion", "Axel")
>>> repr(p1)
> 'Personne: nom(Pion), prénom(Axel), âge(28)'

# Méthode __str__

    def __str__(self):
        """
            Méthode permettant d'afficher plus joliment notre objet
        """
        return "{} {}, âgé de {} ans".format(self.prenom, self.nom, self.age)

>>> p1 = Personne("Pion", "Axel")
>>> print(p1)
> 'Axel Pion, âgé de 28 ans'
>>> chaine = str(p1)
>>> chaine
> 'Axel Pion, âgé de 28 ans'

# Méthode __getattr__

class Protege:
    """
        Classe possédant une méthode particulière d'accès à ses attributs:
        Si l'attribut n'est pas trouvé, on affiche une arlerte et renvoie None
    """

    def __init__(self):
        """
            On crée quelques attributs par défaut
        """
        self.a = 1
        self.b = 2
        self.c = 3

    def __getattr__(self, nom):
        """
            Si Python ne trouve pas l'attribut nommé nom, il appelle
            cette méthode. On affiche une alerte
        """

        print("Alerte! Il n'y a pas d'attribut {} ici !".format(nom))

>>> pro = Protege()
>>> pro.a
> 1
>>> pro.c
> 3
>>> pro.e
> 'Alerte! Il n'y pas d'attribut e ici !'

# Méthode __setattr__

def __setattr__(self, nom_attr, val_attr):
    """
        Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet
    """

    object.__setattr__(self, nom_attr, val_attr)
    self.enregistrer()

# Méthode __delattr__

"""
    Méthode appelée quand on souhaite supprimer un attribut de l'objet en faisant
    del objet.attribut
    ou
    object.__delattr__
"""

def __delattr__(self, nom_attr):
    """
        On ne peut supprimer d'attribut, on lève l'exception
        AttributeError
    """

    raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

# Bonus

objet = MaClasse()
getattr(objet, "nom") # Semblable à objet.nom
setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon

# Les méthodes de conteneur

# Accès aux éléments d'un conteneur

class ZDict:
    """
        Classe enveloppe d'un dictionnaire
    """

    def __init__(self):
        """
            Notre classe n'accepte aucun paramêtre
        """
        self.dictionnaire = {}

    def __getitem__(self, index): # objet[index]
        """
            Cette méthode spéciale est appelée quand on fait objet[index]
            Elle redirige vers self._dictionnaire[index]
        """

        return self._dictionnaire[index]

    def __setitem__(self, index, valeur): # objet[index] = valeur
        """
            Cette méthode est appelée quand on écrit objet[index] = valeur
            On redirige vers self._dictionnaire[index] = valeur
        """

        self._dictionnaire[index] = valeur

# Méthodes mathématiques

class Duree:
    """
        Classe contenant des durées sous la forme d'un nombre de minutes
        et de secondes
    """

    def __init__(self, min=0, sec=0):
        """
            Constructeur de la classe
        """
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes

    def __str__(self):
        """
            Affichage un peu plu joli de nos objets
        """

        return "{0:02}:{1:02}".format(self.min, self.sec) # {0:02} > 0: = premier argument
                                                            # :02 = nombre de 0 a afficher

>>> d1 = Duree(3, 5)
>>> print(d1)
> '03:05'


    def __add__(self, objet_a_ajouter):
        """
            L'objet à ajouter est un entier, le nombre de secondes
        """
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_duree

>>> d1 = Duree(12, 8)
>>> print(d1)
> '12:08'
>>> d2 = d1 + 54 # d1 + 54 secondes
# Ou
>>> d2 = d1.__add__(54)
>>> print(d2)
> '13:02'

# Bonus

    """
        __sub__
        __mul__
        __truediv__
        __floordiv__
        __mod__
        __pow__
        ... Voir man Python
    """

# Reverse add. Méthode __radd__

def __radd__(self, objet_a_ajouter):
    """
        Cette méthode est appelée si on écrit 4 + objet et que le premier objet
        (4 dans cet exemple) ne sait pas comment ajouter le seconde.
        On se contente de rediriger sur __add__ puisque, ici, cela revient
        au même: l'opération doit avoir le même résultat, posée dans un sens
        ou dans l'autre
    """

        return self + objet_a_ajouter

>>> d2 = 4 + d1

# Surcharge des opérateurs += et -= avec __iadd__

def __iadd__(self, objet_a_ajouter):
    """
        L'objet à ajouter est un entier, le nombre de secondes
    """
    # On travaille directement sur self cette fois
    # On ajoute la durée
    self.sec += objet_a_ajouter
    # Si le nombre de secondes >= 60
    if self.sec >= 60:
        self.min += self.sec // 60
        self.sec = self.sec % 60
    # On renvoie self
    return self

>>> d1 = Duree(8, 5)
>>> d1 += 128
>>> print(d1)
> '10:13'

"""
    == : def __eq__(self, objet_a_comparer):
    Renvoie True si self et objet_a_comparer son égaux

    != : def __ne__(self, objet_a_comparer):
    Renvoie True si self et objet_a_comparer sont différents

    > : def __gt__(self, objet_a_comparer):

    >= : def __ge__(self, objet_a_comparer):

    < : def __lt__(self, objet_a_comparer):

    <= : def __le__(self, objet_a_comparer):
"""

def __eq__(self, autre_duree):
    """
        Test si self et autre_duree sont égales
    """

    return self.sec == autre_duree.sec and self.min == autre_duree.min # True ou False

def __gt__(self, autre_duree):
    """
        Test si self > autre_duree
    """
    nb_sec1 = self.sec + self.min * 60
    nb_sec2 = autre_duree.sec + autre_duree.min * 60
    return nb_sec1 > nb_sec2 # True ou False

# Méthodes spéciales utiles à Pickle

# Méthode __getstate__

class Temp:
    """
        Classe contenant plusieurs attributs, dont un temporaire
    """

    def __init__(self):
        """
            Constructeur de notre objet
        """
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5

    def __getstate__(self):
        """
            Renvoie le dictionnaire d'attributs à sérialiser
        """
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr
        # Pickle enregistrera le dictionnaire modifié, dict_attr

# Unpickler.load()

    def __setstate__(self, dict_attr):
        """
            Méthode appelée lors de la désérialisation de l'objet
        """
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr
