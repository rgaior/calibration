import numpy as np
import matplotlib.pyplot as plt

def read(filename):
    f = open(filename,'r+')
    x = np.array([])
    y = np.array([])
    for l in f:
        print l.split(',')
        x = np.append(x,float(l.split(',')[0]))
        y = np.append(y,float(l.split(',')[1]))
    return [x,y]

#wenteqNF022966.csv
datafolder = '../../data/gain2/'
snarray = ['022966','022967','022968','022969','022970','023230','023231','023232']
for sn in snarray:
    fgainname = datafolder + 'wenteqS21'+ sn + '.csv'
#fgainname = '/Users/romain/Desktop/wenteqS21022966.csv'
#fnoisename = datafolder + 'wenteqNF'+ sn + '.csv'
    data = read(fgainname)
#datanf = read(fnoisename)
    plt.plot(data[0],data[1])
#    plt.plot(datanf[0],datanf[1])


plt.show()
