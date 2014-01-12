class Airplane(object):
    myWeight=0
    myLength=0
    def __init__(self,weight,length):
        self.myWeight=weight
        self.myLength=length
    def getWeight(self):
        return self.myWeight
    def getLength(self):
        return self.myLength
class PassengerJet(Airplane):
    myPassengerCount=0
    def __init__(self,weight,length,passengerCount):
        self.myPassengerCount=passengerCount
        super(PassengerJet, self).__init__(weight,length)
    def getPassengerCount(self):
        return self.myPassengerCount
class MilitaryJet(Airplane):
    myStealthFactor=0
    myBombCapacity=0
    def __init__(self,weight,length,stealth,bombCapacity):
        super(MilitaryJet,self).__init__(weight,length)
        self.myStealthFactor=stealth
        self.myBombCapacity=bombCapacity
    def getStealthFactor(self):
        return myStealthFactor
    def getBombCapacity(self):
        return myBombCapacity
class BusinessPlane(Airplane):
    isJet=True
    def __init__(self,weight,length):
        super(BusinessPlane,self).__init__(weight,length)
    def getJet(self):
        return self.isJet
    def setJet(self,a):
        self.isJet=a
        
