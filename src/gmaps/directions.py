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
        """Get directions between locations

        :param origin: Origin location - string address; (latitude, longitude)
            two-tuple, dict with ("lat", "lon") keys or object with (lat, lon)
            attributes
        :param destination: Destination location - type same as origin
        :param mode: Travel mode as string, defaults to "driving".
            See `google docs details <https://developers.google.com/maps/documentation/directions/#TravelModes>`_
        :param alternatives: True if provide it has to return more then one
            route alternative
        :param avoid: Iterable with set of restrictions,
            like ("tolls", "highways"). For full list refer to
            `google docs details <https://developers.google.com/maps/documentation/directions/#Restrictions>`_
        :param language: The language in which to return results.
            See `list of supported languages <https://developers.google.com/maps/faq#languagesupport>`_
        :param units: Unit system for result. Defaults to unit system of
            origin's country.
            See `google docs details <https://developers.google.com/maps/documentation/directions/#UnitSystems>`_
        :param region: The region code. Affects geocoding of origin and
            destination (see `gmaps.Geocoding.geocode` region parameter)
        :param departure_time: Desired time of departure as
            seconds since midnight, January 1, 1970 UTC
        :param arrival_time: Desired time of arrival for transit directions as
            seconds since midnight, January 1, 1970 UTC.
        """
        parameters = dict(
            origin=self.latlon_or_address(origin),
            destination=self.latlon_or_address(destination),
            mode=mode,
            alternatives=alternatives,
            avoid=avoid,
            language=language,
            units=units,
            region=region,
            departure_time=departure_time,
            arrival_time=arrival_time,
        )
        return self._make_request(self.DIRECTIONS_URL, parameters, "routes")
