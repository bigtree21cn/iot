
# encoding: utf-8
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
RESTful API User resources
--------------------------
"""

import logging

from flask import jsonify, request, abort, make_response
from flask_restful import Resource, reqparse

from app.extensions import api
from .models import db, Measurement
from .schemas import MeasurementSchema

class MeasurementAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('msg_id', type=int, help='The message id')
        args = parser.parse_args()
        msgid = args['msg_id']
        print (msgid)
        return Measurement.query.filter_by(msg_id=msgid).first()


        '''
        query = session.query(models).filter(models.msg_id == msg_id)
        print (query)
        mea = query.first()
        if mea is None:
            return "Nothing found", 200
        else:
            return jsonify(mea.to_serializable_dict())
        '''

    def put(self):
        pass

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return make_response(jsonify({'message': "input incorrect data"}), 400)
        measSchema = MeasurementSchema()
        print (json_data)
        data, error =  measSchema.load(json_data)
        if len(0) > 0:
            jsonify({'message': "failed"}, 400)
        mea = Measurement(**data)
        db.session.add(mea)
        db.session.commit()
        return jsonify({'message' : 'sucessfully'}, 201)
