import utils
datafolder = '/Users/romain/work/Auger/EASIER/LPSC/calibration/data/'

class Detector:
    def __init__(self, name = '', tankid = 0, type = '',
                 zenith = 0, azimuth = 0,
                 antid = 0, elecid = 0, rotation = 0,
                 meanBL = 0
                 ):
        self.name = name
        self.tankid = tankid
        self.type = type
        self.zenith = zenith
        self.azimuth = azimuth
        self.antid = antid
        self.elecid = elecid
        self.rotation = rotation
        self.meanBL = meanBL
        
    def fillwithline(self, data):
        self.name = data[0]
        self.tankid = int(data[1])
        self.zenith = float(data[2])
        self.azimuth = float(data[3])
        self.antid = int(data[4])
        self.elecid = int(data[5])
        self.rotation = float(data[6])
        self.meanBL = float(data[7])

    def fill(self, installfile, name):
        f = open(installfile,'r+')
        counter = 0
        for l in f:
            if counter == 0:
                counter += 1
                continue
            data = l.split()
            print 'name == ' , data[0] 
            #compare in lower case
            if data[0].lower() == name.lower():
                self.fillwithline(data)
                f.close()
                return 
            else:
                print 'no detector of this type with this name, check your input '
                return 
    
            
    def getpotarcalib(self):
        if self.type == 'horn' or self.type == 'cornet':
            filename = datafolder + 'potarCornet.txt'
            data = readpotardata(filename)
        if self.type == 'helix':
            filename = datafolder + 'potarHelix.txt'
            data = readpotardata(filename)
        return data

