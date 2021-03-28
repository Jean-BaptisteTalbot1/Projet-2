# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:20:21 2021

@author: Catherine Roy-Blais && Jean-Baptiste Talbot 
"""

import math
from math import pi
from sympy import Eq, solve, symbols
import matplotlib.pyplot as plt
import Boulons_Projet2
from Donnees_Conversions import *

from collections import OrderedDict

# Nettoyage de la console
#print("\033[H\033[J")

#%% Données des boulons et des grades
boulons = Boulons_Projet2.get_boulons()
grades  = Boulons_Projet2.get_grades()

##############################################################################
#%% Fa
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


#%% FS joint

# Forces initiales des différentes tailles de boulons
Fi = dict()
# Facteur de sécurité du joint selon la force initiale du boulon et la force étendue sur le nombre de boulon
FS_joint = dict()
FS_boulon = dict()

# Parcourt tous les nombres de boulons possibles pour chacune des tailles de chacun des grades
# g1 :  b1 :    n1
#               n2
#       b2 :    n1
#       b3 :    n2
# g2 :  b1 :    n1
# ...          
for g in grades:
    # Création de la première dimension des dictionnaires   
    Fi[g] = dict()
    FS_joint[g] = dict()    
    FS_boulon[g] = dict()
    
    # Parcourt des boulons
    for b in boulons:
        
        FS_joint[g][b] = dict()
        FS_boulon[g][N] = dict()
        Fi[g][b] = dict()
    
        Fi[g][b] = (1.03057 * abs(boulons[b]["AtMM"] * boulons[b]["DrMM"]**3)) * grades[g]["Sp_MPa"] / (math.sqrt(boulons[b]["AtMM"]**2 * boulons[b]["DnomMM"]**2 + 1.2851 * boulons[b]["DrMM"]**6))
        
        for N in n:
            FS_joint[g][b][N] = Fi[g][b] / (Fa_Newton[N] * (1-boulons[b]["c_SI"]))


def printPlot(seuil):
    
    Dmin = dict()
    for g in grades:
        Dmin[g] = dict()
        for N in n:
            for b in boulons:
                if (FS_joint[g][b][N] >= seuil):
                    FS_boulon[g][N] = (grades[g]["Sp_MPa"] * boulons[b]["AtMM"]) / (Fi[g][b] + boulons[b]["c_SI"] * Fa_Newton[N]) 
                    Dmin[g][N] = boulons[b]["DnomPO"]
                    break
     
    Y = dict()
    X = dict()
    for g in grades:
        X[g] = list()
        Y[g] = list()
        for d in Dmin[g]:
            X[g].append(d)
            Y[g].append(Dmin[g][d])
    
    plt.title("Diamètre minimal des boulons en fonction du nombre de boulons avec un FS du joint de " + str(seuil) )
    for g in grades:
        print(X[g])
        plt.plot(X[g],Y[g],label="Grade : " + str(g))
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    #plt.axis([24,48,0.25,1.1])
    plt.show()
    
    for f in FS_boulon:    
        FS_boulon[f] = OrderedDict(sorted(FS_boulon[f].items()))
    
    YY = dict()
    XX = dict()
    for g in grades:
        XX[g] = list()
        YY[g] = list()
        for f in FS_boulon[g]:
            XX[g].append(f)
            YY[g].append(FS_boulon[g][f])
    
    plt.title("Facteur de sécurité des boulons de diamètres minimal en fonction du nombre de boulons avec un FS du joint de " + str(seuil) )
    
    for g in grades:    
        plt.plot(XX[g],YY[g],label="Grade : " + str(g))
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    #plt.axis([24,48,1.3,1.5])
    plt.show()



printPlot(2)

printPlot(3)    
