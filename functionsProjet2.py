# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:38:32 2021

@author: jbtalbot
"""
from Donnees_Conversions import *
import Boulons_Projet2
import math
import matplotlib.pyplot as plt
from collections import OrderedDict


boulons = Boulons_Projet2.get_boulons()
grades  = Boulons_Projet2.get_grades()
plotGrades = Boulons_Projet2.get_PlotGrades()

#%%###########################################################################
# Calcul de la force initiale
##############################################################################
def getFi(g,b,At,Dr,Sp,Dnom):  
    return (1.03057 * abs(boulons[b][At] * boulons[b][Dr]**3)) * grades[g][Sp] / (math.sqrt(boulons[b][At]**2 * boulons[b][Dnom]**2 + 1.2851 * boulons[b][Dr]**6))
##############################################################################



#%%###########################################################################
# Ajustement du grade selon la dimension du boulon (Grade 2)
##############################################################################
def adjustGradeToGet(g,b):
    if g == "2":
            if (boulons[b]["DnomPO"] == "7/8") or (boulons[b]["DnomPO"] == "1"):
                gradeToGet = "2 - 7/8-1 1/2"
            else:
                gradeToGet = "2 - 1/4-3/4"
    else:
            gradeToGet = g
    return gradeToGet
##############################################################################



def calculDiametreMin(seuil, FS_joint, FS_boulon, Fi, Fa):
    # Première dimension du dictionnaire
    Dmin = dict()
    for g in plotGrades:                    

        # Seconde dimension du dictionnaire    
        Dmin[g] = dict()

        # Pour tous les nombres de boulons
        for N in n:
            # Parcourt tous les boulons
            for b in boulons:
                # Jusqu'à atteindre le diamètre minimale pour atteindre le seuil voulu
                if (FS_joint[g][b][N] >= seuil):
                    gradeToGet = adjustGradeToGet(g,b)
                    FS_boulon[g][N] = (grades[gradeToGet]["Sp_MPa"] * boulons[b]["AtMM"]) / (Fi[g][b] + boulons[b]["c_SI"] * Fa[N]) 
                    Dmin[g][N] = boulons[b]["DnomPO"]
                    break
    return Dmin




    



#%%###########################################################################
# Traçage des graphiques des résultats
##############################################################################
def printPlot(Dmin, seuil, FS_joint, FS_boulon):
    
    # Coordonnées du graphique
    Y = dict()
    X = dict()
    
    for g in plotGrades:
        
        # Seconde dimension du dictionnaire de coordonnées du graphique
        X[g] = list()
        Y[g] = list()
        
        for d in Dmin[g]:
            X[g].append(d)
            Y[g].append(Dmin[g][d])
    
    plt.title("Diamètre minimal des boulons en fonction du nombre de boulons avec un FS du joint de " + str(seuil) )
    for g in plotGrades:

        print(X[g])
        plt.plot(X[g],Y[g],label="Grade : " + str(g))
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    #plt.axis([24,48,0.25,1.1])
    plt.show()
    
    for f in FS_boulon:    
        FS_boulon[f] = OrderedDict(sorted(FS_boulon[f].items()))
    
    YY = dict()
    XX = dict()
    for g in plotGrades:
                
        XX[g] = list()
        YY[g] = list()
        for f in FS_boulon[g]:
            XX[g].append(f)
            YY[g].append(FS_boulon[g][f])
    
    plt.title("Facteur de sécurité des boulons de diamètres minimal en fonction du nombre de boulons avec un FS du joint de " + str(seuil) )
    
    for g in plotGrades:       
        plt.plot(XX[g],YY[g],label="Grade : " + str(g))
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    #plt.axis([24,48,1.3,1.5])
    plt.show()