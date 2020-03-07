# Lambda one number arg
print('Lambda one number arg')
oneArg = lambda x: x+x*x
print(oneArg(7))
print('===========================================================')

# Lambda two numbers args
print('Lambda two numbers args')
twoArgs = lambda x, y: (x+x)*y
print(twoArgs(7, 5))
print('===========================================================')

# Lambda string
print('Lambda string')
myName = lambda name, lname: (name, lname)
callFunc = myName('Ismail', 'salmi')
print(callFunc)
print('===========================================================')

# Program to double each item in a list using map()
print('Program to double each item in a list using map')
newList = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(newList)
print('===========================================================')

# Program to double each item in a 2 lists using map
print('Program to double each item in a 2 lists using map')
inOneList = list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))
print(inOneList)
print('===========================================================')

# Get even number using filter function
print('Get even number using filter function')
a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, a)))
print('===========================================================')

# Find item using filter list of dicts
print('Filter list of dicts')
dict1 = {'name': 'ismail', 'age': 26}, {'name': 'yusuf', 'age': 4}
print(list(filter(lambda x: x['name'] == 'yusuf', dict1)))