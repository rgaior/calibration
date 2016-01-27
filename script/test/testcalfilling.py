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

calhorn = calibration.Calibration(datafolder = basefolder, type= 'horn')
calhelix = calibration.Calibration(datafolder = basefolder, type='helix')
#first fill the calibration of the adjustable resistor
calhorn.fillpotardata()
calhelix.fillpotardata()
 
print calhorn.resistor
print calhelix.resistor

calhorn.fillboardfilter()
calhelix.fillboardfilter()

calhorn.fillbiastfilter()
calhelix.fillbiastfilter()

calhorn.fillcable()
calhelix.fillcable()

calhorn.filllna()
calhelix.filllna()

# plt.plot(calhorn.lna[0],calhorn.lna[1])
# plt.plot(calhelix.lna[0],calhelix.lna[1])

plt.plot(calhorn.cable[0],calhorn.cable[1])
plt.plot(calhelix.cable[0],calhelix.cable[1])

plt.plot(calhorn.boardfilter[0],calhorn.boardfilter[1])
plt.plot(calhelix.boardfilter[0],calhelix.boardfilter[1])

#plt.plot(calhelix.otherfilter[0],calhelix.otherfilter[1])

plt.show()