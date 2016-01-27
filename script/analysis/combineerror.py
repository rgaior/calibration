###############################################################################################
### return the error from the uncertainty on the rotation of the resistor for all detectors ###
###############################################################################################
import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import matplotlib
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
import numpy as np
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import detector
import calibration
basefolder = cwd + '/../../data/'
 
delrotation = float(sys.argv[1])

calhorn = calibration.Calibration(datafolder = basefolder, type = 'horn')
calhelix = calibration.Calibration(datafolder = basefolder, type = 'helix')

#fill the calibration information
calhorn.fillcalibdata()
calhelix.fillcalibdata()

#fill the installation information
calhorn.filldetectors()
calhelix.filldetectors()

phorn = np.array([])
errhorn = np.array([])
namehorn = np.array([])
phelix = np.array([])
errhelix = np.array([])
namehelix = np.array([])

for det in calhorn.det:
    cal = calhorn
    cal.seterrorrotation(det,delrotation)
    errBL = utils.adctov_board(det.stdBLyear)*(+cal.boardslope)
    errtotdb = utils.quadraticerrordB(det.errorrotation,errBL)
    phorn = np.append(phorn, cal.getpoweratinstall(det,'monit'))
    errhorn = np.append(errhorn, errtotdb)
    namehorn = np.append(namehorn, det.name)
#    print det.name, ': err rotation = ' , "%.2f" % det.errorrotation, ' error baseline = ' "%.2f" % errBL, ' error tot = ',  "%.2f" % errtotdb

for det in calhelix.det:
    cal = calhelix
    cal.seterrorrotation(det,delrotation)
    errBL = utils.adctov_board(det.stdBLyear)*(cal.boardslope)
    errtotdb = utils.quadraticerrordB(det.errorrotation,errBL)
    phelix = np.append(phelix, cal.getpoweratinstall(det,'monit'))
    errhelix = np.append(errhelix, errtotdb)
    namehelix = np.append(namehelix, det.name)
#    print det.name, ': err rotation = ' , "%.2f" % det.errorrotation, ' error baseline = ' "%.2f" % errBL, ' error tot = ',  "%.2f" % errtotdb

expvaluehorn = calhorn.getexpectedvalue(10,15) #dB
expvaluehelix = calhelix.getexpectedvalue(10,50) #dB
expvaluehorn = expvaluehorn +30 # dBm
expvaluehelix = expvaluehelix +30 #dBm


## plotting
y_horn = np.arange(len(namehorn))
y_helix = np.arange(len(namehelix))
fig = plt.figure(figsize=(6,8))
#plt.subplot(121)
plt.errorbar(phorn,y_horn,xerr=errhorn,fmt='o',lw=4, alpha=0.4,label='measured')
plt.yticks(y_horn, namehorn)
plt.xlim(-34,-26)
plt.ylim(-1,len(y_horn)+0.5)
plt.xlabel('power [dBm]',fontsize=15)
exphorn = np.linspace(expvaluehorn,expvaluehorn,10)
x = np.linspace(-20,20,10)
plt.plot(exphorn,x,lw=2,label='expected')
fig.tight_layout()
plt.legend()

fig2 = plt.figure(figsize=(6,8))
#plt.subplot(121)
plt.errorbar(phelix,y_helix,xerr=errhelix,fmt='o',lw=4, alpha=0.4,label='measured')
plt.ylim(-1,len(y_helix)+0.5)
plt.yticks(y_helix, namehelix)
plt.xlabel('power [dBm]',fontsize=15)
exphelix = np.linspace(expvaluehelix,expvaluehelix,10)
x = np.linspace(-20,20,10)
plt.plot(exphelix,x,lw=2,label='expected')
fig2.tight_layout()


plt.legend()
plt.show()

#utils.quadraticerrordB(1,2)
