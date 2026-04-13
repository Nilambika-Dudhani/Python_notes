##-----------------------------------------##LIBRARY FUNCTIONS##-----------------------------------------------
##1)TOKEN-THIS ARE THE ESSENTIAL ELEMENTS WHICH WE NEED TO WRITE THE PYTHON CODE
##A)KEYWORD
##B)VARIABLES
##C)IDENTIFIERS
##D)DATA TYPES
#____________________________________________________________________________________________________________
##A) KEYWORD- UNIVERSALLY STANDARD RESERVED WORDS(PREDEFINED FUNCTIONS)
##THERE ARE 36 KEYWORDS IN PYTHON
#To print all the keywords 
import keyword
print(keyword.kwlist)
##There are 3 special Keywords
#1) True
#2) False
#3) None
#because these 3 keywords can be treated as value
#ex- a=True,b=False,c=None

#__________________________________________________________________________________________________________
#B) Variables- Variables are the name given to an value in python or it is a reference name for the data
#Syntax- variables_name=value
#ex- a=10,b=20,name=nil

##Memory allocation of Variables
#______________________________________
#   Variables| value Space            |
#--------------------------------------
#     a      |      10                |
#     b      |      20                |
#     name   |      nil               |
#--------------------------------------
#id - it is the built in function to get the memory address or the variable
#ex-
a=10
print(id(a))
#Declaring Multiple variables in single line
#ex-
x,y,z=10,20,30
print(x,y,z)

#____________________________________________________________________________________________________________
#C)Identifiers -  Identifiers are the name given to the variables, functions, classes in python
#Rules for the Identifiers:
#1)It should not be any keyword - ex- IF =10
#2)It should not start with any number  Ex- 3num=10
#3)It should not contain any void spaces at beginning or in between Ex-  num=10 or n um=10
#4)It should not conain any special character expect underscore(_) ex-N_um=10
#5)It can be alphbet or group of alphabet either uppercase or lowercase or it can be alphanumeric or it can be single underscore
#6)As per industrial standard the number length of identifier should be within 32 bit 

#____________________________________________________________________________________________________________________
#4)Datatypes-  Data type represent the type of data present inside the variable
#in python we are not required to specify the type of data .based on the value provided the type of data will be assigned automaticaaly 
#to the variable
#Types of The data types:

#1) Single value datatypes
#In this we are going to store the single value into the single variable
#Types- Integer, Float, Complex, boolean

#2)Multivalue data types
#In this datatype we are going to store a multiple value into a single variable
#Types- String, List, Tuple, Dictionary, Set

