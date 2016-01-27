import utils
import detector
from numpy import interp
import numpy as np

#point set before installation in number of rotation
refrotationhelix = 0
refrotationhorn = -13.5
#frequency at whcih calibration was done
frefhorn = 1400 # MHz
frefhelix = 1400 # MHz

class Calibration:
    def __init__(self, datafolder = '' ,type =''):
        self.type = type
        
        self.datafolder = datafolder
        #adjustable resistor
        self.resistor = []
        #filter on board:
        self.boardfilter = []
        #lna gain
        self.lna = []
        #other filter (like biasT filter): 
        self.other = []
        #cable attenuation 
        self.cable = []
        #include the detector (with its position and installation data)
        self.det = []
        #value of the board slope in db/V 
        self.boardslope = -10.4 # (cf thesis 1/0.0234*4.1)

        #reset the detectors
        self.det = []
        # set the folder:
        if self.type.lower() == 'cornet' or type.lower() == 'horn':
            self.datafolder = datafolder + '/horn/'
        elif self.type.lower() == 'helix' or self.type.lower() == 'helice':
            self.datafolder = datafolder + '/helix/'
        else:
            print 'not the right type of detector type, it should be either horn or helix'
    def reset(self):
        self.resistor = []
        self.det = []
    def fillcalibdata(self):
        self.reset()
        self.fillpotardata()
        self.fillboardfilter()
        self.fillbiastfilter()
        self.fillcable()
        self.filllna()

    def fillpotardata(self):
        resistorfile = self.datafolder + 'potar/calib.txt'
        self.resistor = utils.readtwocolumns(resistorfile)

    def fillboardfilter(self):
        boardfilterdata = self.datafolder + 'filter/boardfilterconst.txt'
        self.boardfilter = utils.readtwocolumns(boardfilterdata)
        
    # here we have values from constructor or data measured by Jacques.
    # you have to choose, or default is measured data
    def fillbiastfilter(self,constordata=None):
        if self.type== 'horn':
            return
        biastfilterdata = []
        if constordata is None: 
            biastfilterdata = self.datafolder + 'filter/biasTfilterdata.txt'
        elif constordata == 'const':
            biastfilterdata = self.datafolder + 'filter/biasTfilterconst.txt'
        elif constordata == 'data':
            biastfilterdata = self.datafolder + 'filter/biasTfilterdata.txt'
        self.otherfilter = utils.readtwocolumns(biastfilterdata)

    def fillcable(self):
        cablename = self.datafolder + 'cable/cabledata.txt'
        self.cable = utils.readtwocolumns(cablename)

    def filllna(self):
        lnaname = self.datafolder + 'gain/lnadata.txt'
        self.lna = utils.readtwocolumns(lnaname)

    # fill one detector
    def filldetector(self, name):
        #install file :
        file = self.datafolder + '/install/' + 'install.txt' 
        det = detector.Detector()
        det.type = self.type
        det.fill(file,name)
        if (det.tankid == 0):
            print 'detector not filled ! '
        else: self.det.append(det)

    #fill the detectors parameters from a file in /data
    def filldetectors(self):
        file = self.datafolder + '/install/' + 'install.txt' 
        f = open(file, 'r+')
        counter = 0
        for l in f:
            if counter == 0:
                counter +=1
                continue
            det = detector.Detector()
            det.type = self.type
            det.fillwithline(l.split())                
            det.type = type
            if (det.tankid == 0):
                print 'detector not filled ! '
            else:self.det.append(det)

    def seterrorrotation(self, det, deltarotation):
        refrotation = 0
        ## done that way because data didn't give something very regular 
        fit = np.polyfit(self.resistor[0],self.resistor[1],2)
        errorfunction = np.poly1d([2*fit[0], fit[1]])
        refrotation = det.refrotation
        det.errorrotation = errorfunction(refrotation + det.rotation)*deltarotation

    def getdetector(self,name):
        found = False
        for det in self.det:
            if det.name.lower() == name.lower():
                found = True
                return det
        if found == False:
            print '!!! couldn t find the det with the name: ' , name
            
    ## the procedure to find the power at the installation 
    ## is described in a note.
    ## we first find the power at -2V from the resistor calibration
    ## then we exptrapolate knowing the slope of the board.
    def getpoweratinstall(self, det, whatbaseline):
        #value of the nr of rotation set before installation (hardcoded)
        # find the power at -2V from calibration
        ref = 0 
        rotation = 0 
        poweratminus2 = 0
        ref = det.refrotation
        rotation = ref + det.rotation
        poweratminus2 = interp(rotation,self.resistor[0],self.resistor[1])
        if det.name.lower()=='nono':
            poweratminus2 = -29.2
        #now get the voltage difference between -2V and the voltage at install
        if whatbaseline == 'install':
            deltav = utils.adctov_board(det.meanBL) - (-2)
        elif whatbaseline == 'monit':
            deltav = utils.adctov_board(det.meanBLyear) - (-2)
        poweratinstall = poweratminus2 + self.boardslope*deltav
        return poweratinstall

    def gettotalgain(self):
        ## slightly different for horn and helix (helix has the biasT filter)
        ## and for the horn there is a frequency down shift
        freq = np.array([])
        totgain = np.array([])
        # horn # 
        if self.type == 'horn':
            #first switch the LNA gain:
            LOfreq = 5150 #MHz
            freqlna = self.lna[0]
            freq = freqlna[::-1]
            LOfreq = 5150 # MHz
            freqlna = LOfreq - freq
            freqfilt = self.boardfilter[0]
            freq = freqlna
            # interpolate all the gains with the same frequency step and range
            newboard = np.interp(freq,self.boardfilter[0],self.boardfilter[1])
            newcable = np.interp(freq,self.cable[0],self.cable[1])
            # normalize board filter attenuation to the reference freqeuncy
            attenatfref = np.interp([frefhorn],freq,newboard)
#            newboard = self.boardfilter[1]
            newboard = newboard - attenatfref
            #totgain = newlna + newboard + newcable
            totgain = self.lna[1] + newboard + newcable
            
        if self.type == 'helix':
            freq = self.lna[0]
            # interpolate all the gains with the same frequency step and range
            newboard = np.interp(freq,self.boardfilter[0],self.boardfilter[1])
            newbiast = np.interp(freq,self.otherfilter[0],self.otherfilter[1])
            newcable = np.interp(freq,self.cable[0],self.cable[1])
            # normalize board filter attenuation to the reference freqeuncy
            attenatfref = np.interp([frefhelix],freq,newboard)
            newboard = newboard - attenatfref
            totgain = self.lna[1] + newboard + newbiast + newcable

        return [freq,totgain]

    def getexpectedvalue(self,tant, tlna):
        kb = 1.38e-23
        totgain = self.gettotalgain()
        gainbwlin = utils.integratebw(totgain,'db')
        pexplin = kb*(tant + tlna)*gainbwlin
        pexpdb = 10*np.log10(pexplin)
        return pexpdb
