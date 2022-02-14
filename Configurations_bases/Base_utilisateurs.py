#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:28:29 2020

@author: macbookair
"""
import os
import pickle






    
    
class Base_users: 

    dico_users ={}
    def __init__(self):
        raise NotImplementedError("Vous ne pouvez pas creer une base, cette autorisation n'existe pas")
         ## dico users est le dictionnaire des utilisatuers
        ## il contient l'ensemble des utilisateurs prives et leurs mot de passe mais aussi leur
        ## leur historique
        ## Sa structure est la suivante: ex_dico_users:={user1:utilisateur1}
        ## où user1 est l'identifiant de l'utilisateur comme cle du dico, utilisateur est l'objet de type utilisateur
        ## associe à ce nom d'utilisateur
#def creer_compte(utilisateur,admin=0):
#        ## encore à definir
#    if not admin :
#        raise("Vous n'êtes pas autorises à ajouter modifier la base utilisateurs")
#    Base_users.dico_users[utilisateur.identifiant]= utilisateur
#
#def supprimer_compte(username,admin=0):
#    if not admin :
#        raise("Vous n'êtes pas autorises à ajouter modifier la base utilisateurs")
#    try:
#        Base_users.dico_users.pop(username)
#    except KeyError:
#        raise("L'utilisateur que vous voulez supprimer n'est pas present dans la base")
    
  
    


if __name__ == 'base_users_generate':
        try:
            fichier_base=open("bases_appli/Base_utilisateurs.pkl","wb")   
            pickle.dump({},fichier_base)
            fichier_base.close()
        except FileNotFoundError:
            with os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
                fichier_base=open("bases_appli/Base_utilisateurs.pkl","wb")   
                pickle.dump({},fichier_base)
                fichier_base.close()