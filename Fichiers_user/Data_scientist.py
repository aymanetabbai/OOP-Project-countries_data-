#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:55:29 2020


"""

import os
import pickle 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

from Fichiers_user.UtilisateurPrive import utilisateurPrive
import pandas
from Configurations_bases.BasePays import basePays,Pays,sauvegarder_base_correction
import Configurations_bases.Acces_donnees as Acces_donnees


class Data_s(utilisateurPrive):### Classe Data_scientist
#%%
    def __init__(self,identifiant,mdp,historique=[],etat=0):
        self.identifiant=identifiant
        self.mdp=mdp
        self.historique=historique
        self.etat=etat
     
#%%       
    def afficher_pays(self,nom_pays):
        basePays.base[nom_pays].afficherPays()   
        
    
        
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
                    pays_a_ajouter=input("Entrer le nom du pays numero "+str(nombre_pays+1)+": ")
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
#%%        
    def proposer_correction(self):


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
                elif info in 13:
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
                    modification=int(modification)
                    
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
                except ValueError:
                    print("Veuillez faire une entrée valide")
        else:
            
            exit()

        basePays.corrections.append([nom_pays,dico_criteres[info],modification])
        sauvegarder_base_correction()
        print("         ")
        print("Modification bien soumise!!")
    

    
        ## Reste à faire les questions pour chacun
        
            
