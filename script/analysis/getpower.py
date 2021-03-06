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
cal = calibration.Calibration(datafolder = basefolder)
#first fill the calibration of the adjustable resistor
cal.fillpotardata()

#fill the installation information
cal.filldetectors('horn')
cal.filldetectors('helix')

## definition of the slope of the electronics board.
## delP is the dynamic range (I guess 20dB) and delV is 2V
#det = cal.getdetector('vieira')
p = cal.getpoweratinstall(cal.getdetector(nameoftank))
print 'power at install = ', p

