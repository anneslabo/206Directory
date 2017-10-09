
#this opens and reads a text file
file_object  = open("TheVictors.txt", 'r')
#creates a list
lists = []
#creates a list from reading a document and splits it up and puts words into list
lists = list(file_object.read().split())
d = {}
  #add everything to d
for word in lists:
      #this just made a list of tupples
      #dictionary at whichever word, if word not there add word put zero if it is there add 1
      d[word] = d.get(word, 0) + 1
l=[]
#this for loop takes all the items from the dictionary
for item in d.items():
    #append them from the list so that we go from dic key value pairs to tuples in list
    l.append(item)
#print(d)
#print(l)
#don't forget that true needs to be capital
#then sort by second value in descending order 
l = sorted(l, key = lambda x:x[1], reverse=True)
print(l[:15])
