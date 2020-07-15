#usr/src/python3.7
# -*- coding:utf-8 -*-

inventaire = {
    "pommes": 22,
    "melons": 4,
    "poires": 18,
    "fraises": 76,
    "prunes": 51,
    }

print(inventaire)

dict_rev = [(valeur, clef) for clef, valeur in inventaire.items()]

print(dict_rev)

inventaire = [(clef, valeur) for valeur, clef in sorted(dict_rev, reverse = False)]

print(inventaire)
