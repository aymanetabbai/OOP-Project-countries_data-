#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:20:52 2020


"""

import pickle
import os






from Fichiers_Menus.Menu import menu
from Configurations_bases.Base_utilisateurs import Base_users
import Fichiers_user.Data_scientist as Data_scientist
import Fichiers_user.Utilisateurs_connecte as Utilisateurs_connecte
import Fichiers_user.Consultant as Consultant
import Global_config.config_global as config_global


if __name__=='__main__':
    with open("Messages_menus/message_menu_ouverture.pkl", 'wb') as fichier_menu_open:
        message_open="Bienvenu dans notre applcation \n Veuillez selectionner une action pour continuer"
        pickle.dump(message_open,fichier_menu_open)
        fichier_menu_open.close()
                        
    
class menu_ouverture(menu):
    with open("Messages_menus/message_menu_ouverture.pkl", 'rb') as fichier_menu_open:
        message_bienvenu=pickle.load(fichier_menu_open)
        
    
    def __init__(self,dico_taches={"connexion":"afficher_menu_connexion"},dico_messages={}):
        self.dico_taches=dico_taches
        self.dico_messages=dico_messages
    def afficher_menu_ouverture(self):
        passer=True
        print("Bienvenu Dans Notre application !!!!!")
        print("Voulez vous vous connecter?")
        while passer:
            try:
                reponse_connexion=input("1:Oui \n2:Non \n ")
                reponse_connexion=int(reponse_connexion)
                if reponse_connexion not in [1,2]:
                    print("Veuillez entrer une reponse valide")
                else:
                    if reponse_connexion in [1,str(1)]:
                        self.afficher_menu_connexion()
                        break
                    else:
                        config_global.utilisateur_qui_se_connecte_pas=Consultant.consultant()
                        self.fermer_menu_ouverture()
                        break
            except NameError :
                print("veuillez entrer un reponse valide")
            except ValueError:
                print("Veuillez entrer une réponse sous forme d'entier")
                
        
    def fermer_menu_ouverture(self):
        print("Merci de patienter")
        print(".....")
        print(".............")
    def afficher_menu_connexion(self):
        print("Selectionnez votre type de compte parmi ces choix  ")
        print("1: Geographe   ")
        print("2: Data scientist   ")
        print("3: Admin   ")
        print("4: pour retourner en arriere")

        while True:
            try:
                type_compte=input()
                type_compte=int(type_compte)
                if type_compte not in [1,2,3,4]:
                    print("Veuillez rentrer une reponse parmi 1, 2 ou 3")
                else:
                    break
            except NameError :
                print("Veuillez rentrer une reponse parmi 1, 2 ou 3")
            except ValueError:
                print("Veuillez entrer une réponse sous la forme d'un entier")
        
        if type_compte==4:
            self.afficher_menu_ouverture()
            exit()

        print("identifiant::")
        while True:
            try:
                username=input("Entrer votre nom d'utilisateur:  ")
                if len(str(username))>10 or type(username)!=str:
                    username=username=input("Entrer votre nom d'utilisateur entre crochets sans depasser 10 caracteres")
                elif username  not in Base_users.dico_users.keys():
                    print("Ce Nom d'utilisateur n'existe pas" )
                else:
                    break
            except NameError or SyntaxError:
                print("Veuillez entrer votre nom d'utilisateur entre crochets")
        print(":::::: ")
        tentatives_mdp=0
        while True:
            try:
                password=input("entrer votre mot de passe:   ")
                tentatives_mdp+=1
                if len(str(password))>10 or type(password)!=str:
                    password=input("entrer votre mot de passe entre crochets sans depasser 10 caracteres")
                elif password != Base_users.dico_users[username].mdp :
                    if tentatives_mdp<3:
                        print("Mot de passe incorrecte veuillez reessayer")
                        print("         ")
                    else:
                        self.afficher_menu_ouverture()
                        exit()
                
                else:
                    break
            except NameError :
                print("Veuillez entrer votre mot de passe entre crochets")
                
        username,password=str(username),str(password)

        if type_compte==1:
            config_global.utilisateur_qui_se_connecte=Utilisateurs_connecte.Geographe(username,password)

            if Base_users.dico_users[username].__class__.__name__=="Geographe":
                config_global.utilisateur_qui_se_connecte.connexion()
                self.fermer_menu_ouverture()
            else:
                print("Cet nom d'utilisateur ne correspond pas à votre type de compte")
                print("::::::")
                print("           ")
                print("            ")
                self.afficher_menu_ouverture()

        if type_compte==2:
            config_global.utilisateur_qui_se_connecte=Data_scientist.Data_s(username,password)

            if Base_users.dico_users[username].__class__.__name__=="Data_s":
                config_global.utilisateur_qui_se_connecte.connexion()
                self.fermer_menu_ouverture()
            else:
                print("Cet nom d'utilisateur ne correspond pas à votre type de compte")
                self.afficher_menu_connexion()

        if type_compte==3:
            config_global.utilisateur_qui_se_connecte=Utilisateurs_connecte.Admin(username,password,0,[])

            if Base_users.dico_users[username].__class__.__name__=="Admin":
                config_global.utilisateur_qui_se_connecte.connexion()
                self.fermer_menu_ouverture()
            else:
                print("Cet nom d'utilisateur ne correspond pas à votre type de compte")
                self.afficher_menu_connexion()
        if type_compte==4:
            self.afficher_menu_ouverture()


        
        
        
        
        
        
        
        
        