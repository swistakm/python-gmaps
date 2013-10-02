# -*- coding: utf-8 -*-
import status

class GmapException(BaseException):
    """Base exception for all python-gmap exceptions"""

class NoResults(GmapException):
    """Raised when api returned no results"""

class RequestDenied(GmapException):
    """Raised when request to API was denied"""

EXCEPTION_MAPPING = {
    status.OK: None,
    status.ZERO_RESULTS: NoResults,
    status.REQUEST_DENIED: RequestDenied,
}

