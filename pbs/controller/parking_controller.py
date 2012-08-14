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
def addSell():
    app.logger.debug("adding new sell for user")
    
    userId = None
    parkingName = None
    addressLine1 = None
    addressLine2 = None
    city = None
    state = None
    country = None
    availableStart = None
    availableEnd   = None
    startDate = None
    endDate = None

    try:
        userId = request.form['uid']
        parkingName = request.form['pname']
        addressLine1 = request.form['add1']
        addressLine2 = request.form['add2']
        city = request.form['city']
        state = request.form['state']
        country = request.form['cntry']
        availableStart = request.form['astart']
        availableEnd   = request.form['aend']
        startDate = request.form['sdate']
        endDate = request.form['edate']
    except:
        return jsonify(success=False, error="missing parameter")
    
    parkingSvc = ParkingService()
    
    insert_response = parkingSvc.addParkingSellToUser(userId ,parkingName ,
                                            addressLine1 ,addressLine2 ,city ,
                                            state ,country ,availableStart ,
                                            availableEnd ,startDate ,endDate)
    
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
    

    