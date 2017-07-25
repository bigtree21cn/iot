
# encoding: utf-8
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
RESTful API User resources
--------------------------
"""

import logging

from flask import jsonify, request, abort, make_response, current_app
from flask_restful import Resource, reqparse
from marshmallow import ValidationError
from datetime import datetime

from app.extensions import auth, api
from .models import db, Measurement
from .schemas import MeasurementSchema, MeaQuerySChema


class MeasurementAPI(Resource):
    '''
    example: http://127.0.0.1:5000/api/measurements/?dev_id=1&dev_id=0&stime=2017-07-11T03:17:44.332&etime=2017-07-21T03:17:44.332
    '''
    @auth.login_required
    def get(self):
        args = dict(request.args)   # convert to dictionary, and each value is a list
        if 'etime' in args and 'stime' not in args:
            del args['etime']
        if 'stime' in args and 'etime' not in args:
            args['etime'] = [str(datetime.utcnow())]
        if 'stime' in args:   # truncate the date list to a value
            args['stime'] = args['stime'][0]
            args['etime'] = args['etime'][0]
        print(args)
        try:
            MeaQuerySChema(strict=True).validate(args)
        except ValidationError as error:
            print(error.messages)
            return make_response(jsonify(error.messages), 400)

        #meas = Measurement.query.filter(Measurement.device_id==1).all()
        #return make_response(jsonify(MeasurementSchema(many=True).dump(obj=meas, many=True)), 200)

        if 'stime' in args:
            meas = Measurement.query.filter(Measurement.device_id.in_(args['dev_id']),
                                               Measurement.start_time.between(args['stime'], args['etime'])).all()
        else:
            meas = Measurement.query.filter(Measurement.device_id.in_(args['dev_id'])).all()
        return make_response(jsonify(MeasurementSchema(many=True).dump(obj=meas)), 200)


    def put(self):
        pass

    '''
    example: 
    { "msg_id":  7, 
      "start_time": "2017-07-12T03:17:44.332",
      "device_id": 1,
      "mea_id": 1,
      "c1": 0.5,
      "c2": 1.5,
      "c3": 22
    }
    '''
    @auth.login_required
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return make_response(jsonify({'message': "input incorrect data"}), 400)
        try:
            data, error = MeaQuerySChema(strict=True).validate(json_data)
        except ValidationError as error:
            print(error.messages)
            return make_response(jsonify(error.messages), 400)

        try:
            data, error =  MeasurementSchema(partial=True).load(json_data, strict=True)
        except ValidationError as error:
            #current_app.logger.error(error.messages)
            return make_response(jsonify(error.messages), 400)

        print (json_data)
        print (data)
        print (error)
        db.session.add(data)
        db.session.commit()
        return make_response(jsonify({'message' : 'sucessfully'}), 201)
