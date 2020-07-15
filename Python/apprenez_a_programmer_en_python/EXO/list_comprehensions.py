#!user/src/python3.7
# -*- coding:utf-8 *-*

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
    ]

## Afin de pouvoir trier le nombre de fruits, on doit inverser l'ordre entre les noms et les chiffres

list_rev = [(nb_fruits, nom) for nom, nb_fruits in inventaire] # On fait passer les chiffres avant les les noms dans la liste inventaire 
inventaire = [(nom, nb_fruits) for nb_fruits, nom in sorted(list_rev, reverse = True)] # Puis on trie list_rev avec sorted afin de placer les plus grands chiffres en premier. Une fois cela fait, on refait passer les noms avant les chiffres dans la liste
print(inventaire)
