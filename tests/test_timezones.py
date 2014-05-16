# -*- coding: utf-8 -*-
from datetime import datetime
import pytz

from gmaps.timezone import unixtimestamp
from gmaps.timezone import Timezone
from .testutils import retry

timezone = Timezone().timezone


@retry
def test_unixtimestamp_naive():
    # test if that was UTC
    assert unixtimestamp(datetime(1970, 1, 1)) == 0.0


@retry
def test_unixtimestamp_tzaware():
    warsaw = pytz.timezone(u'Europe/Warsaw')
    dt = warsaw.localize(datetime(1970, 1, 1))

    # because it was CET+1:00:00 on that day
    assert unixtimestamp(dt) == -3600.0


@retry
def test_timezone():
    once_upon_a_time = datetime(2014, 5, 9)
    somwhere_in_poland = lat, lon = 51.115355, 17.0256261

    result = timezone(lat, lon, once_upon_a_time)
    assert result['timeZoneId'] == u'Europe/Warsaw'


@retry
def test_timezone_language():
    once_upon_a_time = datetime(2014, 5, 9)
    somwhere_in_poland = lat, lon = 51.115355, 17.0256261

    result = timezone(lat, lon, once_upon_a_time, language='PL')
    assert result['timeZoneId'] == u'Europe/Warsaw'
    assert result['timeZoneName'] == u'Czas \u015brodkowoeuropejski letni'
