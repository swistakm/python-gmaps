# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 0, 0):
    import urlparse  # noqa
    is_string = lambda s: isinstance(s, basestring)
else:
    from urllib import parse as urlparse  # noqa
    is_string = lambda s: isinstance(s, str)
