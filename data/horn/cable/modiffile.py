import numpy as np
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../../../script/utils/'
sys.path.append(utilspath)
import utils

#################################################
### change cable Jacques data      ######
#################################################
measdata = utils.getjacquesmeas('scope_46.csv','scope_47.csv')
newcabledata = 'cabledata.txt' 
#put in MHz
utils.writeintwocolumns([measdata[0]*1000,measdata[1]],newcabledata)
