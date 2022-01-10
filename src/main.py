'''
File: main.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Aug 30 2021
Modified By: Ammar Mian
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''
import matplotlib.pyplot as plt
from image import Image
from reconnaissance import reconnaissance_chiffre, lecture_modeles


if __name__ == '__main__':

    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion() # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display

    #==============================================================================
    # Lecture image et affichage
    #==============================================================================
    image = Image()
    image.load(path_to_assets + 'test7.JPG')
    image.display("Exemple d'image")
    
    image2 = Image()
    image2.load(path_to_assets + 'test2.JPG')
    image2.display("Exemple d'image")

    image3 = Image()
    image3.load(path_to_assets + 'test2.JPG')
    image3.display("Exemple d'image")
    
    image4 = Image()
    image4.load(path_to_assets + 'test8.JPG')
    image4.display("Exemple d'image")
    
    #==============================================================================
    # Binarisation de l'image et affichage
    #==============================================================================
    S = 100
    image_binarisee = image.binarisation(S)
    image_binarisee.display("Image binarisee")

    #==============================================================================
    # Localisation de l'image et affichage
    #==============================================================================
    image_localisee = image_binarisee.localisation()
    image_localisee.display("Image localisee")

    #==============================================================================
    # Redimensionnement de l'image et affichage
    #==============================================================================
    image_resizee = image_localisee.resize(300, 100)
    image_resizee.display("Image redimensionee")

    #==============================================================================
    # Lecture modeles et reconnaissance
    #==============================================================================
    liste_modeles = lecture_modeles(path_to_assets)
    chiffre = reconnaissance_chiffre(image, liste_modeles, 5)
    print("Le chiffre reconnu est : ", chiffre)
