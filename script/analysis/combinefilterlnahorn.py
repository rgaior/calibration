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
import utils
gainfolder = cwd + '/../../data/gain/'
filterfolder = cwd + '/../../data/filter/'

#get the norsat gain:
ftot = open(gainfolder+ 'norsattotgain.txt','r+')
fant = open(gainfolder+ 'norsatantgain.txt','r+')
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

#only LNB gain:
gainlnb  = gaintot- gainant
#reverse frequency
freq1 = freq1*1000
freq = freq1[::-1]
LOfreq = 5150 # MHz
freq = LOfreq - freq

#get the on board filter normalized attenuation
fref = 1400 # MHz
fname = 'SXBP-1430-75+___Plus25degC.S2P'
data = utils.readminicircuitdata(filterfolder + fname)
freqfilt = data[0]
gainfilt = data[1]
attenatfref = np.interp([fref],freqfilt,gainfilt)
print 'attenat ref = ' , attenatfref
normedgain = gainfilt - attenatfref

#get the cable loss from data
meascable = utils.getjacquesmeas(filterfolder+'/scope_46.csv',filterfolder+'/scope_47.csv')


#interpolate the gains to add them:
newgainlnb = np.interp(freqfilt,freq,gainlnb)
newgaincable =  np.interp(freqfilt,meascable[0],meascable[1])


totgain = newgainlnb + normedgain + newgaincable

gainlin = np.power(10, (totgain)/10)
#newgainlin = gainlin[ (freqfilt > 500 ) & (freqfilt <2000)]
newgainlin = gainlin
sum = np.sum(newgainlin)*(freqfilt[1]- freqfilt[0])*1e6
print 'sum = ' , sum
print 'sum dB = ' , 10*np.log10(sum)

plt.plot(freqfilt,newgainlnb,label='LNB only')
plt.plot(freqfilt,newgainlnb + normedgain,label='LNB and board filter')
plt.plot(freqfilt,totgain,label='total gain')
#plt.plot(meascable[0],meascable[1],label='total gain')
plt.xlabel('frequency [GHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
plt.xlim(800,2000)
#plt.ylim(7,70)
plt.ylim(60,70)
plt.legend()
plt.show()
