#coding:UTF-8

#Afficheur d'arguments: Créer un programme qui affiche les arguments qu'il reçoit ligne par ligne. 



#1ère solution



import sys

def diplayArgument():
    arguments = sys.argv[1:]    
    for argument in arguments:
        print(argument)

diplayArgument()