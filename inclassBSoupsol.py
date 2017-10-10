from bs4 import BeautifulSoup

## Answers to the lecture 11 exercise, instructions in comments

# open the samplehtml file and read it into a string
f = open("samplehtml.html","r")
text_data_from_file = f.read()
f.close()

# create a BeautifulSoup object from the string
soup = BeautifulSoup(text_data_from_file,"html.parser")
#print(soup.find_all("img"))
imgs = soup.find_all("img")
xkcd_img = imgs[0]

# Write/plan code to print the URL to the XKCD comic, using BSoup and this file.
print(xkcd_img["src"])

print("\n")
# Write/plan code to grab all the links (URLs) in that html page, but nothing else.
for lnk in soup.find_all('a'):
	print(lnk['href'])

print("\n")
# Write/plan code to grab the TEXT of all the links in that html page, but nothing else.
for lnk in soup.find_all('a'):
	print(lnk.text)

print("\n")
# Write/plan code to grab the text of each of the items in the ordered list. (Not the 1/2/2, just the text. 
list_objs = soup.find_all('li')
for li in list_objs:
	print(li.text)

print("\n")
# - Write/plan code to grab the alt text associated with the image of the XKCD comic.
# see way above for accessing xkcd_img...
print(xkcd_img["aria-text"])

print("\n")
#   - And code to assign the BeautifulSoup object holding the div that contains the image to a variable `image_div_obj` 
image_div_obj = soup.find('div',{"id":"below-section"})
print(image_div_obj)


print("\n")
# - Write/plan code to add these three strings to a list, using just BSoup and the html doc available…
#   > An image from the comic XKCD below.
#   > Find more similar stuff at the comic web site.
#   > Or just check out your homework after you sign into Canvas.

# first, get the thing that contains them all, the span!
span_container = soup.find("span") # there's only one
print(span_container) # check it out
paragraph_tags = span_container.find_all("p") # they're all in p tags, and span_container is itself a BSoup object!
print(paragraph_tags) # check it out
print("\n")
for pt in paragraph_tags:
	print(pt.text) # and if you want to cut out the extra space, .strip().rstrip()
	# e.g.
	# print(pt.text.strip().rstrip())