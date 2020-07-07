#! /usr/bin/env python3
# coding: utf-8

class MyIterator:
    def __init__(self):
        print("Je m'initialise à 0")
        self.i = 0
    def __iter__(self):
        print("J'ai appelé __iter__")
        return self
    def __next__(self):
        print("J'ai appelé __next__")
        self.i += 2
        if self.i > 30:
            raise StopIteration()
        return self.i

for i in MyIterator():
    print(i)
myIteratorListed = list(MyIterator())
myIteratorSummed = sum(MyIterator())
print(myIteratorListed)
print(myIteratorSummed)

#######################################

def generator(beginning, end):
    print("    On commence !")

    cpt = beginning
    while cpt <= end:
        if cpt % 2 == 0:
            print("    On s'arrete au yield")
            yield float(cpt)
            print("    On reprend après le yield")
        else:
            print("    On s'arrete au yield")
            yield str(cpt)
            print("    On reprend après le yield")
        cpt += 1
    yield "C'est bientôt la fin"
    yield "C'est VRAIMENT bientôt la fin"
    yield "Là c'est la fin" # Mot clef yield est un générateur. Utilisé pour simplifier la création d'itérateurs

for i in generator(4, 8):
    print(i)

#########################################

gen = (2 * x for x in range(3))
print(gen)
print(sum(gen))

#########################################
# EXEMPLE D'UTILISATION DES GENERATEURS #
#########################################

import re

big_data = """Le sénateur, dont il a été parlé plus haut, était un homme entendu qui
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt.
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)"""

def is_part_of_a_word(character):
    return len(re.findall('\w', character, flags = re.UNICODE)) # \w mots alphanumérics + "_"

def get_words(text): # Lecture de la chaîne de caractère et découpe du texte en liste de mots
    print("Je commence à lire le texte maintenant")

    words = []
    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                words += [current_word]
                current_word = ""
        else:
            current_word += character
    return words

def filter_by_size(words): # Filtre les mots >= à 6 lettres
    return [w for w in words if len(w) >= 6]

def filter_by_letters(words): # Filtre les mots possédant la lettre "a"
    return [w for w in words if "a" in w]

words = get_words(big_data)
print("Nombre de mots: %i" % len(words))
words = filter_by_size(words)
print("Nombre de mots ayant plus de 6 lettres: %i" % len(words))
words = filter_by_letters(words)
print("Nombre de mots ayant plus de 6 lettres et possédant la lettre \"a\": %i" % len(words))

print(words)

print("\nCependant, si le texte est plus long que, les mots enregistrés dans get_words peuvent faire planter le pc.\nVoici donc l'utilité des générateurs comme yield:\n")

def get_words(text):
    print("Je commence à lire le texte maintenant")

    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                yield current_word
                current_word = ""
        else:
            current_word += character

def filter_by_size(words):
    return (w for w in words if len(w) >= 6)

def filter_by_letters(words):
    return (w for w in words if "a" in w)

words = get_words(big_data)
words = filter_by_size(words)
words = filter_by_letters(words)
print("'words' est encore un générateur. Le texte n'a toujours pas été lu")

print("L'opération suivante va lancer la lecture du texte: ")
print([w for w in words])
