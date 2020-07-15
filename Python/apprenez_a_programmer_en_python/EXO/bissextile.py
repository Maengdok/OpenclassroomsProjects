#!/usr/src/python3.7
# -*- coding: utf-8 -*-

user_entry = input("Entrez une année: ")
print(user_entry)
user_entry = int(user_entry)
bissextile = False # Déclaration d'un booléen

if user_entry % 400 == 0:
    bissextile = True
elif user_entry % 100 == 0:
    bissextile = False
elif user_entry % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print (user_entry, " est une année bissextile")
else:
    print (user_entry, " n'est pas une année bissextile")
