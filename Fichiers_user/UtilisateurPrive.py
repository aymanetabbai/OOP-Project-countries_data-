#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:29:33 2020


"""
import os
import pickle

import Configurations_bases.Base_utilisateurs as Base_utilisateurs

import Configurations_bases.BasePays as BasePays

class utilisateurPrive:

    # Classe generale qui contient les utilisateurs pouvant se connecter cette classe 
    #accede à la base utilisateur pour pouvoir se connecter
    
    def __init__(self,identifiant,mdp,historique=[],etat=0):
        self.identifiant= identifiant
        self.mdp= mdp
        self.historique =historique
        self.etat=etat
    
    def afficher_pays(self):
        """
        Fonction  qui affiche le pays entré par l'utilisateur
        la fonction continue de demander d'entrer un nom du pays
        si le pays demadé n'est pas dan la base
        """
        
        """
        @param: void
        @return: void
        """
        
        while True:
            try:
                nom_pays=input("nom pays:  ")
                print("        ")
                print("         ")
                if nom_pays not in BasePays.basePays.base.keys():
                    print("Ce Pays n'est pas dans la base")
                else:
                    break
            except:
                print("Veuillez faire une entrée correcte")
            
        BasePays.basePays.base[nom_pays].afficherPays()
    
    def connexion(self):

        username=self.identifiant
        password=self.mdp
        
        try:
            if Base_utilisateurs.Base_users.dico_users[username].etat:
                print("Cet utilisateur est deja connecte")
            self.etat= (username in Base_utilisateurs.Base_users.dico_users.keys())*(password in [user.mdp for user in Base_utilisateurs.Base_users.dico_users.values()])
            if self.etat:     
                Base_utilisateurs.Base_users.dico_users[username].etat=self.etat
                print("Vous êtes maintenant connectes en tant que "+username)
            if not self.etat:
                raise("nom d'utilisateur ou mot de passe incorrecte")
        except KeyError:
            raise KeyError("Cet utilisateur n'existe pas")
        
    def deconnexion(self):
        
        if not self.etat:
            print("Cet utilisateur est deja deconnecte")
            exit()
        
        Base_utilisateurs.Base_users.dico_users[self.identifiant].etat=0
        self.etat=0
    def supprimer_historique(self):
        if self.etat:
            Base_utilisateurs.Base_users.dico_users[self.identifiant].historique=[]
            self.historique=[]
            print("     ")
            print("historique supprime")
            print("        ")
        else:
            print("Vous n'etes pas connectes")
    def afficher_historique(self):
        if len(self.historique)>0:
            for i in range(len(self.historique),-1):
                message_tache=self.historique[i]
                print("    ")
                print("["+str(len(self.historique+i+1))+"] "+str(message_tache))
                print("      ")
        else:
            print("     ")
            print("Votre historique est vide")
            print("      ")
        
        