# -*- coding: utf-8 -*-
from pprint import pprint
import pytest
from gmaps import Directions

api = Directions()


def test_simple_directions():
    results = api.directions("Warsaw, Poland", "Katowice, Poland")
    assert results[0]


def test_directions_lat_lon_tuples():
    results = api.directions((40.728783, -73.7897503),
                             (40.6497484, -73.97767999999999))
    assert results[0]


def test_directions_lat_lon_dicts():
    results = api.directions({"lat": 40.728783, "lon": -73.7897503},
                             {"lat": 40.6497484, "lon": -73.97767999999999})
    assert results[0]


def test_directions_lat_lon_google_formated():
    results = api.directions("40.728783,-73.7897503",
                             "40.6497484,-73.97767999999999")
    assert results[0]


def test_directions_lat_lon_some_object():
    class LatLon(object):
        def __init__(self, lat, lon):
            self.lat = lat
            self.lon = lon

    results = api.directions(LatLon(40.728783, -73.7897503),
                             LatLon(40.6497484, -73.97767999999999))
    assert results[0]


def test_directions_wrong_type():
    with pytest.raises(TypeError):
        # wrong list size
        api.directions((40.728783, -73.7897503, 3.434),
                                 (40.6497484, -73.97767999999999))
    with pytest.raises(TypeError):
        # no keys
        api.directions({}, {})
    with pytest.raises(TypeError):
        # unsupported type
        api.directions(2, 3)

