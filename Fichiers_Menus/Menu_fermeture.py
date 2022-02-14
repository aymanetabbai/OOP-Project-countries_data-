#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:43:56 2020


"""

import os
import pickle
import runpy
from Fichiers_Menus.Menu import menu
from Fichiers_Menus.Menu_ouverture import menu_ouverture
import Global_config.config_global as config_global



if __name__=='__main__':
    with open("Messages_menus/message_menu_fermeture.pkl", 'wb') as fichier_menu_close:
        message_close="Merci d'avoir utilise notre application!!"
        pickle.dump(message_close,fichier_menu_close)
        fichier_menu_close.close()
class menu_fermeture(menu):
    with open("Messages_menus/message_menu_fermeture.pkl", 'rb') as fichier_menu_close:
        message_fermeture=pickle.load(fichier_menu_close)
    def __init__(self,dico_taches,dico_messages):
        self.dico_taches=dico_taches
        self.dico_messages=dico_messages
    def afficher_menu_fermeture(self):
        print("Voulez-vous retourner au menu d'ouverture?")
        print("O: oui")
        print("N: non")
        
        while True:
            try:
                reponse=input()
                if reponse not in ["O","o","N","n"]:
                    print("Veuillez entrer une reponse valide pour continuer")
                    print("      ")
                if reponse in ["O","o"]:

                        runpy.run_module("Global_config.config_global",run_name="__initial__")
                        config_global.redemarrer_application=True
                        break
                else:
                    self.fermer_menu_fermeture()
                    break
            except NameError:
                print("Veuillez entrer une reponse valide sous forme de string")
                self.afficher_menu_fermeture()
    
    def fermer_menu_fermeture(self):
        print(self.message_fermeture)
        print(".....")

        print(".............")
        
            
        
        