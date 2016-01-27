import numpy as np
import os
import sys
cwd = os.getcwd()
utilspath = cwd + '/../../../script/utils/'
sys.path.append(utilspath)
import utils

############################################################
### get the LNB gain from the total and antenna gain  ######
############################################################
totgain = utils.readtwocolumns('norsattotgain.txt')
antgain = utils.readtwocolumns('norsatantgain.txt')
newlnadata = 'lnadata.txt' 
#put in MHz
utils.writeintwocolumns([totgain[0]*1000,totgain[1] - antgain[1]],newlnadata)
