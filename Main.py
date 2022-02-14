#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:16:00 2020

@author: macbookair
"""

import os
import pickle
import pandas
import numpy
import random
import matplotlib.pyplot as plt
import runpy
import pydoc
import Fichiers_user.Consultant as Consultant
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from Fichiers_Menus.Menu_ouverture import menu_ouverture

import Fichiers_Menus.Menu_fermeture as Menu_fermeture

import Fichiers_Menus.Menu as Menu

from Fichiers_user.Utilisateurs_connecte import Admin,Geographe

from Fichiers_user.Consultant import consultant

import Configurations_bases.Base_utilisateurs as Base_utilisateurs

from Fichiers_user.Data_scientist import Data_s

import Global_config.config_global as config_global

import Configurations_bases.BasePays as BasePays

from Fichiers_user.UtilisateurPrive import utilisateurPrive




#%%%
## Cette partie sert à charger la base utilisateur avant le début de l'application
## Si cette base n'est pas présente dans le fichier recherché:
##### à l'aide du module runpy on fait tourner le fichier ""Configurations_bases/Base_utilisateurs"
##### sous le nom "__base__user__generate__" ce qui permet de recréer une base vide 
##### à l'emplacement désiré puis de la charger avec le module pickle
try:
    
    with open("bases_appli/Base_utilisateurs.pkl","rb") as fichier_users:
        setattr(Base_utilisateurs.Base_users,"dico_users",pickle.load(fichier_users))
except FileNotFoundError:

    runpy.run_module("Configurations_bases.Base_utilisateurs",run_name='base_users_generate')
    with open("bases_appli/Base_utilisateurs.pkl","rb") as fichier_users:
        setattr(Base_utilisateurs.Base_users,"dico_users",pickle.load(fichier_users))

#%% 
## Cette fonction sert à sauvegarder la base utilisateur dans le dossier 
## "bases_appli" son principal but est d'assurer la non perte de cette base en cas de
## fermeture de l'application

def sauvegarder_base_utilisateurs():
    """Cette fonction sauvegarde la base utilisateur dans le fichier  "bases_appli/Base_utilisateurs.pkl" """

    fichier_base=open("bases_appli/Base_utilisateurs.pkl","wb")
    Admin.__module__="Fichiers_user.Utilisateurs_connecte"
    Geographe.__module__="Fichiers_user.Utilisateurs_connecte"
    consultant.__module__="Fichiers_user.Consultant"
    Data_s.__module__="Fichiers_user.Data_scientist"
    pickle.dump(Base_utilisateurs.Base_users.dico_users,fichier_base)

#%%
## Cette fonction sert à actualiser la base utilisateurs à partir du fichier associé


def actualiser_base_utilisateurs():
    """Cette fonction actualise la base utilisateur à partir du fichier "bases_appli/Base_utilisateurs.pkl" """
    
    
    fichier_base=open("bases_appli/Base_utilisateurs.pkl","rb")
    Admin.__module__="Fichiers_user.Utilisateurs_connecte"
    Geographe.__module__="Fichiers_user.Utilisateurs_connecte"
    consultant.__module__="Fichiers_user.Consultant"
    Data_s.__module__="Fichiers_user.Data_scientist"
    setattr(Base_utilisateurs.Base_users,"dico_users",pickle.load(fichier_base))



#%%%    
## On crée un admin pour avoir accès à l'application en tant qu'admiistrateur
utilisateur_pour_moi=Admin("ajey99","azerty",0,[])
Base_utilisateurs.Base_users.dico_users["ajey99"]=utilisateur_pour_moi
sauvegarder_base_utilisateurs()

#%%


def renvoyer_dico_taches_messages(utilisateur):
    """ Cette fonction renvois le dictionnaire de tache associé à un type utilisateur"""
    
    """@param: utilisateurPrive or consultant
        @return : dict
        """
    
    global Dictionnaire_taches_utilisateur
    Dictionnaire_taches_utilisateur={}
    global Dictionnaire_messages_utilisateur
    Dictionnaire_messages_utilisateur={}
    if isinstance(utilisateur,consultant):
        Dictionnaire_taches_utilisateur={1: "afficher_pays",
                                         2: "proposer_correction"}
        Dictionnaire_messages_utilisateur={1: "afficher un pays",
                                          2: "proposer une correction",
                                          3: "quitter_menu_taches"}
    elif isinstance(utilisateur,Geographe) and  (not isinstance(utilisateur,Admin)):
        Dictionnaire_taches_utilisateur={1: "afficher_pays",
                                         2:"accepter_proposition_correction",
                                         3: "ajouter_pays",
                                         4: "Modifier_pays",
                                         5: "deconnexion",
                                         6: "afficher_historique"}
        Dictionnaire_messages_utilisateur={1: "afficher un pays",
                                         2:"accepter une proposition de correction",
                                         3: "ajouter un pays",
                                         4: "Modifier un pays",
                                         5: "Deconnexion",
                                         6: "Afficher l'historique des actions"}
    elif isinstance(utilisateur,Admin):
        Dictionnaire_taches_utilisateur={1: "afficher_pays",
                                         2:"accepter_proposition_correction",
                                         3: "ajouter_pays",
                                         4: "Modifier_pays",
                                         5: "supprimer_pays",
                                         6: "ajouter_utilisateur",
                                         7: "supprimer_utilisateur",
                                         8: "resume_d_info",
                                         9: "representation_graphique",
                                         10: "clustering_classes",
                                         11: "deconnexion",
                                         12: "afficher_historique"}
        Dictionnaire_messages_utilisateur={1: "afficher un pays",
                                         2:"accepter une proposition correction",
                                         3: "ajouter un pays",
                                         4: "Modifier un pays",
                                         5: "supprimer un pays",
                                         6: "ajouter un utilisateur",
                                         7: "supprimer un utilisateur",
                                         8: "affihcer resume d'info",
                                         9: "afficher une representation graphique",
                                         10: "Tri des pays en fonction des classes",
                                         11: "Deconnexion",
                                         12: "Afficher l'historique des actions"}
        
    elif isinstance(utilisateur,Data_s):
        Dictionnaire_taches_utilisateur={1:"afficher_pays",
                                         2: "representation_graphique",
                                         3: "proposer_correction",
                                         4: "resume_d_info",
                                         5: "clustering_classes",
                                         6: "deconnexion",
                                         7: "afficher_historique"}
        Dictionnaire_messages_utilisateur={1:"afficher un pays",
                                         2: "afficher representation graphique",
                                         3: "proposer un correction",
                                         4: "afficher resume d'info",
                                         5: "Tri des pays en fonction des classes",
                                         6: "Deconnexion",
                                         7: "Afficher l'historique des actions"}
    
    else:
        raise TypeError("La classe d'utilisateur n'est pas connue")
def Lancer_application():
    """Cette Fonction lance l'application """
    """
    @param: void
    @return: void
    """

    Menu_open=menu_ouverture()
    Menu_open.afficher_menu_ouverture()
    try:
        if config_global.utilisateur_qui_se_connecte!=None:
            print(":::::::")
            print(":::::::")
            print("       ")
            print("        ")
            config_global.utilisateur_en_cour=config_global.utilisateur_qui_se_connecte
        else:
            
            config_global.utilisateur_en_cour=config_global.utilisateur_qui_se_connecte_pas
    except NameError:
        print("Les deux utilisateurs ne sont pas bien definis")

    renvoyer_dico_taches_messages(config_global.utilisateur_en_cour)
    Menu_taches=Menu.menu(Dictionnaire_taches_utilisateur,Dictionnaire_messages_utilisateur)

    if isinstance(config_global.utilisateur_en_cour,utilisateurPrive):
        while config_global.utilisateur_en_cour.etat==1:
            try:
                
                BasePays.actualiser_base_pays()
                BasePays.actualiser_base_corrections()
                BasePays.actualiser_cinq_c_age()
                actualiser_base_utilisateurs()
                Menu_taches.afficher_menu(config_global.utilisateur_en_cour)
                
                print(" ")
                print(" ")
                print("1: Quitter le Menu des taches et vous deconnecter")
                print("2: Retourner au Menu des taches")
                quitter_menu_taches=input("Voulez vous quitter le menu des taches ou retourner au menu:  ")
                quitter_menu_taches=int(quitter_menu_taches)
                print("    ")
                print("     ")
                if quitter_menu_taches not in [1,2]:
                    print("Veuillez effectuer un choix valide")
                elif quitter_menu_taches==1:
                    Menu_taches.fermer_menu()
                    config_global.utilisateur_en_cour.deconnexion()
                    sauvegarder_base_utilisateurs()
                    break
                else:
                    sauvegarder_base_utilisateurs()
                    BasePays.sauvegarder_base_correction()
                    BasePays.sauvegarder_cinq_c_age()
                    BasePays.sauvegarder_base_pays()
    
            except NameError:
                print("Veuillez entrer 1 ou 2 comme choix")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un entier")
        Menu_close=Menu_fermeture.menu_fermeture({},{})
        Menu_close.afficher_menu_fermeture()
        if config_global.redemarrer_application:
            Lancer_application()
        
        exit()         
    else:
        config_global.quitter_menu_tache_consultant=False
        while not config_global.quitter_menu_tache_consultant:
            try:
                BasePays.actualiser_base_pays()
                BasePays.actualiser_base_corrections()
                BasePays.actualiser_cinq_c_age()
                actualiser_base_utilisateurs()
                Menu_taches.afficher_menu(config_global.utilisateur_en_cour)
                print(" ")
                print(" ")
                print("1: Quitter le Menu des taches et vous deconnecter")
                print("2: Retourner au Menu des taches")
                quitter_menu_taches=input("Voulez vous quitter le menu des taches ou retourner au menu:  ")
                quitter_menu_taches=int(quitter_menu_taches)
                print("    ")
                print("     ")
                if quitter_menu_taches not in [1,2]:
                    print("Veuillez effectuer un choix valide")
                elif quitter_menu_taches==1:
                    Menu_taches.fermer_menu()
                    sauvegarder_base_utilisateurs()
                    break
                else:
                    sauvegarder_base_utilisateurs()
                    BasePays.sauvegarder_base_correction()
                    BasePays.sauvegarder_cinq_c_age()
                    BasePays.sauvegarder_base_pays()
                    
            except NameError:
                print("Veuillez entrer 1 ou 2 comme choix")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un entier")
        Menu_close=Menu_fermeture.menu_fermeture({},{})
        Menu_close.afficher_menu_fermeture()
        if config_global.redemarrer_application:
            Lancer_application()
    exit()   



if __name__=="__main__":
    Lancer_application()
    
        
