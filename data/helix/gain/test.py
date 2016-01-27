import numpy as np
import matplotlib.pyplot as plt
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../../../script/utils/'
sys.path.append(utilspath)
import utils

data = utils.readtwocolumns('wenteq.txt')
plt.plot(data[0],data[1])
plt.show()
