import numpy as np
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../../../script/utils/'
sys.path.append(utilspath)
import utils

################################################
### get the average gain of amplifier     ######
################################################
basename = 'wenteqS21'
snarray  = ['022966','022967','022968','022969','022970','023230','023231','023232']
allgains = []
onefreq = np.array([])
thefreq = np.arange(0,2000,1)
for sn in snarray:
    filename = basename + sn + '.csv'
    datagain = utils.readcsv(filename)
    freq = datagain[0]
    gain = datagain[1]    
    newgain = np.interp(thefreq,freq,gain)
    allgains.append(newgain)
allgainsnp = np.ndarray(shape=(len(allgains),len(allgains[0])))
counter = 0
for gain in allgains:
    allgainsnp[counter] = gain
    counter +=1
meangain = np.mean(allgainsnp,axis=0)
newgainname = 'lnadata.txt' 
utils.writeintwocolumns([thefreq,meangain],newgainname)
