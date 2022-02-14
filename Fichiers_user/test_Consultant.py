# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:09:27 2020

"""

### Fichier tests unitaires #######"

import unittest2
import mock
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Fichiers_user.Consultant as Consultant

Consult1= Consultant.consultant()
liste_strings_test=[]
liste_inputs_test=["Mon_pays","Sri Lanka"]
### Sachant que Mon_pays nest pas un pays dans la base on s'attends à ce que la fonction
### renvoie une erreur ou gère l'entrée
liste_strings_attendue=['nom pays:  ',
                        '        ',
                        '         ',
                        "Ce Pays n'est pas dans la base",
                        'nom pays:  ',
                        '        ',
                        '         ',
                        'nom pays: Sri Lanka\n',
                        'superficie: 65610\n',
                        'population: 22235000\n',
                        'croissance demographique: 0.8\n',
                        'inflation: 4.3\n',
                        'dette: 47650000000\n',
                        'taux de chomage: 4.5\n',
                        'taux depenses sante: 3.5du PIB\n',
                        'taux depenses education: 2.2du PIB\n',
                        'taux depenses militaires: 2.43du PIB\n',
                        '0-14 ans: 24.35% (male 2,760,821/female 2,652,747)',
                        '15-24 ans: 14.7% (male 1,660,402/female 1,608,022)',
                        '25-54 ans: 41.71% (male 4,544,253/female 4,729,544)',
                        '54-64 ans: 9.89% (male 1,018,357/female 1,181,060)',
                        '65 et plus: 9.89% (male 1,018,357/female 1,181,060)']

def remplace_print(string):
    liste_strings_test.append(string)


def remplace_input(string):
    liste_strings_test.append(string)
    element_a_retourner=liste_inputs_test[0]
    liste_inputs_test.pop(0)
    return(element_a_retourner)

class Test_afficher_pays(unittest2.TestCase):
    
    def test_les_valeurs(self):
        with mock.patch("builtins.input",remplace_input):
            with mock.patch("builtins.print",remplace_print):
                Consult1.afficher_pays() 
        self.assertListEqual(liste_strings_test,liste_strings_attendue)




#%%
## Dans cette partie on teste la méthode proposer correction de consultant
        
## On lui entre différentes valeurs pour voir comment la fonction gère les mauvaises entrées
        
        
liste_strings_correction=[]
liste_inputs_correction=["Panda","France","20","2","panda","2000000"]

liste_sortie_attendue=['Entrer le nom du pays concerne ou retour pour retourner au menu des taches',
                       'nom du Pays:  ',
                       "Le pays que vous avez rentre n'est pas dans la base",
                       'Entrer le nom du pays concerne ou retour pour retourner au menu des taches',
                       'nom du Pays:  ',
                       "Veuillez selectionner l'info que vous voulez corriger",
                       '1: Nom du Pays',
                       '2: Superficie',
                       '3: Population',
                       '4: Croissance demographique',
                       '5: Inflation',
                       '6: Dette',
                       '7: Taux de chomage',
                       '8: Taux de depenses en sante',
                       '9: Taux de depenses en education',
                       '10: Taux de depenses militaires',
                       "11: Repartition de cinq classes d'âge",
                       '12: Retourner au menu des taches', 
                       ':::   ',
                       'Veuillez choisir parmi les options ',
                       ':::   ', 
                       'entrer la superficie:  ',
                       'Veuillez entrer une reponse sous forme de flottant',
                       'entrer la superficie:  ',
                       '         ',
                       'Modification bien soumise!!']


def remplace_print_correction(string):
    liste_strings_correction.append(string)


def remplace_input_correction(string):
    liste_strings_correction.append(string)
    element_a_retourner=liste_inputs_correction[0]
    liste_inputs_correction.pop(0)
    return(element_a_retourner)

class Test_proposer_correction(unittest2.TestCase):
    
    def test_inputs_correction(self):
        with mock.patch("builtins.input",remplace_input_correction):
            with mock.patch("builtins.print",remplace_print_correction):
                Consult1.proposer_correction() 
        self.assertListEqual(liste_strings_correction,
                                                liste_sortie_attendue)
        
        


if __name__=="__main__":
    unittest2.main()
    
 

                
                
                         
                

