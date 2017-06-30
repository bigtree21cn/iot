from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Measurement

DB_CONNECTION_STRING='mysql+pymysql://root:123456@10.140.1.17/iot?charset=utf8'
engine = create_engine(DB_CONNECTION_STRING, echo=True)
DBSession = sessionmaker(bind=engine)


app = Flask(__name__)
api = Api(app)

def mytest():
    session = DBSession()
    #query = session.query(Measurement).filter(Measurement.msg_id == 1)
    #print(query)
    #obj = query.first()
    obj = Measurement.Measurement()
    print(obj.to_serializable_dict())


class MeasurementAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('msg_id', type=int, help='The message id')
        args = parser.parse_args()
        msg_id = args['msg_id']
        session = DBSession()
        print (msg_id)

        query = session.query(Measurement).filter(Measurement.msg_id == msg_id)
        print (query)
        mea = query.first()
        if mea is None:
            return "Nothing found", 200
        else:
            return jsonify(mea.to_serializable_dict())

    def put(self):
        pass

    def post(self):
        json_data = request.get_json(force=True)
        return jsonify(json_data)

api.add_resource(MeasurementAPI, '/measurements/', endpoint = 'measurement')


if __name__ == '__main__':
    mytest()
    #app.run(host='0.0.0.0', port=9090, debug=True)
