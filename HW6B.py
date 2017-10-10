# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
#soup is a text blurb
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
#a tags are links
tags = soup('a')
summ = 0
#making an empty tupple (key value list)
# countlink = []
# count = 0
# for tag in tags:
#     print(tag)
#     count = count + 1
#     countlink.append((count, tag))
# print(countlink)
count = 7 # change to 7!
position = 18 # 18

#i am checking the number of iterations within the range of 4 because that is what we set our variable count to
#we set our variable count to how many times we want to repeat process of checking link
for instance in range(int(count)):
    #open url previously inputted and read it
    html = urlopen(url).read()
    alllinks = soup('a')
    xrepeat = 0
    for x in alllinks:
        xrepeat = xrepeat + 1
        #if number of links is the link at the position we want

        if int(xrepeat) == int(position):
            #get the url at that link

            url = x.get('href')
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            print(x.get('href'))
            #indicating that first iteration is done you have x more to go until you hit 0
            #every time for loop runs x gets one bigger so the last time you want to use it it will = count - 1
            if x == int(count) -1:
                print (x.contents[0])

    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #summ = summ + int(tag.contents[0]
    #print('Attrs:', tag.attrs)
