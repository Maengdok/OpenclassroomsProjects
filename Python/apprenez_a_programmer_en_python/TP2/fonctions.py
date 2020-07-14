import os
import pickle
from random import choice

from donnees import *


def get_scores():
    if os.path.exists(file_name):
        player_list = open(file_name, "rb")
        my_depickler = pickle.Unpickler(player_list)
        scores = my_depickler.load()
        player_list.close()
    else:
        scores = {}
    return scores

def save_scores(scores):
    player_list = open(file_name, "wb")
    my_pickler = pickle.Pickler(player_list)
    my_pickler.dump(scores)
    player_list.close()

def get_user_name():
    user_name = input("Veuillez entrer un pseudo:\n")
    user_name = user_name.capitalize()
    if not user_name.isalnum() or len(user_name) < 4:
        print("Ce nom est invalide.")
        return get_user_name()
    else:
        return user_name

def get_letter():
    letter = input("Veuilllez entrer une lettre:\n")
    letter = letter.capitalize()
    if not letter.isalpha() or len(letter) > 1 or len(letter) < 0:
        print("Letter invalide.")
        return get_letter()
    else:
        return letter


def get_word():
    full_word = choice(words)

    return full_word.upper()

def get_hidden_word(full_word):
    hidden_word = []
    full_word_length = len(full_word)
    caract = "*"
    i = 0
    while i <= full_word_length:
        hidden_word.append(caract)
        i += 1
    print("".join(hidden_word))
    return hidden_word

def insert_letter(full_word, letter_found):
    hidden_word = ""

    for letter in full_word:
        if letter in letter_found:
            hidden_word += letter
        else:
            hidden_word += "*"
    return hidden_word
