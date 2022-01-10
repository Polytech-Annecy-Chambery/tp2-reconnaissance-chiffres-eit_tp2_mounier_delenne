from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im = image.binarisation(S) #On met en forme l'image qu'on veut reconnaitre
    im = im.localisation()
    nb_similitude = 0 #On initialise le nombre de similitudes maximum
    entier_lpr = 0  #Entier le plus ressemblant à l'image dans la liste_modeles 
    for i in range (len(liste_modeles)):  #On parcourt liste_modele
        im = im.resize(liste_modeles[i].H,liste_modeles[i].W)
        #On redimensonne l'image de façon à etre dans la même dimension que
        #celle qu'on cherche dans la liste_modeles
        if nb_similitude<im.similitude(liste_modeles[i]):
            nb_similitude = im.similitude(liste_modeles[i])
            entier_lpr = i
    return entier_lpr    #Ca retourne l'entier reconnu
            

