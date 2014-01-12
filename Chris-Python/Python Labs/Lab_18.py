class Component(object):
    myTypeName=''
    myPartNumber=0
    myVersionNumber=0
    def __init__(self,typeName,partNumber,versionNumber):
        self.myTypeName=typeName
        self.myPartNumber=partNumber
        self.myVersionNumber=versionNumber
    def getTypeName(self):
        return self.myTypeName
    def getPartNumber(self):
        return self.myPartNumber
    def getVersionNumber(self):
        return self.myVersionNumber
class ElectricalComponent(Component):
    myMinRating=0
    myMaxRating=0
    def __init__(self,partNumber,versionNumber,minRating,maxRating):
        super(ElectricalComponent,self).__init__('Electrical',partNumber,versionNumber)
        self.myMinRating=minRating
        self.myMaxRating=maxRating
    def getMinRating(self):
        return self.myMinRating
    def getMaxRating(self):
        return self.myMaxRating
class HighvoltageComponent(ElectricalComponent):
    def __init__(partNumber,versionNumber):
        super(HighvoltageComponet,self).__init__(partNumber,versionNumber,5000,2000)
class MysteryComponent(Component):
    Description=''
    def __init__(self,description1):
        super(MysteryComponent,self).__init__('n/a','n/a',-1)
        self.Description=description1
    def getDescription(self):
        return self.Description
    
bob=MysteryComponent('Stupid')
print bob.getDescription()
print bob.getVersionNumber()
print bob.myTypeName

