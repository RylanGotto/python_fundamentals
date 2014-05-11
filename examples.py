#String/Print format
print "hello", "how", "are you"
print "hello" + "how" + "are you"
"The number %d" % 1
"The number %d, is a number an %s" % (1, "integer")

#substring
"Quick brown fox"[1:] # ->'uick brown fox'
"Quick brown fox"[:1] # ->'Q'
"Quick brown fox"[0:5] # ->'Quick'
['capitalize', 'center', 'count', 'decode', 'encode', 'endswith'
, 'expandtabs', 'find', 'format'
,'index', 'isalnum', 'isalpha', 'isdigit', 'islower'
, 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower'
, 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust'
, 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines'
, 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']

#I/O
users_input = raw_input("Write something here: ")
document = open('lorem.txt','r') #read

document = opent('document_name.txt', 'r')#write
document.write("Some text")
document.close()


#xrange()/range() len()
#list comprehnsions lambda
#list stuff
list = [1,2,3,4,5] 
list.append(6) # @ the end of list
list.insert(1,1) # @ index
list.pop() # pops recently added index
list.sort() # obvious

#iterate over for loop
for i in list:
	print i
#iterate over length of list
for i in range(len(list)):
	print i
#iterate over range of numbers
for i in range(50):
	print i

#List comprehensions
#This
a_list = []
for i in range(50):
	if i % 2 == 0:
		a_list.append(i)
#Could be this
a_list = [i for i in range(50) if i % 2 == 0]

#Flow control
def an_if(x):
	if x > 2:
		print "%s > 2" % x
	elif x < 2:
		print "%s < 2" % x
def an_is(x):
	if x is 4:
		print "%s is 4" % 
	elif x is not 5:
		print "x is not 5"

#args and kwargs
def printarg(*args, **kwargs):
	if args and kwargs:
		print args, "", kwargs
	elif args:
		print args
	elif kwargs:
		print kwargs

def bad_test():
	if x > 10:
		return True
	else:
		return False

def good_test():
	return x > 10

def switch(choice):
	return {
		'a':1,
		'b':2,
		'c':3,
	}[choice]

#Type testing
if type("word") is str:
	print "is string"
if type(1) == int:
	print "is int"

#tuples
duple = (1, "word")
threeple = (1, False, "word")
fourple = (1, 2, True, "word")
fourple[3] # "word"

#dicts
dict = {'one':1, 'two':2}
dict.pop("two") # = 2
dict.popitem() # = last item in table
dict.update({'three':3})

for i in dict.iteritems():
	print i # ('two':2)
			# ('one':1)

for i in dict.itervalues():
	print i # 2
			# 1

for i in dict.iterkeys():
	print i # two
			# one

dict.has_key("two") # = 2

document = open('lorem.txt', 'r')
a_dict = {}
for i in document:
	list = i.split(" ")
	for x in list:
		if x in a_dict:
			a_dict[x] += 1
		else:
			v = x
			a_dict.update({x:0})


#playing with lists
a_dict = {'one':1}
tuples = (1,2)
listt = [1,2,3]

a_list = [a_dict, tuples, listt]

a_list[0]['one'] # = 1
a_list[1][0] # = 1
a_list[2][2] # = 3 

#Store a func
def pwords(words):
	print words

def upper(wrapper):


another_list = [pwords]
another_list[0]("printing these words")

os.walk
re
os.getcwd
#import os, system




