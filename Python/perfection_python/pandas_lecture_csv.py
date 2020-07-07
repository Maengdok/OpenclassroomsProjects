#! /usr/bin/env python3
# coding: utf-8
import os
import pandas as pd

class SetOfParliamentMembers: # Ensemble des députes
    def __init__(self, name): # Chaque ensemble à un nom
        self.name = name

    def data_from_csv(self, csv_file): # Lecture des données dans le fichier csv
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe # dataframe = liste des députés stockée

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        # Séparation des députés en fonction de leur parti politique
        result = {} # Dictionnaire
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()
        # .dropna() permet de retirer les députés dont la valeur du parti est nulle et
        # .unique() permet d'afficher les députés avec une valeur dans leur parti

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()
