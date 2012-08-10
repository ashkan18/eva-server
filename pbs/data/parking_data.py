'''
Created on Aug 6, 2012

@author: anasseri
'''


from base_data import BaseData
from pbs import app

class ParkingData(BaseData):
    
    '''
        This method authenticates the user
        based on username and password
    '''
    def addSellForUser(self, userId ,parkingName ,
                       addressLine1 ,addressLine2 ,
                       city ,state ,country ,
                       availableStart ,availableEnd ,
                       startDate ,endDate):
        user_data = self.engine.execute("""INSERT INTO SELLS
                                            (userId ,parkingName ,
                                            addressLine1 ,addressLine2 ,city ,
                                            state ,country ,availableStart ,
                                            availableEnd ,startDate ,endDate)
                                           VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                                            """, userId ,parkingName ,
                                            addressLine1 ,addressLine2 ,city ,
                                            state ,country ,availableStart ,
                                            availableEnd ,startDate ,endDate)
        return user_data.fetchone()

    def getUsersSells(self, userid):
        app.logger.debug('user=' + userid)
        user_data = self.engine.execute("""SELECT * 
                                        FROM sells
                                        WHERE userid = %s""", userid)
        return user_data.fetchone()
    
    
