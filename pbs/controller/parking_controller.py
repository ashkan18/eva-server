'''
Created on Aug 6, 2012

@author: anasseri
'''


from flask import request
from flask import jsonify
from pbs import app
from pbs.services.parking_service import ParkingService
from pbs.helpers.auth_helper import login_required

@app.route("/sell/", methods=['POST'])
def addParking():
    app.logger.debug("adding new sell for user")
    
    userId = None
    parkingName = None
    addressLine1 = None
    addressLine2 = None
    city = None
    state = None
    country = None
    
    try:
        userId = request.form['uid']
        parkingName = request.form['pname']
        addressLine1 = request.form['add1']
        addressLine2 = request.form['add2']
        city = request.form['city']
        state = request.form['state']
        country = request.form['cntry']
    except:
        return jsonify(success=False, error="missing parameter")
    
    parkingSvc = ParkingService()
    
    insert_response = parkingSvc.addParkingToUser(userId, parkingName, addressLine1, addressLine2, city, state, country)
    
    if insert_response is not None:
        return jsonify(success=True)
    else:
        return jsonify(success=False, error='there was problem in adding this sell')


@app.route("/parking/period", methods=['POST'])
def addParkingSellPeriod():
    app.logger.debug("adding new sell for user")
    
    parking_id = None
    start_date = None
    end_date   = None
    price_per_hour = None
    
    try:
        parking_id = request.form['pid']
        start_date = request.form['start']
        end_date   = request.form['end']
        price_per_hour = request.form['pph']
    except:
        return jsonify(success=False, error="missing parameter")
    
    parkingSvc = ParkingService()
    
    insert_response = parkingSvc.addParkingSellPeriod(parking_id, start_date, end_date, price_per_hour)
    
    if insert_response is not None:
        return jsonify(success=True)
    else:
        return jsonify(success=False, error='there was problem in adding this sell')

@app.route("/parking/period/day", methods=['POST'])
def addParkingSellPeriodDay():
    app.logger.debug("adding new sell for user")
    
    sell_period_id = None
    day            = None
    available_from = None
    available_to   = None
    
    try:
        sell_period_id = request.form['spid']
        day = request.form['day']
        available_from   = request.form['from']
        available_to = request.form['to']
    except:
        return jsonify(success=False, error="missing parameter")
    
    parkingSvc = ParkingService()
    
    insert_response = parkingSvc.addParkingSellPeriodDay(sell_period_id, day, available_from, available_to) 
    if insert_response is not None:
        return jsonify(success=True)
    else:
        return jsonify(success=False, error='there was problem in adding this sell')

@app.route("/parking/sells/<int:userid>", methods=['GET'])
@login_required()
def getUsersSells(userid):
    if userid is not None:
        parking_service = ParkingService()
        return jsonify(success=True, response=parking_service.getUsersParkingSells(userid))
    else:
        return jsonify(success=False, error="Missing userid in request")
    

@app.route("/parking/rents/<int:userid>", methods=['GET'])
@login_required()
def getUsersRents(userid):
    if userid is not None:
        parking_service = ParkingService()
        return jsonify(success=True, response=parking_service.getUsersParkingRents(userid))
    else:
        return jsonify(success=False, error="Missing userid in request")
    

    