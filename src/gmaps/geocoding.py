# -*- coding: utf-8 -*-
from client import Client

class Geocode(Client):
    GEOCODE_URL = "geocode/"

    def __init__(self, components=None, sensor=None, **kwargs):
        super(Geocode, self).__init__(**kwargs)
        self.components = components
        self.sensor = sensor

    def geocode(self, address, **kwargs):
        parameters=dict(
            address=address,
            components=self.components,
            sensor=self.sensor,
        )
        parameters.update(kwargs)
        return self._make_request(self.GEOCODE_URL, parameters)

    def reverse_geocode(self, lat, lon, **kwargs):
        parameters = dict(
            latlng="%s,%s" % (lat, lon)
        )
        parameters.update(kwargs)
        return self._make_request(self.GEOCODE_URL, parameters)