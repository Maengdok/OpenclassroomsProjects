from donnees import *
from fonctions import *

# MAIN
def main():

    scores = get_scores()
    user_name = get_user_name()

    if user_name not in scores.keys():
        scores[user_name] = 0 # Gives a score to the new user

    keep_playing = "O"

    while keep_playing != "N":
        print("Nom du joueur: {}".format(user_name))
        already_picked = []
        chances = nb_try

        full_word = get_word()
        hidden_word = get_hidden_word(full_word)

        while chances > 0 and hidden_word != full_word:
            print("Nombre de tentative(s) restante(s): {}".format(chances))
            letter = get_letter()

            if letter in already_picked:
                print("Vous avez déjà trouvé avec cette lettre.")
            elif letter in full_word:
                already_picked.append(letter)
            else:
                chances -= 1
                print("Cette lettre n'est pas dans le mot...")
            hidden_word = insert_letter(full_word, already_picked)
            print(hidden_word)

        if hidden_word == full_word:
            print("Félicitations ! Vous avez trouvé le mot {}".format(hidden_word))

        else:
            print("Vous avez perdu!")

        scores[user_name] += chances

        keep_playing = input("Voulez-vous rejouer ? (O/N)\n")
        keep_playing = keep_playing.capitalize()

    save_scores(scores)
    print("Voici votre score final: {} points".format(scores[user_name]))



if __name__ == "__main__":
    main()
