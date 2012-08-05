'''
Created on Jul 28, 2012

@author: anasseri
'''
from flask import request
from flask import jsonify
from functools import wraps
from pbs import app

#makes sure user session exist and is valid
def login_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                token = request.form['token']
            except:
                app.logger.debug("token is missing in the request, invalid call")
                return jsonify(error="missing token or session expired")
            ret = f(*args, **kwargs)
            return ret
    
        return decorated_function
    return decorator
