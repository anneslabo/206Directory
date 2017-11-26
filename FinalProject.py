#Final Project Anne Slabotsky
import unittest
import itertools
import collections
import json
import sqlite3
import requests

changetoken = "EAACEdEose0cBAEXs3CrjUHMgmZC6eIYG38OEBmrh7TtuWPNmBEBCqvPVp1qpgqtOdUUWMiTarl4gsqnXRBveFAf3mv4MUXIfH2sCzypahunAFlSUOHacP7ISKnJg3SREEaILZB4ndsasZB9yR0qdXVIgaBRwWvzFYr6osk1GzuFW06AlvJg9UFXGvZBSyZB8njTZByeRIMSAZDZD"
access_token = changetoken
if access_token == None:
    access_token = input ("generate token from https://developers.facebook.com/tools/explorer")

CACHE_FNAME = "facebook_cache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

## [PART 1]

# Here, define a function called get_FB_data


def get_FB_data():
    if "me" in CACHE_DICTION:
        print('using cached data')
        FB_results = CACHE_DICTION['me']
    else:
        print('getting data from internet')
        url = "https://graph.facebook.com/v2.11/me/feed"
        urlparams = {}
        urlparams["access_token"] = access_token
        urlparams["fields"] = "likes"
        urlparams["limit"] = 100
        request = requests.get(url, urlparams)
        print (request.url)
        FB_results = json.loads(request.text)
        CACHE_DICTION['me'] = FB_results
        f = open(CACHE_FNAME, 'w')
        f.write(json.dumps(CACHE_DICTION))
        f.close()
    return FB_results


if __name__ == "__main__":
    get_FB_data()
