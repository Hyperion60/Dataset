# Dataset
Dataset pour entrainer un réseau de neurone sur des caractères imprimés

Ce programme permet d'exporter les caractères contenus dans une font en image bitmap (.bmp) carré de la taille de votre choix.

## Utilisation

* Créer les dossiers `BMP_Brut\` et `BMP_Traite` dans `\bin\` 
* Mettre les fichiers de font (au format .ttf) que vous souhaitez extraire dans le dossier `\bin\Fonts`.
* Ouvrir le fichier `\bin\extract.py` et entrez la taille de l'image dans la variable nommée `resolution`. Et modifier la variable `current_path` pour la faire correspondre à l'emplacement du fichier sur la machine. **/!\ N'oubliez pas de doubler les backslash**.
* Lancer un terminal à l'emplacement de `extract.py` et executer la commande suivante : `ffpython.exe extract.py`
Cette commande va extraire toutes les lettres de tous les fichiers .ttf placé dans le dossier \Fonts. Le format de sortie sera le suivant : un dossier sera créé pour chaque font, et le nom de la font sera le nom du dossier. Et les images bitmap resultantes auront pour hauteur la valeur entrée précedemment + 1.

La deuxième étape consiste à donner un format carré aux images fraîchement créée.
* Ouvrir le fichier `\bin\resize.py` et modifier la variable `current_path` pour la faire correspondre à l'emplacement du fichier sur la machine. **/!\ N'oubliez pas de doubler les backslash**. Et entrez la **même** valeurs dans la variable `resolution` que celle entrée dans `extract.py`.
* Lancer un terminal à l'emplacement de `resize.py` et exectuer la commande suivante `python resize.py`.
* Vous pouvez ensuite récupérer vos fichiers dans le dossier `\bin\BMP_Traite`

## Réglage

Pendant l'extraction, les caractères sont matchés avec une liste de nom de caractère stocké dans le fichier `\bin\liste_caracteres.txt`. Si le nom du caractère testé est dans la liste, alors il est exporté en image. Sinon le programme passe directement au suivant.
Pour récupérer dans la liste tout les noms d'une font afin de pouvoir personnaliser le matching, vous devez utiliser le fichier `\bin\edit_list.py`.
* Ouvrir un terminal à l'emplacement du fichier `edit_list.py` et executer la commande : `ffpython.exe edit_list.py`
* A la fin du programme, le fichier `liste_caracteres.txt` a été modifié.
