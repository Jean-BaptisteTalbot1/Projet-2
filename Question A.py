# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:20:21 2021

@author: Catherine Roy-Blais && Jean-Baptiste Talbot 
"""

import math
from math import pi
from sympy import Eq, solve, symbols
import Boulons_Projet2
from Donnees_Conversions import *
from functionsProjet2 import getFi, printPlot, adjustGradeToGet, calculDiametreMin

# Nettoyage de la console
#print("\033[H\033[J")

#%% Données des boulons et des grades
boulons = Boulons_Projet2.get_boulons()
grades  = Boulons_Projet2.get_grades()
plotGrades = Boulons_Projet2.get_PlotGrades()

#%%###########################################################################
# Fa
##############################################################################
# Force totale  ->  Force = Pression * Surface
# Aire
A = pi * (D/2)**2
F = Pi_Pa * A
# Force 
Fa_Newton   = dict()
Fa_Lbs      = dict()

# Parcourt des nombres de boulons disponibles pour diviser la force par ce nombre
for N in n:
    Fa_Newton[N]    = (F/N)       # Newtons
    Fa_Lbs[N]       = (F*N_lbs)/N  # Livres
##############################################################################



#%%###########################################################################
# FS joint
##############################################################################
# Forces initiales des différentes tailles de boulons
Fi = dict()
# Facteur de sécurité du joint selon la force initiale du boulon et la force étendue sur le nombre de boulon
FS_joint = dict()
FS_boulon = dict()

# Parcourt des grades
for g in plotGrades:    
    
    print(g)
    # Création de la première dimension des dictionnaires   
    Fi[g]           = dict()
    FS_joint[g]     = dict()    
    FS_boulon[g]    = dict()
    
    # Parcourt des boulons
    for b in boulons:
    
        print(b)
        FS_joint[g][b]  = dict()
        FS_boulon[g][N] = dict()
        Fi[g][b]        = dict()
        
        gradeToGet = adjustGradeToGet(g,b)
        
        Fi[g][b] = getFi(gradeToGet,b,"AtMM","DrMM","Sp_MPa","DnomMM")
            
        # Parcourt des nombres de boulons
        for N in n:
            print(N)
            FS_joint[g][b][N] = Fi[g][b] / (Fa_Newton[N] * (1-boulons[b]["c_SI"]))
##############################################################################



#%%###########################################################################
# Traçage des graphiques
##############################################################################
seuils = [2,3]

for seuil in seuils:
    printPlot(calculDiametreMin(seuil, FS_joint, FS_boulon, Fi, Fa_Newton), seuil, FS_joint, FS_boulon)

##############################################################################