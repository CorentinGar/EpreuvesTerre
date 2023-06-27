#coding:UTF-8

#L'alphabet à partir de: Créer un programme qui affiche l'alphabet à partir de la lettre donnée en argumennt en lettres minuscules!


choose_letter = input("Entrez la lettre désirée : ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
index = alphabet.index(choose_letter.lower())

displayAlphabet = alphabet[index:] + alphabet[:index]

result = ""
for letter in displayAlphabet:
    result += letter + " "

print(result.strip())
