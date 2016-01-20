import numpy as np
import matplotlib.pyplot as plt

errdb1 = np.arange(0.1,10,0.1)
errdb2 = np.arange(0.1,10,0.1)

errlin1 = np.power(10,errdb1/10) - 1
errlin2 = np.power(10,errdb2/10) - 1

errtotdb = np.sqrt(errdb1*errdb1 + errdb2*errdb2) 
errtotlin = np.sqrt(errlin1*errlin1 +errlin2*errlin2) 
errtotlindb = 10*np.log10(errtotlin+1)

plt.plot(errdb1, errtotdb)
plt.plot(errdb1, errtotlindb)
plt.show()
