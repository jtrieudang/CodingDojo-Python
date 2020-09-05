# 1. ONLY SPEND 1 hour doing this. Come back when you have more time.
# May be helpful https://github.com/liamcclane/PracticingPythonFunctions/blob/master/functions_intermediateIandII.py (1b is at the bottom)
# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
for i in x:
    for v in range(len(i)):
        if i[v] == 10:
            i[v] = 15           
print(x)

# shortcut way in the bottom
# x[1][0]=15
# print(x)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]
for i in students:
    for i['last_name'] in students:
        if i['last_name'] == 'Jordon':
            i['last_name'] = 'Byrant'
print(students)

# shortcut way in the bottom
# students[0]['last_name'] = 'Bryant'
# print(students)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # 3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # 4.Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
# for i in z:
#     if ['y'] == 20:
#         ['y'] = 30
z[0]['y']= 30
print(z)
# --------------------------------------------------------------------------------------
# # 2.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    string = ''
    for i in students:
        string += f"first_name - {i['first_name']}, last_name - {i['last_name']}\n"
    return string
print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# --------------------------------------------------------------------------------------
# # 3.
# Michael
# John
# Mark
# KB
def iterateDictionary2(key_name, some_list):
    string = ''
    for i in some_list:
        string += f"{i['key_name']}\n"
    return string
print(iterateDictionary2(first_name, some_list))
# Jordan
# Rosales
# Guillen
# Tonel

# --------------------------------------------------------------------------------------
# # 4. NEED TO REDO THIS ONE. 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def Info(some_dict):
    string = ''
    string2 = ''
    count_location = 0
    count_instructor = 0
    for i in some_dict:
        string += f'{i['locations']} \n'
        string2 += f'{i['instructors']} \n'
        count += 1
    return string
print(Info(dojo))
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank


# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon