#coding:UTF-8

#L'alphabet: Créer un programme qui affiche l'alphabet en lettres minuscules suivi d'un retour à la ligne.



#1ère solution

a = 97
z = 123

for alphabet in range(a, z):
    print(chr(alphabet), end = ",")
print()



#2ème solution 

import string
def listAlphabet():
    return list(string.ascii_lowercase)
print(listAlphabet())
print()



#3ème solution

for lettre in range(ord('a'), ord('z')+1):
    print(chr(lettre), end="")
print()

