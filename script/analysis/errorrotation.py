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

# to compute the error on the power, we need to know the derivative of the calibration
# dx = 0.5 # step of the rotation calibration curve
# d_fhelix = np.diff(cal.resistorhelix[1])/dx
# xhelix = cal.resistorhelix[0][:-1]+1/2

# d_fhorn = np.diff(cal.resistorhorn[1])/dx
# xhorn = cal.resistorhorn[0][:-1]+1/2

## second method with a fit instead of differentiating the data
## done that way because data didn't give something very regular
fithorn = np.polyfit(cal.resistorhorn[0],cal.resistorhorn[1],2)
fithelix = np.polyfit(cal.resistorhelix[0],cal.resistorhelix[1],2)

## error:
errorfunctionhorn = np.poly1d([2*fithorn[0], fithorn[1]])
errorfunctionhelix = np.poly1d([2*fithelix[0], fithelix[1]])

cal.reset()
#fill the installation information
cal.filldetectors('horn')
cal.filldetectors('helix')

## data holder:
errhorn = np.array([])
errhelix = np.array([])
namehelix = np.array([])
namehorn = np.array([])


refpointhorn = calibration.refrotationhorn
refpointhelix = calibration.refrotationhelix



for det in cal.horndet:
    errorperrot = errorfunctionhorn(refpointhorn + det.rotation)
#    errorperrot = np.interp([refpointhorn + det.rotation],xhorn,d_fhorn)
    error = errorperrot*delrotation
    print 'station: ', det.name, 'error = ', str('%.2f' % error)
print '\n'
for det in cal.helixdet:
    errorperrot = errorfunctionhelix(refpointhelix + det.rotation)
#    errorperrot = np.interp([refpointhelix + det.rotation],xhelix,d_fhelix)
    error = errorperrot*delrotation
    print 'station: ', det.name, 'error = ', str('%.2f' % error)

# plt.plot(xhelix, d_fhelix,label='helix')
# plt.plot(xhorn, d_fhorn,label='horn')
# plt.xlabel('nr of rotation',fontsize=15)
# plt.ylabel('slope [dB/rotation]',fontsize=15)
# plt.legend(fontsize=15)
# plt.show()

# for det in cal.helixdet:
#     det.delrotation = delrotation
#     patinstallhelix = np.append(patinstallhelix, cal.getpoweratinstall(det))
#     zenithhelix = np.append(zenithhelix, det.zenith)
#     azhelix = np.append(azhelix, det.azimuth)
    
# fig1 = plt.figure(figsize = (8,8))
# n, bins, patches = plt.hist(patinstallhorn, 10, facecolor='green', alpha=0.75, label='horn')
# n1, bins1, patches1 = plt.hist(patinstallhelix, 10, facecolor='red', alpha=0.75, label='helix')
# plt.xlabel('power at installation [dBm]', fontsize =15)
# plt.ylabel('entries',fontsize = 15)
# plt.legend(fontsize=15)

# plt.show()

# ## write down the values (for the notebook)
# print ' helix detectors (in dBm):'
# for det in cal.helixdet:
#     print det.name , ' ' , "%.2f" % cal.getpoweratinstall(det)

# print '\n horn detectors (in dBm):'
# for det in cal.horndet:
#     print det.name , ' ' , "%.2f" % cal.getpoweratinstall(det)

