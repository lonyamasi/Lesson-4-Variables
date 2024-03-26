
#STRING METHODS
sentence = "Python programming"

print(sentence.strip("P")) #means we remove P from the start
print(sentence.strip("g")) #means we remove g from the end

print(sentence.strip("Pyng")) #means we remove Py from the start and ng from the end

print(sentence.lower())
print(sentence.upper())

print(sentence.replace("Python", "Java")) #replace Python with Java

print(sentence.split()) #split the sentence into a list of  2words

print(sentence.split("p")) #split the sentence into a list of 2 words removing p

print(sentence.count("m")) #counts the number of m in the sentence

print(sentence.find("m")) #find the index of m in the sentence

print(sentence.index("m")) #find the index of m in the sentence

print(sentence.startswith("P")) #check if the sentence starts with P

print(sentence.endswith("g")) #check if the sentence ends with g
print

print(sentence.isalnum()) #check if the sentence is alphanumeric

print(sentence.isalpha()) #check if the sentence is alphabetic

print(sentence.isdigit()) #check if the sentence is digit

print(sentence.islower()) #check if the sentence is in lower case

print(sentence.isupper()) #check if the sentence is in upper case

sentence_2 = " "
print(sentence_2.isspace()) #check if the sentence is a space

#STRING CONCATENATION
first_name = "John"
last_name = "Doe"
age = 30

#Using join
print("Hello, my name is " + " ".join([first_name, last_name]) + " and I am " + str(age) + " years old")

print("Hello, my name is " + first_name + " " + last_name + " and I am " + str(age) + " years old")

#string formatting
print("Hello, my name is {} {} and I am {} years old".format(first_name, last_name, age))
#or 
print(f"Hello, my name is {first_name} {last_name} and I am {age} years old")


