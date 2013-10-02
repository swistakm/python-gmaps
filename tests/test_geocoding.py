# -*- coding: utf-8 -*-
import pytest
from pprint import pprint

from gmaps import errors

from gmaps.geocoding import Geocoding

geocoding = Geocoding(sensor=False)

def test_geocode():
    results = geocoding.geocode(u"Hubska")
    assert results
    assert len(results) > 0

def test_geocode_override_sensor():
    results = geocoding.geocode(u"Wrocław, Hubska", sensor=True)
    assert results
    assert len(results) > 0

def test_geocode_components_filters():
    """Test if querying with same route but different component filtering returns different locations"""
    # both these cities has this street
    results1 = geocoding.geocode(u"Łubinowa", components={"locality":"Wrocław"})
    results2 = geocoding.geocode(u"Łubinowa", components={"locality":"Warszawa"})

    assert results1[0]['geometry']['location'] != results2[0]['geometry']['location']

def test_geocode_components_without_address():
    """Test if querying explicitely set components returns same location like with string address"""
    components = {"route": "Łubinowa", "locality": "Wrocław"}
    address = ",".join(components.values())

    results_with_address = geocoding.geocode(components=components)
    results_without_address = geocoding.geocode(address)
    assert results_with_address[0]['geometry']['location'] == results_without_address[0]['geometry']['location']

def test_geocode_no_results_exception():
    components = {"administrative_area": "TX", "country": "FR"}
    with pytest.raises(errors.NoResults):
        geocoding.geocode(components)

def test_reverse():
    results = geocoding.reverse(lat=51.213, lon=21.213)
    assert results
    assert len(results) > 0
    assert results[0]['formatted_address']

def test_reverse_override_sensor():
    results = geocoding.reverse(lat=51.213, lon=21.213, sensor=True)
    assert results
    assert len(results) > 0

def test_reverse_language():
    results = geocoding.reverse(lat=51.213, lon=21.213, language='pl')
    assert results
    # given lat lon are position somwhere in poland so test if there is 'Polska' in
    # in formatted_address of first result
    assert 'Polska' in results[0]['formatted_address']

def test_exception_when_sensor_bad():
    with pytest.raises(errors.GmapException):
        response = geocoding.reverse(lat=51.213, lon=21.213, sensor="foo")

    with pytest.raises(errors.GmapException):
        response = geocoding.geocode(u"Wrocław, Hubska", sensor="foo")