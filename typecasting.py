#---------------------------------------------Typecasting-------------------------------------------
#it is a process of converting data from one type to another type of data
#syntax- destination_var=destination_type(source_value)
#ex-
a=10
b=float(a)
print(b)

#--------------------------------------------------------------------------------------------------
#1)typecasting from integer to all other datatypes
#a)to int- it is possible but no use
print(int(a))
#b)to float - yes it is possible it will ad decimal point
print(float(a))
#c)to complex - yes it is possible but in result adds the imaginary part
print(complex(a))
#d)to boolen- yes it is possible but returns true if it is non default value else return fals
print(bool(a))
#e) to string- yes it is possible it will drop the int into the single quotes
print(str(a))
#f)to list,tuple,dict,set - not possible
#note- we can't able to convert the any single value datatype into any multivalue data type except string

#----------------------------------------------------------------------------------------------------
#2)typecasting from flaot to all other data types
#a)to int - yes it is possible it will remove the decimal number
c=123.67
print(int(c))
#b)to float - yes it is possible but no use
print(float(c))
#c)to complex- yes it is possible it will add imaginary term
print(complex(c))
#d)to boolean- yes it is possible it will check for the default values
print(bool(c))
#e)to string - yes it is possible it will the float number into single quotes
print(str(c))
#f)to list,tuple,dicitionary,set - not possible

#-----------------------------------------------------------------------------------------------------
#3)typecasting from complex all other datatypes
#a) to int- not possible it will throw typeerror- int() argument mustbe a string, bytes like object
#b) to float-not possible
#c)to complex- yes it is possible but noo use
#d)to bool-yes it is possible it will check for default values
comp=1+2j
print(bool(comp))
#e)to string- yes it is possible
print(str(comp))
#e)to list,tuple,dictionary,set-not possible

#---------------------------------------------------------------------------------------------------------
#4)typecasting from bool to all other types
#a)to int- yes it is possible it will return 1 for true and 0 for false
t=True
f=False
print(int(t))
print(int(f))
#b)to float -yes it is possible for true 1.0 and for false 0.0
print(float(t))
print(float(f))
#c)to complex- yes it is possible add imaginary term
print(complex(t))
print(complex(f))
#d)to bool -yes possible but no use
#e)to string- yes it is possible it will drop the keywords into quotes
print(str(t))
print(str(f))
#f)to list,tuple,dictionary,set- not possible

#---------------------------------------------------------------------------------------------
#5)Typecasting from string to all other datatypes
i='123'
ft='12.3'
co='12+3j'
st='apple@gmail.com'
#a)to int
print(int(i)) #yes it is possible if the data inside the quote is int
#print(int(ft))
#print(int(co))
#print(int(st)) #these 3 are not possible
#b)to float
#print(float(st))
#print(float(co)) #not possible
print(float(i))
print(float(ft)) #possible if only the data inside the quotes is float or int
#c)to complex
print(complex(i))
print(complex(ft))
print(complex(co)) #yes it is posible 
#print(complex(st)) #it is not possible to convert string into complex
#d)to boolean-
print(bool(i))
print(bool(ft))
print(bool(st))
print(bool(co)) #it is possible it will check for the default values
#e)to string-possible but no use
#f)to list- yesit possible it wil create the list of characters
print(list(i))
print(list(ft))
print(list(st))
print(list(co))
#g)to tuple-yes it is possible same as list
print(tuple(i))
print(tuple(ft))
print(tuple(st))
print(tuple(co))
#h)to set - yes it possible it will create the unordered set of the string characters
print(set(i))
print(set(ft))
print(set(co))
print(set(st))
#i)to dictionary- not possible because dictionary needs the key value pair

#----------------------------------------------------------------------------------------------------
#6)typecasting from list all other datatypes
lst=[10,20,30,40]
#a)to int, float,complex- not possible 
#b)to boolean - yes it is possible
print(bool(lst))
#c)to string- yes it is possible
print(str(lst))
#d)to list- possible but no use
print(list(lst))
#e)to tuple- possible it will convet square braces list to prenthesis tuple
print(tuple(lst))
#f)to set-yes it possible but if values are repeated then set will remove them
print(set(lst))
#g)to dictionary-not possible but if data is 
DATA=['ab',(2,4),[10,20],{30,40}]
print(dict(DATA))
#it is possible only when list of values are multivalue data type with length2

#--------------------------------------------------------------------------------------------------
#7) Typecasting from Tuple to other datatypes.
tuple1=(1,2,3,4,6)
#a)to int() , float(), complex()- not possible
#b)bool()- yes possible but not useful
print(bool(tuple1))
#c)to string-yes possible 
print(str(tuple1))
#d)to list - yes possible it will convert tuple into list
print(list(tuple1))
#e)to tuple - yes possible but not useful
print(tuple(tuple1))
#f)to dict-not possible
#g)to set-yes possible
print(set(tuple1))

#--------------------------------------------------------------------------------------------------
#typecasting from dictionary to all other datatypes
dct={'a':1,'b':2,'c':2}
#a) to int, float, complex - not possible 
#B) to bool - yes possible 
print(bool(dct))
#c) to string- yes possible 
print(str(dct))
#d) to list - possible but it will form the list of only key values 
print(list(dct))
#e) to dict- possible but no use
print(dict(dct))
#f) to set - yes possible it will form the set of key values only
print(set(dct))
#g)to tuple'- yes possible it will form the tuple of key values 
print(tuple(dct))

#----------------------------------------------------------------------------------------------------------
#typecasting from set to all other datatypes
s={1,2,3,4,5}
#a) to int, float,complex - not possible cannot typecaste multivalue datatype to single value data type except boolean data type
#b)to bool- yes possible 
print(bool(s))
#c) to string - yes possible 
print(str(s))
#d) to list - yes possible
print(list(s))
#e)to tuple - yes possible
print(tuple(s))
#f)to dict- not possible
#g) to set - yes possible but no use
print(set(s))

