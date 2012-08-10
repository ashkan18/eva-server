'''
Created on Jul 28, 2012

@author: anasseri
'''
from flask import request
from flask import jsonify
from pbs import app
from pbs.services.account_service import AccountService
from pbs.helpers.auth_helper import login_required, validate_request

@app.route("/user/login", methods=['POST'])
def login():
    app.logger.debug("login requested")
    app.logger.debug(request.form['un'])
    app.logger.debug(request.form['pw'])
    
    accSvc = AccountService()
    
    login_response = accSvc.login(request.form['un'], request.form['pw'])
    if login_response is not None:
        return jsonify(success=True, response=login_response['id'], 
                       firstname=login_response['firstname'],
                       lastname=login_response['lastname'])
    else:
        return jsonify(success=False, error='User not authenticate')


@app.route("/user/reg", methods=['POST'])
@validate_request('email', 'pw', 'firstname', 'lastname')
def register():
    app.logger.debug("register")
    acc_svc = AccountService()
    register_response = acc_svc.registerUser(request.form['email'], 
                                             request.form['pw'], request.form['firstname'], 
                                             request.form['lastname'])
    if register_response == False:
        return jsonify(success=False)
    else:
        return jsonify(success=True, response=register_response,
                       firstname=request.form['firstname'], lastname=request.form['lastname']) 


@app.route("/user/<int:userid>", methods=['GET'])
@login_required()
def getUserInfo(userid):
    acc_svc = AccountService()
    user_info = acc_svc.getUserInfo(userid)
    return jsonify(success=True,
                   userid=user_info['id'], 
                   firstName=user_info['firstName'], lastName=user_info['lastName'])
    #return jsonify(acc_svc.)
    
    

    