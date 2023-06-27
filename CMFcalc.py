# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:26 2016

@author: Andrew Stockman

"""


import numpy as np



def absorptancefromabsorbance(LMSabsf, Lod, Mod, Sod, loglin):  #Calculates LMS absorptances from absorbances given ODs
    LMSabtanceout = np.zeros(np.shape(LMSabsf)) # For return
    LMSabtanceout[:,0] = LMSabsf[:,0] # Wavelength in column 0

    LMSabtanceout[:,1] = (1-10**(-Lod*LMSabsf[:,1]))/(1-10**(-Lod))     #Lin absorbances
    LMSabtanceout[:,2] = (1-10**(-Mod*LMSabsf[:,2]))/(1-10**(-Mod))
    LMSabtanceout[:,3] = (1-10**(-Sod*LMSabsf[:,3]))/(1-10**(-Sod))

    if loglin == 'log':
        for n in range (1,4):
            LMSabtanceout[:,n] = np.log10(LMSabsf[:,n])             #Log absorbances

    return LMSabtanceout



def absorbancefromabsorptance(LMSin, Lod, Mod, Sod, loglin):
    LMSout = np.copy(LMSin) #For local calculation and return
 
    LMSout[:,1] = -np.log10(1-LMSin[:,1]*(1-10**-Lod))/Lod
    LMSout[:,2] = -np.log10(1-LMSin[:,2]*(1-10**-Mod))/Mod
    LMSout[:,3] = -np.log10(1-LMSin[:,3]*(1-10**-Sod))/Sod

    if loglin == 'log':
        for n in range (1,4):
            LMSout[:,n] = np.log10(LMSout[:,n])   #Log absorptances 

    return LMSout


def absorptancefromlinqcornea(LMSin, mac, lens, mac_460, lens_400, loglin):  #Remove standard macular and lens
    LMSout = np.copy(LMSin) #For local calculation and return

    mac_template_460 = 0.35     #Template peak
    lens_template_400 = 1.7649   #Template peak
    macscale=mac_460/mac_template_460
    lensscale=lens_400/lens_template_400

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] * 10**(macscale*mac) * 10**(lensscale*10**lens)
        LMSout[:,n] = LMSout[:,n]/ np.max(LMSout[:,n]) #renormalise

    if loglin == 'log':
        for n in range (1,4):
            LMSout[:,n] = np.log10(LMSout[:,n])             #Log absorptances

    return LMSout


def absorptancefromlogqcornea(LMSin, mac, lens, mac_460, lens_400, loglin):
    LMSout = np.copy(LMSin) # For local calulation and return

    mac_template_460 = 0.35     #Template peak
    lens_template_400 = 1.7649   #Template peak
    macscale=mac_460/mac_template_460
    lensscale=lens_400/lens_template_400

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] + (macscale*mac) + (lensscale*lens)
        LMSout[:,n] = LMSout[:,n] - np.max(LMSout[:,n]) #renormalise

    if loglin == 'lin':
        for n in range (1,4):
            LMSout[:,n] = 10**(LMSout[:,n])             #Lin absorptances

    return LMSout


def corneafromlinabsorptance(LMSin, mac, lens, mac_460, lens_400, loglin):
    LMSout = np.copy(LMSin) # For local calcuation and return

    mac_template_460 = 0.35     #Template peak
    lens_template_400 = 1.7649   #Template peak
    macscale=mac_460/mac_template_460
    lensscale=lens_400/lens_template_400



    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] / (10**(mac*macscale) * 10**(lens*lensscale))
        LMSout[:,n] = LMSout[:,n] / np.max(LMSout[:,n]) #renormalize
        
    if loglin == 'log':
        for n in range (1,4):
            LMSout[:,n] = np.log10(LMSout[:,n])             #Log absorptances

    return LMSout


def corneafromlogabsorptance(LMSin, mac, lens, mac_460, lens_400, loglin):
    LMSout=np.copy(LMSin) # For local calculation and return

    mac_template_460 = 0.35     #Template peak
    lens_template_400 = 1.7649   #Template peak
    macscale=mac_460/mac_template_460
    lensscale=lens_400/lens_template_400

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] - (mac*macscale) - (lens*lensscale)
        LMSout[:,n] = LMSout[:,n] - np.max(LMSout[:,n])
        
    if loglin == 'lin':
        for n in range (1,4):
            LMSout[:,n] = 10**(LMSout[:,n])             #Lin absorptances

    return LMSout


def energyfromquantalin(LMSin, loglin):
    LMSout=np.copy(LMSin) # For local calculation and return

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] * LMSin[:, 0]
        LMSout[:,n] = LMSout[:,n] / np.max(LMSout[:,n]) #renormalize

    if loglin == 'log':
        for n in range (1,4):
            LMSout[:,n] = np.log10(LMSout[:,n])             #Log absorptances

    return LMSout


def energyfromquantalog(LMSin, loglin):
    LMSout=np.copy(LMSin) # For local calculation and return

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] + np.log10(LMSin[:,0])
        LMSout[:,n] = LMSout[:,n] - np.max(LMSout[:,n])
        
    if loglin == 'lin':
        for n in range (1,4):
            LMSout[:,n] = 10**(LMSout[:,n])             #Lin absorptances

    return LMSout

def quantafromenergylin(LMSin, loglin):
    LMSout=np.copy(LMSin) # For local calculation and return

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] / LMSin[:, 0]
        LMSout[:,n] = LMSout[:,n] / np.max(LMSout[:,n]) #renormalize

    if loglin == 'log':
        for n in range (1,4):
            LMSout[:,n] = np.log10(LMSout[:,n])             #Log absorptances

    return LMSout


def quantafromenergylog(LMSin, loglin):
    LMSout=np.copy(LMSin) # For local calculation and return

    for n in range (1,4):
        LMSout[:,n] = LMSin[:,n] - np.log10(LMSin[:,0])
        LMSout[:,n] = LMSout[:,n] - np.max(LMSout[:,n])
        
    if loglin == 'lin':
        for n in range (1,4):
            LMSout[:,n] = 10**(LMSout[:,n])             #Lin absorptances

    return LMSout
