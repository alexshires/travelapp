"""
Script to acquire data from websites
* on demand
* batch
"""

import requests
from datetime import datetime, timedelta
from collections import OrderedDict
import pandas as pd
from app.utils import get_auth_vals, strava_file

def download_activities(athid, start_date=None, end_date=None):
    """
    download the activites from the website
    :param athid:
    :param start_date:
    :param end_date:
    :return:
    """
    # TODO: start dates, ath ID etc
    start_secs = start_date.timestamp()
    start_str = start_date.strftime("%Y-%m-%d")
    end_secs = end_date.timestamp()
    end_str = end_date.strftime("%Y-%m-%d")
    params = OrderedDict()
    strava_auth = get_auth_vals(strava_file)
    act_url = "https://www.strava.com/api/v3/athlete/activities"
    params['access_token'] = strava_auth['access_token']
    params['before'] = end_secs
    params['after'] = start_secs
    res = requests.get(act_url, params=params)
    print(res.ok, res.status_code)
    data = res.json()
    # convert to dataframe and save
    df = pd.DataFrame.from_dict(data, orient='records')
    df.to_csv("activities_%s_%s_%s.csv" % (athid, start_str, end_str))

if __name__=='__main__':
    # get activities
    end = datetime.now()
    start = end - timedelta(days=30)
    download_activities(None, start, end)



