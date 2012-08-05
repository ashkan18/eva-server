'''
Created on Jul 26, 2012

@author: anasseri
'''

from pbs.data.account_data import AccountDb

class AccountService:
    account_db = None;
    def __init__(self):
        self.account_db = AccountDb()
        
        
    def login (self, username, password):
        return self.account_db.authenticate(username, password);
    
    def getUserInfo(self, user_id):
        return self.account_db.getUserInfo(user_id)
    
    def registerUser(self, username, password, firstname, lastname):
        return self.account_db.registerUser(username, password, firstname, lastname)