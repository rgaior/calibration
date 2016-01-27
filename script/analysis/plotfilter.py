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

typeoffilter = sys.argv[1]
#filtnr = ['1']
#CBP-B1230C+_Plus25DegC.s2p

fref = 1400 #MHz 
################################################
###  for the biasT filter              #########
################################################
if typeoffilter == 'biast':
    filtnr = ['1','2','3','4','5']
    allgain = []
    for filt in filtnr:
        #    fname = 'CBP-B1230C+_Plus25DegC.s2p'
        fname = 'HFCN-1000+ _AP130157_022513_UNIT-'+filt+'.s2p'
        data = utils.readminicircuitdata(basefolder + fname)
        freq = data[0]
        gain = data[1]
        attenatfref = np.interp([fref],freq,gain)
        allgain.append(gain)
        plt.plot(freq,gain,label=filt)
 
    allgainnp = np.ndarray(shape=(len(allgain),len(allgain[0])))
    counter = 0
    for gain in allgain:
        allgainnp[counter] = gain
        counter +=1
    meangain = np.mean(allgainnp,axis=0)
 #print allgain

    measdata = utils.getjacquesmeas(basefolder+'/scope_42.csv',basefolder+'/scope_43.csv')
    plt.plot(freq,meangain,'k',lw=2,label='average const.')
    plt.plot(measdata[0]*1000,measdata[1],'r',lw=2,label='meas. data')


################################################
###       for the board filter (helix)     #####
################################################
if typeoffilter == 'boardhelix':
    fname = 'CBP-B1230C+_Plus25DegC.s2p'
    data = utils.readminicircuitdata(basefolder + fname)
    freq = data[0]
    gain = data[1]
    attenatfref = np.interp([fref],freq,gain)
    plt.plot(freq,gain - attenatfref,label='board filter helix')

################################################
###        for the board filter (horn)     #####
################################################
if typeoffilter == 'boardhorn':
    fname = 'SXBP-1430-75+___Plus25degC.S2P'
    data = utils.readminicircuitdata(basefolder + fname)
    freq = data[0]
    gain = data[1]
    attenatfref = np.interp([fref],freq,gain)
    plt.plot(freq,gain - attenatfref,label='board filter horn')


plt.xlabel('frequency [MHz]',fontsize=15)
plt.ylabel('gain [dB]',fontsize=15)
#plt.xlim(500,2000)
#plt.ylim(-60,3)
plt.xlim(500,2000)
plt.ylim(-1,1)
#plt.legend(ncol=3)
plt.show()
