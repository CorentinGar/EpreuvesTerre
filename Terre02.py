#coding:UTF-8

#Afficheur d'arguments: Créer un programme qui affiche les arguments qu'il reçoit ligne par ligne!


import sys

def displayArgument():
    arguments = sys.argv[1:]    
    for argument in arguments:
        print(argument)

displayArgument()