# -*- coding: utf-8 -*-
from gmaps.client import Client


class Directions(Client):
    DIRECTIONS_URL = 'directions/'

    @staticmethod
    def latlon_or_address(place):
        if isinstance(place, basestring):
            output = place
        elif isinstance(place, dict):
            try:
                output = "%f,%f" % (place["lat"], place["lon"])
            except KeyError:
                raise TypeError("%s is invalid place object" % str(place))
        elif hasattr(place, "__iter__") and len(place) == 2:
            output = "%f,%f" % (place[0], place[1])
        elif hasattr(place, "lat") and hasattr(place, "lon"):
            output = "%f,%f" % (place.lat, place.lon)
        else:
            raise TypeError("%s is invalid place object" % str(place))
        return output

    def directions(self, origin, destination, mode=None, alternatives=None,
                   avoid=None, language=None, units=None,
                   region=None, departure_time=None, arrival_time=None):
        parameters = dict(
            origin=self.latlon_or_address(origin),
            destination=self.latlon_or_address(destination),
            mode=mode,
        )
        return self._make_request(self.DIRECTIONS_URL, parameters, "routes")
