#Final Project Annie Slabotsky
import unittest
import itertools
import collections
import json
import sqlite3
import requests


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

    if "200" in CACHE_DICTION:
        print('using cached data')
        FB_results = CACHE_DICTION["200"]

    else:
        print('getting data from internet')

        access_token = None
        if access_token == None:
            access_token = input ("generate token from https://developers.facebook.com/tools/explorer\n")

        url = "https://graph.facebook.com/v2.11/me/posts"
        urlparams = {}
        urlparams["access_token"] = access_token
        #urlparams["fields"] = "created_time,message,likes,comments,reactions,type"
        urlparams["fields"] = "created_time,comments,type"
        urlparams["limit"] = 100

        request = requests.get(url, urlparams)
# you need to generate a new access token frequently because that is how facebook is set up
        while request.status_code != 200:
            access_token = input ("generate new access token from https://developers.facebook.com/tools/explorer\n")

            urlparams["access_token"] = access_token
            request = requests.get(url, urlparams)

        code = str(request.status_code)
        FB_results = json.loads(request.text)
        #create cache file with FB stuff
        CACHE_DICTION[code] = FB_results
        f = open(CACHE_FNAME, 'w')
        f.write(json.dumps(CACHE_DICTION))
        f.close()

    # print (FB_results)
    return FB_results


conn = sqlite3.connect('FB_DATA.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS FB_DATA')
cur.execute('CREATE TABLE FB_DATA (id TEXT, name TEXT, type INTEGER, created_time TIMESTAMP)')

def write_to_DB(FB_results):
    #print("abc")
    for item in FB_results:
        #print("==============================\n")
        tup = item["id"], item["name"], item["type"], item["created_time"]
        #print(tw)
        #print(type(tw_id))
        cur.execute('INSERT INTO ITEMS (id, name, type, created_time) VALUES (?, ?, ?, ?)', tup)
#  5- Use the database connection to commit the changes to the database

    conn.commit()



if __name__ == "__main__":
    get_FB_data()
