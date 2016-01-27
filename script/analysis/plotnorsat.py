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

ftot = open(basefolder+ 'norsattotgain.txt','r+')
fant = open(basefolder+ 'norsatantgain.txt','r+')
header = 1
count = 0
freq1 = np.array([])
freq2 = np.array([])
gaintot = np.array([])
gainant = np.array([])
for l in ftot:
    if count == 0:
        count +=1
        continue
    onefreq = float(l.split()[0])
    onegain = float(l.split()[1])
    freq1 = np.append(freq1,onefreq)
    gaintot = np.append(gaintot,onegain)

count = 0
for l in fant:
    if count == 0:
        count +=1
        continue
    onefreq = float(l.split()[0])
    onegain = float(l.split()[1])
    freq2 = np.append(freq2,onefreq)
    gainant = np.append(gainant,onegain)

fant.close()
ftot.close()

#BW integration:
gainlnb  = gaintot- gainant
gainlin = np.power(10, (gainlnb)/10)
#newgainlin = gainlin[ (freq > 1 ) & (freq <1.5)]
sum = np.sum(gainlin)*(freq1[1]- freq1[0])*1e9
print 'sum = ' , sum
print 'sum dB = ' , 10*np.log10(sum)

plt.plot(freq1,gaintot,label='total gain')
plt.plot(freq2,gainant,label='antenna gain')
plt.plot(freq1,gaintot-gainant,label='LNB gain')
plt.xlabel('frequency [GHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
plt.ylim(7,100)
plt.legend()
plt.show()
