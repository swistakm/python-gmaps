# -*- coding: utf-8 -*-
import pytest
from gmaps import Directions, errors
from .testutils import retry

api = Directions()


@retry
def test_simple_directions():
    results = api.directions("Warsaw, Poland", "Katowice, Poland")
    assert results[0]


@retry
def test_directions_lat_lon_tuples():
    results = api.directions((40.728783, -73.7897503),
                             (40.6497484, -73.97767999999999))
    assert results[0]


@retry
def test_directions_lat_lon_dicts():
    results = api.directions({"lat": 40.728783, "lon": -73.7897503},
                             {"lat": 40.6497484, "lon": -73.97767999999999})
    assert results[0]


@retry
def test_directions_lat_lon_google_formated():
    results = api.directions("40.728783,-73.7897503",
                             "40.6497484,-73.97767999999999")
    assert results[0]


@retry
def test_directions_lat_lon_some_object():
    class LatLon(object):
        def __init__(self, lat, lon):
            self.lat = lat
            self.lon = lon

    results = api.directions(LatLon(40.728783, -73.7897503),
                             LatLon(40.6497484, -73.97767999999999))
    assert results[0]


@retry
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


@retry
def test_directions_mode():
    results = api.directions(
        "Warsaw, Poland", "Katowice, Poland",
        mode="driving",
    )

    for step in results[0]["legs"][0]["steps"]:
        assert step['travel_mode'] == u"DRIVING"

    results = api.directions(
        u"Łubinowa 1D, Wrocław", u"Gajowa 14, Wrocław",
        mode="walking",
    )
    for step in results[0]["legs"][0]["steps"]:
        assert step['travel_mode'] == u"WALKING"

    results = api.directions(
        u"Łubinowa 1D, Wrocław", u"Gajowa 14, Wrocław",
        mode="bicycling",
    )
    for step in results[0]["legs"][0]["steps"]:
        assert step['travel_mode'] == u"BICYCLING"


@retry
def test_directions_mode_transit_invalid_request():
    """test that mode=transit raises exception when no departure or
    arrival time is set
    """
    with pytest.raises(errors.InvalidRequest):
        api.directions(u"Warsaw, Poland", u"Katowice, Poland", mode="transit")


@retry
def test_directions_mode_transit():
    from datetime import datetime

    try:
        api.directions(
            u"Warsaw, Poland", u"Poznań, Poland",
            mode="transit", departure_time=int(datetime.utcnow().strftime("%s"))
        )

    except errors.NoResults:
        # just test if it doesn't raise any other exceptions, if its
        # ZERO_RESULTS it's - we know that request was ok
        pass

    try:
        api.directions(
            u"Warsaw, Poland", u"Poznań, Poland",
            mode="transit", arrival_time=int(datetime.utcnow().strftime("%s"))
        )
    except errors.NoResults:
        pass


@retry
def test_directions_alternatives():
    with_alts = api.directions(u"Warsaw, Poland", u"Katowice, Poland",
                               alternatives=True)
    without_alts = api.directions(u"Warsaw, Poland", u"Katowice, Poland",
                                  alternatives=False)
    assert len(with_alts) > 1
    assert len(without_alts) == 1


@retry
def test_directions_language():
    pl = api.directions(u"Warsaw, Poland", u"Katowice, Poland", language='pl')
    assert u"Polska" in str(pl) and u"Poland" not in str(pl)
    en = api.directions(u"Warsaw, Poland", u"Katowice, Poland", language='en')
    assert u"Polska" not in str(en) and u"Poland" in str(en)


@retry
def test_directions_units():
    metric = api.directions(u"Warsaw, Poland", u"Katowice, Poland",
                            units="metric")[0]['legs'][0]["distance"]
    imperial = api.directions(u"Warsaw, Poland", u"Katowice, Poland",
                              units="imperial")[0]['legs'][0]["distance"]

    # text is different
    assert u"km" in metric["text"]
    assert u"mi" in imperial["text"]
    # but value is the same (in meters)
    assert metric["value"] == imperial["value"]

@retry
def test_array_serialization():
    tolls_highways = api.directions('paris', 'berlin', 
                                    avoid=('tolls', 'highways'))
    tolls_highways_dur = tolls_highways[0]['legs'][0]['duration']

    highways_tolls = api.directions('paris', 'berlin', 
                                    avoid=('highways', 'tolls'))
    highways_tolls_dur = highways_tolls[0]['legs'][0]['duration']
    assert tolls_highways_dur == highways_tolls_dur


@retry
def test_waypoints():
    no_waypoints_legs = len(api.directions('paris', 'berlin')[0]['legs'])
    one_waypoint_legs = len(api.directions('paris', 'berlin', 
                                           waypoints=['munich'])[0]['legs'])
    two_waypoints_legs = len(api.directions('paris', 'berlin', 
                             waypoints=['munich', 'moscow'])[0]['legs'])
    assert no_waypoints_legs == 1
    assert one_waypoint_legs == 2
    assert two_waypoints_legs == 3

@retry
def test_waypoint_optimization():
    non_optimized = api.directions('Los Angeles', 'New York', 
                                  waypoints=['Dallas', 'Bangor', 'Phoenix'])
    optimized = api.directions('Los Angeles', 'New York', 
                               waypoints=['Dallas', 'Bangor', 'Phoenix'],
                               optimize_waypoints=True)
    assert optimized[0]['waypoint_order'] == [2, 0, 1] 
    assert non_optimized[0]['waypoint_order'] == [0, 1, 2]
