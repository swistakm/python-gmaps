# -*- coding: utf-8 -*-
from gmaps import Elevation
from .testutils import retry

elevation = Elevation(sensor=False)


@retry
def test_elevation_with_only_locations():
    locations = [(38.5, -120.2), (40.7, -120.95), (43.252, -126.453)]
    result = elevation.elevation(locations)
    assert len(result) == len(locations)


@retry
def test_elevation_with_samples():
    path = [(38.5, -120.2), (40.7, -120.95), (43.252, -126.453)]
    result = elevation.elevation(path, samples=10)
    assert len(result) == 10
