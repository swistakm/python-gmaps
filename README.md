[![Build Status](https://travis-ci.org/swistakm/python-gmaps.svg?branch=master)](https://travis-ci.org/swistakm/python-gmaps)
[![Coverage Status](https://img.shields.io/coveralls/swistakm/python-gmaps.svg)](https://coveralls.io/r/swistakm/python-gmaps)

# python-gmaps

Google Maps API client. For full API documentation go to:

http://python-gmaps.readthedocs.org


## Why yet another python google maps client?

There are a bunch of libraries for Google Maps Web Service. To name a few:
* [googlemaps](https://pypi.python.org/pypi/googlemaps/)
* [google.directions](https://pypi.python.org/pypi/google.directions)

What's wrong with them? googlemaps uses deprecated google API and forces
you to format your parameters instead of using native python datatypes.
And what about google.directions? Just take a look inside it's code...

So here is code for new Google Maps API endpoints. It requires
[requests](https://github.com/kennethreitz/requests), supports native python
datatypes and is sweetened with some syntactic sugar. Nothing more.
No bells and whistles.

Any contributions (code/issues) are welcome.

## Instalation

    pip install python-gmaps

## Usage

Just import API endpoint of your choice and start querying:

```python
from gmaps import Geocoding
api = Geocoding()

api.geocode("somwhere")
api.reverse(51.123, 21.123)
```

If you need to use Google Maps API for Business then instantiate your endpoint
with `api_key` param

```python
from gmaps import Geocoding
api = Geocoding(api_key='your_secret_api_key')
```

Each endpoint method raises adequate exception when status of query is different
than `OK`. It also unpacks results list from Google API output dict so you have
one key less to access but it does nothing more.
So if Google geocoding api outputs something like:

```
{
    results: [
    ...
    ],
    status: 'OK'
}
```

You will get only get list that was inside `result` value. At least one element
returned is always assured, otherwise `gmnaps.errors.NoResults` exception is
raised.

For each API endpoint you can specify:
* default `sensor` value
* protocol (http/https)
* api key (only for http)

Available endpoints:
* `Geocoding()`
* `Directions()`
* `Timezone()`
* `Elevation()`

For detailed documentation of each endpoint refer to dosctrings or
[this API documentation](http://python-gmaps.readthedocs.org/en/latest/).
If you need list of available values for some parameters (like geocoding
components, languages, regions etc.) refer to
[Google Maps API docs](https://developers.google.com/maps/documentation/webservices/).
These values can change anytime so there is no reason to check for them in this
lib - they will be checked anyway.

## Changes

### 0.3.1 (2016-03-23)

- updated list of trove classifiers
- nicer `long_description` on PyPI
- simplified requirements in `setup.py` script


### 0.3.0 (2015-08-31)
- added two additional optional parameters to reverse geocoding that
  allow restricting type of results (`result_type` and `location_type`)
  thanks to @20tab
- added `gmaps.polyline.encode()` utility function to encode paths using
  [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm?hl=en)
- `Elevation` endpoint added implemented

### 0.2.1 (2014-11-11)
- `gmaps.errors.GmapException` inherits from `Exception` instead of `BaseException`

### 0.2.0 (2014-10-02)
- fixed lists serialization issue (#1) thanks to @feighter09
- added pep8 compliance test using flake8
- pep8 compliance

### 0.1.1 (2014-05-16)
- python 3.3 support

### 0.1.0 (2014-05-09)
- `Timezone` endpoint added

### 0.0.2 (2013-10-03)
- `Directions` endpoint added

### 0.0.1 (2013-10-02)
- initial release
- ```Geocoding``` endpoint
