from sqlalchemy import create_engine
import datetime

class BaseData(object):
    def __init__(self):
        start = datetime.datetime.now()
        self.engine = create_engine('mysql://root:ashkinas@localhost/eva?charset=utf8&use_unicode=0')
        end = datetime.datetime.now()
        elapsed = end - start
        print("elapsed=" + str(elapsed))
