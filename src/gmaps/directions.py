# -*- coding: utf-8 -*-
from gmaps.client import Client


class Directions(Client):
    DIRECTIONS_URL = 'directions/'

    def directions(self, origin, destination, mode=None, alternatives=None,
                   waypoints=[], optimize_waypoints=False,
                   avoid=None, language=None, units=None,
                   region=None, departure_time=None,
                   arrival_time=None, sensor=None):
        """Get directions between locations

        :param origin: Origin location - string address; (latitude, longitude)
            two-tuple, dict with ("lat", "lon") keys or object with (lat, lon)
            attributes
        :param destination: Destination location - type same as origin
        :param mode: Travel mode as string, defaults to "driving".
            See `google docs details <https://developers.google.com/maps/documentation/directions/#TravelModes>`_
        :param alternatives: True if provide it has to return more then one
            route alternative
        :param waypoints: Iterable with set of intermediate stops,
            like ("Munich", "Dallas")
            `See google docs details under <https://developers.google.com/maps/documentation/javascript/reference#DirectionsRequest>`_
        :param optimize_waypoints: if true will attempt to re-order supplied
            waypoints to minimize overall cost of the route. If waypoints are
            optimized, the route returned will show the optimized order under
            "waypoint_order"
            `See google docs details under <https://developers.google.com/maps/documentation/javascript/reference#DirectionsRequest>`_
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
        """  # noqa
        if optimize_waypoints:
            waypoints.insert(0, "optimize:true")
        parameters = dict(
            origin=self.assume_latlon_or_address(origin),
            destination=self.assume_latlon_or_address(destination),
            mode=mode,
            alternatives=alternatives,
            waypoints=waypoints,
            avoid=avoid,
            language=language,
            units=units,
            region=region,
            departure_time=departure_time,
            arrival_time=arrival_time,
            sensor=sensor,
        )
        return self._make_request(self.DIRECTIONS_URL, parameters, "routes")
