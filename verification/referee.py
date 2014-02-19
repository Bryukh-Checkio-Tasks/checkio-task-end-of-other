
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

cover_set = """
def cover(func, in_data):
    return func(set(in_data))
"""

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover_set,
            'python-3': cover_set
        }).on_ready)
