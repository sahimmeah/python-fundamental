
# ___________________________String Expression________________________________
   
"""
In Python, strings are used for representing textual data. A string is a sequence of characters enclosed in either single quotes ('').In Python, a string is a sequence of characters. For example, "hello" is a string containing a sequence of characters 'h' , 'e' , 'l' , 'l' , and 'o' .

"""


# str1 = "This is string.\nIt's used in Phython"
# print(str1)

# str1 = "This is string.\tIt's used in Phython"
# print(str1)

###  Concatenation-----------------------------------------

# str1 = "Sahim Meah"
# str2 = "Sikder"
# print(str1 + str2)
# print(str1 + " " + str2)

### Length of String----------------------------------------

# a = "Hello.Welcome to my Code"
# print(len(a))

### Indexing----------------------------------------------------


# when we write indexing code we used [ ] 3rd bracked. Idexing count start from 0.

# sta = "Hello.Welcome to my Code"

# print(sta [6])     
# print(sta [13])   

### Slicing ----------------------------------------

# It's mean slice a apple .when we slicing a apple we see 2 part. part 1 & part 2. 
# str [ Starting_ ind : Ending index] ------- Here ending index is not included.


# a = "HelloWorld"
# print(a[1 : 6])

# str = "ApnaCollege"

# print( str[1 : 4])

# print(str[ : 4])          #it's whows same as (str[ 0 : 4 ])

# print(str[ 1 : ])         # is same as ( str [ 1 : len(str) ])
# print(str[ 0 : ])         # is same as ( str [ 0 : len(str) ])

# print (str[ -7 : -1])     # it's show the  Negative indexing. here return is , Colleg

### String Functions ----------------------------------------


# str = "My Name is Sahim"


# print(str.endswith("him"))       # endswith function shows -- last  carecter (him) diye shes hoi kina?? jodi hoi then retun TRUE prent hobe or False.

# print(str.find("Name"))
# print(str.find("Karim"))   # kono carecter khuje na pele -1 return kore.



# str = "my Name is Sahim"
# print(str.capitalize())

# print(str.replace("i","o"))
# print(str.replace("Sahim","Tushar"))

# str = " Hello Every one.I hope you all are good.Today we learn Phython from our resources.I hope you will all are enjoy thia program. "

# print(str.count("o"))
# print(str.count("hope"))
# print(str.count("z"))

# Let's Practice______________________________________________________________

"""
Question: WAP to input users first name & print its length.
"""
# Name = input("First Name")
# print("First name: ", Name)
# print("Length of Name:", len(Name))

"""
Question: WAP to find the occurrence of '$' in a string.

here, occurrence means how much it's happend?
"""

# str = "The $ sign is string.And is show USA $ of currency"
# print(str.count("$"))



# ________________________________Condition Statements____________________________________

# (if - elif - else) CONDITION SHOW THE  TRUE & fALSE .

# Age = 25
# if ( Age >= 25 ):
#     print("Can Apply For license")    

# if  Age >= 25:
#     print("Can Apply For license")      
#     print("Can Apply For Vote")

#****prite er age 4 space must importent or codition er por  (:) use kore press enter. its Called *** Intentation.

"""
*** Elif : The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

*** Else: The else keyword catches anything which isn't caught by the preceding conditions.
"""

# Age = 20
# if ( Age >= 25 ):
#     print("Can Apply For license")
# elif ( Age <= 25 ):
#     print("Can Apply For license")
# else:
#     print( "can't Apply For License")
    
# ---------------------------------------------------------------

# Signal = "Red"
# Signal = "Green"
# Signal = "Yello"
# Signal = "Pink"

# if ( Signal == "Red" ):
#     print("Stope Please")
# elif ( Signal == "Green" ):
#     print("Go and Run Please")
# elif ( Signal == "Yello" ):
#     print( " Look Around Please")
# else:
#     print("Wate Please")  
# ___________________________________________________________________________________

"""
Question: Grade students based on marks 
"""

# marks = 80             #*** Here, Marks can be different.

# if( marks >= 90 ):   #*** If condition ,any one can used from different two statement


# if ( marks == 90 or marks >= 90):
#     print("Grade = A")
# elif ( marks >= 80 ):
#     print (" Grade = B")
# elif ( marks >= 70 ):
#     print ("Grade = c")
# else:
#     print( "Grade = D ")

# ----------------------------------------------------------------------------


# marks = int(input("Enter Your Marks: "))

# if ( marks >= 90 ):
#     Grade = "A"
# elif ( marks >= 80 and marks < 90 ):
#     Grade = "B"
# elif ( marks >= 70 and marks < 80):
#     Grade = "C"
# else:
#     Grade = "D"

# print("Gread Of the student is : ", Grade )

# __________________________________ NESTING CONDITION ______________________________________

"""
Nesting of if statements mean to write an if condition inside another if condition.

Example: 
if (condition):
    if (condition 2 ):
        Print()
 
"""

# Age = int(input("Type Your Age: "))

# if ( Age >= 20 and Age <= 50 ):
#     if(Age >=50 ):
#         print( "Can't Drive A Car")
#     else:
#         print("Can Drive A Car")

#     # print("Can Drive A Car")
# else:
#     print("Can't drive A Car")



# Let's Practice______________________________________________________________________


"""
Question: WAP to check if a number entered by the user is odd or even.
"""

# number = int(input("Type a number : "))

# if ( number%2==0):
#     print("The Number is Even")
# else:
#     print("The Number is Odd")

"""
Question: WAP to find the gretest of 3 numbers entered by the user.
"""
# a=10
# b=20
# c=40


# # a = int(input("Type Of Number A :"))
# # b = int(input("Type Of Number B :"))
# # c = int(input("Type Of Number C :"))


# if( a>b and a>c):
#     print("Greatest: A")
# elif( b>a and b>c):
#     print("Gretest: B")
# else:
#     print("Gretest: c")

"""
Question: WAP to find the gretest of 5 numbers entered by the user.
# """

# a=57
# b=20
# c=92
# d=30
# e=27


# if( a>b and a>c and a>d and a>e):
#     print("Greatest: A")
# elif( b>c and b>d and b>e):
#     print("Gretest: B")
# elif( c>d and c>e ):
#     print("Gretest: C")
# elif( d>e ):
#     print("Gretest: D")
# else:
#     print("Gretest: E")


"""
Question: WAP to check if a number is a multiple of 7 or not.
"""
# number = int(input("Enter Number:"))

# if(number % 7 == 0):
#     print( "Yes")
# else:
#     print("Not")















































