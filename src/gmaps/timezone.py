# -*- coding: utf-8 -*-
from __future__ import division
from pytz import UTC
from gmaps.client import Client


def total_seconds(td):
    """
    Take a timedelta and return the number of seconds it represents
    """
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6  # noqa


def unixtimestamp(datetime):
    """Get unix time stamp from that given datetime. If datetime
    is not tzaware then it's assumed that it is UTC
    """
    epoch = UTC.localize(datetime.utcfromtimestamp(0))
    if not datetime.tzinfo:
        dt = UTC.localize(datetime)
    else:
        dt = UTC.normalize(datetime)
    delta = dt - epoch
    return total_seconds(delta)


class Timezone(Client):
    TIMEZONE_URL = 'timezone/'

    def timezone(self, lat, lon, datetime,
                 language=None, sensor=None):
        """Get time offset data for given location.

        :param lat: Latitude of queried point
        :param lon: Longitude of queried point
        :param language: The language in which to return results. For full list
             of laguages go to Google Maps API docs
        :param datetime: Desired time. The Time Zone API uses the timestamp to
             determine whether or not Daylight Savings should be applied.
             datetime should be timezone aware. If it isn't the UTC timezone
             is assumed.
        :type datetime: datetime.datetime
        :param sensor: Override default client sensor parameter
        """

        parameters = dict(
            location="%f,%f" % (lat, lon),
            timestamp=unixtimestamp(datetime),
            language=language,
            sensor=sensor,
        )
        return self._make_request(self.TIMEZONE_URL, parameters, None)
