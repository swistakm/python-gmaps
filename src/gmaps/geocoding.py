# -*- coding: utf-8 -*-
from client import Client

class Geocoding(Client):
    GEOCODE_URL = "geocode/"

    def geocode(self, address=None, components=None, region=None, language=None, bounds=None, sensor=None):
        parameters=dict(
            address=address,
            components=components,
            language=language,
            sensor=sensor,
            region=region,

        )
        if bounds:
            parameters['bounds'] = "%f,%f|%f,%f" % (bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1])
        return self._make_request(self.GEOCODE_URL, parameters, "results")

    def reverse(self, lat, lon, language=None, sensor=None):
        parameters = dict(
            latlng="%f,%f" % (lat, lon),
            language=language,
            sensor=sensor,
        )
        return self._make_request(self.GEOCODE_URL, parameters, "results")