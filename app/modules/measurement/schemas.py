# encoding: utf-8
# pylint: disable=too-few-public-methods
"""
measurement schemas
------------
"""
from marshmallow import fields, Schema, post_load
from .models import Measurement


class MeasurementSchema(Schema):
    msg_id = fields.Int()
    start_time = fields.DateTime()
    device_id = fields.Int()
    mea_id = fields.Int()
    c1 = fields.Float()
    c2 = fields.Float()
    c3 = fields.Float()

    class Meta:
        #load_only = ("msg_id",)
        load_only = ("msg_id", "device_id", "mea_id")



    @post_load
    def make_Measurement(self, data):
        return Measurement(**data)

class MeaQuerySChema(Schema):
    "This calss used to validate the input parameters for query measurement"
    #dev_id = fields.Int(required=True, allow_none=False)
    dev_id = fields.List(fields.Int, required=True, allow_none=False)
    stime = fields.DateTime(required=False)
    etime = fields.DateTime(required=False)






