# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:41:13 2020

@author: Chloé
"""

## fichier configuration de la base
import os
import pickle
import pandas
import numpy
import random

import  Configurations_bases.Acces_donnees as Acces_donnees
from Configurations_bases.BasePays import Pays


    
if __name__ == "run_base_pays":

    dico=Acces_donnees.AccesDonnees(Acces_donnees.donnees)
    base_temporaire={}

    for cle in dico.keys():
        try:
            base_temporaire[cle] = Pays(cle,
                           dico[cle]["superficie"],
                           dico[cle]["population"],
                           dico[cle]["croissance demographique"],
                           dico[cle]["inflation"],
                           dico[cle]["dette"],
                           dico[cle]["taux de chomage"],
                           dico[cle]["taux depenses sante"],
                           dico[cle]["taux depenses education"],
                           dico[cle]["taux depenses militaires"],
                           dico[cle]["cinq classes age"])
        except AttributeError:
            pass
            
    fichier_base= open("bases_appli/base_pays.pkl","wb")
    Pays.__module__="Configurations_bases.BasePays"
    pickle.dump(base_temporaire,fichier_base)
    fichier_base.close()

if __name__=="run_correction":
    fichier_correction=open("bases_appli/base_corrections.pkl","wb")
    Pays.__module__="Configurations_bases.BasePays"
    pickle.dump([],fichier_correction)
    fichier_correction.close()
    
    
if __name__=="run_c_age":

    dico=Acces_donnees.AccesDonnees(Acces_donnees.donnees)
    base_temporaire={}
    for cle in dico.keys():
        base_temporaire[cle] = Pays(cle,
                       dico[cle]["superficie"],
                       dico[cle]["population"],
                       dico[cle]["croissance demographique"],
                       dico[cle]["inflation"],
                       dico[cle]["dette"],
                       dico[cle]["taux de chomage"],
                       dico[cle]["taux depenses sante"],
                       dico[cle]["taux depenses education"],
                       dico[cle]["taux depenses militaires"],
                       dico[cle]["cinq classes age"])
    dico_cinq_C_ages ={cle : getattr(pays1,"cinq_classes_age") for (cle,pays1) in base_temporaire.items() } 
    cinq_C_age_temporaire=Acces_donnees.dico_classes_ages_to_liste(dico_cinq_C_ages)
    fichier_classes_age= open("bases_appli/base_classes_age.pkl","wb")

    Pays.__module__="Configurations_bases.BasePays"
    pickle.dump(cinq_C_age_temporaire,fichier_classes_age)
    fichier_classes_age.close()
