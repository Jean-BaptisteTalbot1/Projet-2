# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:20:21 2021

@author: Catherine
"""

import math
from math import pi
from sympy import Eq, solve, symbols 

# Nettoyage de la console
#print("\033[H\033[J")

##############################################################################
#%% CONSTANTES

d = symbols('d')

K   = 0.2 #pour relation entre couple appliqué et force initiale
Pi  = 10 # bar
Pi_psi = Pi*14.5 # psi
L = 2 # po
n1 = 24 
n2 = 28 
n3 = 32 
n4 = 36 
n5 = 40 
n6 = 44 
n7 = 48 
FS_boulon = 1.1
E = 207*(10**3)



##############################################################################
#%% Fa

Fa_24 = (Pi_psi*math.pi*(500/4))/n1
Fa_28 = (Pi_psi*math.pi*(500/4))/n2
Fa_32 = (Pi_psi*math.pi*(500/4))/n3
Fa_36 = (Pi_psi*math.pi*(500/4))/n4
Fa_40 = (Pi_psi*math.pi*(500/4))/n5
Fa_44 = (Pi_psi*math.pi*(500/4))/n6
Fa_48 = (Pi_psi*math.pi*(500/4))/n7



##############################################################################
#%% Cônes inversés Approche 1

km = symbols('km')

km = (0.5774*math.pi*E*d)/(2*math.log(5*(((0.5774*L)+(0.5*d))/((0.5774*L)+(2.5*d)))))

##############################################################################
#%% FS Serrage



