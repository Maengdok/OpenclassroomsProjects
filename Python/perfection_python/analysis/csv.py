#! /usr/bin/env python3
# coding: utf-8
import os
import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging as lg

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

    def split_by_political_party(self): # Séparation des députés en fonction de leur parti politique
        result = {} # Dictionnaire
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique() # .dropna() permet de retirer les députés dont la valeur du parti est nulle et .unique() permet d'afficher les députés avec une valeur dans leur parti

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result

    def __iter__(self):
        self.iterator_state = 0
        return self

    def __next__(self):
        if self.iterator_state >= len(self):
            raise StopIteration()

        result = self[self.iterator_state]
        self.iterator_state += 1
        return result

    def __str__(self):
        names = [] ## todo: remplacer a la fin par une comprehension
        for row_index, mp in self.dataframe.iterrows(): ##todo: ici il y a du packing/unpacking
            names += [mp.nom]
        return str(names) # Python knows how to convert a list into a string

    def __repr__(self): # Nombre total de membres
        return "SetOfParliamentMember: {} members".format(len(self.dataframe))

    def __len__(self):
        return self.number_of_mps

    def __contains__(self, mp_name): # Recherche par noms
        return mp_name in self.dataframe["nom"].values

    def __getitem__(self, index): # Chercher un député avec un index
        try:
            result = dict(self.dataframe.iloc[index])
        except:
            if index < 0:
                raise Exception("Please select a positive index")
            elif index >= len(self.dataframe):
                raise Exception("There are only {} MPs!".format(len(self.dataframe)))
            else:
                raise Exception("Wrong index")
        return result

    def __add__(self, other):
        if not isinstance(other, SetOfParliamentMembers):
            raise Exception("Can not add a SetOfParliamentMember with an object of type {}".format(type(other)))

        df1, df2 = self.dataframe, other.dataframe ##todo: ici il y a du packing/unpacking
        df = df1.append(df2)
        df = df.drop_duplicates()

        s = SetOfParliamentMembers("{} - {}".format(self.name, other.name))
        s.data_from_dataframe(df)
        return s

    def __radd__(self, other): ## todo: l'implementation de cette methode ne suit a mon avis pas les bonnes pratiques
        return self

    def __lt__(self, other):
        return self.number_of_mps < other.number_of_mps

    def __gt__(self, other):
        return self.number_of_mps > other.number_of_mps

    # The following 2 methods are a way to simulate a calculated attribute
    # (attribute 'number_of_mps' is calculated from attribute 'seld.dataframe')
    # There is a much better way to do it, using decorator '@property'
    def __getattr__(self, attr):
        if attr == "number_of_mps": ##todo: faire la version avec @property
            return len(self.dataframe)

    def __setattr__(self, attr, value):
        if attr == "number_of_mps":
            raise Exception("You can not set the number of MPs!")
        self.__dict__[attr] = value ## todo: c'est l'occasion de parler de __dict__ dans le cours ;)


def launch_analysis(data_file,
                    by_party = False, info = False, displaynames = False,
                    searchname = None, index = None, groupfirst = None):
    sopm = SetOfParliamentMembers("All Members of Parliament")
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()
    if info:
        print(sopm)

    if displaynames:
        for mp in sopm:
            print(mp["nom"],":", mp["emails"])

    if searchname != None:
        is_present = searchname in sopm
        print()
        print("Testing if {} is present: {}".format(searchname, is_present))

    if index is not None:
        index = int(index)
        print()
        pprint.pprint(sopm[index]) # prints the dict a nice way

    if groupfirst is not None:
        groupfirst = int(groupfirst)
        parties = sopm.split_by_political_party()
        parties = parties.values()
        parties_by_size = sorted(parties, reverse = True)

        print()
        print("Info: the {} biggest groups are :".format(groupfirst))
        for p in parties_by_size[0:groupfirst]:
            print(p.name)

        s = sum(parties_by_size[0:groupfirst])

        s.display_chart()

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
