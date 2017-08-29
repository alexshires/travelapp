"""
Utilitites
"""


def get_strava_key(filename="/Users/user/stravakey.txt"):
    f = open(filename)
    key = f.readline()[:-1]
    auth = f.readline()[:-1]
    f.close()
    return key, auth

def get_tfl_key(filename="/Users/user/tflkey.txt"):
    f = open(filename)
    key = f.readline()[:-1]
    auth = f.readline()[:-1]
    f.close()
    return key, auth

def get_google_key(filename="/Users/user/googlekey.txt"):
    f = open(filename)
    key = f.readline()[:-1]
    auth = f.readline()[:-1]
    f.close()
    return key, auth