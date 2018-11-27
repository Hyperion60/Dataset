import fontforge
import os

current_path = "C:\\Users\\Hyperion\\Documents\\Create_dataset\\bin\\"

#Match les caracères avec la liste pré-définie
def found(liste, name):
    for test in liste:
        if test == name:
            return True
    return False

#Déplace les fichiers dans le dossier correspondant
def move_file(name, ttf):
    old_file = os.path.join(current_path, name)
    new_file = os.path.join(current_path + "BMP_Brut\\" + ttf + "\\", name)
    #print(new_file)
    if os.path.exists(new_file):
        new_file = os.path.join(current_path + "BMP_Brut\\" + ttf + "\\", '1' + name)
    os.rename(old_file, new_file)

def extract(filettf, ttf):
    #Lecture du fichier .tff
    F = fontforge.open(filettf)
    file = open("liste_caracteres.txt", "r")
    tmp = file.readline()
    liste = tmp.split(",")
    file.close()
    #Traitement des caractères
    i = 0
    for name in F:
        #print(name)
        if i > 2 and found(liste, name):
            filename = name + ".bmp"
            F[name].export(filename, 24, 1)
            move_file(filename, ttf)
        i += 1

def main():
    accu = ""
    i = 0
    #Ouverture des fichiers .ttf
    listfile = os.listdir(current_path + "Fonts\\")
    for ttf in listfile:
        accu = ""
        i = 0
        while ttf[i] != ".":
            accu += ttf[i]
            i += 1
        #Création d'un dossier pour chaque font
        os.makedirs(current_path + "BMP_Brut\\" + accu)
        extract(current_path + "Fonts\\" + ttf, accu)

main()