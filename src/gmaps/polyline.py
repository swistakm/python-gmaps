# -*- coding: utf-8 -*-
"""
Polyline encoding inspired with following Gist:

    https://gist.github.com/signed0/2031157

With few tweaks and improvements
"""

from itertools import chain


def encode(locations):
    """
    :param locations: locations list containig (lat, lon) two-tuples
    :return: encoded polyline string
    """
    encoded = (
        (_encode_value(lat, prev_lat), _encode_value(lon, prev_lon))
        for (prev_lat, prev_lon), (lat, lon)
        in _iterate_with_previous(locations, first=(0, 0))
    )
    encoded = chain.from_iterable(encoded)
    return ''.join(c for r in encoded for c in r)


def _iterate_with_previous(iterable, first=None):
    prev = first
    for item in iterable:
        yield prev, item
        prev = item


def _encode_value(value, prev):
    # note: rounding is important
    value = int(round((value - prev) * 1e5))
    value = ~(value << 1) if value < 0 else (value << 1)
    chunks = _split_into_chunks(value)
    return (chr(chunk + 63) for chunk in chunks)


def _split_into_chunks(value):
    while value >= 32:  # 2^5, while there are at least 5 bits
        # first & with 2^5-1, zeros out all the bits other than the first five
        # then OR with 0x20 if another bit chunk follows
        yield (value & 31) | 0x20
        value >>= 5
    yield value
