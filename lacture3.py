
# _________________________________ LIST ______________________________________

"""
list is a built in data type that stores set of values.
Introduction. A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .

***** String ----> immutable----> do not Change 
***** List ------> Mutable------> it will changeable



"""

# marks = [28 , 50 ,80 ,  30]

# print(marks)
# print(type(marks))
# print(marks[0])
# print(len(marks))


# Details = [ "sahim" , 22 , "GEC"]

# print(Details)
# print(len(Details))
# print(type(Details))

# print(Details[0])

# Details[0]="Karim"               # list muttable .
# Details[1]=25
# print(Details)
# print(len("GEC"))

# Details[2] = "Bangladesh"
# print(Details)
# print(Details[0:2])

# -------------------------------------------------------------------

# list = [ 5 , 40 ,30 , 50 , 25 ]

# list.append(4)
# print(list)

# print(list.append(9) ,list)          #**add one element at the end.

# print(list.sort() ,list)             #**Sort shows the  ascending order.

# print(list.sort(reverse=True),list)  #**show Desending order.

# print(list.reverse() , list)         #** all number counted by reverselly.

# print(list.insert( 1 ,60 ), list)    #** insert element at index.( list.insert( inx , el)).

# print(list.pop( 1 ) , list )         #** remove element at index.((list.pop(idx)).

""" Search : python documentation"""


# _________________________________ TUPLE in Python ______________________________________


"""
******A built in data type that lets us create immutable sequences of values.
******Tuple = immutable or Not Changeable
****** here we used ( ) second bracket.

"""

# tub = ( 1 ,25 ,33 ,41 )

# print(tub)
# print (type(tub))

# print(tub[2])    # find index

# tub[2] = 5   #**it's not allowed in python.Here it's can't change & assign the value in idx.


# tub= ()        # empty tuple
# print(tub)
# -------------------------------------------------------------------
# tub = ( 1 )
# print ( tub )
# print( type(tub))  #------------> it's return integer type

# -----------------------------------------------------------------

# tub = ( 1 ,)
# print ( tub )
# print( type(tub))    #------> used , for Tuple and it's make difference from integer.

# -----------------------------------------------------------------

# tub = ( 1 , 10 , 25 , 66 )
# print ( tub )
# print( type(tub))  

# -----------------------------------------------------------------

# tup = (1 , 25 ,42 ,55 ,12 ,25 ,66 ,25 )                   # Sliching in tuple


# print(tup [ 1:3 ])

# print(tup.index(25))                      # koto tomo index a ache seta dekhai.

# print(tup.count(25))                        # 25 koto bar ache dekhai

# --------------------------------------------------------------------


# ___________________________ Let's Practice _______________________
"""Question: WAP to ask the user names of there 3 favorite movies & store them in a list.  """

# movie1=input("movie name first : ")
# movie2=input("movie name second : ")
# movie3=input("movie name third : ")

# list = [ movie1 , movie2 ,movie3 ]
# print(list)

# -------------------

# movies =[]
# movies.append (input("movie name first : "))
# movies.append (input("movie name Second : "))
# movies.append (input("movie name 3rd : "))

# print(movies)




"""Question: WAP to check if a list contains a palindrome of elements. (Hint : Use Copy() method )  

[ 1,2,3,2,1]                  [ 1,"abc" , "abc" , 1 ]

"""
# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.( samne and piche theke same dekhai). Example: Ma'am , Racecar.
# ----------------------------------------------------------------

# list1 = [ 1 ,2 ,3 ,2 , 1 ]
# # list2 = [ 1 , 2 ,3 ,4 ,2]

# list1_copy = list1.copy()
# list1_copy.reverse()

# if(list1_copy == list1):
#     print("Palindrom")
# else:
#     print("Not palindrom")




"""Question: WAP to count the number of students with the "A" grade in the following tuble

[ "C" , "D" ,"A", "A", "B", "B", "A" ]

"""
# Student_list = ("C" , "D" ,"A", "A", "B", "B", "A") 


# print(Student_list.count("A"))

# print(type(Student_list))


"""Question: Store the above values in list & sort  them from "A" to "D". """

Student_list = [ "C" , "D" ,"A", "A", "B", "B", "A" ]
 
# Student_list.sort()
# print(Student_list)

print(Student_list.sort(),Student_list)

































































