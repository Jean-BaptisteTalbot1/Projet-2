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
def getFi(g,b,At,Dr,Sp,Dnom,f):  
    #return (1.03057 * abs(boulons[b][At] * boulons[b][Dr]**3)) * grades[g][Sp] / (math.sqrt(boulons[b][At]**2 * boulons[b][Dnom]**2 + 1.2851 * boulons[b][Dr]**6))
    return (0.206114 * abs(boulons[b][At] * boulons[b][Dr]**3)) * grades[g][Sp] / (math.sqrt((k*f)**2 * boulons[b][At]**2 * boulons[b][Dnom]**2 + 0.051404 * boulons[b][Dr]**6))
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



#%%###########################################################################
# Diamètre minimal pour respecter le facteur de sécurité demandé
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
##############################################################################

    

#%%###########################################################################
# Traçage des graphiques des résultats
##############################################################################
def printPlot(Dmin, seuil, FS_joint, FS_boulon, facteur):
    
    ##########################################################################    
    # Graphique du diamètre minimal
    ##########################################################################
    Y = dict()
    X = dict()
    for g in plotGrades:
        # Seconde dimension du dictionnaire de coordonnées du graphique
        X[g] = list()
        Y[g] = list()
        for d in Dmin[g]:
            X[g].append(d)
            Y[g].append(Dmin[g][d])
    plt.title("Diamètre minimal boulons p/r au nombre de boulons pour FS du joint >= " + str(seuil) + " - FC " + str(int(100*facteur)) + "%")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel("Nombre de boulons")
    plt.ylabel("Diamiètre minimal (po)")
    plt.xticks(X[g],X[g])
    plt.vlines(X[g],0.4,1, colors='k', linestyles='dashed')
    for g in plotGrades:
        plt.plot(X[g],Y[g],label="Grade : " + str(g))
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QAB1_S_' + str(seuil) + "_F_" + str(facteur) + e, dpi=q,)
    plt.show()
    ##########################################################################
    
    
    ##########################################################################
    # Graphique du FS selon le diamètre minimal
    ##########################################################################
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
    plt.title("FS boulons de diamètre minimal p/r au nombre de boulons avec un FS du joint >= " + str(seuil) + " - FC " + str(int(100*facteur)) + "%")
    plt.xlabel("Nombre de boulons")
    plt.ylabel("FS boulons du diamètre minimal")
    plt.xticks(X[g],X[g])
    plt.vlines(X[g],1.32,1.47, colors='k', linestyles='dashed')
    for g in plotGrades:       
        plt.plot(XX[g],YY[g],label="Grade : " + str(g))
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QAB2_S_' + str(seuil) + "_F_" + str(facteur) + e, dpi=q,)
    plt.show()
    ##########################################################################
    
    
def printPlot_QuestionC1(Dmin, seuil, FS_joint, FS_boulon, facteur):
    ##########################################################################    
    # Graphique du diamètre minimal
    ##########################################################################
    Y = dict()
    X = dict()
    for g in plotGrades:
        # Seconde dimension du dictionnaire de coordonnées du graphique
        X[g] = list()
        Y[g] = list()
        for d in Dmin[g]:
            X[g].append(d)
            Y[g].append(Dmin[g][d])
    plt.title("Diamètre minimal boulons p/r au nombre de boulons pour FS du joint de " + str(seuil) + " - FC " + str(int(100*facteur)) + "%")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel("Nombre de boulons")
    plt.ylabel("Diamiètre minimal (po)")
    plt.xticks(X[g],X[g])
    plt.vlines(X[g],0.4,1, colors='k', linestyles='dashed')
    for g in plotGrades:
        plt.plot(X[g],Y[g],label="Grade : " + str(g))
    plt.plot(40,0.5, 'ro', label="Question C - P1",)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QC1_S_' + str(seuil) + "_F_" + str(facteur) + e, dpi=q,)
    plt.show()
    ##########################################################################
   
    
    
def printPlot_QuestionC2(Dmin, seuil, FS_joint, FS_boulon, facteur):
    ##########################################################################
    # Graphique du FS selon le diamètre minimal
    ##########################################################################
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
    plt.title("FS boulons de diamètre minimal p/r au nombre de boulons avec un FS du joint de " + str(seuil) + " - FC " + str(int(100*facteur)) + "%")
    plt.xlabel("Nombre de boulons")
    plt.ylabel("FS boulons du diamètre minimal")
    plt.xticks(XX[g],XX[g])
    plt.vlines(XX[g],1.32,1.47, colors='k', linestyles='dashed')
    for g in plotGrades:       
        plt.plot(XX[g],YY[g],label="Grade : " + str(g))
    plt.plot([24,48],[1.45,1.45], label="Question C - Partie 2")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QC2_S_' + str(seuil) + "_F_" + str(facteur) + e, dpi=q,)
    plt.show()
    ##########################################################################
    
    
    
    
    
    
def printPlot_QuestionD(XD, YD, XXD, YYD):

    plt.title("Comparaison du diamètre minimal pour le grade 5 " + " avec un FS du joint >= 2" + " - FC ")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel("Nombre de boulons")
    plt.ylabel("Diamiètre minimal (po)")    
    plt.xticks(XD[1],XD[1])
    
    for X in XD: 
        plt.vlines(XD[X],0.4,1, colors='k', linestyles='dashed')    
        plt.plot(XD[X],YD[X],label="Incertitude : " + str(X))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QD1_S_2' + "_F_" + str(X) + e, dpi=q,)
    plt.show()
    ##########################################################################
    
    
    
    
    plt.title("Comparaison du diamètre minimal pour le grade 5 " + " avec un FS du joint >= 2 " + " - FC ")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel("Nombre de boulons")
    plt.ylabel("Diamiètre minimal (po)")    
    plt.xticks(XD[1],XD[1])
    
    for X in XXD: 
        plt.vlines(XXD[X],1.2,1.6, colors='k', linestyles='dashed')    
        plt.plot(XXD[X],YYD[X],label="Incertitude : " + str(X))
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    plt.rcParams['figure.figsize'] = l, h
    plt.tight_layout()
    plt.savefig(path + '\QD2_S_2' + "_F_" + str(X) + e, dpi=q,)
    plt.show()
    ##########################################################################