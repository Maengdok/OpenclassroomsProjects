#! /usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
import logging as lg
import matplotlib.pyplot as plt
import seaborn as sns

famille_panda = [
    [100, 5, 20, 80], # Maman panda
    [50, 2.5, 10, 40], # Bébé panda
    [110, 6, 22, 80], # Papa panda
]

famille_panda_numpy = np.array(famille_panda)
print("Avec Numpy:\n{}".format(famille_panda_numpy))
famille_panda_df = pd.DataFrame(famille_panda_numpy)
print("\nAvec Pandas [brut]:\n{}".format(famille_panda_df))
famille_panda_df_final = pd.DataFrame(famille_panda_numpy,
                                        index = ['maman', 'bébé', 'papa'],
                                        columns = ['pattes', 'poil', 'queue', 'ventre'])
print("\nAvec Pandas:\n{}".format(famille_panda_df_final))
print("\nColonne ventre au format Pandas:\n{}".format(famille_panda_df_final.ventre)) # == famille_panda_df_final["ventre"]
print("\nValeurs de la colonne ventre au format Numpy:\n{}".format(famille_panda_df_final["ventre"].values))

for ligne in famille_panda_df_final.iterrows():
    index_ligne = ligne[0]
    contenu_ligne = ligne[1]
    print("\nVoici le panda %s:" % index_ligne)
    print(contenu_ligne)
    print("\n----------")

print("\niloc() = indexation positionnelle:\n{}".format(famille_panda_df_final.iloc[1]))
print("\nIndexation par le label [\"papa\"]:\n{}".format(famille_panda_df_final.loc["papa"]))
print("\nVentre de 80?\n{}".format(famille_panda_df_final["ventre"] == 80))

filter = famille_panda_df_final["ventre"] == 80
panda_80 = famille_panda_df_final[filter]
print("\nPandas avec un ventre de 80 filtrés:\n{}".format(panda_80))
print("\nPandas sans un ventre de 80. Filtre inversé avec \"~\":\n{}".format(famille_panda_df_final[~filter]))

quelques_pandas = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]], # Ajout de deux nouveaux pandas
                                columns = famille_panda_df_final.columns) # Sur la même colonne que famille_panda_df_final
tous_les_pandas = famille_panda_df_final.append(quelques_pandas)
print("\nAvec les nouveaux:\n{}".format(tous_les_pandas))
print("\nRenvoie sans doublon:\n{}".format(tous_les_pandas.drop_duplicates()))

famille_panda_df_final["sexe"] = ["f", "f", "m"] # ajout d'une colonne
print("\nLe tableau compte {} pandas:\n{}".format(len(famille_panda_df_final), famille_panda_df_final))

print("\nConnaître les valeurs distinctes d'une colonne avec \".unique\":\n{}".format(famille_panda_df_final.ventre.unique()))

##################################################################

ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

fig, ax = plt.subplots() # ax == unique graphique
ax.hist(ages) # Volonté d'avoir un historiogramme dans cet unique graphique
plt.show() # Affichage du graphique

##################################################################

fig, ax = plt.subplots()
ax.pie([24, 18], # 24 femmes / 18 hommes affichés dans un diagramme circulaire
        labels = ["Femmes", "Hommes"])
plt.show()

##################################################################

fig, ax = plt.subplots()
ax.axis("equal") # Pour garder les dimensions d'un cercle et éviter une disproportion des dimensions en modifiant la taille de la fenêtre
ax.pie([24, 18],
        labels = ["Femmes", "Hommes"],
        autopct="%1.1f pourcents") # Affichage du taux de pourcentage avec un chiffre après la virgule
plt.title("Un superbe graphique")
plt.show()
