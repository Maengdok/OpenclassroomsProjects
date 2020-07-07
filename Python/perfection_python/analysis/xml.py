import os
import logging as lg

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path
    path_to_file = os.path.join(directory, "data", "xml", "compteRendu", data_file) # with this path, we go inside the folder "data", "xml" then "compteRendu"  and get the file.

    with open(path_to_file,"r") as f:
        preview = f.readline()
        print(preview)

if __name__ == "__main__":
    launch_analysis('SyceronBrut.xml')
