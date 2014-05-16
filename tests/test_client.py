# -*- coding: utf-8 -*-
import pytest

from gmaps import errors
from gmaps import Geocoding
from .testutils import retry


@retry
def test_client_with_key():
    geocoding = Geocoding(api_key="invalid_key", use_https=True)
    with pytest.raises(errors.RequestDenied) as excinfo:
        geocoding.geocode("Some address")

    assert "API key is invalid" in str(excinfo)
