import jsonpickle
import time
import datetime


class MeasurementRaw(object):
    def __init__(self):
        self._start_time = datetime.datetime.now()
        self._device_id = ""
        self._mea_id = ""
        self._c1 = None
        self._c2 = None
        self._c3 = None

    @property
    def start_time(self):
        """
        The start_time property - the getter
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        The start_time - the setter
        """
        self._start_time = value

    @property
    def device_id(self):
        """
        The device_id property - the getter
        """
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        """
        The device_id - the setter
        """
        self._device_id = value

    @property
    def mea_id(self):
        """
        The mea_id property - the getter
        """
        return self._mea_id

    @mea_id.setter
    def mea_id(self, value):
        """
        The mea_id - the setter
        """
        self._mea_id = value

    @property
    def c1(self):
        """
        The c1 property - the getter
        """
        return self._c1

    @c1.setter
    def c1(self, value):
        """
        The c1 - the setter
        """
        self._c1 = value

    @property
    def c2(self):
        """
        The c2 property - the getter
        """
        return self._c2

    @c2.setter
    def c2(self, value):
        """
        The c2 - the setter
        """
        self._c2 = value

    @property
    def c3(self):
        """
        The c3 property - the getter
        """
        return self._c3

    @c3.setter
    def c3(self, value):
        """
        The c3 - the setter
        """
        self._c3 = value

    def to_jason(self):
        return jsonpickle.encode(self)

    @staticmethod
    def from_json(self, string):
        """

        :param self:
        :param string:
        :return: the Measurement object instance constructed by the string
        """
        return jsonpickle.decode(string)


obj = MeasurementRaw()
obj.start_time = datetime.datetime.now()
obj.device_id = 1
obj.mea_id = 100
obj.c1 = 12
obj.c2 = 56
obj.c3 = 33

frozen = jsonpickle.encode(obj)
obj2 = jsonpickle.decode(frozen)
print(frozen)
print (obj2)
assert obj.device_id == obj2.device_id
obj2.f
print (isinstance(obj2, MeasurementRaw))