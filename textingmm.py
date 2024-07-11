"""fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    if fruit == "banana":
        break
        print("i dont eat", fruit)
    else:
        print("i eat", fruit) 
    #condition comes before breaking a loop, else runs when the loop of a list is finished and if break is applied the else donesnt run"""


"""
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for odd_number in list_of_numbers:
    if odd_number % 2 != 0:
        continue
    print(odd_number)"""

"""for x in range(2, 10, 2):
    print(x)

"""
"""
i = 1
while i < 11:
    print(i)
    i +=1
    if i == 5:
        break"""

def my_func():
    print("hello,")
    print("how are you doing, today")
my_func()
my_func()

def greetin(name):
    print("Goodmorning", name)

greetin("Franklin")
greetin("Joshua")
greetin("Mark")

person = "Mark"

greetin(person)



def num(num):
    print(num + 10)

nums = 15
num(nums)

num(10)


def fullname(fname, lname):
    firstname = fname.strip().lower().capitalize()
    lastname = lname.strip().lower().capitalize()
    print(firstname + " " + lastname)

fullname(" jOhN", "DoE ")
fullname(" MeRriLL", "HarRy")

def add(x, y):
    print(x + y)
add(10, 40)

def sub(x, y):
    print(x - y)
sub(10, 40)

def mul(x, y):
    print(x * y)
mul(10, 40)

def div(x, y):
    print(x / y)
div(10, 40)
"""