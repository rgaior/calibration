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

calhorn = calibration.Calibration(datafolder = basefolder,type='horn')
calhelix = calibration.Calibration(datafolder = basefolder,type='helix')
#first fill the calibration of the adjustable resistor
calhorn.fillcalibdata()
calhelix.fillcalibdata()


## second method with a fit instead of differentiating the data
## done that way because data didn't give something very regular
fithorn = np.polyfit(calhorn.resistor[0],calhorn.resistor[1],2)
fithelix = np.polyfit(calhelix.resistor[0],calhelix.resistor[1],2)

## error:
errorfunctionhorn = np.poly1d([2*fithorn[0], fithorn[1]])
errorfunctionhelix = np.poly1d([2*fithelix[0], fithelix[1]])

#fill the installation information
calhorn.filldetectors()
calhelix.filldetectors()

## data holder:
errhorn = np.array([])
errhelix = np.array([])
namehelix = np.array([])
namehorn = np.array([])



for det in calhorn.det:
    errorperrot = errorfunctionhorn(det.refrotation + det.rotation)
    error = errorperrot*delrotation
    print 'station: ', det.name, 'error = ', str('%.2f' % error)
print '\n'
for det in calhelix.det:
    errorperrot = errorfunctionhelix(det.refrotation + det.rotation)
    error = errorperrot*delrotation
    print 'station: ', det.name, 'error = ', str('%.2f' % error)


