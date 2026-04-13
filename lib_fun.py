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
#C)
