#----------------------------------Data Types------------------------------------------------
#1) Single Value Datatypes:
#a) Integer - Any real number without decimal points(whole number)
#ex- 1,2,3,4,0,-3,-56
a=10
print(a)
print(type(a))
#type- it is the built in function used to get the type of data
#default value of int =0


#---------------------------------------------------------------------------------------------
#b) Float- any number with decimal points
#ex-1.2,3.4,5.6
b=4.5
print(type(b))
print(b)


#------------------------------------------------------------------------------------------------
#c) Boolean -the only allowed values for this datatypes are True and False
#we can use these datatypes to represent boolean values
c=True
d=False
print(c,d)


#------------------------------------------------------------------------------------------------
#d)Complex -  It is a combination of real numbers and imaginary numbers
#complex is in the form of A+Bj i.e.,, A is real part and B is imaginary part
e=3+4j
f=0+0j
print(e,f)
print(type(e))

#defult value for complex is = 0j

#----------------------------------------------------------------------------------------------------
#* Empty Constructor datatypes having default values
print(int())
print(float())
print(complex())
print(bool())

#----------------------------------------------------------------------------------------------

#2)Multivalue data types

#1)String - It is set or collection of characters
#boundary : '_________' ,"__________", '''________'''
#It is immutable Datatype 
#len- it is in built function which is used to get the length of string
string="Nilambika Dudhani"
print(string)
print(type(string))
print(len(string))

#Note- in string initialization if we start with single quote then we need to finish with single
#quote and same with other boudaries.
#to Write multiple line string
#ex- 
String1='''Hi I am Nilambika Dudhani
I am an Engineering Student
'''
print(String1)
print(len(String1))

#there are various methods in string directory 
print(dir(str))
#this command will print the string methods

#-------------------------------------------------------------------------------------------------
#Indexing a string-A process of extracting a single character at a time 
#indexing can be positive (starts with 0) or negative (starts with -1)
#syntax - var_name[index]
#ex-
string2='indedxing in string'
print(string2[2])
print(string2[-1])


#-----------------------------------------------------------------------------------------------
#Slicing in String -  A process of extracting multiple characters at a time/Simultaneously
#syntax - Var_name[start index: stop index:step value]
#start index - default value - 0(optional)
#End index -  default value - length of the string(optional)
#step value- default value- 1(optional)
#Note- element at last index will not be included in slice
#ex-
slic_str='Python is easy'
print(slic_str[0:6:1]) #it will extract python completely
print(slic_str[0:6:-1]) # it will extract in reverse formamt 
print(slic_str[::2]) # to extract even index character
print(slic_str[1::2]) #to extract odd index character

#-----------------------------------String Methods----------------------------------------------
#python provides a rich set of built in string methods that are used to manipulate and modify text
#A key point to remeber is that strings in python are immutable
#All string methods return a new string and do not change the origina one
#1)capitalize()-python strings capitalize function returns the first letter capital form
#ex-
greet="Good morning"
print(greet.capitalize())

#2)upper()- Python string upper() returns all the alphabet characters to uppercase.
#ex- 
print(greet.upper())

#3)lower()- Python string lower() return all the alphabet characters to lowercase.
#ex- 
print(greet.lower())

#4)Swapcase() - Python string Swapcase returns new string which converts uppercase to lowercse 
#and vice versa.
#Ex- 
print(greet.swapcase())

#5)count()- Python string count() returns the  number of occurence of the specific substring
#inside the given string.
print(greet.count('G'))

#6)Index- python string index() returns the lowest index where the specified substring is found 
#or searches the string for a specified value and return the position where it was found
#find the first occurance of the specified value and return the value error if not found.
#syntax- string.index("substring",start index,end index)

st="date"
print(st.index('a',0,))

#7)rindex()-Searches the string for the specified value and return the last position of where 
#it was found
#Ex-
my_msg='Hello World'
print(my_msg.rindex('l'))

#8)find() -python string find() is used to find the index of substring in the string or 
#serches for the specified string and returns the index where it was found.
#Ex-
print(my_msg.find('o'))

#9)rfind()- same as find method but returns the last position where it was found.
print(my_msg.rfind('o'))

#10)replace()- python string replace() is used to replace some parts of another string or
#replace a specified phrase with another phrase
#syntax- string.replace(oldvalue,new value,count)
#ex-
print(my_msg.replace('o','a'))  #it will replace o to a everywhere
print(my_msg.replace('o','a',1))  #it will replace o to a only once


#11)startswith()- Python string starswith function returns true if the string startswith specified
#value otherwise returns false
#syntax- string.startswith(value,start,end)
#Ex-
print("how are you".startswith("are"))
print("how are you".startswith("how"))


#12)endswith()- python string endswith() function returns True if string ends with  the given
#specified value otherwise it returns false
#syntax-string.endswith(value,start,end)
#ex-
print("how are you".endswith('you'))
print("how are you".endswith('how'))


#13)split() - python string split() is used to split() the string into list of values
#syntax-string.split(separator,max split)
#Ex-
split_msg='Hi I am Learning Python Full Stack Developement'
print(split_msg.split(' '))
print(split_msg.split('a'))

#14)join()- join the elements of an sequence using the string specified 
#syntax- string.join(iterable)
#Ex- 
data='Hello'
print(data.join('World'))

#15)strip() - removes any leading (spaces at beginning) and trailing (spaces at the end)
#characters (space is the default leading character to remove)
#syntax- string.strip()
#Ex-
data1='  Hello I am Student    '
print(data1.strip())

#rstrip()- removes any trailing character
#syntax- string.rstrip()
print(data1.rstrip())

#lstrip()- removes any leading charcter
#syntax-string.lstrip()
print(data1.lstrip())

#16)isalnum()- Returns true if all charcaters in the string are alphanumeric
alpha='alphanumeric123'
print(alpha.isalnum())


#17)isalpha()- return true if all charcaters are alphabet
char='abcdefgh'
print(char.isalpha())

#18)isdigit() - returns true if all characters are digit
dig='875693482'
print(dig.isdigit())

#19)islower()- retunns true if all characters are lowercase
lower='lowercase'
print(lower.islower())

#20)isupper()-returns true if all characters are uppercase.
upper='UPPERCASE'
print(upper.isupper())

#21)isspace() - returns true if all characters in the string are spaces
space='         '
print(space.isspace())

#22)Concatenation- It is the procces of combining 2 or more strings togehter using + operator
#syntax- Str1+str2
#ex-
print('hello'+' world')

#23)replication- it is the process of making some copies of original string by using * operator
#syntax-str*(count)
#ex-
print('helo '*5)

#---------------------------------------------------------------------------------------------------
#2)List datatype-
#list is a collection of homogeneous and heterogenous element separated by comma(,)
#boundary= [    ]
#it is a mutable datatype[we can modify the original list]
#it allows duplicate elements  #to find the length of list = len(list)
#default value of list is = [](empty list)

#Nested list- the list can have one or more list and it is called nested list
#syntax- var_name=[item1,item2,.......,itemn]
#ex-
lst=[1,2,3,4,5,6,7,8]
print(type(lst))
print(len(lst))

#nested list
nes_lst=[1,2,3,4,['nested','list'],'apple']
print(nes_lst)

#---------------------------------------------------------------------------------------------
#Indexing in list - It is process of extracting individual element from the list
#positive indexing starts from 0(traverse from left to right) and negative indexing starts from -1(it traverse from right to left)
#Ex-
names=['apple','google','yahoo','gmail','microsoft','gemini','flipkart']
print(names[1]) #extract the element from index 1
print(names[-1]) #extract the last element from the list

#indexing for nested list
lst1=['apple','google',[2,3,4,5],['amzon','yahoo']]
print(names[2][3])
print(names[3][1])

#Slicing in List - it is a process of extracting multiple elements from list simultaneuously is called slicing
#ex-
print(names[0::1]) #extract all elements
print(names[3:6:1])  #extrct elements from index 3 to 5 with step of 1
print(names[0:1:]) #extract all elements in reverse 
print(names[:4]) #start extracting from 0th index
print(names[0:]) #extract till last
print(names[:]) #extract entire list
print(names[::2]) #extract alternative elements
print(names[::-1]) #extract reverse list



#--------------------------------methods in list-------------------------------------------------
#1)append() - Adds an element at the end of the list (both individual and collection)
#syntax- list.append(element)
#a element can be of any datatypes
#Ex-
print([1,2,3].append('methods'))
print(['apple','google'].append('microsoft'))

#2)extend()-extends the existing list with the items of the given sequence
#syntax- list.extend(iterable)
#ex-
print([1,2].extend([3,4]))

#3)insert()-adds an element at a speicified position(both individual and collection)
#syntax- list.insert(position,element)
#ex-
print(names.insert(1,'newelement'))

#4)pop() - removes the element at the specified position
#syntax- list.pop([pos])
print(names.pop(2))

#5)remove() - removes the first occurence of the elements specified
#$syntax- list.remove(element)
#ex-
print(names.remove('microsoft'))

#6)clear() - it is used to clear the entire list without deleting the list
#it returns none
#syntax-list.clear()
clear_lst=[1,2,3,4,5,6]
print(clear_lst.clear())

#7)sort()- sort the list In order to sort a list should be homogenous
#modifies the original list itself
#syntax-list.sort([key=function],[reverse=True])
num=[1,5,6,7,8,9,3,2,4]
print(num.sort())

#8)index() - returns the index of the first element with specified value 
#syntax-list.index(element)
#ex-
print(names.index('gemini'))

#9)count() - returns the no of occurance of the specified value
#syntax- list.count(element)
#ex-
print(names.count('apple'))

#---------------------------------------------------------------------------------------------
#3)Tuple datatypes- It is collection of homogenoues and heterogenous data items or values 
#this is closed between two parenthesis()
#syntax- var_name=(values1,values2,.....,valuesn) #with boundaries
# var_name=values1,values2,.......,valuesn  #without boundaries
#Ex-
number=(1,2,3,4,5,6)
print(type(number))
#default value for tuple =()

#indexing and Slicing on tuple
#Ex-
emp_names=('steve jobs','john','bill gates','tim cook','alex')
#indexing
print(emp_names[0])
print(emp_names[-1])
print(emp_names[3])

#slicing
print(emp_names[::1])
print(emp_names[:2:])
print(emp_names[-2::])

#index()
print(emp_names.count('john'))
print(emp_names.count('alex'))

#count()
print(emp_names.count('alex'))

#Properties of Tuple
#1)It is a immutable datatype
#2)ordered collection
#3)It allows the duplicate values and also any data types as element of tuple
#4)It will take less memory as compare to list
#5)it will support for indexing and slicing

#-------------------------------------------------------------------------------------------------------
#4)Sets- it is Collectionof homogeenous or heterogenous.
#immutable data items are values enclosed between {} (curly braces) also unordered collection
#syntax- var_name={value1,value2,....,valuen}
#ex-
sets={1,4,5,6,7,7,8,8,9,0,0}
print(sets)
print(type(sets))
print(len(sets))
#default value of set is = set()

#Properties of set
#1)Set is used to remove values from the comma separated initialization/removes duplicate values
#2)It is a unordered Collection
#3)it will not allow any mutable datatype as element
#4)Memory allocation is random memory allocation
#5)set will not allow indexing and slicing
#6)set is a mutable datatype

#---------------------------------Set methods------------------------------------------------------------------
#1)add()- it is a builtin function which is used to add the new value to the set
#syntax- var.add(value)
new_set={1,2,3,9,8,6,4,4,6}
print(new_set.add(12))
print(new_set)

#2)remove()-it is a builtin function which is used to remove the value from the set
#syntax-var.remove(value)
print(new_set.remove(1))
print(new_set)


#----------------------------------------------------------------------------------------------------------------------
#5)Dictionary- collection of key value pairs separated by comma operator 
#boundary = {....}
#each element associated with unique key
#syntax- var_name={key1:value1,key2:value2,.......,keyn:valuen}

#length= returns the no of keys present in the dictionary
#len(dict_name)
# it does not support idexing and slicing
#different ways to construct dictionary
#d={}
#d=dict()
#d=dict(banglore=25,goa=56,mumbai=60)
#d=dict([('banglore'=25),('goa'=56),('mumbai'=60)])

#properties of Dictionary
#1)Key cannot be duplicated
#2)key will be a single element
#3)values can be of any datatypes
#4)values can be accessed through key only
#5)keys must be of immutable data type

#composite key - dictonaries can have composite keys
#i.e.,, tuple as keys
#ex-
holiday={(26,1):'republic day',(15,8):'independence day',(21,6):'yoga day'}

#nested dictionary
#ex-
prices={'IBM':{'curent':90.1,'low':88.3,'high':92.7},'hp':{'curent':29.70,'low':28.30,'high':31.2}}

#list inside the dict as values
location={'country':'india','states':['karnataka','delhi','punjab']}

#points
points={'a':1,'b':2,'c':3}

#Accessing and update vlues from a dict using dict lookup method
#ex-
d={'banglore':25,'goa':35,'punjab':30}
print(d['banglore']) # print the value for the given pair

print(d.get('banglore')) #another method to print the value of given pair

d['goa']=45  #assining new value to the pair if the key alredy exist
print(d)

d['delhi']=96 #adding new key value pair to dict
print(d)

#get()- returns the value of the item with the specified key if keyname and value is not present then it will
#give the second parameter(value) as value
#get() method does not throw error but returns none by default if second argument isnot given


#setdefault()- returns the value of the item with specified key if the value not specified then it adds none
#syntax- dict.setdefault(keyname,[value])
#if the key does not exist it will insert the key with the specified value
d.setdefault('mysore')
print(d)

#fromkeys()- returns a dictionary with the specified key and the secified value
#syntax- dict.fromkeys(keys,[value])
#key required an iterble specifying the keys of the new dictionary value optional.the value for all keys is none
values={'apple':43,'orange':34,'mango':78,'gauva':34}
print(dict.fromkeys(values,0))

#items()-method returns a view object returns the key value pair of the dictionary as tuples in a list
#syntax- dictionary_names.items()

#keys() - returns a list of all keys present in the dictionary
#syntax- dictionary_name.keys()

#values() - returns a list of all the values
#syntax-dictionary_name.values()

#deleting the key and value
#pop()-removes the specified item from the dictionary
#returns the removed value as output
#syntax-dictinary.pop(keyname,defaultvalue)

#popitem()-removes the item that was inserted at last into the dictionary
#return the last key value pair



