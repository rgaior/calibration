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
basefolder = cwd + '/../../data/gain/'

f = open(basefolder+ 'newwenteq.txt','r+')
header = 1
count = 0
freq = np.array([])
gain = np.array([])
for l in f:
    if count == 0:
        count +=1
        continue
    onefreq = float(l.split()[0])
    onegain = float(l.split()[3])
#    print onefreq,  ' ' , onegain
    freq = np.append(freq,onefreq)
    gain = np.append(gain,onegain)

#BW integration:
gainlin = np.power(10, (gain+50)/10)
newgainlin = gainlin[ (freq > 1 ) & (freq <1.5)]
sum = np.sum(newgainlin)*(freq[1]- freq[0])*1e9
print 'sum = ' , sum
print 'sum dB = ' , 10*np.log10(sum)

plt.plot(freq,gain+50)
plt.xlabel('frequency [GHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
#plt.show()
