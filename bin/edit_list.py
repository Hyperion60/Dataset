import fontforge
import os

current_path = "C:\\Users\\Hyperion\\Documents\\Create_dataset\\bin\\Fonts\\"
ttf_ref = "times.ttf"

#Ouverture du fichier .ttf
F = fontforge.open(current_path + ttf_ref)

#Ouverture du fichier .txt
file = open("liste_caracteres.txt", "w")
listecaractere = ""

i = 0
for name in F:
    listecaractere += name
    listecaractere += ','

listecaractere = listecaractere[:-1]

file.write(listecaractere)
file.close()