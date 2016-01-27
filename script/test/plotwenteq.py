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
def readcsv(filename):
    f = open(filename,'r+')
    x = np.array([])
    y = np.array([])
    for l in f:
        x = np.append(x,float(l.split(',')[0]))
        y = np.append(y,float(l.split(',')[1]))
    return [x,y]

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
    freq = np.append(freq,onefreq)
    gain = np.append(gain,onegain)



#wenteqNF022966.csv
datafolder2 = '../../data/gain2/'
snarray = ['022966','022967','022968','022969','022970','023230','023231','023232']
#snarray = ['027570']
for sn in snarray:
    fgainname = datafolder2 + 'wenteqS21'+ sn + '.csv'
    fnoisename = basefolder + 'wenteqNF'+ sn + '.csv'
    data = readcsv(fgainname)
    datanoise = readcsv(fnoisename)
    plt.plot(datanoise[0],datanoise[1],label=sn)
#    plt.plot(data[0],data[1],label=sn)




#BW integration:
gainlin = np.power(10, (gain+50)/10)
newgainlin = gainlin[ (freq > 1 ) & (freq <1.5)]
sum = np.sum(newgainlin)*(freq[1]- freq[0])*1e9
#print 'sum = ' , sum
#print 'sum dB = ' , 10*np.log10(sum)

#plt.plot(freq*1000,gain+50,'k',lw=2,label='measured')
plt.xlabel('frequency [MHz]',fontsize=15)
#plt.ylabel('gain [dB]',fontsize=15)
plt.ylabel('noise figure [dB]',fontsize=15)
plt.xlim(950,1400)
plt.locator_params(nbins=7)
#plt.ylim(50,53)
plt.ylim(0.5,0.8)
plt.legend(ncol=3)
plt.show()
