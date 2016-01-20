import numpy as np
from datetime import date

###############################################
####  reading functions                   #####
###############################################


def readpotardata(filename):
    f = open(filename, 'r+')
    x = np.array([])
    y = np.array([])
    for l in f:
        x = np.append(x, float(l.split()[0]))
        y = np.append(y, float(l.split()[1]))
    return [x,y]


def readmonit(filename):
    f = open(filename,'r+')
    x = np.array([])
    y = np.array([])
    for l in f:
        stamp = float(l.split()[0])
        thedate = date.fromtimestamp(stamp)
        x = np.append(x, thedate)
        y = np.append(y, float(l.split()[1]))
#        print thedate, 'float(l.split()[1]) = ',float(l.split()[1])
    return [x,y]




###############################################
#### conversion function (voltage to adc, #####
#### voltage FE to voltage board etc... ) #####
###############################################

#adc counts to volt at the FE input (between 0-1V)
def adctov_fe(adc):
    return float(adc)/1024
def v_fetoadc(vfe):
    return float(vfe)*1024

#voltage at front end to voltage at GIGAS/EASIER board
def v_fetov_board(vfe):
    return vfe*(-2)
def v_boardtov_fe(vboard):
    return vboard*(-1/2)

#adc to v board (between -2 and 0 V)
def adctov_board(adc):
    return v_fetov_board(adctov_fe(adc))
def v_boardtoadc(vboard):
    return v_fetoadc(v_boardtov_fe(vboard))

 
#combine error in dB
def quadraticerrordB(err1, err2):
    #errlin1 = np.power(10,0.1) - 1
    errlin1 = np.power(10,float(err1)/10) - 1
    errlin2 = np.power(10,float(err2)/10)  - 1
    errtot = np.sqrt(errlin1*errlin1 + errlin2*errlin2)
#    print 'error lin 1' , errlin1 ,' errlin2 = ', errlin2, 'errtot = ',errtot
    errtotdb = 10*np.log10(errtot +1)
    return errtotdb
