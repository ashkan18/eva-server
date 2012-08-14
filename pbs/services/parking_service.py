'''
Created on Aug 6, 2012

@author: anasseri
'''

from pbs.data.parking_data import ParkingData

class ParkingService():
    
    def addParkingToUser(self,userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country, start_date, end_date):
        parking_data = ParkingData()
        insert_response = parking_data.addSellForUser(userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country, start_date, end_date)
        
        return insert_response;
    
    def assignFreeTimeToParking(self, parking_id, day_of_week, price_per_hour):
        parking_data = ParkingData()
        assign_response = parking_data.assign_free_time_to_parking()
        return assign_response
        
    
    def getUsersParkingSells(self, userid):
        parking_data = ParkingData()
        return parking_data.getUsersSells(userid)
    
    def getUsersParkingRents(self, userid):
        parking_data = ParkingData()
        return parking_data.getUsersRents(userid)