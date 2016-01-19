import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import time
import datetime
from matplotlib.legend_handler import HandlerLine2D
from datetime import date
import numpy as np
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils

base = cwd + '/../../data/monit/'


station = sys.argv[1]
cutdate = sys.argv[2]

#s = "01/12/2015"
cut = datetime.datetime.strptime(cutdate, "%d/%m/%Y").date()
#print cut.year


databl = base+ 'monit'+station+ '2.txt'
datatemp = base+ 'monit'+station+ 'temp.txt'

#set the data in a list [time, baseline [adc]]
thedatabl = utils.readmonit(databl)
thedatatemp = utils.readmonit(datatemp)

newtime = thedatabl[0][thedatabl[0] > cut]
newbl = thedatabl[1][thedatabl[0] > cut]
newtemp = thedatatemp[1][thedatatemp[0] > cut]

totdays = (newtime[-1]- newtime[0]).total_seconds()/(24*3600)



fit = np.polyfit(newtemp,newbl,1)
p = np.poly1d(fit)

fig = plt.figure(figsize=(10, 6))
fig.suptitle('monit '+str(totdays)+' days for '+ station, fontsize=14, fontweight='bold')
ax1 = fig.add_subplot(121)

#new data normalize w.r.t. reftem deg
reftemp = 25
dataatref = newbl - (newtemp-reftemp)*fit[0]

#ax1.set_ylabel('<baseline> [adc]')
ax1.plot(newtemp,newbl,'b.',label=station)
ax1.plot(newtemp,p(newtemp),'k-',lw=2,label=station)

# fig.autofmt_xdate()

# # use a more precise date string for the x axis locations in the
# # toolbar
# import matplotlib.dates as mdates
# ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
# #plt.legend(loc=3)

#fig2 = plt.figure(figsize=(10, 8))
#fig2.suptitle('monit 300 days for '+ station, fontsize=14, fontweight='bold')
ax2 = fig.add_subplot(122)
n, bins, patches = ax2.hist(dataatref, 100, facecolor='green', alpha=0.75, label='horn')
ax2.text(0.95, 0.90, 'mean = '+ str("%.2f" % np.mean(dataatref)) + '\n'+ ' standard dev. = '+ str("%.2f" % np.std(dataatref)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax2.transAxes,
        color='black', fontsize=15)
 
plt.show()
