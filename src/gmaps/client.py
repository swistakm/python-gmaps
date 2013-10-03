# -*- coding: utf-8 -*-
from copy import copy
import urlparse

import requests

import status
import errors


class Client(object):
    """Base class for Google Maps API endpoints

    :param sensor: boolean value indicating if application is using sensor
        (such as a GPS locator) to determine the user's location.
    :param api_key: google business API key
    :param use_https: boolean indicating if https should be use to make requests

    .. note:: Google API won't allow you to make plain http requests with
        API key. If you would like to use api_key you should use https too.
    """
    BASE_API_HTTP_URL = "http://maps.googleapis.com/maps/api/"
    BASE_API_HTTPS_URL = "https://maps.googleapis.com/maps/api/"

    def __init__(self, sensor=False, api_key=None, use_https=True):


        self.sensor = sensor
        self.api_key = api_key
        if use_https:
            self.base = self.BASE_API_HTTPS_URL
        else:
            self.base = self.BASE_API_HTTP_URL

        self.use_https = use_https

    @staticmethod
    def _serialize_parameters(parameters):
        """Serialize some parameters to match python native types with formats
        specified in google api docs like:
        * True/False -> "true"/"false",
        * {"a": 1, "b":2} -> "a:1|b:2"

        :type parameters: dict oif query parameters
        """

        for key, value in parameters.iteritems():
            if isinstance(value, bool):
                parameters[key] = "true" if value else "false"
            if isinstance(value, dict):
                parameters[key] = "|".join(
                    ("%s:%s" % (k, v) for k, v in value.iteritems()))
        return parameters

    def _make_request(self, url, parameters, result_key):
        """Make http/https request to Google API.

        Method prepares url parameters, drops None values, and gets default
        values. Finally makes request using protocol assigned to client and
        returns data.

        :param url: url part - specifies API endpoint
        :param parameters: dictionary of url parameters
        :param result_key: key in output where result is expected
        """
        url = urlparse.urljoin(urlparse.urljoin(self.base, url), "json")

        #drop all None values and use defaults if not set
        parameters = {key: value for key, value in parameters.iteritems() if
                      value is not None}
        parameters.setdefault("sensor", self.sensor)
        parameters = self._serialize_parameters(parameters)
        if self.api_key:
            parameters["key"] = self.api_key

        raw_response = requests.get(url, params=parameters)
        response = raw_response.json()

        if response["status"] == status.OK:
            return response[result_key]
        else:
            response["url"] = raw_response.url
            raise errors.EXCEPTION_MAPPING.get(response["status"],
                                               errors.GmapException)(response)
