#! /usr/bin/env python3
# coding: utf-8

"""
This is the docstring of parite.py
This code is used to learn some specification of python
You can find this course here:
https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463152-tirez-parti-de-ce-cours
"""

import argparse
import logging as lg
import re # Librairie pour les expressions régulières

import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments(): # ex: python -d current_mps.csv -e csv -i
    """
    Docstring for the parse_arguments. function that allows us to add arguments
    while analyzing a file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse.
                        Is it a CSV or an XML?""") # File's extension. ex: "-e csv"
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of
                        information about the members of parliament""")
                        # File's name.extension. ex: "-d current_mps.cvs"
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="""Make the application talk!""")
    parser.add_argument("-p", "--byparty", action='store_true', help="""displays
                        a graph for each political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""information about
                        the file""")
    parser.add_argument("-n", "--displaynames", action='store_true', help="""displays
                        the names of all the mps""")
    parser.add_argument("-s", "--searchname", help="""search for a mp name.
                        ex: "Barbara Bessot Ballot" """)
    parser.add_argument("-I", "--index", help="""displays informations about the Ith mp""")
    parser.add_argument("-g", "--groupfirst", help="""displays a graph groupping all the 'g'
                        biggest political parties. ex: -g 5""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile is None:
            raise Warning('You must indicate a datafile!')
    except Warning as err:
        lg.warning(err) # log d'erreur pour éviter la surcharge de print()
    else:
        e = re.search(r'^.+\.(\D{3})$', args.datafile)
        # Recherche de l'expression régulière <nom du fichier>.3lettres
        # (csv, txt, xml, etc...)
        extension = e.group(1)
        # Ayant séparé l'expression en deux groupes: ^.+\. et (\D{3})$,
        # nous recherchons uniquement la deuxième partie de l'expression: (\D{3})
        if extension == 'xml':
            x_an.launch_analysis(datafile)
        elif extension == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info, args.displaynames,
                                 args.searchname, args.index, args.groupfirst)
    finally:
        if args.verbose:
            lg.basicConfig(level=lg.INFO)
            lg.info('#################### Analysis is over ######################')
