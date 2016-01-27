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
basefolder = cwd + '/../../data/filter/'

#first get the LNA gain:
datafolder2 = '../../data/gain2/'
snarray = ['022966','022967','022968','022969','022970','023230','023231','023232']
lnagain = []
for sn in snarray:
    fgainname = datafolder2 + 'wenteqS21'+ sn + '.csv'
    data = utils.readcsv(fgainname)
    lnagain.append(data)


# get the on board filter data (CBP-B1230C+_Plus25DegC.s2p)
fref = 1400 #MHz freq to be normalized to (because resistor calibration was done at this frequency)
fname = '/CBP-B1230C+_Plus25DegC.s2p'
boardfilter = utils.readminicircuitdata(basefolder + fname) # (return [freq,gain])
attenatfref = np.interp([fref],boardfilter[0],boardfilter[1])
boardfilter[1] = boardfilter[1] - attenatfref # normalize the gain to the reference frequency

#get the biasT filter from data
measbiast = utils.getjacquesmeas(basefolder+'/scope_42.csv',basefolder+'/scope_43.csv')

#get the cable loss from data
meascable = utils.getjacquesmeas(basefolder+'/scope_43.csv',basefolder+'/scope_44.csv')

#we interpolate w.r.t. the constructor data:
freq = boardfilter[0]
newmeasbiast = np.interp(freq,measbiast[0]*1000,measbiast[1])
newmeascable = np.interp(freq,meascable[0]*1000,meascable[1])

totgains = []
gainbw = np.array([])
for lnag in lnagain:
    newgain = np.interp(freq,lnag[0],lnag[1])
    totgain = newgain + boardfilter[1]+ newmeasbiast + newmeascable
#    totgain = newgain + boardfilter[1] + newmeasbiast + newmeascable
    totgains.append(totgain)
    
    gainlin = np.power(10, (totgain)/10)
    newgainlin = gainlin[(freq > 500) &  (freq <2000)]
    sum = np.sum(newgainlin)*(freq[1]- freq[0])*1e6
    gainbw = np.append(gainbw,10*np.log10(sum))
#    print 'sum = ' , sum
#    print 'sum dB = ' , 10*np.log10(sum)

fig = plt.figure(figsize=(8,5))
#plt.subplot(131)
for data,name in zip(totgains,snarray):
    plt.plot(freq,data,label=name)
    plt.xlabel('frequency [MHz]',fontsize=15)
    plt.ylabel('gain [dB]',fontsize=15)
    plt.xlim(500,2000)
    plt.ylim(-40,60)
#plt.subplot(132)
fig2 = plt.figure(figsize=(8,5))
for data,name in zip(totgains,snarray):
    plt.plot(freq,data,label=name)
    plt.xlabel('frequency [MHz]',fontsize=15)
    plt.ylabel('gain [dB]',fontsize=15)
    plt.xlim(950,1500)
    plt.ylim(45,50)

fig3 = plt.figure(figsize=(5,5))
ax = fig3.add_subplot(111)
n, bins, patches = ax.hist(gainbw, 10, facecolor='green', alpha=0.75, label='horn')
ax.text(0.95, 0.90, 'mean = '+ str("%.2f" % np.mean(gainbw)) + '\n'+ ' standard dev. = '+ str("%.2f" % np.std(gainbw)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=15)
ax.set_xlim(130,133)
ax.set_xlabel('10*log10(gain*bandwidth) [dB]', fontsize =15)
ax.set_ylabel('entries',fontsize = 15)
#plt.legend(fontsize=15)


#    plt.legend()
#    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#plt.subplot(133)

plt.show()
