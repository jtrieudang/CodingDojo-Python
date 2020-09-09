print("Hello_world")
print("this is a sample string")

name = "Jimmy"
print("My name is" , name)
# Output: My name is Jimmy
# OR

name = "Jimmy"
print("My name is" + name) 
# problem with that is that you need to add a space in the quote to run it with the space.
# Output: My name isJimmy

first_name = "Jimmy"
last_name = "Trieudang"
age = 27
# f-string place for (lieral string interpolation)
print(f"My name is {first_name} {last_name} and I am {age} years old.")
# Output: My name is Jimmy Trieudang and I am 27 years old.

# string.format(), string reads from left to right $ needs to have the same # of strings.
first_name = "Zen"
last_name = "Dang"
age = 28
print("My name is {} {} and I am {} years old." .format(first_name, last_name, age))
# output: My name is Zen Dang and I am 27 years old.
print("My name is {} {} and I am {} years old." .format(age, last_name, first_name))
# output: My name is 28 Dang and I am Zenyears old.

# %-formatting, this is an old version, it needs %s for a string and %d for a integer
hw = "Hello %s" % "world"  
py = "I love Python %d" % 3 
print(hw, py)
# Output: Hello world I love Python 3
name = "Jimmy"
age = 27
print("My name is %s and I'm %d" % (name,age))
# Output: My name is Jimmy and I'm 27

# Build-in string methods
x = "hello world"
print(x.title())
# Output: Hello World

# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.