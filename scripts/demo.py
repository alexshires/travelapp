"""
Demonstration script to test functionality
"""



import requests


from utils import get_strava_key, get_tfl_key, get_google_key

strava_client, strava_token = get_strava_key()
google_api_key, google_secret = get_google_key()
tfl_api_key, tfl_api_secret = get_tfl_key()


def test_strava_api():
    """
    testing strava api
    :return:
    """
    pass
