'''
Created on Aug 6, 2012

@author: anasseri
'''

from pbs.data.parking_data import ParkingData

class ParkingService():
    
    def __init__(self, parking_data = ParkingData()):
        self.__parking_data = parking_data
        
    
    def addParkingToUser(self,userId ,parkingName ,addressLine1 ,addressLine2 ,city ,state ,country):
        insert_response = self.__parking_data.addParkinForUser(userId ,parkingName 
                                                               ,addressLine1 ,addressLine2 
                                                               ,city ,state ,country)
        return insert_response;
    
    def addParkingSellPeriod(self, parking_id, start_date, end_date, price_per_hour):
        assign_response = self.__parking_data.addParkingSellPeriod(parking_id, start_date, 
                                                                   end_date, price_per_hour)
        return assign_response
    
    def addParkingSellPeriodDay(self, sell_period_id, day, available_from, available_to): 
        add_parking_day_response = self.__parking_data.addParkingSellPeriodDay(sell_period_id, 
                                                                               day, available_from, 
                                                                               available_to)
        return add_parking_day_response
        
    def getUsersParkingSells(self, userid):
        parking_data = ParkingData()
        return parking_data.getUsersSells(userid)
    
    def getUsersParkingRents(self, userid):
        parking_data = ParkingData()
        return parking_data.getUsersRents(userid)