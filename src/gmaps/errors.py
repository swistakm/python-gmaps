# -*- coding: utf-8 -*-
from gmaps import status


class GmapException(Exception):
    """Base exception for all python-gmap exceptions"""


class NoResults(GmapException):
    """Raised when api returned no results"""


class RequestDenied(GmapException):
    """Raised when request to API was denied"""


class InvalidRequest(GmapException):
    """Raised when request to Google API was invalid"""


class RateLimitExceeded(GmapException):
    """Raised when rate limit to API endpoint was exceeded"""

EXCEPTION_MAPPING = {
    status.OK: None,
    status.ZERO_RESULTS: NoResults,
    status.REQUEST_DENIED: RequestDenied,
    status.INVALID_REQUEST: InvalidRequest,
    status.OVER_QUERY_LIMIT: RateLimitExceeded,
}
