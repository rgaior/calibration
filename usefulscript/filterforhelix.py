import numpy as np
import math
import matplotlib.pyplot as plt
Tphys = 290
Ts = 100
NF = np.arange(0.1, 2, 0.1)
NFlin = np.power(10,NF/10)
t0= 290
temp = ( NFlin - 1)*t0
alpha = ((NFlin - 1)*Ts/Tphys)

L = alpha / (1+alpha)
plt.plot(temp,10*np.log10(1+L))
plt.show()
print L , ' in dB = ', 10*np.log10(1+L)
#print 'noise temperature for a physical temp of ', t0 , ' is :', temp

