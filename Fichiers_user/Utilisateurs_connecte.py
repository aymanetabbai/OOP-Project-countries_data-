#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:27:37 2020


"""

import os
import pickle
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


from Fichiers_user.UtilisateurPrive import utilisateurPrive
from Configurations_bases.BasePays import basePays, Pays , sauvegarder_base_pays, sauvegarder_cinq_c_age

from Configurations_bases.Base_utilisateurs import Base_users
import Fichiers_user.Data_scientist as Data_scientist
import Configurations_bases.Acces_donnees as Acces_donnees


def n_premiers_derniers_denses(self,m,indice):
     data1 = self.transforme('population')
     data2 = self.transforme('superficie')
     densite = []
     densiteTriee = []
     l = []
     for key, value in data1.items():
         densite.append([data1[key]['nom pays'], data1[key]['population']/data2[key]['superficie']])
     val = densite[0][1]
     if (indice==1):
     #on s'arrange à ce qu'il ait au moins m valeurs superieures a minim dans le tableau des densites
         for i in range(m):
             if val > densite[i][1]:
                 val = densite[i][1]
         for i in range(m):
             n = 0
     #ainsi maxim est une des valeurs du tableau restant
             maxim = val            
             for j in range(len(densite)):
                 if maxim < densite[j][1] and j not in l:
                     maxim = densite[j][1]
                     n = j
             l.append(n)
             densiteTriee.append([densite[n][0],densite[n][1]])
     else:
         #on s'arrange à ce qu'il ait au moins m valeurs inferieures a minim dans le tableau des densites
         for i in range(m):
             if val < densite[i][1]:
                 val = densite[i][1]
         for i in range(m):
             n = 0
     #ainsi minim est une des valeurs du tableau restant
             minim = val            
             for j in range(len(densite)):
                 if minim > densite[j][1] and j not in l:
                     minim = densite[j][1]
                     n = j
             l.append(n)
             densiteTriee.append([densite[n][0],densite[n][1]])
     return densiteTriee
def transforme(self, critere):        
   data = {}
   if (critere=="superficie"):
       for key, value in self.dico.items():
           s = value[critere].split(' ')
           s[0] = s[0].replace(',', '')
           if s[1] == 'million':
               res = float(s[0])
               res = res*10**6
           else:
               res = float(s[0])
           data[key] = {'nom pays':key, critere: res}
   if (critere=='population'):
       for key, value in self.dico.items():
           s = value[critere].split(' ')
           s[0] = s[0].replace(',','')
           s[0] = s[0].replace('.','')
           res = int(s[0])
           data[key] = {'nom pays':key, critere: res}
   if (critere=='croissance demographique' or critere =='inflation' or critere=='taux de chomage' \
       or critere == 'taux depenses sante' or critere =='taux depenses education' or critere=='taux depenses militaires'):
       for key, value in self.dico.items():
           s = value[critere].split(' ')
           s[0]=s[0].replace('%','')
           res = float(s[0])
           data[key] = {'nom pays':key, critere: res}
   if (critere=='dette'):
       for key, value in self.dico.items():
           s = value[critere].split(' ')
           s[0] = s[0].replace('$', '')
           s[0] = float(s[0])
           if s[1] == 'billion':
               res = s[0]*10**9
           elif s[1] == 'trillion':
               res = s[0]*10**12
           elif s[1] == 'million':                    
               res = s[0]*10**6
           else:
               res = s[0]                    
           data[key] = {'nom pays':key, critere: res}
   return data

class Geographe(utilisateurPrive):
    """ Cette classe est une classe qui specifie le type d'utilisateur geographe
    elle beneficie des attributs de utilisateurPrive et de ses methodes
    """
    def __init__(self,identifiant,mdp,historique=[],etat=0):
        self.identifiant=identifiant
        self.mdp=mdp
        self.historique=historique
        self.etat=etat

    def accepter_proposition_correction(self):## la correction est donnee sous la forme [nom_pays,info,correction]
        if len(basePays.corrections)!=0:   
            for correction in basePays.corrections:
                    print("correction Nº"+str(basePays.corrections.index(correction)+1)+":")
                    print("---Nom du Pays: "+str(correction[0]))
                    print("---info à corriger: "+str(correction[1]))
                    print("---Correction de l'info: "+str(correction[2]))
            while True:
                try:
                    choix_num_correction=input("Entrer Le numero de la correction que vous voulez accepter ou refuser: ")
                    choix_num_correction=int(choix_num_correction)
                    if choix_num_correction not in range(1,len(basePays.corrections)+1):
                        print("Veuillez entrer un numero dans la liste")
                        print("     ")
                    else:
                        break
                except NameError :
                    print("Veuillez entrer un numero")
                    print("       ")
                except ValueError:
                    print("Veuillez entrer une numero sous la forme d'un entier")
                    print(" ")
            correction=basePays.corrections[choix_num_correction-1]
            try: 
                print("      ")
                print("       ")
                print("Acceptez vous la correction suivante: ")
                print("Pour le Pays : "+str(correction[0]))
                print("Modifier "+str(correction[1]))
                print("En "+str(correction[2]))
                print("Accepter: 1")
                print("Refuser: 2")
                print("Retourner au menu des taches: 3")
                print(" ")
    
                while True:
                    try:
                        acceptation=input(":::  ")
                        acceptation=int(acceptation)
                        if acceptation in [1,2,3]:
                            break
                        else:
                            print("Veuillez entrer un choix parmi les options")
                            print(" ")
                    except NameError:
                        print("Veuillez entrer un choix valide")
                        print(" ")
                    except ValueError:
                        print("Veuillez entrer un choix sous la forme d'un entier")
                        print("  ")
                    
                    
                if acceptation==1:
                    setattr(basePays.base[correction[0]],correction[1],correction[2])
                    sauvegarder_base_pays()
                    basePays.corrections.pop(basePays.corrections.index(correction))
                elif acceptation==2:
                    basePays.corrections.pop(basePays.corrections.index(correction))
                    sauvegarder_base_pays()
                else:
                    ## retourner au menu des taches
                    exit()
    
            except IndexError :
                raise IndexError("la liste de correction n'est pas de la bonne taille ou le pays n'est pas dans la base")
    
        else:
            print("Il n'y a pas de propositions de correction pour le moment")
            print("     ")
            print("     ")
    
    def ajouter_pays(self):
        
        while True:
            try:
                nom=input("Entrer le nom du pays: ")
                if type(nom)!=str:
                    print("le nom du pays peut seulement être de type caractere")
                    print("    ")
                elif nom in basePays.base.keys():
                    print("Ce pays existe dejà dans la base!")
                    print("    ")
                else:
                    break
            except NameError:
                print("Veuillez entrer le nom du pays entre crochets")
                print("     ")
        while True:
            try:
                superficie=input("Entrer La superficie: ")
                superficie=int(superficie)
                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer la superficie sous la forme d'un entier")
                print("    ")
        while True:
            try:
                population=input("Entrer La population: ")
                population=int(population)
                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("     ")
            except ValueError:
                print("Veuillez entrer la population sous la forme d'un entier")
                print("    ")
        while True:
            try:
                croissance_demo=input("Entrer La croissance demographique: ")
                croissance_demo=float(croissance_demo)

                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer la croissance démographique sous la forme d'un flottant")
                print("    ")

        while True:
            try:
                inflation=input("Entrer L'inflation: ")
                inflation=float(inflation)

                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer l'inflation sous la forme d'un flottant")
                print("    ")
        while True:
            try:
                dette=input("Entrer La dette: ")
                dette=float(dette)

                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer la dette sous la forme d'un flottant")
                print("    ")
        while True:
            try:
                taux_chomage=input("Entrer le taux de chômage: ")
                taux_chomage=float(taux_chomage)

                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
        while True:
            try:
                taux_depenses_sante=input("Entrer Le taux de depenses de sante: ")
                taux_depenses_sante=float(taux_depenses_sante)
                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
        while True:
            try:
                taux_depenses_educ=input("Entrer le taux de depenses d'education: ")
                taux_depenses_educ=float(taux_depenses_educ)
                
                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
        while True:
            try:
                taux_depenses_militaires=input("Entrer Le taux de depenses militaires: ")
                taux_depenses_militaires=float(taux_depenses_militaires)
                break
            except NameError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
            except ValueError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
        while True:
            try:
                cinq_classes_age={}
                print("Entrer les tranches d'âge")
                print("    ")
                cinq_classes_age["0-14 years"]=input("0-14 years:  ")
                cinq_classes_age["15-24 years"]=input("15-24 years:  ")
                cinq_classes_age["25-54 years"]=input("25-54 years:  ")
                cinq_classes_age["55-64 years"]=input("55-64 years:  ")
                cinq_classes_age["65 years and over"]=input("65 years and over:  ")
                print("    ")
                break
            except NameError or ValueError:
                print("Veuillez entrer un entier ou un flottant")
                print("    ")
                
        p = Pays(nom, 
             superficie, 
             population, 
             croissance_demo, 
             inflation, dette, 
             taux_chomage, 
             taux_depenses_sante, 
             taux_depenses_educ, 
             taux_depenses_militaires,
             cinq_classes_age)
        

        basePays.base[nom] = p
        sauvegarder_base_pays()
        sauvegarder_cinq_c_age()
        print("    ")
        print("Pays bien ajoute!!!")
        print("          ")
             
   
    def Modifier_pays(self):
        while True:
            try:
                print("Entrer le nom du pays ou tapez 'Retour' pour retourner au menu des taches")
                nom_pays=input(":::  ")
                if type(nom_pays)!=str:
                    print("Le nom du pays doit être de type charactere")
                    print("    ")
                elif nom_pays not in basePays.base.keys() and nom_pays!="Retour":
                    print("Le pays que vous avez selectionne n'est pas dans la base ou taper 'Retour'")
                    print("    ")
                elif nom_pays=="Retour":
                    ##afficher menu taches
                    exit()
                else:
                    
                    break
            except NameError:
                print("Veuillez entrer le nom du pays entre crochets")
                print("    ")


        print("       ")
        print("        ")
        print("Veuillez selectionner l'info que vous voulez modifier")
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
        print("         ")
        while True :
            try:
                choix=input(":::   ")
                choix=int(choix)
                if choix not in range(1,13):
                    print("Veuillez choisir parmi les options ")
                    print("    ")
                elif choix==13:
                    exit()
                    break
                elif type(choix)!=int:
                    print("Le choix doit être donne sous forme d'un nombre")
                    print("    ")
                else:
                    break
            
                        
            except NameError:
                print("Veuillez entrer un nombre representant votre choix")
                print("    ")
            except ValueError:
                print("Veuillez entrer un entier comme reponse")
                print("    ")
            
            
        if choix==1:
            modification=input("entrer la modification du nom de pays entre "" ")
            setattr(basePays.base[nom_pays],"nom",modification)
        elif choix==2:
            while True:
                try:
                    modification=input("entrer la superficie  ")
                    modification=int(modification)
                    setattr(basePays.base[nom_pays],"superficie",modification)
                except NameError:
                    print("Veuillez faire une entree valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==3:
            while True:
                try:
                    modification=input("entrer la population  ")
                    modification=int(modification)
                    setattr(basePays.base[nom_pays],"population",modification)
                except NameError:
                    print("Veuillez faire une entree valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==4:
            while True:
                try:
                    modification=input("entrer la croissance demographique ")
                    modification=int(modification)
                    setattr(basePays.base[nom_pays],"croissance_demo",modification)
                except NameError:
                    print("Veuillez faire une entree valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
                
        elif choix==5:
            while True:
                try:
                    modification=input("entrer l'inflation  ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"inflation",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==6:
            while True:
                try:
                    modification=input("entrer la dette entre ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"dette",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
                
        elif choix==7:
            while True:
                try:
                    modification=input("entrer le taux de chomage ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"taux_chomage",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==8:
            while True:
                try:
                    modification=input("entrer le taux de depenses en sante ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"tauc_depenses_sante",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==9:
            while True:
                try:
                    modification=input("entrer le taux de depenses en education ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"taux_depenses_educ",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
        elif choix==10:
            while True:
                try:
                    modification=input("entrer le taux de depenses militaires ")
                    modification=float(modification)
                    setattr(basePays.base[nom_pays],"taux_depenses_militaires",modification)
                except NameError:
                    print("Veuillez faire une entrée valide")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer un entier ou flottant")
                    print("    ")
                    
        elif choix==11:
            dico_modif={}
            print("Entrer les tranches d'âge")
            dico_modif["0-14 years"]=input("0-14 years:  ")
            dico_modif["15-24 years"]=input("15-24 years:  ")
            dico_modif["25-54 years"]=input("25-54 years:  ")
            dico_modif["55-64 years"]=input("55-64 years:  ")
            dico_modif["65 years and over"]=input("65 years and over:  ")
            setattr(basePays.base[nom_pays],"cinq_classes_age",modification)
            sauvegarder_cinq_c_age()
        else:
            
            exit()

        print("Modification effectuee!!!")
        print("        ")
                
                
    
class Admin(Geographe):
    
    def __init__(self,identifiant,mdp,etat,historique):
        self.identifiant=identifiant
        self.mdp=mdp
        self.historique=historique
        self.etat=0
    
    def supprimer_pays(self):
        while True:
            try:
                nom_pays=input("Entrer le nom du pays entre crochets ou Retour pour retourner au menu des taches")
                if type(nom_pays)!=str:
                    raise TypeError("Le nom doit être de type caractere")
                elif nom_pays not in basePays.base.keys() and nom_pays!="Retour":
                    print("Veuillez entrer un pays qui existe dans la base ou verifier l'orthographe")
                    print("    ")
                elif nom_pays=="Retour":
                    exit()
                else:
                    break
            except NameError:
                print("Veuillez entrer le nom du pays entre crochets")
        basePays.base.pop(nom_pays)
        sauvegarder_base_pays()

    def ajouter_utilisateur(self):
        while True:
            try:
                print("types utilisateurs: ")
                print("1 : Admin")
                print("2 : Geographe")
                print("3 : Data scientist")
                print("4: Retourner au menu des taches")
                print("    ")
                type_utilisateur=input("Entrer le type d'utilisateur: ")
                type_utilisateur=int(type_utilisateur)
                if type_utilisateur not in range(1,5):
                    print("Le type d'utilisateur que vous voulez creer n'existe pas")
                    print("    ")
                elif type_utilisateur==4:
                    exit()
                else:
                    break
            except NameError:
                print("Veuillez entrer un type d'utilisateur entre crochet")
                print("    ")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un entier")
                print("    ")
        while True:
            try:
                identifiant=input("Entrer l'identifiant: ")
                if type(identifiant)!=str:
                    print("l'identifiant doit être un string")
                    print("    ")
                elif identifiant in Base_users.dico_users.keys():
                    print("Cet utilisateur est deja present dans la base")
                    print("    ")
                    exit()
                else:
                    break
            except NameError:
                print("Veuillez entrer le nom d'utilisateur entre crochet")
                print("    ")
        while True:
            try:
                mdp=input("Entrer le mot de passe: ")
                if type(mdp)!=str:
                    raise TypeError("le mot de passe doit être un string")
                else:
                    break
            except NameError:
                print("Veuillez entrer le mot de passe entre crochet")
                print("    ")
        
            
        if type_utilisateur==2:
            Base_users.dico_users[identifiant]=Geographe(identifiant,mdp,[],0)
        elif type_utilisateur==1:
            Base_users.dico_users[identifiant]=Admin(identifiant,mdp,[],0)
        elif type_utilisateur==3:
            Base_users.dico_users[identifiant]=Data_scientist.Data_s(identifiant,mdp,[],0)
        print("Utilisateur ajouté avec succes")
        print("    ")
        print("    ")


        
    def supprimer_utilisateur(self):
        while True:
            try:
                identifiant=input("Entrer l'identifiant: ")
                if type(identifiant)!=str:
                    print("l'identifiant doit être un string")
                    print("    ")
                elif identifiant not in Base_users.dico_users.keys():
                    print("Cet utilisateur n'est pas present dans la base")
                    print("    ")
                    exit()
                else:
                    break
            except NameError:
                print("Veuillez entrer le nom d'utilisateur entre crochets")
                print("    ")
        Base_users.dico_users.pop(identifiant)
        print("Utilisateur supprime avec succes")
        print("    ")
        print("    ")
    
    #%%       
    def representation_graphique(self):
        ## On possede le fichier de la base contenant les classes d'age dans le format
        ## {"Pays": "Sri Lanka","14-25 ans" : 28.5 }
        ## on le transforme en dataframe
        print("Quel type de representation graphique voulez vous faire?")
        print("1: Barplot selon un critere d'une liste de pays")
        print("2: Boxplot des cinq classes d'âge sur tout les pays")
        print("3: Retourner au menu des taches")
        print("    ")
        while True:
            try:
                choix=input(":::   ")
                choix=int(choix)
                if choix in [1,2,3]:
                    break
                else:
                    print("Veuillez entrer un choix dans la liste des choix")
                    print("    ")
            except NameError:
                print("Veuillez entrer un choix valide")
                print("    ")
            except ValueError:
                print("Veuillez entrer une reponse sous forme d'entier")
                print("    ")
        if choix==1:
            nombre_pays=0
            liste_pays=[]
            while True:
                try:
                    pays_a_ajouter=input("Entrer le nom du pays numero "+str(nombre_pays+1)+"entre crochets")
                    if pays_a_ajouter not in basePays.base.keys():
                        print("Le pays que vous venez de selectionner n'est pas dans la base")
                        print("    ")
                    elif nombre_pays>=10:
                        print("Vous avez atteint le nombre maximal de pays")
                        print("    ")
                        break
                    else:
                        liste_pays.append(pays_a_ajouter)
                        nombre_pays+=1
                        ajouter_pays=True
                        while ajouter_pays:
                            try:
                                print("1: Ajouter un autre pays")
                                print("2: Continuer avec la liste des pays entres")
                                print("    ")
                                ajouter_pays=input("Voulez vous ajouter un autre pays: ")
                                ajouter_pays=int(ajouter_pays)
                                if ajouter_pays not in [1,2]:
                                    print("Veuillez entrer un choix parmi la liste des choix")
                                    print("    ")
                                elif ajouter_pays==2:
                                    break
                                else:
                                    ajouter_pays=False
                                    
                            except NameError:
                                print("Veuillez entrer un choix valide")
                                print("    ")
                            except ValueError:
                                print("Veuillez entrer une reponse sous forme d'entier")
                                print("    ")
                        if ajouter_pays:
                            break  
                                
                        
                except NameError:
                     print("Veuillez entrer le nom d'un pays correcte entre crochets")
                     print("    ")
            while True:
                try:
                    print("Veuillez choisir un critere dans la liste suivante:")
                    print("1: Superficie")
                    print("2: Population")
                    print("3: Croissance demographique")
                    print("4: Inflation")
                    print("5: Dette")
                    print("6: Taux de chômage")
                    print("7: Taux de depenses en sante")
                    print("8: Taux de depenses en education")
                    print("9: Taux de depenses militaires")
                    print("    ")
                    choix_critere=input(":::  ")
                    choix_critere=int(choix_critere)
                    if choix_critere not in range(1,10):
                        print("Veuillez entrer un choix dans la liste des choix")
                        print("    ")
                    else:
                        break
                except NameError:
                    print("Veuillez entrer votre choix sous la forme d'un entier")
                    print("    ")
                except ValueError:
                    print("Veuillez entrer une reponse sous forme d'entier")
                    print("    ")
            dico_criteres={1: "superficie",
                           2: "population",
                           3: "croissance_demo",
                           4: "inflation",
                           5: "dette",
                           6: "taux_chomage",
                           7: "taux_depenses_sante",
                           8: "taux_depenses_educ",
                           9: "taux_depenses_militaires"}
            critere=dico_criteres[choix_critere]
            liste_pays_objets=[]
            for Pays1 in liste_pays:
                liste_pays_objets.append(basePays.base[Pays1])              
            data_pour_barplot={"nom du pays":[pays1.nom for pays1 in liste_pays_objets],
                                  critere:[float(getattr(pays1,critere)) for pays1 in liste_pays_objets]}

            dataframe_barplot=pandas.DataFrame(data_pour_barplot,columns=data_pour_barplot.keys())
            barplot=dataframe_barplot.plot.bar(x="nom du pays")
            barplot.legend([critere])
            plt.show()
        elif choix==2:
        
            data_frame_boxplot=pandas.DataFrame(basePays.cinq_C_age, columns=basePays.cinq_C_age.keys())
            data_frame_boxplot.boxplot(column=["0-14 ans","25-54 ans","15-24 ans","55-64 ans","65 ans et +"])
            plt.show()
        else:
            exit()
        
#%%
    def resume_d_info(self):
        
        
        print("Veuillez entrer une liste de pays à afficher")
        nombre_pays=0
        liste_pays=[]
        while True:
            try:
                pays_a_ajouter=input("Entrer le nom du pays numero "+str(nombre_pays+1)+" : ")
                if pays_a_ajouter not in list(basePays.base.keys()):
                    print("Le pays que vous venez de selectionner n'est pas dans la base")
                    print("    ")
                elif nombre_pays>=10:
                    print("Vous avez atteint le nombre maximal de pays")
                    print("    ")
                    break
                else:
                    liste_pays.append(pays_a_ajouter)
                    nombre_pays+=1
                    ajouter_pays=True
                    while ajouter_pays:
                        try:
                            print("1: Ajouter un autre pays")
                            print("2: Continuer avec la liste des pays entres")
                            print("    ")
                            ajouter_pays=input("Voulez vous ajouter un autre pays: ")
                            ajouter_pays=int(ajouter_pays)
                            if ajouter_pays not in [1,2]:
                                print("Veuillez entrer un choix parmi la liste des choix")
                                print("    ")
                            elif ajouter_pays==1:
                                ajouter_pays=False
                            else:
                                break
                                
                        except NameError:
                            print("Veuillez entrer un choix valide")
                            print("    ")
                        except ValueError:
                            print("Veuillez faire une entree sous la forme d'un entier")
                            print("    ")
                    if ajouter_pays:
                        break
                            
                    
            except NameError:
                 print("Veuillez entrer le nom d'un pays correcte entre crochets")
                 print("    ")
        
        
        print("Veuillez choisir votre critere de seuil pour le resume")
        print("          ")
        print("1: Superficie")
        print("2: Population")
        print("3: Croissance demographique")
        print("4: Inflation")
        print("5: Dette")
        print("6: Taux de chomage")
        print("7: Taux de depenses en sante")
        print("8: Taux de depenses en education")
        print("9: Taux de depenses militaires")
        print("10: Retourner au menu des taches")
        dico_criteres={1: "superficie",
               2: "population",
               3: "croissance_demo",
               4: "inflation",
               5: "dette",
               6: "taux_chomage",
               7: "taux_depenses_sante",
               8: "taux_depenses_educ",
               9: "taux_depenses_militaires"}
        while True:
            try:
                critere_pour_seuil=input("Entrez le critere de seuil: ")
                critere_pour_seuil=int(critere_pour_seuil)
                if critere_pour_seuil not in range(1,11):
                    print("Veuillez choisir un critere dans la liste")
                elif critere_pour_seuil==10:
                    exit()
                else:
                    break
            except NameError :
                print("Veuillez entrer un choix valide")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un entier")
        critere_pour_seuil=dico_criteres[critere_pour_seuil]
        

        
        while True:
            try:
                seuil=input("Entrer le seuil:  ")
                seuil=float(seuil)
                break
            except NameError :
                print("Veuillez entrer une seuil valide")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un flottant")
            
        print("")
        print("Afficher les Pays....")
        print("1: en dessous du seuil")
        print("2: au dessus du seuil" )
        print("     ")
        while True:
            try:
                au_dessus_seuil=input("::::     ")
                au_dessus_seuil=int(au_dessus_seuil)
                if au_dessus_seuil not in [1,2]:
                    print("Veuillez faire un choix parmi les choix possibles")
                else:
                    au_dessus_seuil=bool(au_dessus_seuil-1)
                    break
            except NameError  :
                print("Veuillez entrer un choix valide")
            except ValueError:
                print("Veuillez entrer une reponse sous la forme d'un entier")
        
        
        print("     ")
        print(" ")
        
        print("Veuillez entrer un critere selon lequel trier les pays")
        print("1: Superficie")
        print("2: Population")
        print("3: Croissance demographique")
        print("4: Inflation")
        print("5: Dette")
        print("6: Taux de chomage")
        print("7: Taux de depenses en sante")
        print("8: Taux de depenses en education")
        print("9: Taux de depenses militaires")
        print("10: Retourner au menu des taches")
        print("      ")
        
        while True:
            try:
                critere_pour_tri=input("Entrez le critere de tri: ")
                critere_pour_tri=int(critere_pour_tri)
                if critere_pour_tri not in range(1,11):
                    print("Veuillez choisir un critere dans la liste")
                elif critere_pour_tri==10:
                    exit()
                else:
                    break
            except NameError :
                print("Veuillez entrer un choix valide")
            except ValueError:
                print("Veuillez faire une entree sous la forme d'un entier")
        critere_de_tri=dico_criteres[critere_pour_tri]
        
        while True:
            try:
                print("1: afficher les n premiers pour le critere")
                print("2: afficher les n derniers pour le critere")
                n_premier_pour_critere=input("::::   ")
                n_premier_pour_critere=int(n_premier_pour_critere)
                if n_premier_pour_critere not in [1,2]:
                    print("Veuillez selectionner un choix parmis les options")
                elif n_premier_pour_critere==1:
                    n_premier_pour_critere=True
                    break
                elif n_premier_pour_critere==2:
                    n_premier_pour_critere=False
                    break
            except NameError :
                print("Veuillez entrer une reponse valide")
            except ValueError:
                print("Veuillez entrer un entier parmi les choix")
                    
        while True:
            try:
                nb_pays_pour_critere=input("Entrer le nombre de Pays a afficher Pour le critere de tri: ")
                nb_pays_pour_critere=int(nb_pays_pour_critere)
                if nb_pays_pour_critere<=0:
                    print("Veuillez rentrer un entier strictement positif")
                else:
                    break
                
            except NameError :
                print("Veuillez entrer une reponse valide")
            except ValueError:
                print("Veuillez entrer un entier strictement positif")
        
        nb_pays_classes_age=0
        liste_pays_classes_age=[]
        print("Veuillez entrer les pays dont vous voulez afficher un tableau des classes d'âge")
        while True:
            try:
                pays_a_ajouter=input("Entrer le nom du pays numero "+str(nb_pays_classes_age+1)+" : ")
                if pays_a_ajouter not in list(basePays.base.keys()):
                    print("Le pays que vous venez de selectionner n'est pas dans la base")
                elif nb_pays_classes_age>=10:
                    print("    ")
                    print("Vous avez atteint le nombre maximal de pays")
                    break
                else:
                    liste_pays_classes_age.append(pays_a_ajouter)
                    nb_pays_classes_age+=1
                    ajouter_pays=True
                    while ajouter_pays:
                        try:
                            print("1: Ajouter un autre pays")
                            print("2: Continuer avec la liste des pays entres")
                            ajouter_pays=input("Voulez vous ajouter un autre pays: ")
                            ajouter_pays=int(ajouter_pays)
                            if ajouter_pays not in [1,2]:
                                print("Veuillez entrer un choix parmi la liste des choix")
                            elif ajouter_pays==1:
                                ajouter_pays=False
                            else:
                                break
                                
                        except NameError:
                            print("Veuillez entrer un choix valide")
                        except ValueError:
                            print("Veuillez entrer une reponse sous la forme d'un entier")
                    if ajouter_pays:
                        break
                            
                    
            except NameError:
                 print("Veuillez entrer le nom d'un pays correcte entre crochets")
            except SyntaxError:
                print("Veuillez entrer une reponse")
        
        while True:
            try:
                print("1: afficher les n pays les moins denses en population")
                print("2: afficher les n pays les plus denses en population")
                n_premiers=input("""voulez-vous afficher Les n premiers ou)
                                    ou n derniers pays les plus denses en population:   """)
                n_premiers=bool(n_premiers-1)
                n_pays=input("Entrer le nombre de pays a afficher:  ")
                n_pays=int(n_pays)
                
                if n_premiers not in [1,2]:
                    print("Veuillez entrer un choix parmi les options")
                elif n_pays>len(list(basePays.base.keys())):
                    print("Le nombrede pays est trop grand")
                else: 
                    break
            except:
                print("Veuillez faire une entrée valide")
        
        
        liste_pays_objets=[]
        for Pays1 in liste_pays:
            try:
                liste_pays_objets.append(basePays.base[Pays1])
            except KeyError:
                raise KeyError("Le pays "+Pays1+" ne se trouve pas dans la base verifier l'orthographe du nom")
        for pays1 in liste_pays_objets:
            pays1.afficherPays()
            print("Dette par habitant :"+str(pays1.dette/pays1.population))
            print("\n")
            
        print("\n")
        liste_pays_pour_critere=sorted(basePays.base.values(),key=lambda pays1: getattr(pays1,critere_de_tri),reverse=(not n_premier_pour_critere))[0:nb_pays_pour_critere-1]
        print("Liste des "+str(nb_pays_pour_critere)+str((lambda x: " premiers "if n_premier_pour_critere else " derniers ")(n_premier_pour_critere))+ "pays pour le critere "+dico_criteres[critere_pour_tri])
        print("     ")
        for pays1 in liste_pays_pour_critere:

            print(str(liste_pays_pour_critere.index(pays1)+1)+" : "+pays1.nom+"\n")
        print("\n")
        
        
        
        liste_pays_trie_critere=sorted(basePays.base.values(),key=lambda pays1: getattr(pays1,critere_pour_seuil),reverse=True)
        if au_dessus_seuil:
            j=0
            print("Liste des pays dont le critere "+critere_pour_seuil+" depasse  "+str(seuil))
            print("     ")
            while getattr(liste_pays_trie_critere[j],critere_de_tri)>seuil and j<len(liste_pays_trie_critere):
                print(str(j)+": "+getattr(liste_pays_trie_critere[j],"nom"))
                j+=1
        if not au_dessus_seuil:
            print("Liste des pays dont le critere "+critere_pour_seuil+" ne depasse pas "+str(seuil))
            print( "      ")
            while getattr(liste_pays_trie_critere[j],critere_de_tri)>seuil and j<len(liste_pays_trie_critere)+1:
                print(str(j)+": "+getattr(liste_pays_trie_critere[-j],"nom"))
                j+=1
        print("\n")
        print("       ")
        print("Tableau des cinqs classes d'age demande:    ")
        print("     ")
        print("      ")
        data_frame_pays_c_age=pandas.DataFrame(basePays.cinq_C_age, columns=list(basePays.cinq_C_age.keys()))

            
        data_frame_pays_c_age=data_frame_pays_c_age.loc[data_frame_pays_c_age["Pays"].isin(liste_pays_classes_age)]
        print(data_frame_pays_c_age.head())
        
        print("     ")
        liste_pays_denses=sorted(list(basePays.base.values()),key=lambda x: x.population/x.superficie,reverse=n_premiers)[0,n_pays]
        print("Voici le classement des pays les plus plus denses demandé")
        for pays1 in liste_pays_denses:
            print(liste_pays_denses.index(pays1),": ",pays1.nom)
            print("densité de population: "+str(pays1.population/pays1.superficie))
            print("      ")
        
#superficie, 
#                 population, 
#                 croissance_demo, 
#                 inflation, 
#                 dette,
#                 taux_chomage,
#                 taux_depenses_sante, 
#                 taux_depenses_educ, 
#                 taux_depenses_militaires, 
#                 cinq_classes_age)    
    def clustering_classes(self):
        data_frame_clustering=Acces_donnees.basePays_to_data_frame(basePays.cinq_C_age)
        kmeans=KMeans(n_clusters=5)
        data_frame_clustering_passage=data_frame_clustering.drop("nom_pays",axis=1)
        data_frame_clustering_passage=data_frame_clustering_passage.drop("Pays",axis=1)
        clustering_total=kmeans.fit(data_frame_clustering_passage.values)
        data_frame_clustering["Classe"]=clustering_total.labels_
        print("Vous pouvez maintenant avoir acces aux classes de pays")
        print("Selectionnez un pays pour l'afficher et connaitre sa classe")
        while True:
            try:
                pays_a_afficher=input("Nom du Pays:  ")
                if pays_a_afficher not in list(basePays.base.keys()):
                    print("Le pays selectione n'est pas dans la base")
                else:
                    break
            except ValueError:
                print("Veuillez entrer un nom de pays")
        basePays.base[pays_a_afficher].afficherPays()
#        print(type(data_frame_clustering.loc[data_frame_clustering["nom_pays"]==pays_a_afficher,"Classe"]))
        print("Classe du Pays: ",data_frame_clustering.loc[data_frame_clustering["nom_pays"]==pays_a_afficher,"Classe"])
        

        
        
        
        

        
        

            
            
            
                

        


















