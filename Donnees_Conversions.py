# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:21:16 2021

@author: jbtalbot
"""

# Coefficient de conversion
bar_Pa = 100000         # Bar en Pascals
N_lbs = 0.2248089431    # Newtons en livres
po_mm = 25.4            # Pouce en mm
po2_mm2 = 645.1600      # Pouce carré en mm carré
kPSI_MPa = 6.89476      # Kilo PSI en mégaPascals


L_mm = 2 * po_mm # mm
Eb = 207*(10**3)


# Facteur de couple pour relation entre couple appliqué et force initiale 
K   = 0.2 
Pi  = 10 # bar

Pi_Pa = Pi * bar_Pa # Pa


FS_serrage = 1.1


D = 1 # mètres

# Nombre admissible de boulons
n = [24,28,32,36,40,44,48]
