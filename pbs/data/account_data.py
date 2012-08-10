'''
Created on Jul 26, 2012

@author: anasseri
'''
from base_data import BaseData
from pbs import app

class AccountData(BaseData):
    
    '''
        This method authenticates the user
        based on username and password
    '''
    def authenticate(self, username, password):
        app.logger.debug('u=' + username + " pw=" + password)
        user_data = self.engine.execute("""SELECT id, 
                                                 firstname, 
                                                 lastname, 
                                                 email
                                           FROM users
                                           WHERE email=%s
                                           AND password = md5(%s)
                                           LIMIT 1""", username, password)
        return user_data.fetchone()
    
    
    '''
        This method getting user_id returns userinfo
    ''' 
    def getUserInfo(self, user_id):
        user_data = self.engine.execute("""SELECT id, 
                                                 firstname, 
                                                 lastname, 
                                                 email
                                           FROM users
                                           WHERE id=%s
                                           LIMIT 1""", user_id)
        return user_data.fetchone()
    
    '''
        This method getting username, firstname, lastname and password
        creates a new user
    '''
    def registerUser(self, username, password, firstname, lastname):
        try:
            data = self.engine.execute(""" INSERT INTO users(firstname, lastname, email, password)
                                    VALUES (%s, %s, %s, md5(%s))""", firstname, lastname, username, password)
            
            
            return data.lastrowid
        except:
            return False

    
    
    
    
    
    