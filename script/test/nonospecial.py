import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import numpy as np
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils

#get the base of the field folder
base = cwd + '/../../data/potar/'

## data of the needed input power at 1.4GHz for a given rotation 
## for the voltage to be kept at -2V
datapotarhelix = base+ 'potarHelix.txt'
datapotarcornet = base+ 'potarCornet.txt'

#set the data in a list [rotation,power in dBm]
datahelix = utils.readpotardata(datapotarhelix)
datacornet = utils.readpotardata(datapotarcornet)

fit = np.polyfit(datahelix[0],datahelix[1],2)

p = np.poly1d(fit)


fit2 = np.polyfit(datacornet[0],datacornet[1],2)
p2 = np.poly1d(fit2)
print 'P at -2V for r = -5 = ', p(-5)


fig = plt.figure(figsize=(8, 8))
fig.suptitle('calibration potentiometre', fontsize=14, fontweight='bold')

ax1 = fig.add_subplot(111)
#fig.subplots_adjust(top=0.85)

ax1.set_xlabel('nr of rotation')
ax1.set_ylabel('power at -2V [dBm]')
ax1.plot(datahelix[0],datahelix[1],'b',lw=2,label='helix')
ax1.plot([0],[-22],'bo',label='reference helix')
ax1.plot(datacornet[0],datacornet[1],'g',lw=2,label='horn')
ax1.plot([-13.5],[-18.8],'go',label='reference horn')
x = np.linspace(-8,15)
ax1.plot(x,p(x),'k--',lw=2,label='fit helix')
x2 = np.linspace(-20,10)
ax1.plot(x2,p2(x2),'k--',lw=2,label='fit horn')

plt.legend(loc=3)
plt.show()
