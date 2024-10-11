# print("hi everyone.","My name is Sahim")
# print(20+15)


# ------------------Example of Variable & Data Type-------------

# Name ="Sahim"
# Age =25
# Location ="Chattagong"
# CGPA = 3.50
# age2 = Name
# old=False
# a=None


# print("My name is:",Name)
# print("I am:",Age,"years old")
# print("My location is:",Location)
# print("My CGPA is:",CGPA)

# print(age2)
# print(type(Name))
# print(type(Age))
# print(type(Location))
# print(type(CGPA))
# print(type(old))
# print(type(a))


# a=50
# b=30
# sum=a+b
# print(sum)

"""
example of Multi-type comment.

Hello My Name is Sahim.I am a new learner of Python.It's my firts project where i learn different types of topic like ,data type,variable,input type etc.

"""

# Arithmetic Operators

a=5
b=2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
print(a % b)   # when we calculate 5/2 then we find 2.5 normally 2*2=4 and extra 1 is show Modillo.so % return show modillo.
# print(a ** b)  # Here calculate a^b


# Relational / Comparison Operators

# a=20
# b=10

# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
# print(a > b)
# print(a < b)


# Assignment Operators 

# num = 20


# num = num + 20   # when, num value is 20 then, num =num + 20 shows: num = 20+20 =40 , which are similar of ( num += 20 )=40
# num += 20

# num -= 20      # which mean, (num = num - 20)

# num *= 20      # which mean, (num = num * 20)

# num /= 20      # which mean, (num = num / 20)

# num %= 20        # which mean, (num = num % 20)

# num **= 20        # which mean, (num = num ** 20) simply, ( num = num ^ num)

# print("Number is:", num)


# Logical Operators 

#------- here always shows the oposite return-----

# print( not True )    # return False
# print ( not False )  # return True

# example:----------------

# a = 20
# b = 10

# print ( not ( a>b) )
# print ( not ( a<b) )

# --------example of And / Or Operators ------------

# val1 = True     # if, 2 value are shows true then, ( and ) operateros given True.
# val2 = True

# # print ("And Operators:", val1 and val2 )

# val1 = True
# val2 = False

# print ("And Operators:", val1 and val2 )

# ----------------------------------------------------

# val1 = True      # if, 1 value shows True then, ( or ) operateros given True .
# val2 = True

# print ("OR Operators:", val1 or val2 )

# val1 = True
# val2 = False

# print ("Or Operators:", val1 or val2 )

# ---------Extra Example ------------------------

# a = 20
# b = 10

# print ( (a==b) and (a>b) )   # return False

# print ( (a!=b) and (a>b) )   # return True

# print ( (a!=b) or (a>b) )   # return True

# print ( (a!=b) and (a>b) )   # return True


# _________________________Type Conversion_________________________________________

# if one type variable  convert to another type variable,suppose ; int to float it's called type conversion.

# Python has 2 type of type conversion. 1) type conversion -Interpretter automatically convert. 2)type castint- Interpreter foces for convert.

# a = 2            # int value
# b = 4.25         # float value

# sum = a + b      # here, (Sum = int value + Float value) and int convert to float value
# print ( sum )    # answer shows the float value = 6.25

# ------------------------------------------------------------

# a = "2"             # string value
# b = 4.25            # float value

# print (type (a))   # show string value

# sum = a + b
# print ( sum )      # string value not convert to float value . only int value can convert to float.

# ------------------------------------------------------------

# a = "2"             # string value

# a = int("2")          # Convert string To Integer
# b = 4.25              # float value

# print (type (a))    # show intger value

# sum = a + b
# print ( sum )         # convert float value

# -----------------------------------------------------------

# a = 4.00
# # print(type(a))   # return float value

# a = str(a)
# print(type(a))     # value of a convert to string

# _________________________ INPUT In Python ________________________________________

# input("Enter Your Name:")

# ------------------------------------------------

# Name = input("Enter Your Name:")
# print("welcome", Name )

# age = input("Enter Your Age:")
# print( age )

# ------------------------------------------------

# val = input("Enter Some Value: ")
# print( type (val) , val)

# ------------------------------------------------

# val = int(input("Enter Some Value: "))
# print( type (val) , val)

# --------------------------------------------------

# val = float(input("Enter Some Value: "))
# print( type (val) , val)

# -----------------------------------------------

# Example-----------------

# Name = input("Your name: ")
# print("welcome", Name)
# Age = int(input("Your Age: "))
# CGPA = float(input("Your CGPA: "))
# print("Your Age", Age)
# print("Your CGPA", CGPA)



# ___________________________ PRACTICE Example_____________________________________

# num1 = int(input("enter num1 value:" ))
# num2 = int(input("enter num2 value:" ))

# sum = ( num1 + num2 )
# print(sum)

## print("sum =" , num1 + num2 )

# --------------------------------------------------

# val = int(input("value of the Number: "))

# val = float(input("value of the Number: "))

# # print("value of the Number: " , val)

# Area = val * val
# print("Area is:" , Area )

# --------------------------------------------------

# Num1 = float(input("value of the Number: "))

# Num2 = float(input("value of the Number: "))

# print("Average Is:" , ((Num1+Num2)/2 ))

# ----------------------------------------------------


# a = int(input("First Number: "))
# b = int(input("Second Number: "))

# print(a >= b)








