# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 0, 0):
    import urlparse  # noqa

    def is_string(s):
        return isinstance(s, basestring)  # noqa

else:
    from urllib import parse as urlparse  # noqa

    def is_string(s):
        return isinstance(s, str)
