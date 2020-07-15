#!/usr/src/python3.7 # Emplacement de Python
#-*-coding:Utf-8 #Sélection de l'encodage pour les accents


# Fichier à titre d'information. Utilisé uniquement pour répertorier les leçons


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

