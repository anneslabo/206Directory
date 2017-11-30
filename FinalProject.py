#Final Project Annie Slabotsky
import unittest
import itertools
import collections
import json
import sqlite3
import requests
import datetime


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
#get the day of the week from a timestamp
def d_o_w(year, month, day):

    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    answer = datetime.date(int(year), int(month), int(day)).weekday()
    if answer == 1:
        day = 'Sunday'
    elif answer == 2:
        day = 'Tuesday'
    elif answer == 3:
        day = 'Wednesday'
    elif answer == 4:
        day = 'Thursday'
    elif answer == 5:
        day = 'Friday'
    elif answer == 6:
        day = 'Saturday'
    elif answer == 0:
        day = 'Sunday'
    return (day)
    # print(day)

def convert_time(created_time):
    # print(created_time)
    year = created_time[:4]
    # print(year)
    month = created_time[5:7]
    # print(month)
    day = created_time[8:10]
    # print(day)
    time = created_time[11:16]
    # print(time)
    day = d_o_w(year, month, day)
    # print (day)


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
cur.execute('CREATE TABLE FB_DATA (id INTEGER, type TEXT, created_time TIMESTAMP)')



def write_to_DB(FB_results):
    #print("abc")
    #print (FB_results)
    for chunk in FB_results['data']:
        #getting the id from the data section in the json file
        idNum = (chunk['id'])


        item_type = (chunk['type'])
        #print (chunk)
        # cm = chunk['comments']
        # print(cm)
        comments = chunk.get('comments')
        if comments != None:
            for item in comments['data']:
                created_time = item['created_time']
                convert_time(created_time)
        # data = comments.get('data')

        # for item in comments:
        #     #print(type(comments))
        #     cm_msg = item['data']
        #     print(cm_msg)
            #time = item['created_time']

        #print("==============================\n")
        #for item in chunk:
        #    print("item id *************",item)
        tup = idNum, item_type, created_time
            #print(tup)
        #print(type(tw_id))
        cur.execute('INSERT INTO FB_DATA (id, type, created_time) VALUES (?, ?, ?)', tup)
#  5- Use the database connection to commit the changes to the database

    conn.commit()



if __name__ == "__main__":
    FB_results = get_FB_data()
    write_to_DB(FB_results)
