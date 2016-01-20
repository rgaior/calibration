import numpy as np
x = y = z = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', [x,y], delimiter=',')   # X is an array
#np.savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays
