#######################################################################
### return the power at the installation for a given detector name  ###
#######################################################################
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
import detector
import calibration
basefolder = cwd + '/../../data/'

if len(sys.argv) < 2:
    print 'usage: python getpower <name of tank>' 
    sys.exit()

nameoftank = sys.argv[1]
print 'name of tank = ', nameoftank
calhorn = calibration.Calibration(datafolder = basefolder,type = 'horn')
calhelix = calibration.Calibration(datafolder = basefolder,type='helix')

#first fill the calibration of the adjustable resistor
calhorn.fillcalibdata()
calhelix.fillcalibdata()

#fill the installation information
calhorn.filldetectors()
calhelix.filldetectors()

for det in calhorn.det:
    if det.name == nameoftank:
        p = calhorn.getpoweratinstall(calhorn.getdetector(nameoftank),'monit')
for det in calhelix.det:
    if det.name == nameoftank:
        p = calhelix.getpoweratinstall(calhelix.getdetector(nameoftank),'monit')

print 'power at install = ', p

