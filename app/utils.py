"""
Utilitites
"""

# __author__ == 'Alex Shires'
import logging
from collections import OrderedDict

strava_file = "/Users/user/stravakey.txt"
tfl_file = "/Users/user/tflkey.txt"
google_file = "/Users/user/googlekey.txt"

logger = logging.getLogger("travelapp")


def get_auth_vals(filename=None):
    """
    get authentication values
    :param filename:
    :return:
    """
    f = open(filename)
    auth_data = OrderedDict()
    for line in f:
        try:
            k, v = line[:-1].split("=")
            auth_data[k.strip()] = v.strip()
        except ValueError as e:
            logger.warning(e)
    f.close()
    return auth_data
