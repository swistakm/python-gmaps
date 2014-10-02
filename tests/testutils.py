# -*- coding: utf-8 -*-
from time import sleep
from gmaps.errors import RateLimitExceeded

MAX_RETRIES = 4


def retry(test):
    def retrying_test(*args, **kwargs):
        retries = 0

        while retries < MAX_RETRIES:
            try:
                return test(*args, **kwargs)
            except RateLimitExceeded:
                sleep(2 ** (retries+1))
                retries += 1

        raise AssertionError("Max retries count excceded for this test")

    return retrying_test
