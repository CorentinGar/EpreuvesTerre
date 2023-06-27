#coding:UTF-8

#Nom du programme: Créer un programme qui affiche son nom de fichier.


import os

def afficher_nom_fichier(chemin_fichier):
    nom_fichier = os.path.basename(chemin_fichier)
    print("Nom du fichier :", nom_fichier)


chemin_fichier = "/bin/python /home/dangvannghia/Documents/Terre01.py"
afficher_nom_fichier(chemin_fichier)