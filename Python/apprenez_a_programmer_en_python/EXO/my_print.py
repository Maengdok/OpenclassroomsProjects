#!usr/src/python3.7
# -*- coding:utf-8 -*-

def afficher(*parametres, sep=" ", fin='\n'):

    parametres = list(parametres)

    chaine = sep.join(parametres)
    chaine += fin
        
    print(parametres, end='\n')

chaine = str(input("Veuillez entrer le nombre paramêtres que vous voulez afficher\n"))
",".join(chaine)
afficher(chaine)
