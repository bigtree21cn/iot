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

    @post_load
    def make_Measurement(self, data):
        m = Measurement()
        m.__dict__.update(**data)
        return m






