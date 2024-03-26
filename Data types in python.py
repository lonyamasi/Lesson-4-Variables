#Data types in python
#why are they important? its important to know the data type of a variable because 
# it determines the operations that can be performed on the variable
#Type 1:None
#if we have a variable that has no value, we can assign it the value None
#in other languages we use null to represent a variable with no value

#Type 2:Numeric
#Here we have 4 different types of numeric data types
#1. Integers
#Integers are whole numbers, they can be positive or negative
num= 5
print(type(num)) #prints the data type of the variable num

#2. Floats
#Floats are numbers that have a decimal point
num2= 4.5

print(type(num2)) #prints the data type of the variable num2

#3. Complex
#Complex numbers are numbers that have a real and imaginary part
#They are written in the form a+bj where a and b are floats and j is the square root of -1
num3= 3 + 4j
print (type(num3)) #prints the data type of the variable num3

#can we convert between the different numeric data types?
a= 5.6
b= int(a) #converts a to an integer using the int() function
#to convert a number to a float we use the float() function

k=float(b) #converts b to a float
print(k) #prints the value of k 5.0

#if we want to make a number complex we use the complex() function
c= complex(b,k)
print(c) #prints the value of c 5+5j

#Type Boolean
#Booleans are used to represent the truth value of an expression, they can only have 2 values True or False.
#They are used to make decisions in programs

bool = b<k #this is a boolean expression, it checks if b is less than k
#if we print the value of bool it will print True

#In python we use 1 as True and 0 as False
#so we can convert a boolean to an integer by using the int() function

#TYPE 3 SEQUENCE TYPES
#These are data types that can hold multiple values
#1. Strings
#Strings are sequences of characters, they are immutable.
#They are written in single or double quotes
string= 'Hello'
string2= "World"
#we can use the + operator to concatenate strings
string3= string + string2
print(string3) #prints HelloWorld

#we can also use the * operator to repeat a string
string4= string*3
print(string4) #prints HelloHelloHello

#we can access the characters in a string using the index
print(string[0]) #prints H
print(string[1]) #prints e
print(string[2]) #prints l
print(string[3]) #prints l

#we can also use negative indexing
print(string[-1]) #prints o 
print(string[-2]) #prints l
print(string[-3]) #prints l
print(string[-4]) #prints e

#we can also use slicing to get a substring
print(string[1:3]) #prints el
print(string[:3]) #prints Hel
print(string[1:]) #prints ello

#we can also use the len() function to get the length of a string
print(len(string)) #prints 5

#we can also use the -in- operator to check if a character is in a string
print('H' in string) #prints True
print('z' in string) #prints False

#we can also use the -not in- operator to check if a character is not in a string
print('z' not in string) #prints True

#Strings are immutable, this means that we cannot change the value of a string
#we can only create a new string

#2. Lists
#Lists are ordered sequences of items, they are mutable
#They are written in square brackets
list= [1,2,3,4,5]
#we can access the items in a list using the index
print(list[0]) #prints 1
print(list[1]) #prints 2
print(list[2]) #prints 3

#we can also use negative indexing
print(list[-1]) #prints 5
print(list[-2]) #prints 4
print(list[-3]) #prints 3

#we can also use slicing to get a sublist
print(list[1:3]) #prints [2,3]
print(list[:3]) #prints [1,2,3]
print(list[1:]) #prints [2,3,4,5]

#we can also use the len() function to get the length of a list
print(len(list)) #prints 5

#we can also use the -in- operator to check if an item is in a list
print(1 in list) #prints True
print(6 in list) #prints False

#we can also use the -not in- operator to check if an item is not in a list
print(6 not in list) #prints True

#we can also use the + operator to concatenate lists
list2= [6,7,8,9,10]
list3= list + list2
print(list3) #prints [1,2,3,4,5,6,7,8,9,10]

#we can also use the * operator to repeat a list
list4= list*3
print(list4) #prints [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

#we can also use the append() method to add an item to a list
list.append(6)
print(list) #prints [1,2,3,4,5,6]

#we can also use the insert() method to add an item to a list at a specific index
list.insert(0,0) #takes 2 arguments, the index and the item to be inserted
print(list) #prints [0,1,2,3,4,5,6]

#we can also use the remove() method to remove an item from a list
list.remove(0)
print(list) #prints [1,2,3,4,5,6]

#we can also use the pop() method to remove an item from a list at a specific index
list.pop(0) #takes 1 argument, the index of the item to be removed
print(list) #prints [2,3,4,5,6]

#we can also use the clear() method to remove all the items from a list
list.clear()
print(list) #prints []

#3. Tuples
#Tuples are ordered sequences of items, they are immutable
#They are written in round brackets
tuple= (1,2,3,4,5)
#we can access the items in a tuple using the index
print(tuple[0]) #prints 1
print(tuple[1]) #prints 2
print(tuple[2]) #prints 3

#we can also use negative indexing
print(tuple[-1]) #prints 5
print(tuple[-2]) #prints 4
print(tuple[-3]) #prints 3

#we can also use slicing to get a subtuple
print(tuple[1:3]) #prints (2,3)
print(tuple[:3]) #prints (1,2,3)

#we can also use the len() function to get the length of a tuple
print(len(tuple)) #prints 5

#we can also use the -in- operator to check if an item is in a tuple
print(1 in tuple) #prints True
print(6 in tuple) #prints False

#we can also use the -not in- operator to check if an item is not in a tuple
print(6 not in tuple) #prints True

#we can also use the + operator to concatenate tuples
tuple2= (6,7,8,9,10)
tuple3= tuple + tuple2
print(tuple3) #prints (1,2,3,4,5,6,7,8,9,10)

#we can also use the * operator to repeat a tuple
tuple4= tuple*3
print(tuple4) #prints (1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)

#4. Range
#Range is a sequence of numbers, it is immutable
#It is used to generate a sequence of numbers
#It is written in round brackets
range= range(5)
print(range) #prints range(0,5)






   