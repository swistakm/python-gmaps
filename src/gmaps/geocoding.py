# -*- coding: utf-8 -*-
from gmaps.client import Client


class Geocoding(Client):
    GEOCODE_URL = "geocode/"

    def geocode(self, address=None, components=None, region=None,
                language=None, bounds=None, sensor=None):
        """Geocode given address. Geocoder can queried using address and/or
        components. Components when used with address will restrict your query
        to specific area. When used without address they act like more precise
        query. For full details see
        `Google docs <https://developers.google.com/maps/documentation/geocoding/>`_.

        :param address: address string
        :param components: ditc of components
        :param region: region code specified as a ccTLD ("top-level domain")
            two-character value, influences but not restricts query result
        :param language: the language in which to return results. For full list
            of laguages go to Google Maps API docs
        :param bounds: two-tuple of (latitude, longitude) pairs of bounding
            box. Influences but not restricts result (same as region parameter)
        :param sensor: override default client sensor parameter
        """  # noqa
        parameters = dict(
            address=address,
            components=components,
            language=language,
            sensor=sensor,
            region=region,

        )
        if bounds:
            parameters['bounds'] = "%f,%f|%f,%f" % (
                bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1])
        return self._make_request(self.GEOCODE_URL, parameters, "results")

    def reverse(self, lat, lon, language=None, sensor=None):
        """Reverse geocode with given latitude and longitude.

        :param lat: latitude of queried point
        :param lon: longitude of queried point
        :param language: the language in which to return results. For full
             list of laguages go to Google Maps API docs
        :param sensor: override default client sensor parameter

        .. note:: Google API allows to specify both latlng and address params
            but it makes no sense and would not reverse geocode your query, so
            here geocoding and reverse geocoding are separated
        """
        parameters = dict(
            latlng="%f,%f" % (lat, lon),
            language=language,
            sensor=sensor,
        )
        return self._make_request(self.GEOCODE_URL, parameters, "results")
