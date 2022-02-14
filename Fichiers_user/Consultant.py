#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:04:19 2020

"""
import random
import os
import pickle

from Configurations_bases.BasePays import basePays, Pays,sauvegarder_base_pays,sauvegarder_base_correction,sauvegarder_cinq_c_age
import Configurations_bases.Base_utilisateurs as Base_utilisateurs


""" Module Consultant """

"""Ce module définit la classe de consultant"""



class consultant:
    """Definition de la classe consultant"""
    def __init__(self):
        """
        @param: null
        @return: Consultant
           """
           
    
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
                if nom_pays not in basePays.base.keys():
                    print("Ce Pays n'est pas dans la base")
                else:
                    break
            except:
                print("Veuillez faire une entrée correcte")
            
        basePays.base[nom_pays].afficherPays()

            
    def proposer_correction(self):
        """
        Fonction qui soumet une correction entrée par l'utilisateur
        dans la base des corrections sur "bases_appli/base_correction.pkl.
        """
        """
        @param: void
        @return: void
        """

        while True:
            try:
                print("Entrer le nom du pays concerne ou retour pour retourner au menu des taches")
                nom_pays=input("nom du Pays:  ")
                if type(nom_pays)!=str:
                    print("Le nom du Pays doit être en caracteres")
                elif nom_pays not in basePays.base.keys() and nom_pays not in ["Retour","retour"]:
                    print("Le pays que vous avez rentre n'est pas dans la base")
                else:
                    break
            except NameError :
                print("Veuillez entrer votre reponse entre guillemets")

        print("Veuillez selectionner l'info que vous voulez corriger")
        print("1: Nom du Pays")
        print("2: Superficie")
        print("3: Population")
        print("4: Croissance demographique")
        print("5: Inflation")
        print("6: Dette")
        print("7: Taux de chomage")
        print("8: Taux de depenses en sante")
        print("9: Taux de depenses en education")
        print("10: Taux de depenses militaires")
        print("11: Repartition de cinq classes d'âge")
        print("12: Retourner au menu des taches")
        dico_criteres={1:"nom",
                2: "superficie",
               3: "population",
               4: "croissance_demo",
               5: "inflation",
               6: "dette",
               7: "taux_chomage",
               8: "taux_depenses_sante",
               9: "taux_depenses_educ",
               10: "taux_depenses_militaires",
               11: "cinq_classes_age"}
        
        while True :
            try:
                info=input(":::   ")
                info=int(info)
                if info not in range(1,13):
                    print("Veuillez choisir parmi les options ")
                elif info ==13:
                    exit()
                elif type(info)!=int:
                    print("Le info doit être donne sous forme d'un nombre")
                else:
                    break
            
                        
            except NameError:
                print("Veuillez entrer un nombre representant votre info")
            except ValueError:
                print("Veuillez entrer une réponse sous forme de chiffre")
            
        
        if info==1:
            while True:
                try:
                    modification=input("entrer la modification du nom de pays entre guillemets:  ")
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
        elif info==2:
            while True:
                try:
                    modification=input("entrer la superficie:  ")
                    modification=int(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous forme de flottant")
           
        elif info==3:
            while True:
                try:
                    modification=input("entrer la population:  ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'entier")
        elif info==4:
            while True:
                try:
                    modification=input("entrer la croissance demographique: ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'un floattant")
        elif info==5:
            while True:
                try:
                    modification=input("entrer l'inflation:  ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'un flottant")
                
        elif info==6:
            while True:
                try:
                    modification=input("entrer la dette:  ")
                    modification=float(modification)

                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'un entier")
            
        elif info==7:
            while True:
                try:
                    modification=input("entrer le taux de chomage ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la frome d'un flottant")
        elif info==8:
            while True:
                try:
                    modification=input("entrer le taux de depenses en sante ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'un floattant")
        elif info==9:
            while True:
                try:
                    modification=input("entrer le taux de depenses en education: ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la forme d'un flottant")
        elif info==10:
            while True:
                try:
                    modification=input("entrer le taux de depenses militaires ")
                    modification=float(modification)
                    break
                except NameError:
                    print("Veuillez faire une entree entre crochet si c'est un string")
                except ValueError:
                    print("Veuillez entrer une reponse sous la frome d'u flottant")
        elif info==11:
            dico_modif={}
            while True:
                try:
                    print("Entrer les tranches d'âge")
                    print("Entrer Le pourcentage de la classe d'age suivi d'une info")
                    dico_modif["0-14 years"]=input("0-14 years:  ")
                    dico_modif["15-24 years"]=input("15-24 years:  ")
                    dico_modif["25-54 years"]=input("25-54 years:  ")
                    dico_modif["55-64 years"]=input("55-64 years:  ")
                    dico_modif["65 years and over"]=input("65 years and over:  ")
                except NameError :
                    print("Entrer la tranche d'age entre guillemets" )
        else:
            
            exit()

        basePays.corrections.append([nom_pays,dico_criteres[info],modification])
        sauvegarder_base_correction()
        print("         ")
        print("Modification bien soumise!!")
        
    