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
boardfiltername = 'SXBP-1430-75+___Plus25degC.S2P'
databoardfilter = utils.readminicircuitdata(boardfiltername)
newnboardfiltername = 'boardfilterconst.txt' 
utils.writeintwocolumns(databoardfilter,newnboardfiltername)
