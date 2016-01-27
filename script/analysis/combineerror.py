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

cal = calibration.Calibration(datafolder = basefolder)
#first fill the calibration of the adjustable resistor
cal.fillpotardata()
cal.reset()
#fill the installation information
cal.filldetectors('horn')
cal.filldetectors('helix')

phorn = np.array([])
errhorn = np.array([])
namehorn = np.array([])
phelix = np.array([])
errhelix = np.array([])
namehelix = np.array([])

for det in cal.horndet:
    cal.seterrorrotation(det,delrotation)
    errBL = utils.adctov_board(det.stdBLyear)*(+cal.boardslope)
    errtotdb = utils.quadraticerrordB(det.errorrotation,errBL)
    phorn = np.append(phorn, cal.getpoweratinstall(det,'monit'))
    errhorn = np.append(errhorn, errtotdb)
    namehorn = np.append(namehorn, det.name)
#    print det.name, ': err rotation = ' , "%.2f" % det.errorrotation, ' error baseline = ' "%.2f" % errBL, ' error tot = ',  "%.2f" % errtotdb

for det in cal.helixdet:
    cal.seterrorrotation(det,delrotation)
    errBL = utils.adctov_board(det.stdBLyear)*(cal.boardslope)
    errtotdb = utils.quadraticerrordB(det.errorrotation,errBL)
    phelix = np.append(phelix, cal.getpoweratinstall(det,'monit'))
    errhelix = np.append(errhelix, errtotdb)
    namehelix = np.append(namehelix, det.name)
#    print det.name, ': err rotation = ' , "%.2f" % det.errorrotation, ' error baseline = ' "%.2f" % errBL, ' error tot = ',  "%.2f" % errtotdb


y_horn = np.arange(len(namehorn))
y_helix = np.arange(len(namehelix))
fig = plt.figure(figsize=(6,8))
#plt.subplot(121)
plt.errorbar(phorn,y_horn,xerr=errhorn,fmt='o',lw=4, alpha=0.4,label='measured')
plt.yticks(y_horn, namehorn)
plt.xlim(-34,-26)
plt.ylim(-1,len(y_horn)+0.5)
plt.xlabel('power [dBm]',fontsize=15)
#expected value: -29.52
expvaluehorn = -30.22
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
#expected value: -43.7
expvaluehelix = -49.12
exphelix = np.linspace(expvaluehelix,expvaluehelix,10)
x = np.linspace(-20,20,10)
plt.plot(exphelix,x,lw=2,label='expected')
fig2.tight_layout()


 #.xlabel('Performance')
#plt.title('How fast do you want to go today?')

# ax2 = plt.subplot(122)
# ax2.errorbar(phelix,y_helix,xerr=errhelix,fmt='o',lw=4, alpha=0.4)
# ax2.set_yticks(y_helix, namehelix)
# #plt.xlabel('Performance')
# #plt.title('How fast do you want to go today?')
plt.legend()
plt.show()

#utils.quadraticerrordB(1,2)
