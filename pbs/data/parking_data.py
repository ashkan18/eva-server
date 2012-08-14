'''
Created on Aug 6, 2012

@author: anasseri
'''


from base_data import BaseData
from pbs import app

class ParkingData(BaseData):
    
    def addParkinForUser(self, userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country):
        try:
            user_data = self.engine.execute("""INSERT INTO parking_info
                                                (user_id ,name ,
                                                address_line1 ,address_line2 ,city ,
                                                state ,country)
                                               VALUES(%s, %s, %s, %s, %s, %s, %s) 
                                                """, userId ,parkingName ,
                                                addressLine1 ,addressLine2 ,city ,
                                                state ,country)
            return user_data.lastrowid
        except:
            return False

    def addParkingSellPeriod(self, parking_id, start_date, end_date, price_per_hour):
        try:
            user_data = self.engine.execute("""INSERT INTO sell_period
                                                (parking_id ,start_date ,
                                                end_date , price_per_hour)
                                               VALUES(%s, %s, %s, %s) 
                                                """, parking_id ,start_date ,
                                                end_date ,price_per_hour)
            return user_data.lastrowid
        except:
            return False

    def addParkingSellPeriodDay(self, parking_id, start_date, end_date, price_per_hour):
        try:
            user_data = self.engine.execute("""INSERT INTO sell_period
                                                (parking_id ,start_date ,
                                                end_date , price_per_hour)
                                               VALUES(%s, %s, %s, %s) 
                                                """, parking_id ,start_date ,
                                                end_date ,price_per_hour)
            return user_data.lastrowid
        except:
            return False

    def getUsersSells(self, userid):
        app.logger.debug('user=' + userid)
        user_data = self.engine.execute("""SELECT * 
                                        FROM sells
                                        WHERE userid = %s""", userid)
        return user_data.fetchone()
    
    def getUsersRents(self, userid):
        app.logger.debug("user" + userid)
        user_data = self.engine.excute(""" SELECT *
                                            FROM rents
                                            WHERE userid = %s""", userid)
        return user_data;
    
    
