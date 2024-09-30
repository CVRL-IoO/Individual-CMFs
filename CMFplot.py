# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:26 2016

"""


import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")

import numpy as np

class CMFPlot( object ):

    def __init__(self, rows = 3, cols = 3, nmstepsize=1):
        
        self.__rows = rows
        self.__cols = cols
        self.__nmstepsize = nmstepsize
        self.__fig = matplotlib.pyplot.figure(facecolor= (1.0, 1.0, 0.8))
        self.__fig.subplots_adjust(hspace=0.4,wspace=0.4)
     
    def LMSview( self, nm, L, M, S, loy, hiy, title, posn): #Plot LMS values
         
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Add single plot
        ax.plot(nm, L, color='red', linestyle='solid', marker='',
           markersize=7, label ='L') #Plot response analysis
    
        ax.plot(nm, M, color='green', linestyle='solid', marker='',
           markersize=7, label ='M') #Plot response analysis
    
        ax.plot(nm, S, color='blue', linestyle='solid', marker='',
           markersize=7, label ='S') #Plot response analysis
    
        ax.legend(loc=1, fontsize = 9, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Sensitivity', size=9)
        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        

        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')
        
    
    def LMScompare( self, nm, L, M, S, L2, M2, S2, loy, hiy, title, posn): #Plot 2xLMS values
         
        ax = self.__fig.add_subplot(self.__rows, self.__cols, posn)  #Add single plot
      
        ax.plot(nm, L, color='red', linestyle='solid', marker='',
           markersize=7, label ='L') #Plot response analysis
    
        ax.plot(nm, M, color='green', linestyle='solid', marker='',
           markersize=7, label ='M') #Plot response analysis
    
        ax.plot(nm, S, color='blue', linestyle='solid', marker='',
           markersize=7, label ='S') #Plot response analysis
    
        ax.plot(nm, L2, color='red', linestyle='dashed', marker='',
           markersize=7, label ='LN') #Plot response analysis
    
        ax.plot(nm, M2, color='green', linestyle='dashed', marker='',
           markersize=7, label ='MN') #Plot response analysis
    
        ax.plot(nm, S2, color='blue', linestyle='dashed', marker='',
           markersize=7, label ='SN') #Plot response analysis
    
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
      
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Sensitivity', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')

 
    def macularcompare(self, nm, mac, mac2, loy, hiy, title, posn): #Plot 2xLMS values
         
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Add single plot
      
        ax.plot(nm, mac, color='black', linestyle='solid', marker='',
           markersize=7, label ='mac1') #Plot lens1
    
        ax.plot(nm, mac2, color='black', linestyle='dashed', marker='',
           markersize=7, label ='mac2') #Plot lens2
    
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
      
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Optical density', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')

       
    def lenscompare(self, nm, lens, lens2, loy, hiy, title, posn): #Plot 2xLMS values
         
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Add single plot
      
        ax.plot(nm, lens, color='black', linestyle='solid', marker='',
           markersize=7, label ='lens1') #Plot lens1
    
        ax.plot(nm, lens2, color='black', linestyle='dashed', marker='',
           markersize=7, label ='lens2') #Plot lens2
    
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
      
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Optical density', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')

    
    def LMScompareqe(self, nm, L, M, S, L2, M2, S2, loy, hiy, title, posn): #Plot 2xLMS quantal vs energy values
         
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Select subplot
        
        ax.plot(nm, L, color='red', linestyle='solid', marker='',
           markersize=7, label ='Lq') #Plot response analysis
    
        ax.plot(nm, M, color='green', linestyle='solid', marker='',
           markersize=7, label ='Mq') #Plot response analysis
    
        ax.plot(nm, S, color='blue', linestyle='solid', marker='',
           markersize=7, label ='Sq') #Plot response analysis
    
        ax.plot(nm, L2, color='red', linestyle='dashed', marker='',
           markersize=7, label ='Le') #Plot response analysis
    
        ax.plot(nm, M2, color='green', linestyle='dashed', marker='',
           markersize=7, label ='Me') #Plot response analysis
    
        ax.plot(nm, S2, color='blue', linestyle='dashed', marker='',
           markersize=7, label ='Se') #Plot response analysis
    
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)

        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
        
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Sensitivity', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')
    
    
    def LMchromaticity(self, LMSin, title, posn): #Plot LM chromaticities
      
        LMSplot=np.copy(LMSin)
        
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn )  #Select subplot
        
        ax.plot(LMSplot[:,1]/(LMSplot[:,1]+LMSplot[:,2]+LMSplot[:,3]), LMSplot[:,2]/(LMSplot[:,1]+LMSplot[:,2]+LMSplot[:,3]),
            color='black', linestyle='solid', marker='', markersize=7, label ='spectrum locus') #Spectrum locus
        
        index20step = int(20/self.__nmstepsize)          #20nm step size         

        LMSplotcoarse=LMSplot[0:len(LMSplot[:,1]):index20step,:]
        ax.plot(LMSplotcoarse[:,1]/(LMSplotcoarse[:,1]+LMSplotcoarse[:,2]+LMSplotcoarse[:,3]),
            LMSplotcoarse[:,2]/(LMSplotcoarse[:,1]+LMSplotcoarse[:,2]+LMSplotcoarse[:,3]), color='red',
            linestyle='', marker='o', markersize=5, label = "20-nm steps") #Spectrum locus

        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1, numpoints = 1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(0,1)

        loy, hiy = ax.get_ylim()

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
        
        ax.set_xlabel('l/(l+m+s)', size=9)
        ax.set_ylabel('m/(l+m+s)', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')

    def LoverMcompare(self, nm, L, M, L2, M2, loy, hiy, title, posn): #Plot 2xL/M differences
         
        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Select subplot
        
        ax.plot(nm, L-M, color='black', linestyle='solid', marker='',
           markersize=7, label ='L-M') #Plot L/M
    
        ax.plot(nm, L2-M2, color='black', linestyle='dashed', marker='',
           markersize=7, label =' LN-MN') #L2/M2
    
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)

        ax.set_xlim(375,725)
        ax.set_ylim(loy,hiy)   

        ax.xaxis.set_tick_params(labelsize=8)        
        ax.yaxis.set_tick_params(labelsize=8)        
        
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Sensitivity', size=9)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')
        
    
    def RGBCMFsPlot(self, RGBCMFs, title, posn):

        ax = self.__fig.add_subplot( self.__rows, self.__cols, posn)  #Select subplot

        ax.plot(RGBCMFs[:,0], RGBCMFs[:,1], color='red', linestyle='solid', marker='',
            markersize=7, label ='R') #Plot response analysis
        
        ax.plot(RGBCMFs[:,0], RGBCMFs[:,2], color='green', linestyle='solid', marker='',
            markersize=7, label ='G') #Plot response analysis
        
        ax.plot(RGBCMFs[:,0], RGBCMFs[:,3], color='blue', linestyle='solid', marker='',
            markersize=7, label ='B') #Plot response analysis
        
        ax.legend(loc=1, fontsize = 8, labelspacing = 0.1)   #Location upper right (defaults to 1 anyhow)
        ax.set_xlim(375,725)
        ax.set_xlabel('Wavelength (nm)', size=9)
        ax.set_ylabel('Tristimulus value', size=9)
        ax.xaxis.set_tick_params(labelsize=8)
        matplotlib.pyplot.title(title, loc='left', size=9, style ='italic')
        


       
    def displayAll(self, xleft, ytop, width, height, holdornot):
        figManager = matplotlib.pyplot.get_current_fig_manager()

        figManager.window.setGeometry(xleft, ytop, width, height)      
      
        matplotlib.pyplot.show(block = holdornot)
        