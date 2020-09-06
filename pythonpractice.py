x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

class EmptyClass:
    pass

# Boolean (true and false)
is_hungry = True
has_freckles = False

# Numbers, integers
age = 35 # storing an int
weight = 160.57 # storing a float

# String 
name = "Joe Blue"

# Tuples
dog = ('Bruce', "cookie", 19, False)
print(dog[0])

# List - collection of data
empty_list = []
ninjas = ['Rogen', 'KV', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# Dictionaries
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

print(type(2.87))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>
print(type(ninjas))  # output: <class 'list'>

# counting the # in the variable/strings within
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

# Typing cast
print("Hello " + str(42))

total = 35
user_val = "26" #define as integer
total = total + int(user_val)		# total will be 61
print(total)

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

for x in range(10):	# increment of +1 and start at 0 is implied
    print(x)

for count in range(0,5):
    print("looping - ", count)

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)  # notice, when line 95 is true it did not print i since it breaks the statement

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")