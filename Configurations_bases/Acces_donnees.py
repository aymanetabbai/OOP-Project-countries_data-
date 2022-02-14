# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:05:37 2020

@author: Chloé
"""

import json
import pickle
import pandas
filename="factbook-country-profiles.json"

with open(filename) as json_file:
    donnees = json.load(json_file)


#%%

def arret_paranthese(string):
#    """Cette fonction prends en paramètre un string et s'arrête à la première paranthèse
#     elle sert à la trasnformation des données sous forme de string pour la conversion en int ou float"""
     
#     """
#     @param: string
#     @return: string
#     """
    j=0
    retour=""
    while string[j]!='(' and j<len(string)-1:
        retour+=string[j]
        j+=1
    return(retour)
def arret_o(string):## la fonction prends en paramètre un string et renvoie un string
    ## Cette fonction prends en paramètre un string et s'arrête au premier "o"
    ## elle sert à la trasnformation des données sous forme de string pour la conversion en int ou float
    j=0
    retour=""
    while string[j]!='o' and j<len(string)-1:
        retour+=string[j]
        j+=1
    return(retour)
#%%
    
#    """ enlève les pays avec des données manquantes et se charge de la conversion des donnéées en int
#     cette fonctin renvois un dictionnaire avec comme clés les noms des pays et comme valeur associée à la clé
#     les informations du pays sous forme de dictionnaire 
#     """
def AccesDonnees(donnees):

     
#     """@param: dict:
#         @return: dict:{ nom_pays": {"nom_pays": nom_pays,"superficie":superficie\
#                                             ,"population":population\
#                                             ,"croissance demographique":croiss_demo,\
#                                             "inflation":inflation,\
#                                             "dette":dette,\
#                                             "taux de chomage":taux_chomage,\
#                                             "taux depenses sante":taux_depenses_sante,\
#                                             "taux depenses education":taux_depense_educ,\
#                                             "taux depenses militaires":taux_depense_militaire,\
#                                             "cinq classes age":cinq_classes_age},....   }"""
    
    dico = {} 
    n=0
    for i in range(len(donnees)):
    ##on conserve juste les pays ne possédant aucun critère manquant 
        if (donnees[i].get('Geography')!= None and donnees[i]['Geography'].get('Area')!= None and donnees[i]['Geography']['Area'].get('total')!= None and \
                donnees[i]['Geography']['Area']['total'].get('text')!= None and  donnees[i].get('People and Society')!=None and \
                donnees[i]['People and Society'].get('Population')!= None and donnees[i]['People and Society']['Population'].get('text')!= None and\
                donnees[i].get('People and Society') != None and donnees[i]['People and Society'].get('Population growth rate') != None and \
                donnees[i]['People and Society']['Population growth rate'].get('text') != None and donnees[i].get('Economy')!= None and \
                donnees[i]['Economy'].get('Inflation rate (consumer prices)')!= None and donnees[i]['Economy']['Inflation rate (consumer prices)'].get('text')!= None and\
                donnees[i]['Economy'].get('Debt - external') != None and donnees[i]['Economy']['Debt - external'].get('text') != None and\
                "NA" not in str(donnees[i]['Economy']['Unemployment rate'].get('text'))  and\
                donnees[i]['People and Society'].get('Health expenditures') != None and "NA" not in str(donnees[i]['People and Society']['Health expenditures'].get('text'))  and \
                donnees[i]['People and Society'].get('Education expenditures') != None and "NA" not in str(donnees[i]['People and Society']['Education expenditures'].get('text'))  and\
                donnees[i].get('Military and Security')!= None and donnees[i]['Military and Security'].get('Military expenditures')!= None and \
                "NA" not in donnees[i]['Military and Security']['Military expenditures'].get('text')  and\
                donnees[i]['People and Society']['Age structure']!= None and len(donnees[i]['People and Society']['Age structure'].values())==5):
            nom_pays = str(donnees[i]['Government']['Country name']['conventional short form']['text'])
            ## correction de population transformation en int
            population=str(donnees[i]['People and Society']['Population']['text']).replace("(July 2016 est.)","")
            population=population.replace("(includes populations of the Golan Heights of Golan Sub-District and also East Jerusalem, which was annexed by Israel after 1967)","")
            
            population=population.replace(',','')
            if "million" in population:
                population=population.replace("million","")
                population=int(float(population)*(10**6))
            population=int(population)

            ##correction de superficie transformation en int
            superficie=donnees[i]['Geography']['Area']['total']['text'].replace("sq km","").replace(',','')
            superficie=superficie.replace("(metropolitan France)","")
            superficie=superficie.replace("(of which 3355  are in north Cyprus)","")
            if nom_pays=="France":
                superficie=551500
            elif "million" in superficie:
                superficie=int(float(superficie)*(10**6))
            else:
                superficie=int(superficie)

            ## correction croissance demo transformation en float
            croiss_demo=str(donnees[i]['People and Society']['Population growth rate']['text']).replace("% (2016 est.)","")
            croiss_demo=float(croiss_demo)
            ## correction inflation transformation en float
            inflation=arret_paranthese(str(donnees[i]['Economy']['Inflation rate (consumer prices)']['text'])).replace("%","")
            inflation=float(inflation)
            ## Correction dette en int 
            dette=arret_paranthese(donnees[i]['Economy']['Debt - external']['text'])
    
            if "million" in dette:
                dette=dette.replace("million","")
                dette=dette.replace("$","")
                dette=int(float(dette)*(10**6))
            elif "billion" in dette:
                dette=dette.replace("billion","")
                dette=dette.replace("$","")
                dette=int(float(dette)*(10**9))
            elif "trillion" in dette:
                dette=dette.replace("trillion","")
                dette=dette.replace("$","")
                dette=int(float(dette)*(10**12))
            elif dette=='$0 ':
                dette=0

                ## correction taux de chomage transformation en float
            taux_chomage=arret_paranthese(str(donnees[i]['Economy']['Unemployment rate']['text'])).replace('%','')
            taux_chomage=float(taux_chomage)
            ##correction taux de depenses sante transformation en float
            taux_depenses_sante=arret_o(str(donnees[i]['People and Society']['Health expenditures']['text'])).replace('%','')
            taux_depenses_sante=float(taux_depenses_sante)
            ##correction taux depense educ
            taux_depense_educ=arret_o(str(donnees[i]['People and Society']['Education expenditures']['text'])).replace('%','')
            taux_depense_educ=float(taux_depense_educ)
            ## corection taux depense militaire
            taux_depense_militaire=arret_o(str(donnees[i]['Military and Security']['Military expenditures']['text'])).replace('%','')
            taux_depense_militaire=float(taux_depense_militaire)
            dico[nom_pays] = {"nom_pays": nom_pays,"superficie":superficie\
                                             ,"population":population\
                                             ,"croissance demographique":croiss_demo,\
                                             "inflation":inflation,\
                                             "dette":dette,\
                                             "taux de chomage":taux_chomage,\
                                             "taux depenses sante":taux_depenses_sante,\
                                             "taux depenses education":taux_depense_educ,\
                                             "taux depenses militaires":taux_depense_militaire,\
                                             "cinq classes age":donnees[i]['People and Society']['Age structure']}
                
            n=n+1
    print(str(n) + ' pays sans valeurs manquantes')
    return dico
##%%
    


def dico_classes_ages_to_liste(dico_c_ages):
#    """Cette fonction transforme un dico de classes d'age en un dictionnaire de liste pour être transformé en 
#    DataFrame """
#    
#    """@param : dict
#       @return: dict: {"0-14 ans": [.....], ....}
#       """
#    
    
    
    dico_resultats={"Pays":[],
                   "0-14 ans":[],
                   "15-24 ans":[],
                   "25-54 ans":[],
                   "55-64 ans":[],
                   "65 ans et +":[]}
    for cle,attribut_c_c_ages in dico_c_ages.items():
        #print(len(attribut_c_c_ages.values()))
        dico_resultats["Pays"].append(cle)
        c_age=list(attribut_c_c_ages.values())
        #print(type(c_age))
        #print(c_age)
        #print(c_age[0].values())
        #print(len(c_age))
        c1 = list(c_age[0].values())[0][0:5].strip('% (male ')
        #print("c1=",c1)
        c2 = list(c_age[1].values())[0][0:5].strip('% (male ')
        #print(c2)
        c3 = list(c_age[2].values())[0][0:5].strip('% (male ')
        #print(c3)
        c4 = list(c_age[3].values())[0][0:5].strip('% (male ')
        #print(c4)
        c5 = list(c_age[4].values())[0][0:5].strip('% (male ')
        #print(c5)
        dico_resultats["0-14 ans"]=dico_resultats["0-14 ans"]+[float(c1)]
        dico_resultats["25-54 ans"]=dico_resultats["25-54 ans"]+[float(c3)]
        dico_resultats["15-24 ans"]=dico_resultats["15-24 ans"]+[float(c2)]
        dico_resultats["55-64 ans"]=dico_resultats["55-64 ans"]+[float(c4)]
        dico_resultats["65 ans et +"]=dico_resultats["65 ans et +"]+[float(c5)]
    return(dico_resultats)
#%%
    
def dico_c_age_to_dataframe(c_age,nom_pays):
    liste_c_age=list(c_age.values())
    print(liste_c_age)
    c1 = list(liste_c_age[0].values())[0][0:5].strip('% (male ')
    #print("c1=",c1)
    c2 = list(liste_c_age[1].values())[0][0:5].strip('% (male ')
    #print(c2)
    c3 = list(liste_c_age[2].values())[0][0:5].strip('% (male ')
    #print(c3)
    c4 = list(liste_c_age[3].values())[0][0:5].strip('% (male ')
    #print(c4)
    c5 = list(liste_c_age[4].values())[0][0:5].strip('% (male ')
    #print(c5)
    data_frame_retourne=pandas.DataFrame({"nom du Pays":[nom_pays],
                                          "0-14 ans":[c1],
                                          "15-24 ans":[c2],
                                          "25-54 ans":[c3],
                                          "55-64 ans":[c4],
                                          "65 ans et +":[c5]})
    return(data_frame_retourne)
    
def basePays_to_data_frame(base_c_age):
    dico=AccesDonnees(donnees)
    for key,value in dico.items():
        dico[key].pop('cinq classes age')
    dico_passage={"nom_pays": [],
                  "superficie":[],\
                 "population":[],\
                 "croissance demographique":[],\
                 "inflation":[],\
                 "dette":[],\
                 "taux de chomage":[],\
                 "taux depenses sante":[],\
                 "taux depenses education":[],\
                 "taux depenses militaires":[]}
    for value in dico.values():
        dico_passage["nom_pays"].append(value["nom_pays"])
        dico_passage["superficie"].append(value["superficie"])
        dico_passage["population"].append(value["population"])
        dico_passage["croissance demographique"].append(value["croissance demographique"])
        dico_passage["inflation"].append(value["inflation"])
        dico_passage["dette"].append(value["dette"])
        dico_passage["taux de chomage"].append(value["taux de chomage"])
        dico_passage["taux depenses sante"].append(value["taux depenses sante"])
        dico_passage["taux depenses education"].append(value["taux depenses education"])
        dico_passage["taux depenses militaires"].append(value["taux depenses militaires"])
        
    data_frame_pays=pandas.DataFrame(dico_passage,columns=list(dico_passage.keys()))
    data_frame_c_age=pandas.DataFrame(base_c_age,columns=list(base_c_age.keys()))
    data_frame_merged=pandas.merge(data_frame_pays,data_frame_c_age,left_on="nom_pays",right_on="Pays")
    return(data_frame_merged)
    

    
    
    
    
    
    
    
    