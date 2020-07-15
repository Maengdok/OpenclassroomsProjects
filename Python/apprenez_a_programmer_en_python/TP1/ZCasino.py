#!user/src/Python3.7#
# -*- coding:utf-8 -*-

from random import randrange
from math import ceil

user_credit = 1000
keep_playing = True

# Credit

def credit(user_credit, user_bid, result_game):
    if result_game == "jackpot":
        user_credit = user_credit + user_bid + (user_bid  * 3)
    elif result_game == "color":
        user_credit = user_credit + user_bid + (user_bid * 0.5)
    else:
        user_credit = user_credit - user_bid

    print("Crédit:", user_credit, "€")
    return(user_credit)

# Party

def party(rand_case, user_choice):

    print("La boule est tombé sur la case:", rand_case)

    if rand_case == user_choice:
        result_game = "jackpot"
        print("Félicitation, c'est le jackpot!")
    elif rand_case % 2 == 0 and user_choice % 2 == 0:
        result_game = "color"
        print("Couleur! Félicitation!")
    elif rand_case % 2 != 0 and user_choice % 2 != 0:
        result_game = "color"
        print("Couleur! Félicitation!")
    else:
        result_game = "lose"
        print("Quel dommage! Essayez une nouvelle fois")

    return(result_game)

# Bid

def userBid(user_credit):

    user_bid = input("Veuillez faire une mise: ")
    user_bid = int(user_bid)

    if user_bid != TypeError and user_bid != NameError:
        if user_bid > 0 and user_bid <= user_credit:
            print("Vous avez misé:", user_bid, "€")
        else:
            print("Veuillez faire une mise valide.")
            userBid(user_credit)

        return(user_bid)

# Choice

def userChoice():

    user_choice = input("Veuillez choisir une case: ")
    user_choice = int(user_choice)

    if user_choice != TypeError and user_choice != NameError:
        if user_choice < 0 or user_choice > 49:
            print("Veuillez choisir une case entre 0 et et 49.")
            userChoice()

        else:
            print("Vous avez choisi le numéro:", user_choice)

    return(user_choice)

# Main


while user_credit > 0 and keep_playing == True:
    print("Crédit:", user_credit, "€")
    user_choice = userChoice()
    user_bid = userBid(user_credit)
    rand_case = randrange(50)
    result_game = party(rand_case, user_choice)
    user_credit = credit(user_credit, user_bid, result_game)
    keep_playing = input("Voulez-vous rejouer? \nO/N\n")
    if keep_playing == "O":
        keep_playing = True
    elif keep_playing == "N":
        keep_playing = False
    print("\n")
