#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:33:33 2020

@author: macbookair
"""

import pickle
import os
import runpy
import pandas

import Configurations_bases.Acces_donnees as Acces_donnees
#%%



###%%

#if __name__=="__main__":
#    for i in basePays.base.values():
#       print(str(i.inflation),"\n")
###      
###     #%

#%%


class Pays:
    #constructeur
    def __init__(self, 
                 nom, 
                 superficie, 
                 population, 
                 croissance_demo, 
                 inflation, 
                 dette,
                 taux_chomage,
                 taux_depenses_sante, 
                 taux_depenses_educ, 
                 taux_depenses_militaires, 
                 cinq_classes_age):
        self.nom = nom
        self.superficie = superficie
        self.population = population
        self.croissance_demo = croissance_demo
        self.inflation = inflation
        self.dette = dette
        self.taux_chomage = taux_chomage
        self.taux_depenses_sante = taux_depenses_sante
        self.taux_depenses_educ = taux_depenses_educ
        self.taux_depenses_militaires = taux_depenses_militaires
        self.cinq_classes_age = cinq_classes_age
    def afficherPays(self):
        print("nom pays: "+self.nom+"\n")
        print("superficie: "+str(self.superficie)+"\n")
        print("population: "+str(self.population)+"\n")
        print("croissance demographique: "+str(self.croissance_demo)+"\n")
        print("inflation: "+str(self.inflation)+"\n")
        print("dette: "+str(self.dette)+"\n")
        print("taux de chomage: "+str(self.taux_chomage)+"\n")
        print("taux depenses sante: "+str(self.taux_depenses_sante)+"du PIB"+"\n")
        print("taux depenses education: "+str(self.taux_depenses_educ)+"du PIB"+"\n")
        print("taux depenses militaires: "+str(self.taux_depenses_militaires)+"du PIB"+"\n")
        print("0-14 ans: "+str(list(list(self.cinq_classes_age.values())[0].values())[0]))
        print("15-24 ans: "+str(list(list(self.cinq_classes_age.values())[1].values())[0]))
        print("25-54 ans: "+str(list(list(self.cinq_classes_age.values())[2].values())[0]))
        print("54-64 ans: "+str(list(list(self.cinq_classes_age.values())[3].values())[0]))
        print("65 et plus: "+str(list(list(self.cinq_classes_age.values())[3].values())[0]))
Pays.__module__="Configurations_bases.BasePays"
#%%


        
    
#%%


    
        

        
         

class basePays:
    #cette classe contient des informations de classe c'est une classe abstraite
    ## elle contient la base de pays chargée à partir du fichier "~/bases_appli/base_pays.pkl"
    try:
        with open("bases_appli/base_pays.pkl", 'rb') as fichier:
            base=pickle.load(fichier)
    except FileNotFoundError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_base_pays")
        with open("bases_appli/base_pays.pkl", 'rb') as fichier:
            base=pickle.load(fichier)
    except EOFError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_base_pays")
        with open("bases_appli/base_pays.pkl", 'rb') as fichier:
            base=pickle.load(fichier)
        
    
    
    try:
        
        with open("bases_appli/base_corrections.pkl", 'rb') as fichier:
            corrections=pickle.load(fichier)
    except FileNotFoundError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_correction")
        with open("bases_appli/base_corrections.pkl", 'rb') as fichier:
            corrections=pickle.load(fichier)
            
    except EOFError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_correction")
        with open("bases_appli/base_corrections.pkl", 'rb') as fichier:
            corrections=pickle.load(fichier)
    
    
    
    try:
        
        with open("bases_appli/base_classes_age.pkl","rb") as fichier:
            cinq_C_age=pickle.load(fichier)
    except FileNotFoundError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_c_age")
        with open("bases_appli/base_classes_age.pkl","rb") as fichier:
            cinq_C_age=pickle.load(fichier)
    except EOFError:
        runpy.run_module("Configurations_bases.config_base",run_name="run_c_age")
        with open("bases_appli/base_classes_age.pkl","rb") as fichier:
            cinq_C_age=pickle.load(fichier)
    
            
        
        
    
    def __init__(self):
        
        raise NotImplementedError("Vous ne pouvez pas créer une base, cette autorisation n'existe pas")

basePays.__module__="Configurations_bases.BasePays"
#%%
def sauvegarder_base_pays():
    with open("bases_appli/base_pays.pkl","wb") as fichier_base:
        basePays.__module__="Configurations_bases.BasePays"
        base_pickle=basePays.base
        pickle.dump(base_pickle,fichier_base)
def actualiser_base_pays():
    with open("bases_appli/base_pays.pkl","rb") as fichier_base:
        setattr(basePays,"base",pickle.load(fichier_base))

def sauvegarder_base_correction():
    fichier_correction=open("bases_appli/base_corrections.pkl","wb")
    pickle.dump(basePays.corrections,fichier_correction)
    fichier_correction.close()

      
actualiser_base_pays()
def sauvegarder_cinq_c_age():
    basePays.cinq_C_age=Acces_donnees.dico_classes_ages_to_liste({cle : getattr(pays1,"cinq_classes_age") for (cle,pays1) in basePays.base.items() })
    with open("bases_appli/base_classes_age.pkl","wb") as fichier_classes_age:
        basePays.__module__="Configurations_bases.BasePays"
        Pays.__module__="Configurations_bases.BasePays"
        pickle.dump(basePays.cinq_C_age,fichier_classes_age)
        fichier_classes_age.close()

def actualiser_cinq_c_age():
    with open("bases_appli/base_classes_age.pkl","rb") as fichier_classes_age:
        basePays.__module__="Configurations_bases.BasePays"
        Pays.__module__="Configurations_bases.BasePays"
        setattr(basePays,"cinq_C_age",pickle.load(fichier_classes_age))

def actualiser_base_corrections():
    fichier_correction=open("bases_appli/base_corrections.pkl","rb")
    setattr(basePays,"corrections",pickle.load(fichier_correction))
    fichier_correction.close()

#    
#    b=basePays(dico)
#    nom = "Abracadabra"
#    superficie = "18000 km²"
#    pop = "1800000"
#    croissance_demo = "10%"
#    inflation = "2%"
#    dette = "54 milliard d'euros"
#    taux_chomage = "10%"
#    taux_depenses_sante = "3%"
#    taux_depenses_educ = "5%"
#    taux_depenses_militaires = "10%"
#    cinq_classes_age = "RAS"
#    
#    b.ajouter_pays(nom, superficie, pop, croissance_demo, inflation, dette, taux_chomage, taux_depenses_sante, \
#                taux_depenses_educ, taux_depenses_militaires, cinq_classes_age)
#    print(b.dico["Abracadabra"])
#    b.supprimer_pays("Abracadabra")
#
