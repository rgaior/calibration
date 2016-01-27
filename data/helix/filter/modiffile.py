import numpy as np
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../../../script/utils/'
sys.path.append(utilspath)
import utils

################################################
### change board filter constructor data  ######
################################################
boardfiltername = 'CBP-B1230C+_Plus25DegC.s2p'
databoardfilter = utils.readminicircuitdata(boardfiltername)
newnboardfiltername = 'boardfilterconst.txt' 
utils.writeintwocolumns(databoardfilter,newnboardfiltername)


#################################################
### change bias T filter constructor data  ######
#################################################
biasTfilterdata = 'HFCN-1000+ _AP130157_022513_UNIT-'
filenr = ['1','2','3','4','5']
allfilters = []
onefreq = np.array([])
for nr in filenr:
    filename = biasTfilterdata + nr + '.s2p'
    databiasTfilter = utils.readminicircuitdata(filename)
    freq = databiasTfilter[0]
    filter = databiasTfilter[1]
    onefreq = freq
    allfilters.append(filter)
allfiltersnp = np.ndarray(shape=(len(allfilters),len(allfilters[0])))
counter = 0
for filt in allfilters:
    allfiltersnp[counter] = filt
    counter +=1
meanfilter = np.mean(allfiltersnp,axis=0)
newnbiasTfiltername = 'biasTfilterconst.txt' 
utils.writeintwocolumns([onefreq,meanfilter],newnbiasTfiltername)

#################################################
### change bias T filter Jacques data      ######
#################################################
measdata = utils.getjacquesmeas('scope_42.csv','scope_43.csv')
newnbiasTdata = 'biasTfilterdata.txt' 
#put in MHz
utils.writeintwocolumns([measdata[0]*1000,measdata[1]],newnbiasTdata)