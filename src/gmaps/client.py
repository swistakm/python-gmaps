# -*- coding: utf-8 -*-
from copy import copy
import urlparse

import requests

import status
import errors

class Client(object):
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

    def _serialize_parameters(self, parameters):
        """
        :type parameters: dict
        """

        for key, value in parameters.iteritems():
            if isinstance(value, bool):
                parameters[key] = "true" if value else "false"
            if isinstance(value, dict):
                parameters[key] = "|".join(("%s:%s" % (k, v) for k,v in value.iteritems()))
        return parameters

    def _make_request(self, url, parameters):
        url = urlparse.urljoin(urlparse.urljoin(self.base, url), "json")

        #drop all None values and use defaults if not set
        parameters = {key: value for key, value in parameters.iteritems() if value is not None}
        parameters.setdefault("sensor", self.sensor)
        parameters = self._serialize_parameters(parameters)
        if self.api_key:
            parameters["key"] = self.api_key

        raw_response = requests.get(url, params=parameters)
        response = raw_response.json()

        if response["status"] == status.OK:
            return response["results"]
        else:
            response["url"] = raw_response.url
            raise errors.EXCEPTION_MAPPING.get(response["status"], errors.GmapException)(response)
