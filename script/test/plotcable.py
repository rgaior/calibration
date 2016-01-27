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
basefolder = cwd + '/../../data/filter/'

measdata = getjacquesmeas(basefolder+'/scope_43.csv',basefolder+'/scope_44.csv')

plt.plot(measdata[0]*1000,measdata[1],'r',lw=2,label='meas. data (cable)')
plt.xlabel('frequency [MHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
#plt.xlim(500,2000)
#plt.ylim(-60,3)
plt.xlim(1000,1500)
plt.ylim(-4,2)
plt.legend(ncol=3)
plt.show()
