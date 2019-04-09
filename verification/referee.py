
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

cover = """def cover(f, data):
    return f(set(data))"""

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "checkio",
            "js": "endOfOther"
        },
        cover_code={
            'python-3': cover,
            #'js-node': cover_codes.js_unwrap_args
        }
    ).on_ready)