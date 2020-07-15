#!usr/src/Python3.7
# -*- coding:utf-8 -*-

""" Module multiply contenant la fonction table """

def table(nb, max=10):
    """ Fonction affichant la table de multiplication par nb de 1 * nb jusqu"à max * nb """
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# Test de la fonction table

if __name__ == "__main__":
    table(27, 10)
