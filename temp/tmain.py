import threading
import sys
import os
import sqlite3
import time

#from concurrent.futures import ThreadPoolExecutor
#from concurrent.futures import as_completed

dbfile = "./mydb.db"

class A1:
    def create_db(self):

        if os.path.isfile(dbfile):
            os.remove(dbfile)

        with sqlite3.connect(dbfile) as c:
            try:
                c.execute('''CREATE TABLE mytable
                        (Time DATETIME, Id INTEGER, remark VARCHAR(12))''')
            except Exception as ex:
                print (ex)
                exit(1)

    def inserter(self, id):
        with sqlite3.connect(dbfile) as conn:
            try:
                conn.execute("INSERT INTO mytable VALUES(%d, %d, '%s')" % (time.time(), id, "aaa"))
            except Exception as ex:
                print(ex)

'''
    def main(self, ids):
        self.create_db()
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.inserter, id) for id in ids]
        for future in as_completed(futures):
            print(future.result())
'''

from flask import  Flask, jsonify
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, String, Integer
#from flask_marshmallow import Marshmallow, Schema
from marshmallow import Schema, pre_load, fields




app1 = Flask("test app")
db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class AuthorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

    @pre_load()
    def process_name(self, data):
        name  = data.get('name')
        if name:
            data['name'] = name + 'abcedefg'
        else:
            data['name'] = "nothing found"
        return data

user_schame = AuthorSchema()
users_schema=AuthorSchema(many=True)



if __name__ == "__main__":
    usr1 = Author(id=1, name="lihuaming")
    usr2 = Author(id=2, name="jeffrey")
    users = [usr1, usr2]

    data = users_schema.dump(users).data
    print (data)

    users2 = users_schema.load(data, many=True)
    print (users2)

    from app.modules.measurement import models
    from app.modules.measurement import schemas
    from datetime import datetime
    mea = models.Measurement()
    mea.device_id = 1
    mea.mea_id = 11
    mea.msg_id = 111
    mea.start_time = datetime.now()
    mea.c1 = 100
    mea.c2 = 200
    mea.c3 = 300

    mea_schema = schemas.MeasurementSchema()
    print (mea_schema.dump(mea).data)






    #ids = range(1,2000)
    #main(ids)



