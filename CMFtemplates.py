# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:26 2016. Revised substantially January 2020

@author: Andrew Stockman

Template functions for normal and hybrid cone fundamentals and macular and lens
"""

import numpy as np

#NB nm = np.arange(360.0, 850+nm_step, nm_step) in main program sets nm values at equal steps from 360 to 850


def LMSconelogcommon(nm, LMS, shift):   #Best-fitting log-lin 8x2 Fourier Series Polynomial that fits the
# Stockman & Sharpe log L M and S absorbances extended to 360 nm and 850 nm.
                                                    
    Lsercommonlmax = 557.5
    Lalacommonlmax = 554.8
    Mcommonlmax = 527.3
    Scommonlmax = 418.5

# Log shifts in lmax from Lser with log 390 to log 850 scaled 0 to pi
    Soffset = -1.048690123          #relative to Lser 0 to pi
    Moffset = -0.2036522967         #relative to Lser 0 to pi
    Lalaoffset = -0.01775262143     #relative to Lser 0 to pi	
    Lseroffset= 0  	


    x=(np.log10(nm)-2.556302500767287267)/0.1187666467581842301 #Rescales log 360 - log 850 to 0 to pi

    if LMS == 'Lser':
        x = x + Lseroffset + np.log10(Lsercommonlmax/(Lsercommonlmax+shift))/0.1187666467581842301   #Scaled as above from nm to lognm
    elif LMS == 'Lala':
        x = x + Lalaoffset + np.log10(Lalacommonlmax/(Lalacommonlmax+shift))/0.1187666467581842301   
    elif LMS =='M':
        x = x + Moffset + np.log10(Mcommonlmax/(Mcommonlmax+shift))/0.1187666467581842301 
    elif LMS == 'S':
        x = x + Soffset + np.log10(Scommonlmax/(Scommonlmax+shift))/0.1187666467581842301 
    else:
        print ("Cone type not specified")
        
    c = list(range(18))
    
     
    c[0] =	-2.1256563197            #Normalised to unity peak
    c[1] =	5.4677929400
    c[2] =	0.8960658918
    c[3] =	-0.9530108239
    c[4] =	-5.0377095815
    c[5] =	-3.0039987529
    c[6] =	-0.9508620342
    c[7] =	-1.3670849620
    c[8] =	1.7702113766
    c[9] =	0.5165048525
    c[10] =	1.1505501831
    c[11] =	0.6100416117
    c[12] =	0.0518211044
    c[13] =	0.1009282570
    c[14] =	-0.1773573074
    c[15] =	-0.0278798136
    c[16] =	-0.0427736834
    c[17] = 0.0007050030               #Normalisation factor
   
    y = c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*np.cos(2*x) + c[4]*np.sin(2*x)\
        + c[5]*np.cos(3*x) + c[6]*np.sin(3*x) + c[7]*np.cos(4*x) + c[8]*np.sin(4*x)\
        + c[9]*np.cos(5*x) + c[10]*np.sin(5*x) + c[11]*np.cos(6*x) + c[12]*np.sin(6*x)\
        + c[13]*np.cos(7*x) + c[14]*np.sin(7*x) +  + c[15]*np.cos(8*x) + c[16]*np.sin(8*x) + c[17]

    return y
   

def Lmeanlogcommon(nm):   # L log mean template averaged from 0.56*Lser and 0.44*Lala common templates normalised to 0
                                                    #Fourier Series Polynomial to Stockman & Sharpe log LMS absorbances.
   
    x=(np.log10(nm)-2.556302500767287267)/0.1187666467581842301 #Rescales log 360 - log 850 to 0 to pi
    
#    Lmeanlmax_template=551.9  #lmax with no shift (not used)
   
    c = list(range(18))
    
    c[0] = -42.9263580477
    c[1] = -2.0396798842
    c[2] = 75.9717833722
    c[3] = 57.3308210897
    c[4] = 6.5733913482
    c[5] = 8.1111028646
    c[6] = -38.7656494836
    c[7] = -21.4483453428
    c[8] = -5.9397465531
    c[9] = -3.3896198598
    c[10] = 9.5882997573
    c[11] = 3.2507563437
    c[12] = 1.4412770784
    c[13] = 0.3966003448
    c[14] = -0.7113921460
    c[15] = -0.0793542168
    c[16] = -0.0729797618
    c[17] = -0.0016552130       #normalized to peak at 0 at lmax

    y = c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*np.cos(2*x) + c[4]*np.sin(2*x)\
        + c[5]*np.cos(3*x) + c[6]*np.sin(3*x) + c[7]*np.cos(4*x) + c[8]*np.sin(4*x)\
        + c[9]*np.cos(5*x) + c[10]*np.sin(5*x) + c[11]*np.cos(6*x) + c[12]*np.sin(6*x)\
        + c[13]*np.cos(7*x) + c[14]*np.sin(7*x) +  + c[15]*np.cos(8*x) + c[16]*np.sin(8*x) + c[17]

    return y



def Lserconelog(nm, Lshift):   #Lser180 log-lin 8x2 Fourier Series Polynomial best-fitting template such that 
#0.56 Lser180 + 0.44 Lala180 with a 2.7 nm shift best fits the Stockman & Sharpe log L absorbance extropolated
#using Lamb template at long-wavelength and extended to 360 nm.

    x=(np.log10(nm)-2.556302500767287267)/0.1187666467581842301 #Rescales log 360 - log 850 to 0 to pi
    
    Lserlmax_template=553.1  #lmax with no shift
    xshift = np.log10(Lserlmax_template/(Lserlmax_template+Lshift))/ 0.1187666467581842301
    x=x + xshift
   
    c = list(range(18))
    
    c[0] = -42.417608560
    c[1] = -2.656791612
    c[2] = 75.011093607
    c[3] = 56.477062776
    c[4] = 7.509397607
    c[5] = 9.061442173
    c[6] = -38.068488495
    c[7] = -20.974610259
    c[8] = -6.642746250
    c[9] = -3.785039126
    c[10] = 9.322071459
    c[11] = 3.134494745
    c[12] = 1.603799055
    c[13] = 0.439302358
    c[14] = -0.676958684
    c[15] = -0.072988371
    c[16] = -0.078857510
    c[17] = -0.004264105  #normalized to peak at 0 at lmax


    y = c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*np.cos(2*x) + c[4]*np.sin(2*x)\
        + c[5]*np.cos(3*x) + c[6]*np.sin(3*x) + c[7]*np.cos(4*x) + c[8]*np.sin(4*x)\
        + c[9]*np.cos(5*x) + c[10]*np.sin(5*x) + c[11]*np.cos(6*x) + c[12]*np.sin(6*x)\
        + c[13]*np.cos(7*x) + c[14]*np.sin(7*x) +  + c[15]*np.cos(8*x) + c[16]*np.sin(8*x) + c[17]

    return y
    
    
def Lalaconelog(nm):   #Lser individual template shifted -2.70 nm to alanine position.
    
    y = Lserconelog(nm, -2.70) 
    return y
    
    

def Lmeanconelog(nm):   #L log mean template averaged from 0.56*Lser and 0.44*Lala individual templates normalised to 0
                                #Normalised to 1.

    y = np.log10(1.0009350552348480 * (0.56*10**(Lserconelog(nm,0)) + 0.44*10**(Lalaconelog(nm))))
    return y



def Mconelog(nm, Mshift):  #M template best-fitting log-lin 8x2 Fourier Series Polynomial to Stockman & Sharpe log M absorbance
#extropolated using Lamb template at long-wavelengths and by the L function at shorter wavelengths to 360 nm.

    x=(np.log10(nm)-2.556302500767287267)/0.1187666467581842301 #Rescales log 360 - log 850 to 0 to pi

    Mlmax_template=529.9  #Known lmax with no shift
    xshift = np.log10(Mlmax_template/(Mlmax_template+Mshift))/0.1187666467581842301
    x=x + xshift
    
    c = list(range(18))

    c[0] = -210.6568853069       #Normalised to peak at 0
    c[1] = -0.1458073553
    c[2] = 386.7319763250
    c[3] = 305.4710584670
    c[4] = 5.0218382813
    c[5] = 6.8386224350
    c[6] = -208.2062335724
    c[7] = -118.4890200521
    c[8] = -5.7625866330
    c[9] = -3.7973553168
    c[10] = 55.1803460639
    c[11] = 19.9728512548
    c[12] = 1.8990456325
    c[13] = 0.6913410864
    c[14] = -5.0891806213
    c[15] = -0.7070689492
    c[16] = -0.1419926703
    c[17] = 0.0005894876
    

    y = c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*np.cos(2*x) + c[4]*np.sin(2*x)\
        + c[5]*np.cos(3*x) + c[6]*np.sin(3*x) + c[7]*np.cos(4*x) + c[8]*np.sin(4*x)\
        + c[9]*np.cos(5*x) + c[10]*np.sin(5*x) + c[11]*np.cos(6*x) + c[12]*np.sin(6*x)\
        + c[13]*np.cos(7*x) + c[14]*np.sin(7*x) +  + c[15]*np.cos(8*x) + c[16]*np.sin(8*x) + c[17]


    return y


def Sconelog(nm, Sshift):   #New S template best-fitting log-lin 8x2 Fourier Series Polynomial to Stockman & Sharpe
# log S absorbance extropolated using Lamb template to 850 nm and extended to 360 nm.
 
    x=(np.log10(nm)-2.556302500767287267)/0.1187666467581842301 #Rescales log 360 - log 850 to 0 to pi

    Slmax_template=416.9  #lmax with no shift
    xshift = np.log10(Slmax_template/(Slmax_template+Sshift))/0.1187666467581842301
    x=x + xshift

    c = list(range(18))

    c[0] = 207.3880950935       #Normalised to peak at 0
    c[1] = -6.3065623516
    c[2] = -393.7100478026
    c[3] = -315.6650602846
    c[4] = 19.2917535553
    c[5] = 19.6414743488
    c[6] = 214.2211570447
    c[7] = 121.8584683485
    c[8] = -15.1820737886
    c[9] = -8.6774057156
    c[10] = -56.7596380441
    c[11] = -20.6318720369
    c[12] = 3.6934875040
    c[13] = 1.0483022480
    c[14] = 5.3656615075
    c[15] = 0.7898783086
    c[16] = -0.1480357836
    c[17] = 0.0002358232

    y = c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*np.cos(2*x) + c[4]*np.sin(2*x)\
        + c[5]*np.cos(3*x) + c[6]*np.sin(3*x) + c[7]*np.cos(4*x) + c[8]*np.sin(4*x)\
        + c[9]*np.cos(5*x) + c[10]*np.sin(5*x) + c[11]*np.cos(6*x) + c[12]*np.sin(6*x)\
        + c[13]*np.cos(7*x) + c[14]*np.sin(7*x) +  + c[15]*np.cos(8*x) + c[16]*np.sin(8*x) + c[17]


    return y


def LMSconelog(nm, LMS_array_size, Lshift, Mshift, Sshift, loglin):   #Calculate LMS abs from individual Fourier 5 x 2 templates.
    LMSabsout = np.zeros(LMS_array_size) # For return
    
    LMSabsout[:,0] = nm # Wavelength in column 0
    LMSabsout[:,1] = Lserconelog(nm, Lshift)  #Log absorbances
    LMSabsout[:,2] = Mconelog(nm, Mshift)
    LMSabsout[:,3] = Sconelog(nm, Sshift)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsout[:,n] = 10**(LMSabsout[:,n])             #Lin absorbances
    
    return LMSabsout


def LLSconelog(nm, LMS_array_size, Lshift, Mshift, Sshift, loglin):   #Calculate LMS abs from Fourier 5 x 2 templates TWO L-cones!
    LMSabsout = np.zeros(LMS_array_size) # For return
    
    LMSabsout[:,0] = nm # Wavelength in column 0
    LMSabsout[:,1] = Lserconelog(nm, Lshift)  #Log absorbances
    LMSabsout[:,2] = Lserconelog(nm, Mshift)
    LMSabsout[:,3] = Sconelog(nm, Sshift)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsout[:,n] = 10**(LMSabsout[:,n])             #Lin absorbances
    
    return LMSabsout


def MMSconelog(nm, LMS_array_size, Lshift, Mshift, Sshift, loglin):   #Calculate LMS abs from Fourier 5 x 2 templates TWO M-cones!
    LMSabsout = np.zeros(LMS_array_size) # For return
    
    LMSabsout[:,0] = nm # Wavelength in column 0
    LMSabsout[:,1] = Mconelog(nm, Lshift)  #Log absorbances
    LMSabsout[:,2] = Mconelog(nm, Mshift)
    LMSabsout[:,3] = Sconelog(nm, Sshift)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsout[:,n] = 10**(LMSabsout[:,n])             #Lin absorbances
    
    return LMSabsout


def MLSconelog(nm, LMS_array_size, Lshift, Mshift, Sshift, loglin):   #Calculate LMS abs from Fourier 5 x 2 templates M and L switched around.
    LMSabsout = np.zeros(LMS_array_size) # For return
    
    LMSabsout[:,0] = nm # Wavelength in column 0
    LMSabsout[:,1] = Mconelog(nm, Lshift)  #Log absorbances
    LMSabsout[:,2] = Lserconelog(nm, Mshift)
    LMSabsout[:,3] = Sconelog(nm, Sshift)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsout[:,n] = 10**(LMSabsout[:,n])             #Lin absorbances
    
    return LMSabsout


def LMSconelognormal(nm, LMS_array_size, loglin):   #Calculate LMS abs from Fourier 5 x 2 templates. Default L is Lmean
    LMSabsoutcom = np.zeros(LMS_array_size) # For return

    LMSabsoutcom[:,0] = nm # Wavelength in column 0
    LMSabsoutcom[:,1] = Lmeanconelog(nm)
    LMSabsoutcom[:,2] = Mconelog(nm, 0)
    LMSabsoutcom[:,3] = Sconelog(nm, 0)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsoutcom[:,n] = 10**(LMSabsoutcom[:,n])             #Lin absorbances
    
    return LMSabsoutcom


def LMSconelogcommonall(nm, LMS_array_size, Lshift, Mshift, Sshift, loglin):   #Calculate LMS abs from Fourier 5 x 2 templates. Default L is Lser
    LMSabsoutcom = np.zeros(LMS_array_size) # For return

    LMSabsoutcom[:,0] = nm # Wavelength in column 0
    LMSabsoutcom[:,1]=LMSconelogcommon(nm,'Lser', Lshift)
    LMSabsoutcom[:,2]=LMSconelogcommon(nm, 'M', Mshift)
    LMSabsoutcom[:,3]=LMSconelogcommon(nm, 'S', Sshift)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsoutcom[:,n] = 10**(LMSabsoutcom[:,n])             #Lin absorbances
    
    return LMSabsoutcom


def LMSconelogcommonnormalall(nm, LMS_array_size, loglin):   #Calculate LMS abs from Fourier 7 x 2 templates. Default L is Lmean
    LMSabsoutcom = np.zeros(LMS_array_size) # For return

    LMSabsoutcom[:,0] = nm # Wavelength in column 0
    LMSabsoutcom[:,1]=Lmeanlogcommon(nm)                    #Mixed Lmean
    LMSabsoutcom[:,2]=LMSconelogcommon(nm, 'M', 0)
    LMSabsoutcom[:,3]=LMSconelogcommon(nm, 'S', 0)
    
    if loglin == 'lin':
        for n in range (1,4):
            LMSabsoutcom[:,n] = 10**(LMSabsoutcom[:,n])             #Lin absorbances
    
    return LMSabsoutcom


def macular(nm):   #Macular best-fitting 11x2 Fourier Series Polynomial to Stockman_Sharpe/CIE macular.
    
    x=(nm-375)/55.70423008 #Rescales 375 to 550 nm 0 to pi. Extrapolated < 390 nm using best guess. For < 375 assumed to be 0.
    
    #Set template to 0 > 550.0 nm
    y=np.copy(x) # For output
    
    c = list(range(24))
  
    c[0] = 3712.2037792986
    c[1] = 374.1811575175
    c[2] = -7007.6989637831
    c[3] = -5887.2857515364
    c[4] = -633.0475233043
    c[5] = -716.0429039473
    c[6] = 4386.8811254914
    c[7] = 2882.1092658881
    c[8] = 638.1347550701
    c[9] = 468.4980700497
    c[10] = -1653.7567388120
    c[11] = -817.1240899995
    c[12] = -286.4038978705
    c[13] = -144.7996457395
    c[14] = 340.3364828167
    c[15] = 115.5652804221
    c[16] = 59.1650826447
    c[17] = 18.6678197694
    c[18] = -30.2344535413
    c[19] = -5.4683753172
    c[20] = -4.1335064207
    c[21] = -0.5043959566
    c[22] = 0.5094171266
    c[23] = 1.0050048550        #Normalisation to peak at 0.35 at 460 nm
 
    
    for n in range (0, len(x)): #Calculate and add zeros > 550 nm and < 375 nm

        if x[n]>= 0 and x[n] <=((550-375)/55.70423008):    
        
            y[n] = (c[0] + c[1]*np.cos(x[n]) + c[2]*np.sin(x[n]) + c[3]*np.cos(2*x[n]) + c[4]*np.sin(2*x[n]) + \
                c[5]*np.cos(3*x[n]) + c[6]*np.sin(3*x[n]) + c[7]*np.cos(4*x[n]) + c[8]*np.sin(4*x[n]) + \
                c[9]*np.cos(5*x[n]) + c[10]*np.sin(5*x[n]) + c[11]*np.cos(6*x[n]) + c[12]*np.sin(6*x[n]) + \
                c[13]*np.cos(7*x[n]) + c[14]*np.sin(7*x[n]) + c[15]*np.cos(8*x[n]) + c[16]*np.sin(8*x[n]) + \
                c[17]*np.cos(9*x[n]) + c[18]*np.sin(9*x[n]) + c[19]*np.cos(10*x[n]) + c[20]*np.sin(10*x[n]) + \
                c[21]*np.cos(11*x[n]) + c[22]*np.sin(11*x[n]))* c[23]

            
        if x[n] > ((550-375)/55.70423008) or x[n] < 0:    #Template 0 in this wavelength range
            y[n]=0

    return y


def lens(nm):   #Lens best-fitting 9x2 Fourier Series Polynomial to Stockman_Sharpe/CIE lens extended to 360 nm.

    x=(nm-360.0)/95.49296586  #Rescales 360 to 660 nm to 0 to pi

    y=np.copy(x) # For output

    c = list(range(21))

    c[0] = -313.9508632762
    c[1] = -70.3216819666
    c[2] = 585.4719725809
    c[3] = 471.5395862431
    c[4] = 117.3539102044
    c[5] = 127.0168222865
    c[6] = -324.4700544731
    c[7] = -188.1638078982
    c[8] = -104.5512488013
    c[9] = -68.3078486904
    c[10] = 89.7815373733
    c[11] = 33.4498264952
    c[12] = 35.2723638870
    c[13] = 13.6524086627
    c[14] = -8.7568168893
    c[15] = -1.2825766708
    c[16] = -3.5126531075
    c[17] = -0.4477840959
    c[18] = 0.0428291365
    c[19] = 1.0091871745       #Normalisation to 1.7649 at 400 nm
   

    for n in range (0, len(x)): #Add zeros > 660 nm

        if x[n] <= ((660-360)/95.49296586):    
            y[n] = (c[0] + c[1]*np.cos(x[n]) + c[2]*np.sin(x[n]) + c[3]*np.cos(2*x[n]) + c[4]*np.sin(2*x[n]) + \
                c[5]*np.cos(3*x[n]) + c[6]*np.sin(3*x[n]) + c[7]*np.cos(4*x[n]) + c[8]*np.sin(4*x[n]) + \
                c[9]*np.cos(5*x[n]) + c[10]*np.sin(5*x[n]) + c[11]*np.cos(6*x[n]) + c[12]*np.sin(6*x[n]) + \
                c[13]*np.cos(7*x[n]) + c[14]*np.sin(7*x[n]) + c[15]*np.cos(8*x[n]) + c[16]*np.sin(8*x[n]) + \
                c[17]*np.cos(9*x[n]) + c[18]*np.sin(9*x[n])) * c[19]
           
      
        if x[n] > ((660-360)/95.49296586): 
            
            y[n]=0

    return y
