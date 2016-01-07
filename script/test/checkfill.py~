import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import numpy as np
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import utils
import utils
import detector
import calibration
basefolder = cwd + '/../../data/'

cal = calibration.Calibration(datafolder = basefolder)
#first fill the calibration of the adjustable resistor
cal.fillpotardata()

dethorn = cal.filldetectors('horn')
dethelix = cal.filldetectors('helix')

adc = [0,500,1024]
print 'adc to v front end: ', utils.adctov_fe(adc[0]), ' ' , utils.adctov_fe(adc[1]), ' ' , utils.adctov_fe(adc[2])
print 'adc to v board: ', utils.adctov_board(adc[0]), ' ' , utils.adctov_board(adc[1]), ' ' , utils.adctov_board(adc[2])

print 'size of dets = ', len(cal.horndet)
for det in cal.horndet:
    print det.type, ' ', det.name, ' ',  det.tankid , ' ', det.zenith, ' ' , det.azimuth, ' ' , det.antid, ' ' , det.elecid, ' ' ,  det.rotation , ' ', det.meanBL 
print ' '
for det in cal.helixdet:
    print det.type , ' ',  det.name, ' ',  det.tankid , ' ', det.zenith, ' ' , det.azimuth, ' ' , det.antid, ' ' , det.elecid, ' ' ,  det.rotation , ' ', det.meanBL 
