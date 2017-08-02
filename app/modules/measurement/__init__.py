# encoding: utf-8
"""
measurements module
============
"""


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init users module.
    """
    from .resources import api, MeasurementAPI, LastDataAPI
    api.add_resource(MeasurementAPI, '/api/measurements/', endpoint='measurement')
    api.add_resource(LastDataAPI, '/api/last/', endpoint='gauge')