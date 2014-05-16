# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 0, 0):
    import urlparse
else:
    from urllib import parse as urlparse
