from PIL import Image
import os

current_path = "C:\\Users\\Hyperion\\Documents\\Create_dataset\\bin\\"
resolution = 24 #Mettre la même résolution que dans extract.py

#Nettoyage de la liste des fichiers
def clean_list_file(filelist):
    newfilelist = []
    for element in filelist:
        if element[-3] != '.' and element[-4] != '.':
            newfilelist.append(element)
    return newfilelist


#Création de l'image de sortie
def Bmp_nxn(n):
    img = Image.new("L", (n, n), 255)
    return img

#Traitement de l'image
def merge (image_in, image_out, x, z):
    if x % 2 == 0:
        y = (resolution - x) // 2
    else:
        y = (resolution - (x - 1)) // 2
    pixel_in = image_in.load()
    pixel_out = image_out.load()
    for i in range(y, y + x):
        for j in range (resolution + 1):
            if pixel_in[i - y, j] == 0:
                pixel_out[i,j] = 0

def main():
    #Parcours de tous les fichiers
    listdir = os.listdir(current_path + "BMP_Brut\\")
    listdir = clean_list_file(listdir)
    for directory in listdir:
        listfile = os.listdir(current_path + 'BMP_Brut\\' + directory + "\\")
        os.makedirs(current_path + 'BMP_Traite\\' + directory)
        for file in listfile:
            image_out = Bmp_nxn(resolution + 1)
            image_in = Image.open(current_path + 'BMP_Brut\\' + directory + "\\" + file)
            (width, height) = image_in.size
            merge(image_in, image_out, (width % (resolution + 1)), height)
            #Sauvegarde de l'image à la fin du traitement
            image_out.save(current_path + 'BMP_Traite\\' + directory + '\\' + file)

main()
print("Traitement terminé")
