#######################################################################
### return the power vs azimuth just to check if any correlation    ###
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
basefolder = cwd + '/../../data/'

cal = calibration.Calibration(datafolder = basefolder)
#first fill the calibration of the adjustable resistor
cal.fillpotardata()

cal.reset()
#fill the installation information
cal.filldetectors('horn')
cal.filldetectors('helix')

## data holder:
patinstallhorn = np.array([])
patinstallhelix = np.array([])
zenithhelix = np.array([])
zenithhorn = np.array([])
azhelix = np.array([])
azhorn = np.array([])

for det in cal.horndet:
    patinstallhorn = np.append(patinstallhorn, cal.getpoweratinstall(det))
    zenithhorn = np.append(zenithhorn, det.zenith)
    azhorn = np.append(azhorn, det.azimuth)
for det in cal.helixdet:
    patinstallhelix = np.append(patinstallhelix, cal.getpoweratinstall(det))
    zenithhelix = np.append(zenithhelix, det.zenith)
    azhelix = np.append(azhelix, det.azimuth)

fig1 = plt.figure(figsize = (8,8))
plt.plot(azhelix,patinstallhelix, 'o',label='helix')
plt.plot(azhorn,patinstallhorn,'o',label= 'horn')
plt.xlabel('antenna azimuth [degree]',fontsize=15)
plt.ylabel('power at installation [dBm]',fontsize=15)
plt.legend(fontsize=15)
plt.show()


