# -*- coding: utf-8 -*-
from gmaps.polyline import encode

# examplez taken from Google Maps API documentation
DECODED_EXAMPLE = [(38.5, -120.2), (40.7, -120.95), (43.252, -126.453)]
ENCODED_EXAMPLE = '_p~iF~ps|U_ulLnnqC_mqNvxq`@'


def almost_equal(a, b, err):
    return abs(a - b) < err


def test_encode():
    assert encode(DECODED_EXAMPLE) == ENCODED_EXAMPLE
