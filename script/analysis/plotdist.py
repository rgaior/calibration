#######################################################################
### return the histo of power at the installation for all detectors ###
#######################################################################
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

#usage:
if len(sys.argv) != 2:
    print 'usage : python plotdist <type of baseline wanted [install or monit]>'

typeofbaseline= sys.argv[1]
basefolder = cwd + '/../../data/'

calhorn = calibration.Calibration(datafolder = basefolder,type= 'horn')
calhelix = calibration.Calibration(datafolder = basefolder,type= 'helix')

#first fill the calibration of the adjustable resistor
calhorn.fillcalibdata()
calhelix.fillcalibdata()

#fill the installation information
calhorn.filldetectors()
calhelix.filldetectors()

## data holder:
patinstallhorn = np.array([])
patinstallhelix = np.array([])
zenithhelix = np.array([])
zenithhorn = np.array([])
azhelix = np.array([])
azhorn = np.array([])


for det in calhorn.det:
    patinstallhorn = np.append(patinstallhorn, calhorn.getpoweratinstall(det,typeofbaseline))
    zenithhorn = np.append(zenithhorn, det.zenith)
    azhorn = np.append(azhorn, det.azimuth)

for det in calhelix.det:
    patinstallhelix = np.append(patinstallhelix, calhelix.getpoweratinstall(det,typeofbaseline))
    zenithhelix = np.append(zenithhelix, det.zenith)
    azhelix = np.append(azhelix, det.azimuth)

fig1 = plt.figure(figsize = (8,8))
n, bins, patches = plt.hist(patinstallhorn, 10, facecolor='green', alpha=0.75, label='horn')
n1, bins1, patches1 = plt.hist(patinstallhelix, 10, facecolor='red', alpha=0.75, label='helix')
plt.xlabel('power at installation [dBm]', fontsize =15)
plt.ylabel('entries',fontsize = 15)
plt.legend(fontsize=15)

plt.show()

## write down the values (for the notebook)
print ' helix detectors (in dBm):'
for det in calhelix.det:
    print det.name , ' ' , "%.2f" % calhelix.getpoweratinstall(det,typeofbaseline) , ' +/- ' ,  "%.2f" %  (utils.adctov_board(det.stdBLyear)*(cal.boardslope))

print '\n horn detectors (in dBm):'
for det in calhorn.det:
    print det.name , ' ' , "%.2f" % calhorn.getpoweratinstall(det,typeofbaseline) , ' +/- ' ,  "%.2f" %  (utils.adctov_board(det.stdBLyear)*(cal.boardslope))


