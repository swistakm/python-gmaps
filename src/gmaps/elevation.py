# -*- coding: utf-8 -*-
from gmaps.client import Client
from gmaps.polyline import encode


class Elevation(Client):
    ELEVATION_URL = 'elevation/'

    def elevation(self, locations=None, samples=None, sensor=False):
        """

        :param locations: list of lat/lon positions
        :param samples: specifies the number of sample points along a path
            for which to return elevation data. The samples parameter divides
            the given path into an ordered set of equidistant points along the
            path. If not set then the result will be elevation for every point
            in list of locations.
        :return:
        """

        parameters = {
            # use different key for providing coordinates depending
            # on `samples` parameter (different method)
            'path' if samples else 'locations': 'enc:' + encode(locations),
            'samples': samples,
            'sensor': sensor,
        }
        parameters.update(sensor=sensor)

        return self._make_request(self.ELEVATION_URL, parameters, "results")
