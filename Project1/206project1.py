import os
import csv
import sys
import operator
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	#this opens and reads a text file
	lists = []
	with open(file) as csvfile: #opening file as csv file
		readCSV = csv.reader(csvfile) #read in csv file
		#readCSV.next() #skip first line
		#for loop to read line by line
		for row in readCSV:
			d = {} #making a new dict for every row
			#loop through data in row
			d['First'] = row[0]
			d['Last'] = row[1]
			d['Email'] = row[2]
			d['Class'] = row[3]
			d['DOB'] = row[4]
			lists.append(d)
		return lists[1:]





#Sort based on key/column
#the input is the huge data set
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#soretd will take that giant chucnk of data and sort by the col the main inputs ie First, Last, Email etc.
	orderedList = sorted(data, key=operator.itemgetter(col))
	return orderedList[0]['First']+ " " + orderedList[0]['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	tups = ()
	for row in data:
		orderedlists = sorted(data, key=operator.itemgetter('Class'))
	freshmanCount = 0
	sophmoreCount = 0
	juniorCount = 0
	seniorCount = 0
		#index through each list in the list
	#print(orderedlists)
	#orderedlist is a list, each item is a dict
	#student is a dic and we need to index into the specific dic to figure out its class
	for student in orderedlists:
		if student['Class'] == "Freshman":
				freshmanCount = (freshmanCount + 1)
		elif student['Class'] == "Sophomore":
				sophmoreCount = (sophmoreCount + 1)
		elif student['Class'] == "Junior":
				juniorCount = (juniorCount + 1)
		elif student['Class'] == "Senior":
				seniorCount = (seniorCount + 1)
	#print(orderedtups)
	#print(freshmanCount)
	#print(sophmoreCount)
	#print(juniorCount)
	#print(seniorCount)
	d = dict()
	d['Freshman'] = freshmanCount
	d['Sophomore'] = sophmoreCount
	d['Junior'] = juniorCount
	d['Senior'] = seniorCount
	d.items()
	newd = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
	return(newd)

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	listofdic = a
	#print(listofdic)
	days = []
	counts = dict()
	for dic in listofdic:
		#print(dic['DOB'])
			date = dic['DOB']
			month, day, year = (int(x) for x in date.split('/'))
			days.append(day)
	#days is a list of int(days)
	#item represent the day of the month in the list days
	for item in days:
		if item not in counts:
			counts[item] = 1
		else:
			counts[item] = counts[item] + 1
	#first were sorting by highest number day
	mostcom = sorted(counts.items(), key=operator.itemgetter(0), reverse=True)
	#then we are sorting by how freq number is repeating
	sortedmostcom = sorted(mostcom, key=operator.itemgetter(1), reverse=True)
	return(sortedmostcom[0][0])



	#Your code here:



# Find the average age (rounded) of the Students
def findAge(a):


	listofdic = a
	#print(listofdic)
	age = []
	counts = dict()
	for dic in listofdic:
		#print(dic['DOB'])
			date = dic['DOB']
			month, day, year = (int(x) for x in date.split('/'))
			age.append(2017 - year)
	numofpeople = len(age)
	sumofages = (sum(age))
	return(round(sumofages/numofpeople))
	#Your code here:


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#we want to sort the list of dictionary based on col input ie example by last name

	sortedinfo = sorted(a, key= lambda x: x[col])
	csvfile= open(fileName, "w")
	for item in range(len(sortedinfo)):
		stringcsvinfo = sortedinfo[item]['First']+ "," + sortedinfo[item]['Last'] + "," + sortedinfo[item]['Email'] + "," + sortedinfo[item]['Class'] + "," + sortedinfo[item]['DOB']
		csvfile.write(stringcsvinfo)
	csvfile.close()
	# exit()
	# #csv file is the variable and set it equal to the file we open with
	# for dic in sortedinfo:
	#
	# with open(fileName) as csvfile:
	# #it could ve csvfile= open(fileName)
	# csv.write()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
