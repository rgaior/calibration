import utils
import detector
from numpy import interp
import numpy as np

# files containing the the adjustable resistor calibration
helixfile = '/potar/potarHelix.txt'
hornfile = '/potar/potarCornet.txt'

#file containing the detector parameters (from installation document)
installhelix = '/install/installHelix.txt'
installhorn = '/install/installCornet.txt'

#point set before installation in number of rotation
refrotationhelix = 0
refrotationhorn = -13.5


class Calibration:
    def __init__(self, datafolder = '', 
                 resistorhelix = [],
                 resistorhorn = [],
                 helixdet = [],
                 horndet = []
                 ):

        self.datafolder = datafolder
        self.resistorhelix = resistorhelix
        self.resistorhorn = resistorhorn
        #filter on board:
        self.boardfilterhelix = []
        self.boardfilterhorn = []

        self.helixdet = helixdet
        self.horndet = horndet
        self.boardslope = -10.4 # (cf thesis 1/0.0234*4.1)
        
        
    def reset(self):
        self.helixdet = []
        self.horndet = []
    #get the calibration curve of the adjustable resistor
    def fillpotardata(self):
        resistorhelixfile = self.datafolder + helixfile
        self.resistorhelix = utils.readpotardata(resistorhelixfile)
        resistorhornfile = self.datafolder + hornfile
        self.resistorhorn = utils.readpotardata(resistorhornfile)

    # fill one detector
    def filldetector(self, type, name):
        if type.lower() == 'cornet' or type.lower() == 'horn':
            file = self.datafolder + installhorn
            det = detector.Detector()
            det.fill(file,name)
            if (det.tankid == 0):
                print 'detector not filled ! '
            self.horndet.append(det)
        if type.lower() == 'helix' or type.lower() == 'helice':
            file = self.datafolder + installhelix
            det = detector.Detector()
            det.fill(file,name)
            if (det.tankid == 0):
                print 'detector not filled ! '            
            self.helixdet.append(det)

    #fill the detectors parameters from a file in /data
    def filldetectors(self, type):
        file = ''
        if type.lower() == 'cornet' or type.lower() == 'horn':
            file = self.datafolder + installhorn
        elif type.lower() == 'helix' or type.lower() == 'helice':
            file = self.datafolder + installhelix
        else:
            print 'wrong type !!!! it is either helix or horn'
            return

        f = open(file, 'r+')
        counter = 0
        for l in f:
            if counter == 0:
                counter +=1
                continue
            det = detector.Detector()
            det.fillwithline(l.split())                
            det.type = type
            if (det.tankid == 0):
                print 'detector not filled ! '
            if type.lower() == 'cornet' or type.lower() == 'horn':
                self.horndet.append(det)
            else:
                self.helixdet.append(det)

    def seterrorrotation(self, det, deltarotation):
        refrotation = 0
        ## done that way because data didn't give something very regular 
        if det.type == 'horn': 
            fit = np.polyfit(self.resistorhorn[0],self.resistorhorn[1],2)
            errorfunction = np.poly1d([2*fit[0], fit[1]])
            refrotation = refrotationhorn
        if det.type == 'helix': 
            fit = np.polyfit(self.resistorhelix[0],self.resistorhelix[1],2)
            errorfunction = np.poly1d([2*fit[0], fit[1]])
            refrotation = refrotationhelix
        det.errorrotation = errorfunction(refrotation + det.rotation)*deltarotation

    def getdetector(self,name):
        found = False
        for det in self.horndet:
            if det.name.lower() == name.lower():
                found = True
                return det
        if found == False:
            for det in self.helixdet:
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
        if det.type == 'horn': 
            ref = refrotationhorn
            rotation = ref + det.rotation
            poweratminus2 = interp(rotation,self.resistorhorn[0],self.resistorhorn[1])
        if det.type == 'helix': 
            ref = refrotationhelix
            rotation = ref + det.rotation
            #special case for nono:
            if det.name.lower()=='nono':
                poweratminus2 = -29.2
            else:
                poweratminus2 = interp(rotation,self.resistorhelix[0],self.resistorhelix[1])
        #now get the voltage difference between -2V and the voltage at install
        if whatbaseline == 'install':
            deltav = utils.adctov_board(det.meanBL) - (-2)
        elif whatbaseline == 'monit':
            deltav = utils.adctov_board(det.meanBLyear) - (-2)

        poweratinstall = poweratminus2 + self.boardslope*deltav
        return poweratinstall
