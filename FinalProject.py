#Final Project Annie Slabotsky
# link for plot.ly diagram = https://plot.ly/~anneslabo/2/
from __future__ import print_function
import httplib2
import os
from httplib2 import Http

from apiclient import discovery
from apiclient import errors
from httplib2 import Http
# from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import unittest
import itertools
import collections
import json
import sqlite3
import requests
import datetime
import plotly
import csv


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

def d_o_w(year, month, day, time):

    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    answer = datetime.date(int(year), int(month), int(day)).weekday()
    if int(time[:2]) > 18:
        t_o_d = 'night'
    elif int(time[:2]) > 12:
        t_o_d = 'evening'
    elif int(time[:2]) > 6:
        t_o_d = 'mid-morning'
    else:
        t_o_d = 'morning'
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
    return (day, t_o_d)
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
    day = d_o_w(year, month, day, time)
    return (day)
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

list_tup_data = []

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
                #add the day oe week and time of day to list to then be dded to CSV
                list_tup_data.append(convert_time(created_time))


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


# ----------------------------------------------------------------------------
#now onto spotify api




CACHE_FNAME = "darksky_cache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}


def get_darksky_data():

        print('getting data from internet')
        #west palm beach
        wpb = []
        url1 = 'https://api.darksky.net/forecast/7dba11f5dc3471a2b9ae84225f3042d4/26.714913,-80.033776'
        # urlparams["access_token"] = access_token
        # #urlparams["fields"] = "created_time,message,likes,comments,reactions,type"
        #
        # url = 'https://api.spotify.com/v1/users/12160022617'
        request = requests.get(url1)

# you need to generate a new access token frequently because that is how facebook is set up

        code = str(request.status_code)
        darksky_results = json.loads(request.text)
        # print(darksky_results.keys())
        #this is a function that will takes the top 100 posts from what I retrieve from dark sky
        # darksky_results = {x: darksky_results[x] for x in heapq.nsmallest(darksky_results, 100, key=int)}
        # print(darksky_results)
        # for item in darksky_results['hourly']:
        #     print(item['temperature'])
        miami_beach = []
        url2 = 'https://api.darksky.net/forecast/7dba11f5dc3471a2b9ae84225f3042d4/25.781988,-80.131004'
        ##clear water
        clear_water = []
        url3 = 'https://api.darksky.net/forecast/7dba11f5dc3471a2b9ae84225f3042d4/27.953014,-82.831831'
        #naples beach
        naples = []
        url4 = 'https://api.darksky.net/forecast/7dba11f5dc3471a2b9ae84225f3042d4/26.150900,-81.805014'

        #Daytona beach
        daytona = []
        url5 = 'https://api.darksky.net/forecast/7dba11f5dc3471a2b9ae84225f3042d4/29.223133,-81.007349'

        request = requests.get(url1)
        code = str(request.status_code)
        darksky_results1 = json.loads(request.text)
        for item in (darksky_results['daily']['data']):
            timee = (item['time'])
            correct_time = (datetime.datetime.fromtimestamp(int(timee)).strftime('%Y-%m-%d %H:%M:%S'))
            wpb.append(tuple((item['precipProbability'], correct_time)))


        request = requests.get(url2)
        code = str(request.status_code)
        darksky_results2 = json.loads(request.text)
        for item in (darksky_results2['daily']['data']):
            timee = (item['time'])
            correct_time = (datetime.datetime.fromtimestamp(int(timee)).strftime('%Y-%m-%d %H:%M:%S'))
            miami_beach.append(tuple((item['precipProbability'], correct_time)))

        # request = requests.get(url3)
        # code = str(request.status_code)
        # darksky_results3 = json.loads(request.text)
        # for item in (darksky_results3['daily']['data']):
        #     clear_water(item['precipProbability'])

        request = requests.get(url4)
        code = str(request.status_code)
        darksky_results4 = json.loads(request.text)
        for item in (darksky_results4['daily']['data']):
            timee = (item['time'])
            correct_time = (datetime.datetime.fromtimestamp(int(timee)).strftime('%Y-%m-%d %H:%M:%S'))
            naples.append(tuple((item['precipProbability'], correct_time)))


        request = requests.get(url5)
        code = str(request.status_code)
        darksky_results5 = json.loads(request.text)
        for item in (darksky_results5['daily']['data']):
            timee = (item['time'])
            correct_time = (datetime.datetime.fromtimestamp(int(timee)).strftime('%Y-%m-%d %H:%M:%S'))
            daytona.append(tuple((item['precipProbability'], correct_time)))

        #create cache file with Weather stuff
        f = open(CACHE_FNAME, 'w')
        f.write(json.dumps(darksky_results))
        f.close()

    # print (FB_results)
        with open ('WPB_ds.csv', 'w', newline='') as ds_csv:
            writer_object =  csv.writer(ds_csv)
            writer_object.writerow(['weather', 'date'])
            for row in wpb:
                # print(row)
                writer_object.writerow(row)
        with open ('miami_beach_DK_ds.csv', 'w', newline='') as ds_csv:
            writer_object =  csv.writer(ds_csv)
            writer_object.writerow(['weather', 'date'])
            for row in miami_beach:
                # print(row)
                writer_object.writerow(row)

        with open ('naples_ds_ds.csv', 'w', newline='') as ds_csv:
            writer_object =  csv.writer(ds_csv)
            writer_object.writerow(['weather', 'date'])
            for row in naples:
                # print(row)
                writer_object.writerow(row)
        with open ('daytona_ds.csv', 'w', newline='') as ds_csv:
            writer_object =  csv.writer(ds_csv)
            writer_object.writerow(['weather', 'date'])
            for row in daytona:
                # print(row)
                writer_object.writerow(row)
        return darksky_results


# ==========================================================================================
# gmail


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)

    GMAIL = discovery.build('gmail', 'v1', http=credentials.authorize(Http()))

    user_id =  'me'
    label_id_one = 'INBOX'
    label_id_two = 'UNREAD'


    unread_messages = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two]).execute()

    # -- read values for the key "messages"

    message_list = unread_messages['messages']

    print ("Total unread messages in inbox: ", str(len(message_list)))




def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
      print('Labels:')
      for label in labels:
        print(label['name'])



if __name__ == "__main__":
#     FB_results = get_FB_data()
#     write_to_DB(FB_results)
#     # print(list_tup_data)
# with open ('FB.csv', 'w', newline='') as fb_csv:
#     writer_object =  csv.writer(fb_csv)
#     writer_object.writerow(['day', 'time'])
#     for row in list_tup_data:
#         # print(row)
#         writer_object.writerow(row)
    get_darksky_data()
    main()
