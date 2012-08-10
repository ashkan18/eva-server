'''
Created on Aug 6, 2012

@author: anasseri
'''

from pbs.data.parking_data import ParkingData

class ParkingService():
    
    def addParkingSellToUser(self,userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country ,
                       availableStart ,availableEnd ,
                       startDate ,endDate):
        parking_data = ParkingData()
        insertResponse = parking_data.addSellForUser(userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country ,
                       availableStart ,availableEnd ,
                       startDate ,endDate)
        
        return insertResponse;
    
    def getUsersParkingSells(self, userid):
        parking_data = ParkingData()
        return parking_data.getUsersSells(userid)