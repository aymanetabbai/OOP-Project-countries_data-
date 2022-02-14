#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:52:37 2020


"""
import os
from Fichiers_user.Consultant import consultant
import Global_config.config_global as config_global




class menu:
    def __init__(self,dico_taches,dico_messages):
        self.dico_taches=dico_taches
        self.dico_messages=dico_messages
    
    def afficher_menu(self,utilisateur_en_cour):
        for numero_tache,tache in self.dico_messages.items():
            print(str(numero_tache)+":  "+tache)
        
        while True:
            try:
                num_tache=input("Entrer le numero de la tache desiree:  ")
                num_tache=int(num_tache)
                if num_tache in self.dico_taches.keys():
                    break
                elif isinstance(utilisateur_en_cour,consultant) and num_tache==3:
                    config_global.quitter_menu_tache_consultant=True
                    break
                else:
                    print("Veuillez selectionner une tache dans la liste")
            except NameError:
                print("Veuillez entrer un numero sous forme de int")
            except ValueError:
              
                print("Veuillez entrer un choix sous la forme d'un entier")
        if not config_global.quitter_menu_tache_consultant:
            
            try:
                getattr(utilisateur_en_cour,self.dico_taches[num_tache])()
                if not isinstance(utilisateur_en_cour,consultant):
                    
                    utilisateur_en_cour.historique.append(self.dico_messages[num_tache])
                    if len(utilisateur_en_cour.historique)>10:
                        utilisateur_en_cour.historique.pop(0)
            except KeyError:
                raise KeyError("La tache que vous avez selectionnee n'est pas dans votre nombre de taches autorisees ou elle n'existe pas")
        
    def fermer_menu(self):
        print("")
        print("      ")
            
            