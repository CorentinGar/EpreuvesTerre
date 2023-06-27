#coding:UTF-8

#Nom du programme: Créer un programme qui affiche son nom de fichier!


import os

def display_name_file(path_file):
    name_file = os.path.basename(path_file)
    print("Nom du fichier :", name_file)


path_file = "/bin/python /home/dangvannghia/Documents/Terre01.py"
display_name_file(path_file)