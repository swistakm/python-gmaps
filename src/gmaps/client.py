# -*- coding: utf-8 -*-
import urlparse

import requests

class Client(object):
    BASE_API_HTTP_URL = "http://maps.googleapis.com/maps/api/"
    BASE_API_HTTPS_URL = "https://maps.googleapis.com/maps/api/"

    def __init__(self, api_key=None, api_secret=None, use_https=True):
        self.api_key = api_key
        self.api_secret = api_secret
        if use_https:
            self.base = self.BASE_API_HTTPS_URL
        else:
            self.base = self.BASE_API_HTTP_URL

        self.use_https = use_https

    def _make_request(self, url, parameters):
        url = urlparse.urljoin(urlparse.urljoin(self.base, url), "json")
        return requests.get(url, params=parameters).json()
