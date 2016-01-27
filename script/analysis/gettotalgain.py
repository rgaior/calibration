import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import matplotlib
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
import numpy as np
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
classpath = cwd + '/../classes/'
sys.path.append(classpath)
import utils
import detector
import calibration
basedatafolder = '../../data/'

calhelix = calibration.Calibration(datafolder = basedatafolder, type = 'helix')
calhorn = calibration.Calibration(datafolder = basedatafolder, type = 'horn')
#fill the calibration information                                                                                                
calhelix.fillcalibdata()
calhorn.fillcalibdata()
totgainhelix = calhelix.gettotalgain()
totgainhorn = calhorn.gettotalgain()

plt.plot(totgainhelix[0],totgainhelix[1],lw=2,label='helix')
plt.plot(totgainhorn[0],totgainhorn[1],lw=2,label='horn')
plt.xlabel('frequency [MHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
plt.xlim(500,2000)
plt.ylim(-40,60)
plt.show()
