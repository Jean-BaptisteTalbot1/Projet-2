# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:53:37 2021

@author: jbtalbot
"""

import math
from math import pi

from Donnees_Conversions import *

def get_boulons():

    boulons = {
        
            "1/4" : {
                "DnomPO"    : 0.25,
                "PasPO"     : 20,
                "AtPO"      : 0.0318, 
                "ArPO"      : 0.0269
                },
            
            "5/16" : {
                "DnomPO"    : 0.3125,
                "PasPO"     : 18,
                "AtPO"      : 0.0524,
                "ArPO"      : 0.0454
                },
            
            "3/8" : {
                "DnomPO"      : 0.3750,
                "PasPO"       : 16,
                "AtPO"        : 0.0775, 
                "ArPO"        : 0.0678
                },
            
            "7/16" : {
                "DnomPO"      : 0.4375,
                "PasPO"       : 14,
                "AtPO"        : 0.1063, 
                "ArPO"        : 0.0933
                },
            
            "1/2" : {
                "DnomPO"      : 0.5000,
                "PasPO"       : 13,
                "AtPO"        : 0.1419, 
                "ArPO"        : 0.1257
                },
            
            "9/16" : {
                "DnomPO"      : 0.5625,
                "PasPO"       : 12,
                "AtPO"        : 0.182, 
                "ArPO"        : 0.162
                },
            
            "5/8" : {
                "DnomPO"      : 0.6250,
                "PasPO"       : 11,
                "AtPO"        : 0.226, 
                "ArPO"        : 0.202
                },
            
            "3/4" : {
                "DnomPO"      : 0.7500,
                "PasPO"       : 10,
                "AtPO"        : 0.334, 
                "ArPO"        : 0.302
                },
            
            "7/8" : {
                "DnomPO"      : 0.8750,
                "PasPO"       : 9,
                "AtPO"        : 0.462, 
                "ArPO"        : 0.419
                },
            
            "1" : {
                "DnomPO"      : 1.000,
                "PasPO"       : 8,
                "AtPO"        : 0.606, 
                "ArPO"        : 0.551
                }       
        }


    
    for b in boulons:
        boulons[b]["DnomMM"] = boulons[b]["DnomPO"] * po_mm # Diamètre nominal en mm
        boulons[b]["PasMM"] = po_mm / boulons[b]["PasPO"] # Pas en système international
        boulons[b]["AtMM"] = boulons[b]["AtPO"] * po2_mm2 # Surface de tension At et surface de cisaillement Ar en système international
        boulons[b]["ArMM"] = boulons[b]["ArPO"] * po2_mm2
        boulons[b]["kb_N/mm"] = (boulons[b]["AtMM"] * Eb)/L_mm # Rigidité de la vis
        boulons[b]["km_N/mm"] = (0.5774*pi*Eb*boulons[b]["DnomMM"])/(2*math.log(5*(((0.5774*L_mm)+(0.5*boulons[b]["DnomMM"]))/((0.5774*L_mm)+(2.5*boulons[b]["DnomMM"]))))) # Cônes inversés Approche 1
        boulons[b]["c_SI"] = boulons[b]["kb_N/mm"] / (boulons[b]["kb_N/mm"] + boulons[b]["km_N/mm"]) # Constante de joint
        boulons[b]["DrMM"] = 2 * math.sqrt(boulons[b]["ArMM"]/pi) # Diamètre de la racine
    
    
    return boulons
    
    
#wee%%###########################################################################
##      GRADE
##############################################################################    
    
def get_PlotGrades():
    return ["1","2","4","5","7","8"]

def get_grades():
    
    # Grade admissible des boulons
    grades = {
        "1" : {
            "Sp_kPSI" : 33,
            "Sut_kPSI" : 60,
            "Sy_kPSI" : 36,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "2 - 1/4-3/4" : {
            "Sp_kPSI" : 55,
            "Sut_kPSI" : 74,
            "Sy_kPSI" : 57,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "2 - 7/8-1 1/2" : {
            "Sp_kPSI" : 33,
            "Sut_kPSI" : 60,
            "Sy_kPSI" : 36,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "4" : {
            "Sp_kPSI" : 65,
            "Sut_kPSI" : 115,
            "Sy_kPSI" : 100,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "5" : {
            "Sp_kPSI" : 85,
            "Sut_kPSI" : 120,
            "Sy_kPSI" : 92,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "7" : {
            "Sp_kPSI" : 105,
            "Sut_kPSI" : 133,
            "Sy_kPSI" : 115,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            },
        
        "8" : {
            "Sp_kPSI" : 120,
            "Sut_kPSI" : 150,
            "Sy_kPSI" : 130,
            
            "Sp_MPa" : 0,
            "Sut_MPa" : 0,
            "Sy_MPa" : 0,
            }        
    }

    for g in grades:
        grades[g]["Sp_MPa"] = grades[g]["Sp_kPSI"] * kPSI_MPa


    
    return grades
