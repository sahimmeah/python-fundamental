
# ______________________Diceionary___________________________
"""
 Dictionaries are mutable data structures that allow you to store key-value pairs. Dictionary can be created using the dict() constructor or curly braces' {}'

Dictionaries are used to store data values in ( key:value ) pairs.

they are unorderd , mutable (Changeble) & don't allow duplicate keys

example:
word <-----> meanings
key  <-----> Value

Suppose:

dict = {
    "name"  :  "sahim" ,     ****Coma used( , ) for new line start
    "CGPA"  :  3.50 ,
    "marks" : [ 98 , 90 , 85 ] ,

}
"""


# Details = {

#    "Name" : "Sahim Meah" ,  
#    "Age" : 25 ,
#    "Address" : "GEC",
#    "Subjects" : [ "python" , "C++" , "Java" , " HTML" ] ,
#    "CGPA" : 3.80 ,
#    "Total marks " : [ 95 , 85 , 83 ] ,
#    "Cost" : ( 50 , 100 ,55 ,),
#    12 : 100 ,
# }

# print(Details)
# print(type(Details))

# ---------------------------------------------------------

# print(Details["Name"])               #single value return
# print(Details[12])
# print(Details["Address"])

# ----------------------------------------------------------

# Details["Name"] = "Rahim"             # Name value change
# Details["SurName"] = "Rafi Miya"      # New value create
# print(Details)

# ----------------------------------------------------------

# null_dict = { }      
# null_dict = {"Hello,My Name is Sahim Meah"}
# print(null_dict)

# -----------------------------------------------------------

# _____________________ Nested Dictionaries ______________________

"""
Here nested dictionary refers to the dictionary inside a dictionary.
Example:
"""
# Information = {
#     "Name" : "Md.Sahim Meah" ,
#     "Subject" : {
#         "English" : 85 ,
#         "Math"  :  90 ,
#         "Physics" : 88 ,
#     }
# }
 
# print(Information)

# print(Information ["Subject"])

# print( Information ["Subject"] ["Math"] )

# ------------------------------------------------------------

"""______________ Some Dictionary Methods _________________"""


# Information = {
#     "Name" : "Md.Sahim Meah" ,
#     "Subject" : {
#         "English" : 85 ,
#         "Math"  :  90 ,
#         "Physics" : 88 ,
#     }
# }

# print(Information.keys())
# print (list(Information.keys()))
# print (len(list(Information.keys())))
# print (tuple(Information.keys()))

# print(Information.values())

# -----------------------------------------
# print(Information.items())
# pairs = list(Information.items())
# print(pairs [0])                      #indexing hocce.
# print(pairs [1])
# -----------------------------------------

# print(Information.get("Name"))    # return subject all values properlly.
# print(Information["Name2"])       # return Error
# print(Information.get("Name2"))   # Return None

# -----------------------------------------

# Information.update({"College code" : 3124 })
# Information.update({"College Name" :"Kazem ali"})
# print(Information)
# ----------------
# Information.update({"Name" : "Kajem Ali" , "College Code" : 3124 , "Board" : " Chittagong" })

# print(Information)

# -------------------------------------------------------------
# -------------------------------------------------------------




"""___________________ SET in PYTHON______________________________"""


# A set is a data collection type used in Python for storing multiple items in a single variable

# Set is the collection of the unordered items. ( unorder means age ba pore asbe emn kichu follow korbe na )

# Each element in the set must be unique & immutable.

# Set is collection where we collect unique vales.

# List and  Dictionary are ( Not store ) in SET dueto both are mutable.

# We are used second bracket { } for set sintext.

# Repeated elements stored only once, so it resolved to like, { 1,2}

# Null set = set (). which we called empty set syntax.

# Sets is ----------------------------> Mutable 
# Elements of Sets is ----------------> Immutable 


"""_________________________________________________________________"""

# collection = { 1 ,2,3 ,4 , " Sakib" , "Rakib" }

# print(collection)
# print(type(collection))

# ---------------------------------------------

# collection = { 1 ,2, 3 ,4 , " Sakib" , "Rakib"  , "Rakib" , 2 ,4 }

# print(collection)          # ignore Duplicate value & unorder
# print(type(collection))
# print (len(collection))    # shows total numbers of items & ignor duplicate numbers.


# ----------------------------------------------

"""______Null Or empty______"""

# Collection = set()

# print(type(Collection))

# -----------------------------

# Collection = { }         # shoew dictionary null/ empty sintex.

# print(type(Collection))

"""_____________________ Some Set Methods ________________________"""

# Collection = set( )

# print (Collection)
# print(type(Collection))

# Collection.add(6)
# Collection.add(4)
# Collection.add(6)
# Collection.add(2)
# Collection.add(" New Set")
# Collection.add("New Practice")
# Collection.add(4.00)
# Collection.add(10.5)

# Collection.remove( 4 )

# Collection.clear()
# Collection.pop()               # remove rendom value

# print (Collection)
# print(len(Collection))

# ----------------------------------------------------

# *** Union set = Combines both set values & Return new. all unique value shows. example: Set-1= { 1,2,3} & Set-2= { 2,4,5} .......so Union new set={1,2,3,4,5}.

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y)
# print(z)

# ---------------------------------

# Set_1 = { 1, 2 ,3 ,4}
# Set_2 = { 3, 4 , 5, 6}
# Set_3 = { 4, 7 , 8 ,9, 10}

# print(Set_1.union(Set_2 , Set_3))    # Multiple Union Set sintex


# -------------------------------------------------------


# ***Intersection Set = Intersection set that contains the similarity between two or more sets. Meaning: The returned set contains only items that exist in both sets,

# Set_1 = { 1, 2 ,3 ,4}
# Set_2 = { 3, 4 , 5, 6}

# print(Set_1.intersection(Set_2))

# -----------------------------------

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = {5, 6, 7, 8, 9}

# intersection = set1.intersection(set2, set3)        # Multiple sets.


"""_____________________ Lets Practice ________________________"""

# dict = {
#     "Table" : ["A piece of furniture" , "list Of facts & figures" ],

#     "Cat" : " A small animal"
# }

# print(dict)
# print(dict["Table"])
# print(dict["Cat"])

# -----------------------------------------------


# Classroom = {"Python","java","C++","Python","javascript","java","Python","java","C++","C"}

# print(Classroom)

# print (len(Classroom))

# -------------------------

# A = {"Python"}
# B = {"java" }
# C = {"C++"}
# D = {"Python"}
# E = {"javascript"}
# F = {"java"}
# G = {"Python"}
# H = {"java"}
# I = {"C++"}
# J = {"C"}

# Classroom = (A.union(B,C,D,E,F,G,H,I,J))

# print(Classroom)
# print( len(Classroom))

# -----------------------------------


# id = [1, 2, 3]

# id2= id

# print(id == id2)

# marks = list((1, 2, 3))
# # marks[0] = 1
# print(marks)

# # 1 = 4 bytes | 32 bit


# a = 305
#  ------------------------------------

# dic = {}

# dic["math"] = int(input())
# dic["bengali"] = int(input())
# dic["physics"] = int(input())

# print(dic)

# --------------------------------------

# math = int(input("Enter Math marks: "))
# dic.update({"math": math})

# phy = float(input("marks of phy:"))
# dic.update({"phy":phy})
# print(dic)

# -------------------------------------

# arry = list()
# arry.append(1)
# print(arry)

# dic1 = {

# }

# dic2 = {"phy": 50}

# # dic1[''.join(dic2.keys())] = dic2['phy']
# dic1.update({"phy": 50})

# print(dic1)

# print(type({1, 2, 3}))


# c = []

# ----------------------------------------------




a = 9
b = 9.25

c = { a, b}



print({9, 9.5})











































































